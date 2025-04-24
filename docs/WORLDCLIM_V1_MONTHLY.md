 
#  WorldClim Climatology V1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WORLDCLIM/V1/MONTHLY](https://developers.google.com/earth-engine/datasets/images/WORLDCLIM/WORLDCLIM_V1_MONTHLY_sample.png) 

Dataset Availability
    1960-01-01T00:00:00Z–1991-01-01T00:00:00Z 

Dataset Provider
     [ University of California, Berkeley ](https://www.worldclim.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("WORLDCLIM/V1/MONTHLY")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WORLDCLIM/WORLDCLIM_V1_MONTHLY) 

Climatological Interval
    1 Month 

Tags
     [berkeley](https://developers.google.com/earth-engine/datasets/tags/berkeley) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [precipitation](https://developers.google.com/earth-engine/datasets/tags/precipitation) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature) [weather](https://developers.google.com/earth-engine/datasets/tags/weather) [worldclim](https://developers.google.com/earth-engine/datasets/tags/worldclim)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#citations) More
WorldClim version 1 has average monthly global climate data for minimum, mean, and maximum temperature and for precipitation.
WorldClim version 1 was developed by Robert J. Hijmans, Susan Cameron, and Juan Parra, at the Museum of Vertebrate Zoology, University of California, Berkeley, in collaboration with Peter Jones and Andrew Jarvis (CIAT), and with Karen Richardson (Rainforest CRC).
**Pixel Size** 927.67 meters 
**Bands**
Name | Units | Min | Max | Scale | Description  
---|---|---|---|---|---  
`tavg` | °C |  -53.6*  |  39.4*  | 0.1 | Mean temperature  
`tmin` | °C |  -57.3*  |  32.5*  | 0.1 | Minimum temperature  
`tmax` | °C |  -50*  |  49*  | 0.1 | Maximum temperature  
`prec` | mm |  0*  |  2949*  | Precipitation  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
month | DOUBLE | Month  
**Terms of Use**
[CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html)
Citations:
  * Hijmans, R.J., S.E. Cameron, J.L. Parra, P.G. Jones and A. Jarvis, 2005. Very High Resolution Interpolated Climate Surfaces for Global Land Areas. International Journal of Climatology 25: 1965-1978. [doi:10.1002/joc.1276](https://doi.org/10.1002/joc.1276).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('WORLDCLIM/V1/MONTHLY');
varmeanTemperature=dataset.select('tavg').first().multiply(0.1);
varmeanTemperatureVis={
min:-40,
max:30,
palette:['blue','purple','cyan','green','yellow','red'],
};
Map.setCenter(71.7,52.4,3);
Map.addLayer(meanTemperature,meanTemperatureVis,'Mean Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WORLDCLIM/WORLDCLIM_V1_MONTHLY)
[ WorldClim Climatology V1 ](https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY)
WorldClim version 1 has average monthly global climate data for minimum, mean, and maximum temperature and for precipitation. WorldClim version 1 was developed by Robert J. Hijmans, Susan Cameron, and Juan Parra, at the Museum of Vertebrate Zoology, University of California, Berkeley, in collaboration with Peter Jones and Andrew Jarvis …
WORLDCLIM/V1/MONTHLY, berkeley,climate,monthly,precipitation,temperature,weather,worldclim 
1960-01-01T00:00:00Z/1991-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.worldclim.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WORLDCLIM_V1_MONTHLY)


