 
#  MODIS Terra Daily NDWI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/MOD09GA_006_NDWI](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_MOD09GA_006_NDWI_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2023-02-17T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/MOD09GA_006_NDWI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MOD09GA_006_NDWI) 

Cadence
    1 Day 

Tags
    
daily
global
mod09ga
modis
ndwi
surface-reflectance
terra
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI#terms-of-use) More
The Normalized Difference Water Index (NDWI) is sensitive to changes in liquid water content of vegetation canopies. It is derived from the Near-IR band and a second IR band, ≈1.24μm when available and the nearest available IR band otherwise. It ranges in value from -1.0 to 1.0. See [Gao (1996)](https://www.sciencedirect.com/science/article/pii/S0034425796000673) for details. This product is generated from the MODIS/006/MOD09GA surface reflectance composites.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`NDWI` |  463.313 meters  | Normalized Difference Water Index  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/MOD09GA_006_NDWI')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
varcolorized=dataset.select('NDWI');
varcolorizedVis={
min:0.0,
max:1.0,
palette:['0000ff','00ffff','ffff00','ff0000','ffffff'],
};
Map.setCenter(-7.03125,31.0529339857,2);
Map.addLayer(colorized,colorizedVis,'Colorized');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MOD09GA_006_NDWI)
[ MODIS Terra Daily NDWI ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI)
The Normalized Difference Water Index (NDWI) is sensitive to changes in liquid water content of vegetation canopies. It is derived from the Near-IR band and a second IR band, ≈1.24μm when available and the nearest available IR band otherwise. It ranges in value from -1.0 to 1.0. See Gao (1996) …
MODIS/MOD09GA_006_NDWI, daily,global,modis,ndwi,surface-reflectance,terra,usgs,vegetation-indices 
2000-02-24T00:00:00Z/2023-02-17T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI)


