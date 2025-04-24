 
#  USGS 3DEP 10m National Map Seamless (1/3 Arc-Second) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/3DEP/10m](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_3DEP_10m_sample.png) 

Dataset Availability
    1998-08-16T00:00:00Z–2020-05-06T00:00:00Z 

Dataset Provider
     [ United States Geological Survey ](https://www.usgs.gov/core-science-systems/ngp/3dep/about-3dep-products-services) 

Earth Engine Snippet
     `    ee.Image("USGS/3DEP/10m")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_3DEP_10m) 

Tags
     [3dep](https://developers.google.com/earth-engine/datasets/tags/3dep) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [topography](https://developers.google.com/earth-engine/datasets/tags/topography) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m#citations) More
This is the seamless 3DEP DEM dataset for the U.S. with full coverage of the 48 conterminous states, Hawaii, and U.S. territories. Alaska coverage is partially available now and is being expanded to statewide coverage as part of the Alaska Mapping Initiative. Ground spacing is approximately 10 meters north/south, but variable east/west due to convergence of meridians with latitude.
Spatial metadata dataset is ingested as a separate asset [USGS_3DEP_10m_metadata](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m_metadata).
The 1m dataset is ingested as [USGS_3DEP_1m](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_1m).
Dataset uploaded by [Farmers Business Network](https://fbn.com).
**Bands**
Name | Units | Pixel Size | Description  
---|---|---|---  
`elevation` | m |  10.2 meters  | Elevation  
**Terms of Use**
Most U.S. Geological Survey (USGS) information resides in the public domain and may be used without restriction. Additional information on [Acknowledging or Crediting USGS as Information Source](https://www.usgs.gov/information-policies-and-instructions/crediting-usgs) is available.
Citations:
  * U.S. Geological Survey, 3D Elevation Program 10-Meter Resolution Digital Elevation Model.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m#code-editor-javascript-sample) More
```
vardataset=ee.Image('USGS/3DEP/10m')
varelevation=dataset.select('elevation');
varslope=ee.Terrain.slope(elevation);
Map.setCenter(-112.8598,36.2841,10);
Map.addLayer(elevation,{min:0,max:3000,palette:[
'3ae237','b5e22e','d6e21f','fff705','ffd611','ffb613','ff8b13',
'ff6e08','ff500d','ff0000','de0101','c21301','0602ff','235cb1',
'307ef3','269db1','30c8e2','32d3ef','3be285','3ff38f','86e26f'
],
},'elevation');
Map.addLayer(slope,{min:0,max:60},'slope');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_3DEP_10m)
[ USGS 3DEP 10m National Map Seamless (1/3 Arc-Second) ](https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m)
This is the seamless 3DEP DEM dataset for the U.S. with full coverage of the 48 conterminous states, Hawaii, and U.S. territories. Alaska coverage is partially available now and is being expanded to statewide coverage as part of the Alaska Mapping Initiative. Ground spacing is approximately 10 meters north/south, but …
USGS/3DEP/10m, 3dep,dem,elevation,elevation-topography,geophysical,topography,usgs 
1998-08-16T00:00:00Z/2020-05-06T00:00:00Z
-16.6 -171 76.9 164 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/core-science-systems/ngp/3dep/about-3dep-products-services)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m)


