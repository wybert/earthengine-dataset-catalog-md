 
#  WAPOR Daily Reference Evapotranspiration 2.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![FAO/WAPOR/2/L1_RET_E](https://developers.google.com/earth-engine/datasets/images/FAO/FAO_WAPOR_2_L1_RET_E_sample.png) 

Dataset Availability
    2009-01-01T00:00:00Z–2023-03-20T00:00:00Z 

Dataset Provider
     [ FAO UN ](https://wapor.apps.fao.org/catalog/WAPOR_2/1/L1_RET_E) 

Earth Engine Snippet
     `    ee.ImageCollection("FAO/WAPOR/2/L1_RET_E")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_WAPOR_2_L1_RET_E) 

Cadence
    1 Day 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [fao](https://developers.google.com/earth-engine/datasets/tags/fao) [wapor](https://developers.google.com/earth-engine/datasets/tags/wapor) [water](https://developers.google.com/earth-engine/datasets/tags/water) [water-vapor](https://developers.google.com/earth-engine/datasets/tags/water-vapor)
[Description](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E#citations) More
Reference evapotranspiration (RET) is defined as the evapotranspiration from a hypothetical reference crop and it simulates the behaviour of a well-watered grass surface. Each pixel represents the daily reference evapotranspiration in mm.
**Pixel Size** 18924 meters 
**Bands**
Name | Units | Scale | Description  
---|---|---|---  
`L1_RET_E` | mm | 0.1 | Reference Evapotranspiration (Daily) [mm]  
**Terms of Use**
The Food and Agriculture Organization of the United Nations (FAO) is mandated to collect, analyze, interpret, and disseminate information related to nutrition, food, and agriculture. In this regard, it publishes a number of databases on topics related to FAO's mandate, and encourages the use of them for scientific and research purposes. Consistent with the principles of openness and sharing envisioned under the [Open Data Licensing For Statistical Databases](http://www.fao.org/3/ca7570en/ca7570en.pdf), and consistent with the mandate of FAO, data from the [Water Productivity Open Access Portal (WaPOR)](https://wapor.apps.fao.org/home/WAPOR_2/1), as part of [AQUASTAT](http://www.fao.org/aquastat/en/) - FAO's Global Information System on Water and Agriculture, is available free to the user community.
Citations:
  * FAO 2018. WaPOR Database Methodology: Level 1. Remote Sensing for Water Productivity Technical Report: Methodology Series. Rome, FAO. 72 pages.
  * FAO 2020. WaPOR V2 Database Methodology. Remote Sensing for Water Productivity Technical Report: Methodology Series. Rome, FAO. <https://www.fao.org/3/ca9894en/CA9894EN.pdf>


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E#code-editor-javascript-sample) More
```
varcoll=ee.ImageCollection('FAO/WAPOR/2/L1_RET_E');
varimage=coll.first();
Map.setCenter(17.5,20,3);
Map.addLayer(image,{min:0,max:100});
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_WAPOR_2_L1_RET_E)
[ WAPOR Daily Reference Evapotranspiration 2.0 ](https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E)
Reference evapotranspiration (RET) is defined as the evapotranspiration from a hypothetical reference crop and it simulates the behaviour of a well-watered grass surface. Each pixel represents the daily reference evapotranspiration in mm.
FAO/WAPOR/2/L1_RET_E, agriculture,fao,wapor,water,water-vapor 
2009-01-01T00:00:00Z/2023-03-20T00:00:00Z
-39.9953437 -30.15 40.0044643 65.13 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://wapor.apps.fao.org/catalog/WAPOR_2/1/L1_RET_E)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/FAO_WAPOR_2_L1_RET_E)


