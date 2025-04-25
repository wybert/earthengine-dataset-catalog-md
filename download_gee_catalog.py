import pandas as pd
import asyncio
import os
import re
import json
import requests
from datetime import datetime, timezone
import sys
from crawl4ai import AsyncWebCrawler

def check_last_update():
    # GitHub API endpoint for the file's commit history
    api_url = "https://api.github.com/repos/samapriya/Earth-Engine-Datasets-List/commits"
    params = {
        "path": "gee_catalog.csv",
        "per_page": 1
    }

    try:
        # Get the last commit info
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        commits = response.json()
        if not commits:
            print("No commit history found")
            return False
            
        # Get the last commit date
        last_commit_date = datetime.strptime(
            commits[0]['commit']['committer']['date'],
            '%Y-%m-%dT%H:%M:%SZ'
        ).replace(tzinfo=timezone.utc)
        
        # Get current time in UTC
        current_time = datetime.now(timezone.utc)
        
        # Calculate time difference
        time_diff = current_time - last_commit_date
        hours_diff = time_diff.total_seconds() / 3600  # Convert to hours
        
        print(f"Last commit: {last_commit_date}")
        print(f"Current time: {current_time}")
        print(f"Hours since last update: {hours_diff:.2f}")
        
        # Return True if more than 24 hours have passed
        return hours_diff > 24
        
    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub API: {e}")
        return False
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")
        return False

# Configuration
BATCH_SIZE = 20  # Number of URLs to process in one batch
DELAY_BETWEEN_REQUESTS = 0.5  # Delay between individual requests (seconds)
DELAY_BETWEEN_BATCHES = 5  # Delay between batches (seconds)
PROGRESS_FILE = "download_progress_datasets_catalog.json"
DOCS_DIR = "docs"
os.makedirs(DOCS_DIR, exist_ok=True)

async def main():
    # First check if we need to update
    print("Checking if update is needed...")
    if not check_last_update() and '--force' not in sys.argv:
        print("No update needed - source file hasn't changed in the last 24 hours.")
        print("Use --force flag to run anyway.")
        sys.exit(1)

    print("Update needed or forced. Proceeding with download...")
    
    # Load and process the CSV file
    print("Downloading catalog CSV...")
    df = pd.read_csv("https://raw.githubusercontent.com/samapriya/Earth-Engine-Datasets-List/master/gee_catalog.csv")
    urls_to_process = df['asset_url'].tolist()
    
    # Process in batches
    total_batches = (len(urls_to_process) + BATCH_SIZE - 1) // BATCH_SIZE
    processed_urls = {}
    async with AsyncWebCrawler() as crawler:
        for batch_index in range(total_batches):
            start_idx = batch_index * BATCH_SIZE
            end_idx = min(start_idx + BATCH_SIZE, len(urls_to_process))
            batch_urls = urls_to_process[start_idx:end_idx]

            print(f"\nProcessing batch {batch_index + 1}/{total_batches} ({len(batch_urls)} URLs)")

            for i, url in enumerate(batch_urls):
                print(f"Crawling {start_idx + i + 1}/{len(urls_to_process)}: {url}...")
                try:
                    result = await crawler.arun(url=url)
                    result_markdown = result.markdown
                    try:
                        result_markdown = result_markdown.split("Send feedback")[1]
                    except IndexError:
                        print(f"Warning: No 'Send feedback' section found in {url}")
                    try:
                        result_markdown = result_markdown.split("* [ ![GitHub]")[0]
                    except IndexError:
                        print(f"Warning: No 'GitHub' section found in {url}")
                    [content_clean, summary] = result_markdown.split("Need to tell us more?")

                    # Create a filename from the URL
                    filename = url.rstrip('/').split('/')[-1]
                    filename = re.sub(r'[^\w_.-]', '_', filename)
                    filepath = f"{DOCS_DIR}/{filename}.md"

                    # Write the markdown content to the file
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content_clean)

                    # Update progress
                    processed_urls[url] = {
                        "status": "success",
                        "filename": f"{filename}.md",
                        "timestamp": get_timestamp()
                    }

                    # Save progress after each URL
                    save_progress(processed_urls)

                    print(f"Saved to {filepath}")
                except Exception as e:
                    print(f"Error processing {url}: {str(e)}")
                    # Record the error
                    processed_urls[url] = {
                        "status": "error",
                        "error": str(e),
                        "timestamp": get_timestamp()
                    }
                    save_progress(processed_urls)

                # Delay between requests
                await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

            # Delay between batches
            if batch_index < total_batches - 1:
                print(f"Batch {batch_index + 1} completed. Pausing for {DELAY_BETWEEN_BATCHES} seconds...")
                await asyncio.sleep(DELAY_BETWEEN_BATCHES)

    # Final statistics
    success_count = sum(1 for info in processed_urls.values() if info.get("status") == "success")
    error_count = sum(1 for info in processed_urls.values() if info.get("status") == "error")

    print("\nDownload complete!")
    print(f"Total URLs processed: {len(processed_urls)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {error_count}")

def get_timestamp():
    """Get current timestamp in ISO format."""
    from datetime import datetime
    return datetime.now().isoformat()

def save_progress(progress_data):
    """Save progress to JSON file."""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress_data, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
