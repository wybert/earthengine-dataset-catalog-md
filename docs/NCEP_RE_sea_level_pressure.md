 
#  NCEP/NCAR Reanalysis Data, Sea-Level Pressure 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NCEP_RE/sea_level_pressure](https://developers.google.com/earth-engine/datasets/images/NCEP_RE/NCEP_RE_sea_level_pressure_sample.png) 

Dataset Availability
    1948-01-01T00:00:00Z–2025-04-18T18:00:00Z 

Dataset Provider
     [ NCEP ](https://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis.html) 

Earth Engine Snippet
     `    ee.ImageCollection("NCEP_RE/sea_level_pressure")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NCEP_RE/NCEP_RE_sea_level_pressure) 

Cadence
    6 Hours 

Tags
     [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [ncep](https://developers.google.com/earth-engine/datasets/tags/ncep) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [pressure](https://developers.google.com/earth-engine/datasets/tags/pressure) [reanalysis](https://developers.google.com/earth-engine/datasets/tags/reanalysis)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure#citations) More
The NCEP/NCAR Reanalysis Project is a joint project between the National Centers for Environmental Prediction (NCEP, formerly "NMC") and the National Center for Atmospheric Research (NCAR). The goal of this joint effort is to produce new atmospheric analyses using historical data as well as to produce analyses of the current atmospheric state (Climate Data Assimilation System, CDAS). The NCEP/NCAR Reanalysis 1 project is using a state-of-the-art analysis/forecast system to perform data assimilation using past data from 1948 to the present. The data have 6-hour temporal resolution (0000, 0600, 1200, and 1800 UTC) and 2.5 degree spatial resolution.
**Pixel Size** 278300 meters 
**Bands**
Name | Units | Min | Max | Scale | Description  
---|---|---|---|---|---  
`slp` | mbar |  92590*  |  112590*  | 0.01 | Sea level pressure  
* estimated min or max value 
**Terms of Use**
There are no restrictions on the use of these datasets.
Citations:
  * Kalnay et al., 1996, The NCEP/NCAR 40-Year Reanalysis Project. Bull. Amer. Meteor. Soc., 77, 437-471. [doi:10.1175/1520-0477(1996)077](https://doi.org/10.1175/1520-0477\(1996\)077%3C0437:TNYRP%3E2.0.CO;2)[0437:TNYRP\](https://developers.google.com/earth-engine/datasets/catalog/0437:TNYRP%5C)2.0.CO;2.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NCEP_RE/sea_level_pressure')
.filter(ee.Filter.date('2018-08-01','2018-08-15'));
varseaLevelPressure=dataset.select('slp');
varseaLevelPressureVis={
min:96500.0,
max:104500.0,
palette:['800080','0000ab','008000','ffff00','ffa500','ff0000'],
};
Map.setCenter(-88.6,26.4,1);
Map.addLayer(seaLevelPressure,seaLevelPressureVis,'Sea Level Pressure');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NCEP_RE/NCEP_RE_sea_level_pressure)
[ NCEP/NCAR Reanalysis Data, Sea-Level Pressure ](https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure)
The NCEP/NCAR Reanalysis Project is a joint project between the National Centers for Environmental Prediction (NCEP, formerly "NMC") and the National Center for Atmospheric Research (NCAR). The goal of this joint effort is to produce new atmospheric analyses using historical data as well as to produce analyses of the current …
NCEP_RE/sea_level_pressure, atmosphere,climate,geophysical,ncep,noaa,pressure,reanalysis 
1948-01-01T00:00:00Z/2025-04-18T18:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NCEP_RE_sea_level_pressure)


