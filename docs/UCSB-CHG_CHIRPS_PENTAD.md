 
#  CHIRPS Pentad: Climate Hazards Center InfraRed Precipitation With Station Data (Version 2.0 Final) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UCSB-CHG/CHIRPS/PENTAD](https://developers.google.com/earth-engine/datasets/images/UCSB-CHG/UCSB-CHG_CHIRPS_PENTAD_sample.png) 

Dataset Availability
    1981-01-01T00:00:00Z–2025-02-26T00:00:00Z 

Dataset Provider
     [ UCSB/CHG ](https://chc.ucsb.edu/data/chirps) 

Earth Engine Snippet
     `    ee.ImageCollection("UCSB-CHG/CHIRPS/PENTAD")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UCSB-CHG/UCSB-CHG_CHIRPS_PENTAD) 

Cadence
    1 Custom_time_unit 

Tags
     [chg](https://developers.google.com/earth-engine/datasets/tags/chg) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [precipitation](https://developers.google.com/earth-engine/datasets/tags/precipitation) [ucsb](https://developers.google.com/earth-engine/datasets/tags/ucsb) [weather](https://developers.google.com/earth-engine/datasets/tags/weather)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#citations) More
Climate Hazards Center InfraRed Precipitation with Station data (CHIRPS) is a 30+ year quasi-global rainfall dataset. CHIRPS incorporates 0.05° resolution satellite imagery with in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring.
**Pixel Size** 5566 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`precipitation` | mm/pentad |  0*  |  1072.43*  | Precipitation  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
month | DOUBLE | Month  
pentad | DOUBLE | Pentad  
year | DOUBLE | Year  
**Terms of Use**
This datasets are in the public domain. To the extent possible under law, [Pete Peterson](https://chc.ucsb.edu/people/pete-peterson) has waived all copyright and related or neighboring rights to Climate Hazards Center Infrared Precipitation with Stations (CHIRPS).
Citations:
  * Funk, Chris, Pete Peterson, Martin Landsfeld, Diego Pedreros, James Verdin, Shraddhanand Shukla, Gregory Husak, James Rowland, Laura Harrison, Andrew Hoell & Joel Michaelsen. "The climate hazards infrared precipitation with stations-a new environmental record for monitoring extremes". Scientific Data 2, 150066. [doi:10.1038/sdata.2015.66](https://doi.org/10.1038/sdata.2015.66) 2015.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD')
.filter(ee.Filter.date('2018-05-01','2018-05-05'));
varprecipitation=dataset.select('precipitation');
varprecipitationVis={
min:0,
max:112,
palette:['001137','0aab1e','e7eb05','ff4a2d','e90000'],
};
Map.setCenter(17.93,7.71,2);
Map.addLayer(precipitation,precipitationVis,'Precipitation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UCSB-CHG/UCSB-CHG_CHIRPS_PENTAD)
[ CHIRPS Pentad: Climate Hazards Center InfraRed Precipitation With Station Data (Version 2.0 Final) ](https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD)
Climate Hazards Center InfraRed Precipitation with Station data (CHIRPS) is a 30+ year quasi-global rainfall dataset. CHIRPS incorporates 0.05° resolution satellite imagery with in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring.
UCSB-CHG/CHIRPS/PENTAD, chg,climate,geophysical,precipitation,ucsb,weather 
1981-01-01T00:00:00Z/2025-02-26T00:00:00Z
-50 -180 50 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://chc.ucsb.edu/data/chirps)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD)


