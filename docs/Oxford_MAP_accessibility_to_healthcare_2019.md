 
#  Accessibility to Healthcare 2019 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Oxford/MAP/accessibility_to_healthcare_2019](https://developers.google.com/earth-engine/datasets/images/Oxford/Oxford_MAP_accessibility_to_healthcare_2019_sample.png) 

Dataset Availability
    2019-01-01T00:00:00Z–2020-01-01T00:00:00Z 

Dataset Provider
     [ Malaria Atlas Project ](https://malariaatlas.org/research-project/accessibility-to-cities/) 

Earth Engine Snippet
     `    ee.Image("Oxford/MAP/accessibility_to_healthcare_2019")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Oxford/Oxford_MAP_accessibility_to_healthcare_2019) 

Tags
     [accessibility](https://developers.google.com/earth-engine/datasets/tags/accessibility) [jrc](https://developers.google.com/earth-engine/datasets/tags/jrc) [map](https://developers.google.com/earth-engine/datasets/tags/map) [oxford](https://developers.google.com/earth-engine/datasets/tags/oxford) [population](https://developers.google.com/earth-engine/datasets/tags/population) [twente](https://developers.google.com/earth-engine/datasets/tags/twente)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019#citations) More
This global accessibility map enumerates land-based travel time (in minutes) to the nearest hospital or clinic for all areas between 85 degrees north and 60 degrees south for a nominal year 2019. It also includes "walking-only" travel time, using non-motorized means of transportation only.
Major data collection efforts underway by OpenStreetMap, Google Maps, and academic researchers have been harnessed to compile the most complete collection of healthcare facility locations to date. This map was produced through a collaboration between MAP (University of Oxford), Telethon Kids Institute (Perth, Australia), Google, and the University of Twente, Netherlands.
This project builds on previous work published by Weiss et al 2018 ([doi:10.1038/nature25181](https://doi.org/10.1038/nature25181)). Weiss et al (2018) utilised datasets for roads (comprising the first ever global-scale use of Open Street Map and Google roads datasets), railways, rivers, lakes, oceans, topographic conditions (slope and elevation), landcover types, and national borders. These datasets were each allocated a speed or speeds of travel in terms of time to cross each pixel of that type. The datasets were then combined to produce a "friction surface": a map where every pixel is allocated a nominal overall speed of travel based on the types occurring within that pixel. For the current project, an updated friction surface was created to incorporate recent improvements within OSM roads data.
Least-cost-path algorithms (run in Google Earth Engine and, for high-latitude areas, in R) were used in conjunction with this friction surface to calculate the time of travel from all locations to the nearest (in time) healthcare facility. The healthcare facilities dataset utilized location data from two of the largest global databases: (1) OSM data that was collated and made available for download at [www.healthsites.io](https://www.healthsites.io/); and (2) data extracted from Google Maps. The global datasets were augmented with continental-scale facility locations that were recently published for Africa and Australia. To facilitate comparisons between data sources, only facilities defined as hospitals and clinics were used. Multiple points found within the same pixel were merged to match the resolution of the analysis as defined by the selected gridded representation of the Earth's surface. Each pixel in the resultant accessibility map thus represents the modelled shortest time (in minutes) from that location to a hospital or clinic.
Source dataset credits are as described in the accompanying paper.
**Pixel Size** 927.67 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`accessibility` | min |  0  |  41504.1  | Travel time to the nearest hospital or clinic.  
`accessibility_walking_only` | min |  0  |  138893  | Travel time to the nearest hospital or clinic using non-motorized transport.  
**Terms of Use**
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
Citations:
  * D.J. Weiss, A. Nelson, C.A. Vargas-Ruiz, K. Gligorić, S. Bavadekar, E. Gabrilovich, A. Bertozzi-Villa, J. Rozier, H.S. Gibson, T. Shekel, C. Kamath, A. Lieber, K. Schulman, Y. Shao, V. Qarkaxhija, A.K. Nandi, S.H. Keddie, S. Rumisha, E. Cameron, K.E. Battle, S. Bhatt, P.W. Gething. Global maps of travel time to healthcare facilities. Nature Medicine (2020).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019#code-editor-javascript-sample) More
```
vardataset=ee.Image('Oxford/MAP/accessibility_to_healthcare_2019');
varaccessibility=dataset.select('accessibility');
varaccessibilityVis={
min:0.0,
max:41556.0,
gamma:4.0,
};
Map.setCenter(18.98,6.66,2);
Map.addLayer(accessibility,accessibilityVis,'Accessibility');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Oxford/Oxford_MAP_accessibility_to_healthcare_2019)
[ Accessibility to Healthcare 2019 ](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019)
This global accessibility map enumerates land-based travel time (in minutes) to the nearest hospital or clinic for all areas between 85 degrees north and 60 degrees south for a nominal year 2019. It also includes "walking-only" travel time, using non-motorized means of transportation only. Major data collection efforts underway by …
Oxford/MAP/accessibility_to_healthcare_2019, accessibility,jrc,map,oxford,population,twente 
2019-01-01T00:00:00Z/2020-01-01T00:00:00Z
-60 -180 85 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://malariaatlas.org/research-project/accessibility-to-cities/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_accessibility_to_healthcare_2019)


