 
#  Breathing Earth System Simulator (BESS) Radiation v1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![SNU/ESL/BESS/Rad/v1](https://developers.google.com/earth-engine/datasets/images/SNU/SNU_ESL_BESS_Rad_v1_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2021-12-31T00:00:00Z 

Dataset Provider
     [ Seoul National University (SNU) ](https://www.environment.snu.ac.kr/bess-rad) 

Earth Engine Snippet
     `    ee.ImageCollection("SNU/ESL/BESS/Rad/v1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/SNU/SNU_ESL_BESS_Rad_v1) 

Cadence
    1 Day 

Tags
     [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [evapotranspiration](https://developers.google.com/earth-engine/datasets/tags/evapotranspiration) [gpp](https://developers.google.com/earth-engine/datasets/tags/gpp) [modis-derived](https://developers.google.com/earth-engine/datasets/tags/modis-derived) [par](https://developers.google.com/earth-engine/datasets/tags/par) [radiation](https://developers.google.com/earth-engine/datasets/tags/radiation) [shortwave](https://developers.google.com/earth-engine/datasets/tags/shortwave)
[Description](https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1#terms-of-use) More
Breathing Earth System Simulator (BESS) is a simplified process-based model that couples atmosphere and canopy radiative transfers, canopy photosynthesis, transpiration, and energy balance. It couples an atmospheric radiative transfer model and artificial neural network with forcings from MODIS atmospheric products to generate 5-km daily products.
Publications:
  * Ryu Youngryel, Chongya Jiang, Hideki Kobayashi, Matteo Detto, MODIS-derived global land products of shortwave radiation and diffuse and total photosynthetically active radiation at 5km resolution from 2000. Remote Sensing of Environment, Volume 204, 2018. [doi:10.1016/j.rse.2017.09.021](https://doi.org/10.1016/j.rse.2017.09.021)


**Pixel Size** 5500 meters 
**Bands**
Name | Units | Description  
---|---|---  
`PAR_Daily` | W/m^2 | Surface downwelling photosynthetic radiative flux in air  
`PARdiff_Daily` | W/m^2 | Surface diffuse downwelling photosynthetic radiative flux in air  
`RSDN_Daily` | W/m^2 | Surface downwelling shortwave flux in air  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('SNU/ESL/BESS/Rad/v1');
varvisParams={
bands:['PAR_Daily'],
min:0,
max:70,
palette:['black','purple','blue','yellow','orange','red']
};
Map.setCenter(2.1,24.9,3);
Map.addLayer(
dataset,visParams,
'Surface downwelling photosynthetic radiative flux (W/m^2)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/SNU/SNU_ESL_BESS_Rad_v1)
[ Breathing Earth System Simulator (BESS) Radiation v1 ](https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1)
Breathing Earth System Simulator (BESS) is a simplified process-based model that couples atmosphere and canopy radiative transfers, canopy photosynthesis, transpiration, and energy balance. It couples an atmospheric radiative transfer model and artificial neural network with forcings from MODIS atmospheric products to generate 5-km daily products. Publications: Ryu Youngryel, Chongya Jiang, …
SNU/ESL/BESS/Rad/v1, climate,evapotranspiration,gpp,modis-derived,par,radiation,shortwave 
2001-01-01T00:00:00Z/2021-12-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.environment.snu.ac.kr/bess-rad)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/SNU_ESL_BESS_Rad_v1)


