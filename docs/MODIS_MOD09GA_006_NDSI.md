 
#  MODIS Terra Daily NDSI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/MOD09GA_006_NDSI](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_MOD09GA_006_NDSI_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2023-02-17T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/MOD09GA_006_NDSI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MOD09GA_006_NDSI) 

Cadence
    1 Day 

Tags
    
daily
global
mod09ga
modis
ndsi
surface-reflectance
terra
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI#terms-of-use) More
The Normalized Difference Snow Index is used to identify snow, based on its characteristically higher reflectance in the visible portion of the spectrum compared to the mid-IR. NDSI is computed using the Green and Mid-IR bands, and has a range of -1.0 to 1.0. See [Riggs et al. (1994)](https://doi.org/10.1109/IGARSS.1994.399618) for details. This product is generated from the MODIS/006/MOD09GA surface reflectance composites.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`NDSI` |  463.313 meters  | Normalized Difference Snow Index  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/MOD09GA_006_NDSI')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
varcolorized=dataset.select('NDSI');
varcolorizedVis={
palette:['000088','0000ff','8888ff','ffffff'],
};
Map.setCenter(-7.03125,31.0529339857,2);
Map.addLayer(colorized,colorizedVis,'Colorized');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MOD09GA_006_NDSI)
[ MODIS Terra Daily NDSI ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI)
The Normalized Difference Snow Index is used to identify snow, based on its characteristically higher reflectance in the visible portion of the spectrum compared to the mid-IR. NDSI is computed using the Green and Mid-IR bands, and has a range of -1.0 to 1.0. See Riggs et al. (1994) for …
MODIS/MOD09GA_006_NDSI, daily,global,modis,ndsi,surface-reflectance,terra,usgs,vegetation-indices 
2000-02-24T00:00:00Z/2023-02-17T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDSI)


