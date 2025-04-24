 
#  FAO GAUL 500m Simplified: Global Administrative Unit Layers 2015, Country Boundaries 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![FAO/GAUL_SIMPLIFIED_500m/2015/level0](https://developers.google.com/earth-engine/datasets/images/FAO/FAO_GAUL_SIMPLIFIED_500m_2015_level0_sample.png) 

Dataset Availability
    2014-12-19T16:45:00Z–2014-12-19T16:45:00Z 

Dataset Provider
     [ FAO UN ](http://www.fao.org/geonetwork/srv/en/metadata.show?id=12691) 

Earth Engine Snippet
     `    ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_GAUL_SIMPLIFIED_500m_2015_level0) 

Tags
     [borders](https://developers.google.com/earth-engine/datasets/tags/borders) [countries](https://developers.google.com/earth-engine/datasets/tags/countries) [fao](https://developers.google.com/earth-engine/datasets/tags/fao) [gaul](https://developers.google.com/earth-engine/datasets/tags/gaul) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [table](https://developers.google.com/earth-engine/datasets/tags/table) [un](https://developers.google.com/earth-engine/datasets/tags/un)
[Description](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0#terms-of-use) More
This version of GAUL dataset is simplified at 500m.
The Global Administrative Unit Layers (GAUL) compiles and disseminates the best available information on administrative units for all the countries in the world, providing a contribution to the standardization of the spatial dataset representing administrative units. The GAUL always maintains global layers with a unified coding system at country, first (e.g. departments), and second administrative levels (e.g. districts). Where data is available, it provides layers on a country by country basis down to third, fourth, and lowers levels. The overall methodology consists in a) collecting the best available data from most reliable sources, b) establishing validation periods of the geographic features (when possible), c) adding selected data to the global layer based on the last country boundaries map provided by the UN Cartographic Unit (UNCS), d) generating codes using GAUL Coding System, and e) distribute data to the users (see [Technical Aspects of the GAUL Distribution Set](https://sgst.wr.usgs.gov/gfsad30/FAO_GUAL/TechnicalAspectsGAUL2015_Doc1.pdf)). Note that some administrative units are multipolygon features.
**Table Schema**
Name | Type | Description  
---|---|---  
ADM0_CODE | INT | GAUL country code  
ADM0_NAME | STRING | UN country name  
DISP_AREA | STRING | Unsettled territory: 'Yes' or 'No'  
STATUS | STRING | Status of the country  
Shape_Area | DOUBLE | Shape area  
Shape_Leng | DOUBLE | Shape length  
EXP0_YEAR | INT | Expiry year of the administrative unit  
STR0_YEAR | INT | Creation year of the administrative unit  
**Terms of Use**
The GAUL dataset is distributed to the United Nations and other authorized international and national institutions/agencies. FAO grants a license to use, download and print the materials contained in the GAUL dataset solely for non-commercial purposes and in accordance with the conditions specified in the data license. [The full GAUL Data License document](https://developers.google.com/earth-engine/datasets/catalog/DataLicenseGAUL2015.pdf) is available for downloading. See also [the disclaimer](https://developers.google.com/earth-engine/datasets/catalog/DisclaimerGAUL2015.pdf).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('FAO/GAUL_SIMPLIFIED_500m/2015/level0');
Map.setCenter(7.82,49.1,4);
varstyleParams={
fillColor:'b5ffb4',
color:'00909F',
width:1.0,
};
dataset=dataset.style(styleParams);
Map.addLayer(dataset,{},'Country Boundaries');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/FAO/FAO_GAUL_SIMPLIFIED_500m_2015_level0)
[ FAO GAUL 500m Simplified: Global Administrative Unit Layers 2015, Country Boundaries ](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0)
This version of GAUL dataset is simplified at 500m. The Global Administrative Unit Layers (GAUL) compiles and disseminates the best available information on administrative units for all the countries in the world, providing a contribution to the standardization of the spatial dataset representing administrative units. The GAUL always maintains global …
FAO/GAUL_SIMPLIFIED_500m/2015/level0, borders,countries,fao,gaul,infrastructure-boundaries,table,un 
2014-12-19T16:45:00Z/2014-12-19T16:45:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/http://www.fao.org/geonetwork/srv/en/metadata.show?id=12691)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_SIMPLIFIED_500m_2015_level0)


