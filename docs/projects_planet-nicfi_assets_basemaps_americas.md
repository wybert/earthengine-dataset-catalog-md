 
#  NICFI Satellite Data Program Basemaps for Tropical Forest Monitoring - Americas 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![projects/planet-nicfi/assets/basemaps/americas](https://developers.google.com/earth-engine/datasets/images/planet-nicfi/projects_planet-nicfi_assets_basemaps_americas_sample.png)
info
This dataset is part of a Publisher Catalog, and not managed by Google Earth Engine. Contact support@planet.com for bugs or [view more datasets](https://developers.google.com/earth-engine/datasets/publisher/planet-nicfi) from the Planet Catalog. [Learn more about Publisher datasets](https://developers.google.com/earth-engine/datasets/publisher). 
[ ![Catalog Owner Logo](https://developers.google.com/static/earth-engine/datasets/logos/planet-nicfi_logo.png) ](https://planet.com/nicfi) 

Catalog Owner
    Planet 

Dataset Availability
    2015-12-01T00:00:00Z–2025-03-01T00:00:00Z 

Dataset Provider
     [ Planet ](https://planet.com/nicfi) 

Earth Engine Snippet
     `    ee.ImageCollection("projects/planet-nicfi/assets/basemaps/americas")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/planet-nicfi/projects_planet-nicfi_assets_basemaps_americas) 

Tags
     [basemaps](https://developers.google.com/earth-engine/datasets/tags/basemaps) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [nicfi](https://developers.google.com/earth-engine/datasets/tags/nicfi) [planet](https://developers.google.com/earth-engine/datasets/tags/planet) [planet-nicfi](https://developers.google.com/earth-engine/datasets/tags/planet-nicfi) [publisher-dataset](https://developers.google.com/earth-engine/datasets/tags/publisher-dataset) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance) [tropics](https://developers.google.com/earth-engine/datasets/tags/tropics)
[Description](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#citations) More
This image collection provides access to high-resolution satellite monitoring of the tropics for the primary purpose of reducing and reversing the loss of tropical forests, contributing to combating climate change, conserving biodiversity, contributing to forest regrowth, restoration and enhancement, and facilitating sustainable development, all of which must be Non-Commercial Use.
To learn how to access the Basemaps, follow the [sign up instructions here](https://developers.planet.com/docs/integrations/gee/nicfi/).
The NICFI Satellite Data Program mosaics (also referred to as Planet-NICFI mosaics) contain both monthly and biannual collections generated every 6 months. The type of the mosaic is stored in the image metadata field 'cadence'. Use that field along with the start and end date for each mosaic to find the desired imagery.
Full details about the Basemaps are available in [NICFI Satellite Data Program Basemap spec](https://assets.planet.com/docs/NICFI_Basemap_Spec_Addendum.pdf).
For more information about the NICFI (Norway's International Climate and Forest Initiative) Satellite Data Program and the data offered, please visit [the Program's website](https://assets.planet.com/docs/NICFI_General_FAQs.pdf).
In support of NICFI's mission, you can use this data for a number of projects including, but not limited to:
  * Advance scientific research about the world's tropical forests and the critical services they provide.
  * Implement and improve policies for sustainable forest management and land use in developing tropical forest countries and jurisdictions.
  * Increase transparency and accountability in the tropics.
  * Protect and improve the rights of indigenous peoples and local communities in tropical forest countries.
  * Innovate solutions towards reducing pressure on forests from global commodities and financial markets.


**Pixel Size** 4.77 meters 
**Bands**
Name | Min | Max | Scale | Description  
---|---|---|---|---  
`B` |  0  |  10000  | 0.0001 | Blue  
`G` |  0  |  10000  | 0.0001 | Green  
`R` |  0  |  10000  | 0.0001 | Red  
`N` |  0  |  10000  | 0.0001 | Near-infrared  
**Image Properties**
Name | Type | Description  
---|---|---  
cadence | STRING | The interval the mosaic covers: monthly or biannual  
**Terms of Use**
This data has usage, reproduction, and distribution restrictions in support of the NICFI Satellite Data Program purpose. The full licensing agreement is available [here](https://assets.planet.com/docs/Planet_ParticipantLicenseAgreement_NICFI.pdf).
Copyright notice:
Image © 20xx Planet Labs PBC (where xx denotes the year of the content used)
Citations:
  * Planet Team (2017). Planet Application Program Interface: In Space for Life on Earth. San Francisco, CA. <https://api.planet.com>


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas#code-editor-javascript-sample) More
```
// This collection is not publicly accessible. To sign up for access,
// please see https://developers.planet.com/docs/integrations/gee/nicfi
varnicfi=ee.ImageCollection('projects/planet-nicfi/assets/basemaps/americas');
// Filter basemaps by date and get the first image from filtered results
varbasemap=nicfi.filter(ee.Filter.date('2021-03-01','2021-07-01')).first();
Map.centerObject(basemap,4);
varvis={'bands':['R','G','B'],'min':64,'max':5454,'gamma':1.8};
Map.addLayer(basemap,vis,'2021-03 mosaic');
Map.addLayer(
basemap.normalizedDifference(['N','R']).rename('NDVI'),
{min:-0.55,max:0.8,palette:[
'8bc4f9','c9995c','c7d270','8add60','097210'
]},'NDVI',false);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/planet-nicfi/projects_planet-nicfi_assets_basemaps_americas)
[ NICFI Satellite Data Program Basemaps for Tropical Forest Monitoring - Americas ](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas)
This image collection provides access to high-resolution satellite monitoring of the tropics for the primary purpose of reducing and reversing the loss of tropical forests, contributing to combating climate change, conserving biodiversity, contributing to forest regrowth, restoration and enhancement, and facilitating sustainable development, all of which must be Non-Commercial Use. …
projects/planet-nicfi/assets/basemaps/americas, basemaps,forest,nicfi,planet,planet-nicfi,publisher-dataset,satellite-imagery,sr,surface-reflectance,tropics 
2015-12-01T00:00:00Z/2025-03-01T00:00:00Z
-30.4 -118.5 30.4 -34.5 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://planet.com/nicfi)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas)


