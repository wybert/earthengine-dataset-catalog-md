 
#  GPWv411: Basic Demographic Characteristics (Gridded Population of the World Version 4.11) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CIESIN/GPWv411/GPW_Basic_Demographic_Characteristics](https://developers.google.com/earth-engine/datasets/images/CIESIN/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics_sample.png) 

Dataset Availability
    2000-01-01T00:00:00Z–2020-01-01T00:00:00Z 

Dataset Provider
     [ NASA SEDAC at the Center for International Earth Science Information Network ](https://doi.org/10.7927/H46M34XX) 

Earth Engine Snippet
     `    ee.ImageCollection("CIESIN/GPWv411/GPW_Basic_Demographic_Characteristics")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics) 

Cadence
    5 Years 

Tags
     [ciesin](https://developers.google.com/earth-engine/datasets/tags/ciesin) [gpw](https://developers.google.com/earth-engine/datasets/tags/gpw) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [population](https://developers.google.com/earth-engine/datasets/tags/population)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#dois) More
This dataset contains population estimates, by age and sex, per 30 arc-second grid cell consistent with national censuses and population registers. There is one image for each modeled age and sex category based on the 2010 round of Census.
[General Documentation](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/docs)
The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1 km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year.
**Pixel Size** 927.67 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`basic_demographic_characteristics` |  0*  |  140852*  | The estimated number of persons, by age and sex, per 30 arc-second grid cell.  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
Sex | STRING | The sex of a population subgroup.  
Age_Group | STRING | The age range of a population subgroup.  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Center for International Earth Science Information Network - CIESIN - Columbia University. 2018. Gridded Population of the World, Version 4 (GPWv4): Basic Characteristics, Revision 11. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). [doi:10.7927/H46M34XX](https://doi.org/10.7927/H46M34XX). Accessed DAY MONTH YEAR.


  * [ https://doi.org/10.7927/H46M34XX ](https://doi.org/10.7927/H46M34XX)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('CIESIN/GPWv411/GPW_Basic_Demographic_Characteristics').first();
varraster=dataset.select('basic_demographic_characteristics');
varraster_vis={
'max':1000.0,
'palette':[
'ffffe7',
'86a192',
'509791',
'307296',
'2c4484',
'000066'
],
'min':0.0
};
Map.setCenter(79.1,19.81,3);
Map.addLayer(raster,raster_vis,'basic_demographic_characteristics');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics)
[ GPWv411: Basic Demographic Characteristics (Gridded Population of the World Version 4.11) ](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics)
This dataset contains population estimates, by age and sex, per 30 arc-second grid cell consistent with national censuses and population registers. There is one image for each modeled age and sex category based on the 2010 round of Census. General Documentation The Gridded Population of World Version 4 (GPWv4), Revision …
CIESIN/GPWv411/GPW_Basic_Demographic_Characteristics, ciesin,gpw,nasa,population 
2000-01-01T00:00:00Z/2020-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7927/H46M34XX ](https://doi.org/https://doi.org/10.7927/H46M34XX)
  * [ https://doi.org/10.7927/H46M34XX ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Basic_Demographic_Characteristics)


