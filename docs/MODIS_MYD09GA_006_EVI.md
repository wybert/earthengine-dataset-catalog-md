 
#  MODIS Aqua Daily EVI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/MYD09GA_006_EVI](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_MYD09GA_006_EVI_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2023-02-25T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/MYD09GA_006_EVI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MYD09GA_006_EVI) 

Cadence
    1 Day 

Tags
    
aqua
daily
evi
global
modis
myd09ga
surface-reflectance
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI#terms-of-use) More
The Enhanced Vegetation Index (EVI) is generated from the Near-IR, Red and Blue bands of each scene, and ranges in value from -1.0 to 1.0. See [Huete et al. (2002)](https://www.sciencedirect.com/science/article/pii/S0034425702000962) for details. This product is generated from the MODIS/006/MYD09GA surface reflectance composites.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`EVI` |  463.313 meters  | Enhanced Vegetation Index  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/MYD09GA_006_EVI')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
varcolorized=dataset.select('EVI');
varcolorizedVis={
min:0,
max:1,
palette:[
'ffffff','ce7e45','df923d','f1b555','fcd163','99b718','74a901',
'66a000','529400','3e8601','207401','056201','004c00','023b01',
'012e01','011d01','011301'
],
};
Map.setCenter(-7.03,31.05,2);
Map.addLayer(colorized,colorizedVis,'Colorized');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MYD09GA_006_EVI)
[ MODIS Aqua Daily EVI ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI)
The Enhanced Vegetation Index (EVI) is generated from the Near-IR, Red and Blue bands of each scene, and ranges in value from -1.0 to 1.0. See Huete et al. (2002) for details. This product is generated from the MODIS/006/MYD09GA surface reflectance composites.
MODIS/MYD09GA_006_EVI, aqua,daily,evi,global,modis,surface-reflectance,usgs,vegetation-indices 
2002-07-04T00:00:00Z/2023-02-25T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_MYD09GA_006_EVI)


