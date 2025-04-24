 
#  SoilGrids250m 2.0 - Volumetric Water Content 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![ISRIC/SoilGrids250m/v20](https://developers.google.com/earth-engine/datasets/images/ISRIC/ISRIC_SoilGrids250m_v20_sample.png) 

Dataset Availability
    1905-04-01T00:00:00Z–2016-07-05T00:00:00Z 

Dataset Provider
     [ ISRIC - World Soil Information ](https://www.isric.org/explore/soilgrids) 

Earth Engine Snippet
     `    ee.ImageCollection("ISRIC/SoilGrids250m/v20")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ISRIC/ISRIC_SoilGrids250m_v20) 

Tags
     [soil](https://developers.google.com/earth-engine/datasets/tags/soil) [soil-moisture](https://developers.google.com/earth-engine/datasets/tags/soil-moisture) [water](https://developers.google.com/earth-engine/datasets/tags/water)
[Description](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#dois) More
Volumetric Water Content at 10kPa, 33kPa, and 1500kPa suction in 10^-3 cm^3/cm^3 (0.1 v% or 1 mm/m) at 6 standard depths (0-5cm, 5-15cm, 15-30cm, 30-60cm, 60-100cm, 100-200cm). Predictions were derived using a digital soil mapping approach based on Quantile Random Forest, drawing on a global compilation of soil profile data and environmental layers. This dataset includes predictions for three different suction levels, providing insights into soil water availability.
Documentation:
  * [Scientific Paper](https://www.sciencedirect.com/science/article/pii/S2095633922000636?via%3Dihub)


**Pixel Size** 250 meters 
**Bands**
Name | Units | Description  
---|---|---  
`wv0010_0-5cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (0-5cm depth)  
`wv0010_5-15cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (5-15cm depth)  
`wv0010_15-30cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (15-30cm depth)  
`wv0010_30-60cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (30-60cm depth)  
`wv0010_60-100cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (60-100cm depth)  
`wv0010_100-200cm` | cm^3/cm^3 | Volumetric Water Content at 10kPa (100-200cm depth)  
`wv0033_0-5cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (0-5cm depth)  
`wv0033_5-15cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (5-15cm depth)  
`wv0033_15-30cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (15-30cm depth)  
`wv0033_30-60cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (30-60cm depth)  
`wv0033_60-100cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (60-100cm depth)  
`wv0033_100-200cm` | cm^3/cm^3 | Volumetric Water Content at 33kPa (100-200cm depth)  
`wv1500_0-5cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (0-5cm depth)  
`wv1500_5-15cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (5-15cm depth)  
`wv1500_15-30cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (15-30cm depth)  
`wv1500_30-60cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (30-60cm depth)  
`wv1500_60-100cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (60-100cm depth)  
`wv1500_100-200cm` | cm^3/cm^3 | Volumetric Water Content at 1500kPa (100-200cm depth)  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Global mapping of volumetric water retention at 100, 330 and 15000 cm suction using the WoSIS database Turek M.E., Poggio L., Batjes N.H., Armindo R.A., de Jong van Lier Q., de Sousa L., Heuvelink G.B.M. (2023) International Soil and Water Conservation Research, 11 (2), pp. 225-239.


  * [ https://doi.org/10.1016/j.iswcr.2022.08.001 ](https://doi.org/10.1016/j.iswcr.2022.08.001)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20#code-editor-javascript-sample) More
```
vardataset=ee.Image('ISRIC/SoilGrids250m/v20/Q0_95').select('wv0010_0-5cm');
Map.setCenter(-105.25,52.5,3);
Map.addLayer(
dataset,{
min:-61,
max:636,
palette:[
'#440154','#482878','#3E4A89','#31688E','#26828E','#1F9E89',
'#35B779','#6DCD59','#B4DE2C','#FDE725'
]
},
'SoilGrids250m 10kPa Q0.95');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ISRIC/ISRIC_SoilGrids250m_v20)
[ SoilGrids250m 2.0 - Volumetric Water Content ](https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20)
Volumetric Water Content at 10kPa, 33kPa, and 1500kPa suction in 10^-3 cm^3/cm^3 (0.1 v% or 1 mm/m) at 6 standard depths (0-5cm, 5-15cm, 15-30cm, 30-60cm, 60-100cm, 100-200cm). Predictions were derived using a digital soil mapping approach based on Quantile Random Forest, drawing on a global compilation of soil profile data …
ISRIC/SoilGrids250m/v20, soil,soil-moisture,water 
1905-04-01T00:00:00Z/2016-07-05T00:00:00Z
-56 -180 84 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1016/j.iswcr.2022.08.001 ](https://doi.org/https://www.isric.org/explore/soilgrids)
  * [ https://doi.org/10.1016/j.iswcr.2022.08.001 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ISRIC_SoilGrids250m_v20)


