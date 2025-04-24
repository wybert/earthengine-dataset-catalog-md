 
#  Landsat-derived forest age for Canada 2019 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CANADA/NFIS/NTEMS/CA_FOREST_AGE](https://developers.google.com/earth-engine/datasets/images/CANADA/CANADA_NFIS_NTEMS_CA_FOREST_AGE_sample.png) 

Dataset Availability
    2019-01-01T01:00:00Z–2020-01-01T01:00:00Z 

Dataset Provider
     [ National Forest Information System ](https://opendata.nfis.org/mapserver/nfis-change_eng.html) 

Earth Engine Snippet
     `    ee.ImageCollection("CANADA/NFIS/NTEMS/CA_FOREST_AGE")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CANADA/CANADA_NFIS_NTEMS_CA_FOREST_AGE) 

Tags
     [canada](https://developers.google.com/earth-engine/datasets/tags/canada) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE#terms-of-use) More
Canadian primary forest dataset is a satellite-based forest age map for 2019 across Canada's forested ecozones at a 30-m spatial resolution. Remotely-sensed data from Landsat (disturbances, surface reflectance composites, forest structure) and MODIS (Gross Primary Production) are utilized to determine age.
Forest age can be determined where disturbance can be identified directly (disturbance approach) or inferred using spectral information (recovery approach) or using inverted allometric equations to model age where there is no evidence of disturbance (allometric approach). The disturbance approach is based upon satellite data and mapped changes and is the most accurate. The recovery approach also relies upon satellite data plus logic regarding forest succession, with an accuracy that is greater than pure modeling.
Given the lack of widespread recent disturbance over Canada's forests, the allometric approach is required over the greatest area (86.6%). Using information regarding realized heights and growth and yield modeling, ages are estimated where none are otherwise possible. Trees of all ages are mapped, with trees >150 years old combined in an "old tree" category.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`forest` | y | Forest age  
**Terms of Use**
The forest age map described herein for Canada's forested ecosystems is declared open source and supported by the Government of Canada. The dataset is licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('CANADA/NFIS/NTEMS/CA_FOREST_AGE');
Map.setCenter(-107.94,58.18,3);
Map.addLayer(
dataset,
{palette:['006600','002200','fff700','ab7634','c4d0ff','ffffff']},
'Canada Primary Forest Data');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CANADA/CANADA_NFIS_NTEMS_CA_FOREST_AGE)
[ Landsat-derived forest age for Canada 2019 ](https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE)
Canadian primary forest dataset is a satellite-based forest age map for 2019 across Canada's forested ecozones at a 30-m spatial resolution. Remotely-sensed data from Landsat (disturbances, surface reflectance composites, forest structure) and MODIS (Gross Primary Production) are utilized to determine age. Forest age can be determined where disturbance can be …
CANADA/NFIS/NTEMS/CA_FOREST_AGE, canada,forest,forest-biomass 
2019-01-01T01:00:00Z/2020-01-01T01:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://opendata.nfis.org/mapserver/nfis-change_eng.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CANADA_NFIS_NTEMS_CA_FOREST_AGE)


