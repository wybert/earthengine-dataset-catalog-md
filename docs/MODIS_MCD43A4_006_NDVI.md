 
#  MODIS Combined 16-Day NDVI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/MCD43A4_006_NDVI](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_MCD43A4_006_NDVI_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2023-02-10T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/MCD43A4_006_NDVI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MCD43A4_006_NDVI) 

Cadence
    1 Day 

Tags
    
albedo
brdf
daily
global
mcd43a4
modis
nasa
ndvi
reflectance
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI#terms-of-use) More
The Normalized Difference Vegetation Index is generated from the Near-IR and Red bands of each scene as (NIR - Red) / (NIR + Red), and ranges in value from -1.0 to 1.0. This product is generated from the MODIS/006/MCD43A4 surface reflectance composites.
**Bands**
Name | Min | Max | Pixel Size | Description  
---|---|---|---|---  
`NDVI` |  -1*  |  1*  |  463.313 meters  | Normalized Difference Vegetation Index  
* estimated min or max value 
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/MCD43A4_006_NDVI')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
varcolorized=dataset.select('NDVI');
varcolorizedVis={
min:0,
max:1,
palette:[
'ffffff','ce7e45','df923d','f1b555','fcd163','99b718','74a901',
'66a000','529400','3e8601','207401','056201','004c00','023b01',
'012e01','011d01','011301'
],
};
Map.setCenter(-7.03125,31.0529339857,2);
Map.addLayer(colorized,colorizedVis,'Colorized');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MCD43A4_006_NDVI)
[ MODIS Combined 16-Day NDVI ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI)
The Normalized Difference Vegetation Index is generated from the Near-IR and Red bands of each scene as (NIR - Red) / (NIR + Red), and ranges in value from -1.0 to 1.0. This product is generated from the MODIS/006/MCD43A4 surface reflectance composites.
MODIS/MCD43A4_006_NDVI, albedo,brdf,daily,global,mcd43a4,modis,nasa,ndvi,reflectance,usgs,vegetation-indices 
2000-02-24T00:00:00Z/2023-02-10T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_NDVI)


