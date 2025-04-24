 
#  AHN Netherlands 0.5m DEM, Non-Interpolated 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![AHN/AHN2_05M_NON](https://developers.google.com/earth-engine/datasets/images/AHN/AHN_AHN2_05M_NON_sample.png) 

Dataset Availability
    2012-01-01T00:00:00Z–2012-01-01T00:00:00Z 

Dataset Provider
     [ AHN ](https://www.ahn.nl) 

Earth Engine Snippet
     `    ee.Image("AHN/AHN2_05M_NON")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AHN/AHN_AHN2_05M_NON) 

Tags
     [ahn](https://developers.google.com/earth-engine/datasets/tags/ahn) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [lidar](https://developers.google.com/earth-engine/datasets/tags/lidar) [netherlands](https://developers.google.com/earth-engine/datasets/tags/netherlands)
[Description](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON#terms-of-use) More
The AHN DEM is a 0.5m DEM covering the Netherlands. It was generated from LIDAR data taken in the spring between 2007 and 2012.
It contains ground level samples with all other items above ground (such as buildings, bridges, trees etc.) removed. This version is non-interpolated; the areas where objects have been removed are left blank and not filled with interpolated values. The point cloud was converted to a 0.5m grid using a squared inverse distance weighting method.
**Pixel Size** 0.5 meters 
**Bands**
Name | Units | Description  
---|---|---  
`elevation` | m | Elevation  
**Terms of Use**
The datasets of the AHN are available as Open Data. This means that the data can be used by anyone for free and without restrictions. For more information visit the [Open Data](https://www.ahn.nl/open-data/) page. Downloads are available under the terms of the [CC-0 license](https://data.overheid.nl/licenties-voor-hergebruik).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON#code-editor-javascript-sample) More
```
vardataset=ee.Image('AHN/AHN2_05M_NON');
varelevation=dataset.select('elevation');
varelevationVis={
min:-5.0,
max:30.0,
};
Map.setCenter(5.80258,51.78547,14);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AHN/AHN_AHN2_05M_NON)
[ AHN Netherlands 0.5m DEM, Non-Interpolated ](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON)
The AHN DEM is a 0.5m DEM covering the Netherlands. It was generated from LIDAR data taken in the spring between 2007 and 2012. It contains ground level samples with all other items above ground (such as buildings, bridges, trees etc.) removed. This version is non-interpolated; the areas where objects …
AHN/AHN2_05M_NON, ahn,dem,elevation,elevation-topography,geophysical,lidar,netherlands 
2012-01-01T00:00:00Z/2012-01-01T00:00:00Z
50.74 3.35 53.55 7.24 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.ahn.nl)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN2_05M_NON)


