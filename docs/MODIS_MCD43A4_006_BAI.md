 
#  MODIS Combined 16-Day BAI 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/MCD43A4_006_BAI](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_MCD43A4_006_BAI_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2023-02-10T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/MCD43A4_006_BAI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MCD43A4_006_BAI) 

Cadence
    1 Day 

Tags
    
albedo
bai
brdf
daily
global
mcd43a4
modis
nasa
reflectance
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI#terms-of-use) More
The Burn Area Index (BAI) is generated from the Red and Near-IR bands, and measures the spectral distance of each pixel from a reference spectral point (the measured reflectance of charcoal). This index is intended to emphasize the charcoal signal in post-fire images. See [Chuvieco et al. (2002)](https://www.tandfonline.com/doi/abs/10.1080/01431160210153129) for details. This product is generated from the MODIS/006/MCD43A4 surface reflectance composites.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`BAI` |  463.313 meters  | Burn Area Index  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/MCD43A4_006_BAI')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
varscaled=dataset.select('BAI');
varscaledVis={
min:0.0,
max:100.0,
};
Map.setCenter(-7.03125,31.0529339857,2);
Map.addLayer(scaled,scaledVis,'Scaled');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_MCD43A4_006_BAI)
[ MODIS Combined 16-Day BAI ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI)
The Burn Area Index (BAI) is generated from the Red and Near-IR bands, and measures the spectral distance of each pixel from a reference spectral point (the measured reflectance of charcoal). This index is intended to emphasize the charcoal signal in post-fire images. See Chuvieco et al. (2002) for details. …
MODIS/MCD43A4_006_BAI, albedo,bai,brdf,daily,global,mcd43a4,modis,nasa,reflectance,usgs,vegetation-indices 
2000-02-24T00:00:00Z/2023-02-10T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_MCD43A4_006_BAI)


