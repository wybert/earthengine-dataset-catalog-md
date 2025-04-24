 
#  NOAA CDR OISST v02r01: Optimum Interpolation Sea Surface Temperature 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/CDR/OISST/V2_1](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_CDR_OISST_V2_1_sample.png) 

Dataset Availability
    1981-09-01T00:00:00Z–2025-04-19T00:00:00Z 

Dataset Provider
     [ NOAA ](https://www.ncei.noaa.gov/products/optimum-interpolation-sst) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/CDR/OISST/V2_1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_CDR_OISST_V2_1) 

Cadence
    1 Day 

Tags
     [avhrr](https://developers.google.com/earth-engine/datasets/tags/avhrr) [cdr](https://developers.google.com/earth-engine/datasets/tags/cdr) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [ice](https://developers.google.com/earth-engine/datasets/tags/ice) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans) [oisst](https://developers.google.com/earth-engine/datasets/tags/oisst) [sst](https://developers.google.com/earth-engine/datasets/tags/sst) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature)
real-time
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#dois) More
The NOAA 1/4 degree daily Optimum Interpolation Sea Surface Temperature (OISST) provides complete ocean temperature fields constructed by combining bias-adjusted observations from different platforms (satellite, ships, buoys) on a regular global grid, with gaps filled in by interpolation. Satellite data from the Advanced Very High Resolution Radiometer (AVHRR) provides the main input which permits the high temporal-spatial coverage beginning in late 1981 to the present.
The OISST dataset has a single day's data processed twice. First a near real-time preliminary version is released with a lag of 1 day, and a final version with a lag of 14 days. The final version uses extra days for smoothing, and zonal bias correction in addition to replacing the preliminary version.
**Pixel Size** 27830 meters 
**Bands**
Name | Units | Min | Max | Scale | Description  
---|---|---|---|---|---  
`sst` | °C |  -180*  |  3764*  | 0.01 | Daily sea surface temperature  
`anom` | °C |  -1887*  |  1902*  | 0.01 | Temperature anomaly; the daily OISST minus a 30-year climatological mean.  
`ice` | % |  1*  |  100*  | 0.01 | Seven-day median of daily sea ice concentrations.  
`err` | °C |  11*  |  171*  | 0.01 | Estimated error; standard deviation of analyzed sea surface temperature.  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
status | STRING | 'provisional' or 'permanent'  
**Terms of Use**
The NOAA CDR Program's official distribution point for CDRs is NOAA's National Climatic Data Center which provides sustained, open access and active data management of the CDR packages and related information in keeping with the United States' open data policies and practices as described in the President's Memorandum on "Open Data Policy" and pursuant to the Executive Order of May 9, 2013, "Making Open and Machine Readable the New Default for Government Information". In line with these policies, the CDR data sets are nonproprietary, publicly available, and no restrictions are placed upon their use. For more information, see the [Fair Use of NOAA's CDR Data Sets, Algorithms and Documentation](https://www1.ncdc.noaa.gov/pub/data/sds/cdr/CDRs/Aerosol_Optical_Thickness/UseAgreement_01B-04.pdf) pdf.
Citations:
  * Richard W. Reynolds, Viva F. Banzon, and NOAA CDR Program (2008): NOAA Optimum Interpolation 1/4 Degree Daily Sea Surface Temperature (OISST) Analysis, Version 2. [indicate subset used]. NOAA National Centers for Environmental Information. [doi:10.7289/V5SQ8XB5](https://doi.org/10.7289/V5SQ8XB5) [access date].


  * [ https://doi.org/10.7289/V5SQ8XB5 ](https://doi.org/10.7289/V5SQ8XB5)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NOAA/CDR/OISST/V2_1')
.filter(ee.Filter.date('2017-05-01','2017-05-14'));
varseaSurfaceTemperature=dataset.select('sst');
varvisParams={
min:-180.0,
max:3000.0,
palette:[
'040274','040281','0502a3','0502b8','0502ce','0502e6',
'0602ff','235cb1','307ef3','269db1','30c8e2','32d3ef',
'3be285','3ff38f','86e26f','3ae237','b5e22e','d6e21f',
'fff705','ffd611','ffb613','ff8b13','ff6e08','ff500d',
'ff0000','de0101','c21301','a71001','911003'
],
};
Map.setCenter(20.3,-20.39,2);
Map.addLayer(seaSurfaceTemperature,visParams,'Sea Surface Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_CDR_OISST_V2_1)
[ NOAA CDR OISST v02r01: Optimum Interpolation Sea Surface Temperature ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1)
The NOAA 1/4 degree daily Optimum Interpolation Sea Surface Temperature (OISST) provides complete ocean temperature fields constructed by combining bias-adjusted observations from different platforms (satellite, ships, buoys) on a regular global grid, with gaps filled in by interpolation. Satellite data from the Advanced Very High Resolution Radiometer (AVHRR) provides the …
NOAA/CDR/OISST/V2_1, avhrr,cdr,daily,ice,noaa,ocean,oceans,oisst,sst,temperature 
1981-09-01T00:00:00Z/2025-04-19T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7289/V5SQ8XB5 ](https://doi.org/https://www.ncei.noaa.gov/products/optimum-interpolation-sst)
  * [ https://doi.org/10.7289/V5SQ8XB5 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_OISST_V2_1)


