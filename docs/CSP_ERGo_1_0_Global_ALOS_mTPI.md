 
#  Global ALOS mTPI (Multi-Scale Topographic Position Index) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CSP/ERGo/1_0/Global/ALOS_mTPI](https://developers.google.com/earth-engine/datasets/images/CSP/CSP_ERGo_1_0_Global_ALOS_mTPI_sample.png) 

Dataset Availability
    2006-01-24T00:00:00Z–2011-05-13T00:00:00Z 

Dataset Provider
     [ Conservation Science Partners ](https://www.csp-inc.org/) 

Earth Engine Snippet
     `    ee.Image("CSP/ERGo/1_0/Global/ALOS_mTPI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSP/CSP_ERGo_1_0_Global_ALOS_mTPI) 

Tags
     [aspect](https://developers.google.com/earth-engine/datasets/tags/aspect) [csp](https://developers.google.com/earth-engine/datasets/tags/csp) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [ergo](https://developers.google.com/earth-engine/datasets/tags/ergo) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [global](https://developers.google.com/earth-engine/datasets/tags/global) [landforms](https://developers.google.com/earth-engine/datasets/tags/landforms) [slope](https://developers.google.com/earth-engine/datasets/tags/slope) [topography](https://developers.google.com/earth-engine/datasets/tags/topography)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI#citations) More
The mTPI distinguishes ridge from valley forms. It is calculated using elevation data for each location subtracted by the mean elevation within a neighborhood. mTPI uses moving windows of radius (km): 115.8, 89.9, 35.5, 13.1, 5.6, 2.8, and 1.2. It is based on the 30m "AVE" band of JAXA's ALOS DEM (available in EE as JAXA/ALOS/AW3D30_V1_1).
The Conservation Science Partners (CSP) Ecologically Relevant Geomorphology (ERGo) Datasets, Landforms and Physiography contain detailed, multi-scale data on landforms and physiographic (aka land facet) patterns. Although there are many potential uses of these data, the original purpose for these data was to develop an ecologically relevant classification and map of landforms and physiographic classes that are suitable for climate adaptation planning. Because there is large uncertainty associated with future climate conditions and even more uncertainty around ecological responses, providing information about what is unlikely to change offers a strong foundation for managers to build robust climate adaptation plans. The quantification of these features of the landscape is sensitive to the resolution, so we provide the highest resolution possible given the extent and characteristics of a given index.
**Pixel Size** 270 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`AVE` | m |  -3758*  |  10963*  | ALOS-derived mTPI ranging from negative (valleys) to positive (ridges) values  
* estimated min or max value 
**Terms of Use**
[CC-BY-NC-SA-4.0](https://spdx.org/licenses/CC-BY-NC-SA-4.0.html)
Citations:
  * Theobald, D. M., Harrison-Atlas, D., Monahan, W. B., & Albano, C. M. (2015). Ecologically-relevant maps of landforms and physiographic diversity for climate adaptation planning. PloS one, 10(12), [e0143619](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0143619)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI#code-editor-javascript-sample) More
```
vardataset=ee.Image('CSP/ERGo/1_0/Global/ALOS_mTPI');
varalosMtpi=dataset.select('AVE');
varalosMtpiVis={
min:-200.0,
max:200.0,
palette:['0b1eff','4be450','fffca4','ffa011','ff0000'],
};
Map.setCenter(-105.8636,40.3439,11);
Map.addLayer(alosMtpi,alosMtpiVis,'ALOS mTPI');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSP/CSP_ERGo_1_0_Global_ALOS_mTPI)
[ Global ALOS mTPI (Multi-Scale Topographic Position Index) ](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI)
The mTPI distinguishes ridge from valley forms. It is calculated using elevation data for each location subtracted by the mean elevation within a neighborhood. mTPI uses moving windows of radius (km): 115.8, 89.9, 35.5, 13.1, 5.6, 2.8, and 1.2. It is based on the 30m "AVE" band of JAXA's ALOS …
CSP/ERGo/1_0/Global/ALOS_mTPI, aspect,csp,elevation,elevation-topography,ergo,geophysical,global,landforms,slope,topography 
2006-01-24T00:00:00Z/2011-05-13T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.csp-inc.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_Global_ALOS_mTPI)


