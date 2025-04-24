 
#  Tree proximate people (TPP) 1.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![FAO/SOFO/1/TPP](https://developers.google.com/earth-engine/datasets/images/FAO/FAO_SOFO_1_TPP_sample.png) 

Dataset Availability
    2019-01-01T00:00:00Z–2019-01-01T00:00:00Z 

Dataset Provider
     [ FAO Forestry Division (TPP 500m cropland) ](https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b8) [ FAO Forestry Division (TPP 1km cropland) ](https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b6) [ FAO Forestry Division (TPP 500m agricultural) ](https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b7) [ FAO Forestry Division (TPP 1km agricultural) ](https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b3) 

Earth Engine Snippet
     `    ee.ImageCollection("FAO/SOFO/1/TPP")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_SOFO_1_TPP) 

Cadence
    1 Year 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [fao](https://developers.google.com/earth-engine/datasets/tags/fao) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [global](https://developers.google.com/earth-engine/datasets/tags/global) [plant-productivity](https://developers.google.com/earth-engine/datasets/tags/plant-productivity) [population](https://developers.google.com/earth-engine/datasets/tags/population) [rural-area](https://developers.google.com/earth-engine/datasets/tags/rural-area)
[Description](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#dois) More
The "Tree Proximate People" (TPP) is one of the datasets contributing to the development of indicator #13, number of forest-dependent people in extreme poverty, of the Collaborative Partnership on Forests (CPF) Global Core Set of forest-related indicators (GCS). The TPP dataset provides 4 different estimates of tree proximate people (trees outside forests), all of them for the year 2019 with a pixel size of 100 meters at a global level. [Find out more about the dataset.](https://data.apps.fao.org/catalog/dcat/tree-proximate-people)
**Pixel Size** 0.0009 meters 
**Bands**
Name | Units | Description  
---|---|---  
`TPP_1km` | Number of people/ha | Number of people living in or within 1 km from agricultural lands with at least 10% of tree cover  
`TPP_1km_cropland` | Number of people/ha | Number of people living in or within 1 km from croplands with at least 10% of tree cover  
`TPP_500m` | Number of people/ha | Number of people living in or within 500 m from agricultural lands with at least 10% of tree cover  
`TPP_500m_cropland` | Number of people/ha | Number of people living in or within 500 m from croplands with at least 10% of tree cover  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * FAO 2022. The State of the World's Forests (SOFO) - Forest pathways for green recovery and building inclusive, resilient and sustainable economies. FAO, Rome. <https://www.fao.org/documents/card/en/c/cb9360en>
  * Newton, P., Castle, S.E., Kinzer, A.T., Miller, D.C., Oldekop, J.A., Linhares-Juvenal, T., Pina, L., Madrid, M., & de Lamo, J. 2022. The number of forest- and tree-proximate people: a new methodology and global estimates, One Earth, 2020 [doi:10.1016/j.oneear.2020.08.016](https://doi.org/10.1016/j.oneear.2020.08.016),


  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/10.1016/j.oneear.2020.08.016)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP#code-editor-javascript-sample) More
```
varcoll=ee.ImageCollection('FAO/SOFO/1/TPP');
varimage=coll.first().select('TPP_1km');
Map.setCenter(17.5,20,3);
Map.addLayer(
image,{min:0,max:12,palette:['blue','yellow','red']},
'Tree proximate people – 1km cutoff distance');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_SOFO_1_TPP)
[ Tree proximate people (TPP) 1.0 ](https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP)
The "Tree Proximate People" (TPP) is one of the datasets contributing to the development of indicator #13, number of forest-dependent people in extreme poverty, of the Collaborative Partnership on Forests (CPF) Global Core Set of forest-related indicators (GCS). The TPP dataset provides 4 different estimates of tree proximate people (trees …
FAO/SOFO/1/TPP, agriculture,fao,forest,global,plant-productivity,population,rural-area 
2019-01-01T00:00:00Z/2019-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b8)
  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b6)
  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b7)
  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/https://data.apps.fao.org/catalog/iso/8ed893bd-842a-4866-a655-a0a0c02b79b3)
  * [ https://doi.org/10.1016/j.oneear.2020.08.016 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/FAO_SOFO_1_TPP)


