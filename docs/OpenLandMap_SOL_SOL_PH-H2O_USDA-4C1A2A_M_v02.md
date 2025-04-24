 
#  OpenLandMap Soil pH in H2O 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02](https://developers.google.com/earth-engine/datasets/images/OpenLandMap/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02_sample.png) 

Dataset Availability
    1950-01-01T00:00:00Z–2018-01-01T00:00:00Z 

Dataset Provider
     [ EnvirometriX Ltd ](https://doi.org/10.5281/zenodo.1475459) 

Earth Engine Snippet
     `    ee.Image("OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenLandMap/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02) 

Tags
     [envirometrix](https://developers.google.com/earth-engine/datasets/tags/envirometrix) [opengeohub](https://developers.google.com/earth-engine/datasets/tags/opengeohub) [openlandmap](https://developers.google.com/earth-engine/datasets/tags/openlandmap) [ph](https://developers.google.com/earth-engine/datasets/tags/ph) [soil](https://developers.google.com/earth-engine/datasets/tags/soil)
[Description](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#dois) More
Soil pH in H2O at 6 standard depths (0, 10, 30, 60, 100 and 200 cm) at 250 m resolution
Processing steps are described in detail [here](https://gitlab.com/openlandmap/global-layers/tree/master/soil). Antarctica is not included.
To access and visualize maps outside of Earth Engine, use [this page](https://opengeohub.org/about-openlandmap).
If you discover a bug, artifact or inconsistency in the LandGIS maps or if you have a question please use the following channels:
  * [Technical issues and questions about the code](https://gitlab.com/openlandmap/global-layers/issues)
  * [General questions and comments](https://disqus.com/home/forums/landgis/)


**Pixel Size** 250 meters 
**Bands**
Name | Min | Max | Scale | Description  
---|---|---|---|---  
`b0` |  42*  |  110*  | 10 | Soil pH in H2O at 0 cm depth  
`b10` |  42*  |  110*  | 10 | Soil pH in H2O at 10 cm depth  
`b30` |  42*  |  110*  | 10 | Soil pH in H2O at 30 cm depth  
`b60` |  42*  |  110*  | 10 | Soil pH in H2O at 60 cm depth  
`b100` |  42*  |  110*  | 10 | Soil pH in H2O at 100 cm depth  
`b200` |  42*  |  110*  | 10 | Soil pH in H2O at 200 cm depth  
* estimated min or max value 
**Terms of Use**
[CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html)
Citations:
  * Tomislav Hengl. (2018). Soil pH in H2O at 6 standard depths (0, 10, 30, 60, 100 and 200 cm) at 250 m resolution (Version v02) [Data set]. Zenodo. [10.5281/zenodo.1475459](https://doi.org/10.5281/zenodo.1475459)


  * [ https://doi.org/10.5281/zenodo.1475459 ](https://doi.org/10.5281/zenodo.1475459)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02#code-editor-javascript-sample) More
```
vardataset=ee.Image('OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02');
varvisualization={
bands:['b0'],
min:42,
max:110,
palette:[
'ff0000','ff1c00','ff3900','ff5500','ff7100','ff8e00',
'ffaa00','ffc600','ffe200','ffff00','e3ff00','c7ff00',
'aaff00','8eff00','72ff00','55ff00','39ff00','1dff00',
'01ff00','00ff1c','00ff38','00ff54','00ff71','00ff8d',
'00ffa9','00ffc6','00ffe2','00fffe','00e3ff','00c7ff',
'00abff','008fff','0072ff','0056ff','003aff','001dff',
'0001ff','1b00ff','3800ff','5400ff',
]
};
Map.centerObject(dataset);
Map.addLayer(dataset,visualization,'Soil pH x 10 in H2O');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenLandMap/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02)
[ OpenLandMap Soil pH in H2O ](https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02)
Soil pH in H2O at 6 standard depths (0, 10, 30, 60, 100 and 200 cm) at 250 m resolution Processing steps are described in detail here. Antarctica is not included. To access and visualize maps outside of Earth Engine, use this page. If you discover a bug, artifact or …
OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02, envirometrix,opengeohub,openlandmap,ph,soil 
1950-01-01T00:00:00Z/2018-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5281/zenodo.1475459 ](https://doi.org/https://doi.org/10.5281/zenodo.1475459)
  * [ https://doi.org/10.5281/zenodo.1475459 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/OpenLandMap_SOL_SOL_PH-H2O_USDA-4C1A2A_M_v02)


