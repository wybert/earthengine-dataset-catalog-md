 
#  GPWv411: Adjusted to Match 2015 Revision of UN WPP Country Totals (Gridded Population of the World Version 4.11) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
![CIESIN/GPWv411/GPW_UNWPP-Adjusted_Population_Count](https://developers.google.com/earth-engine/datasets/images/CIESIN/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count_sample.png) 

Dataset Availability
    2000-01-01T00:00:00Z–2020-01-01T00:00:00Z 

Dataset Provider
     [ NASA SEDAC at the Center for International Earth Science Information Network ](https://doi.org/10.7927/H4PN93PB) 

Earth Engine Snippet
     `    ee.ImageCollection("CIESIN/GPWv411/GPW_UNWPP-Adjusted_Population_Count")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count) 

Cadence
    5 Years 

Tags
     [ciesin](https://developers.google.com/earth-engine/datasets/tags/ciesin) [gpw](https://developers.google.com/earth-engine/datasets/tags/gpw) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [population](https://developers.google.com/earth-engine/datasets/tags/population)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#dois) More
This dataset contains estimates of the number of persons per 30 arc-second grid cell, consistent with national censuses and population registers with respect to relative spatial distribution but adjusted to match the 2015 Revision of UN World Population Prospects country totals. There is one image for each modeled year.
[General Documentation](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-density-rev11/docs)
**Note:** Because this collection has a pyramid policy of MEAN, zooming out results in information loss. Calculations need to be performed at native resolution.
The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1 km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year.
**Pixel Size** 927.67 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`unwpp-adjusted_population_count` |  0*  |  602380*  | The estimated number of persons per 30 arc-second grid cell.  
* estimated min or max value 
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Center for International Earth Science Information Network - CIESIN - Columbia University. 2018. Gridded Population of the World, Version 4 (GPWv4): Population Count Adjusted to Match 2015 Revision of UN WPP Country Totals, Revision 11. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). <https://doi.org/10.7927/H4PN93PB>. Accessed DAY MONTH YEAR.


  * [ https://doi.org/10.7927/H4PN93PB ](https://doi.org/10.7927/H4PN93PB)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('CIESIN/GPWv411/GPW_UNWPP-Adjusted_Population_Count').first();
varraster=dataset.select('unwpp-adjusted_population_count');
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
Map.addLayer(raster,raster_vis,'unwpp-adjusted_population_count');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count)
[ GPWv411: Adjusted to Match 2015 Revision of UN WPP Country Totals (Gridded Population of the World Version 4.11) ](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count)
This dataset contains estimates of the number of persons per 30 arc-second grid cell, consistent with national censuses and population registers with respect to relative spatial distribution but adjusted to match the 2015 Revision of UN World Population Prospects country totals. There is one image for each modeled year. General …
CIESIN/GPWv411/GPW_UNWPP-Adjusted_Population_Count, ciesin,gpw,nasa,population 
2000-01-01T00:00:00Z/2020-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7927/H4PN93PB ](https://doi.org/https://doi.org/10.7927/H4PN93PB)
  * [ https://doi.org/10.7927/H4PN93PB ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_UNWPP-Adjusted_Population_Count)


