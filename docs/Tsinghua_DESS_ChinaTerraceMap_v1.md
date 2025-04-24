 
#  DESS China Terrace Map v1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Tsinghua/DESS/ChinaTerraceMap/v1](https://developers.google.com/earth-engine/datasets/images/Tsinghua/Tsinghua_DESS_ChinaTerraceMap_v1_sample.png) 

Dataset Availability
    2018-01-01T00:00:00Z–2019-01-01T00:00:00Z 

Dataset Provider
     [ Department of Earth System Science, Tsinghua University (DESS, THU) ](https://essd.copernicus.org/articles/13/2437/2021/) 

Earth Engine Snippet
     `    ee.Image("Tsinghua/DESS/ChinaTerraceMap/v1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Tsinghua/Tsinghua_DESS_ChinaTerraceMap_v1) 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landuse](https://developers.google.com/earth-engine/datasets/tags/landuse) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [tsinghua](https://developers.google.com/earth-engine/datasets/tags/tsinghua)
china
dess
terrace
[Description](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#dois) More
This dataset is a China terrace map at 30 m resolution in 2018. It was developed through supervised pixel-based classification using multisource and multi-temporal data based on the Google Earth Engine platform. The overall accuracy and kappa coefficient achieved 94% and 0.72, respectively. This first 30 m China terrace map can be used for studies on soil erosion, food security, biogeochemical cycle, biodiversity, and ecosystem service assessments.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`terrace` |  30 meters  | 1 when a terrace is present, 0 when it is not.  
**terrace Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | No terraces  
1 | #a3ff74 | Terraces present  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Cao, B., Yu, L., Naipal, V., Ciais, P., Li, W., Zhao, Y., Wei, W., Chen, D., Liu, Z., and Gong, P.: A 30 m terrace mapping in China using Landsat 8 imagery and digital elevation model based on the Google Earth Engine, Earth Syst. Sci. Data, 13, 2437-2456, [doi:10.5194/essd-13-2437-2021](https://doi.org/10.5194/essd-13-2437-2021), 2021.


  * [ https://doi.org/10.5194/essd-13-2437-2021 ](https://doi.org/10.5194/essd-13-2437-2021)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1#code-editor-javascript-sample) More
```
varimage=ee.Image('Tsinghua/DESS/ChinaTerraceMap/v1');
varimage=image.updateMask(image);
Map.addLayer(image,{min:0,max:1,palette:['a3ff74']},'Terraces');
Map.setCenter(106.6,30.4,10);
Map.setOptions('SATELLITE');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Tsinghua/Tsinghua_DESS_ChinaTerraceMap_v1)
[ DESS China Terrace Map v1 ](https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1)
This dataset is a China terrace map at 30 m resolution in 2018. It was developed through supervised pixel-based classification using multisource and multi-temporal data based on the Google Earth Engine platform. The overall accuracy and kappa coefficient achieved 94% and 0.72, respectively. This first 30 m China terrace map …
Tsinghua/DESS/ChinaTerraceMap/v1, agriculture,landcover,landuse,landuse-landcover,tsinghua 
2018-01-01T00:00:00Z/2019-01-01T00:00:00Z
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/essd-13-2437-2021 ](https://doi.org/https://essd.copernicus.org/articles/13/2437/2021/)
  * [ https://doi.org/10.5194/essd-13-2437-2021 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Tsinghua_DESS_ChinaTerraceMap_v1)


