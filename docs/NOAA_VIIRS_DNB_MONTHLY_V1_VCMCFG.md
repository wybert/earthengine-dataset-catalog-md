 
#  VIIRS Nighttime Day/Night Band Composites Version 1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG_sample.png) 

Dataset Availability
    2012-04-01T00:00:00Z–2025-03-01T00:00:00Z 

Dataset Provider
     [ Earth Observation Group, Payne Institute for Public Policy, Colorado School of Mines ](https://eogdata.mines.edu/products/vnl/#monthly) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG) 

Cadence
    1 Month 

Tags
     [dnb](https://developers.google.com/earth-engine/datasets/tags/dnb) [eog](https://developers.google.com/earth-engine/datasets/tags/eog) [lights](https://developers.google.com/earth-engine/datasets/tags/lights) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [nighttime](https://developers.google.com/earth-engine/datasets/tags/nighttime) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [population](https://developers.google.com/earth-engine/datasets/tags/population) [viirs](https://developers.google.com/earth-engine/datasets/tags/viirs) [visible](https://developers.google.com/earth-engine/datasets/tags/visible)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG#terms-of-use) More
Monthly average radiance composite images using nighttime data from the Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB).
As these data are composited monthly, there are many areas of the globe where it is impossible to get good quality data coverage for that month. This can be due to cloud cover, especially in the tropical regions, or due to solar illumination, as happens toward the poles in their respective summer months. Therefore it is recommended that users of these data utilize the 'cf_cvg' band and not assume a value of zero in the average radiance image means that no lights were observed.
Cloud cover is determined using the VIIRS Cloud Mask product (VCM). In addition, data near the edges of the swath are not included in the composites (aggregation zones 29-32). Version 1 has NOT been filtered to screen out lights from aurora, fires, boats, and other temporal lights. This separation is under development and will be included in a later version of this time series. Also in development is a method to separate lights from background (non-light) values.
Prior to averaging, the DNB data is filtered to exclude data impacted by stray light, lightning, lunar illumination, and cloud-cover.
**Pixel Size** 463.83 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`avg_rad` | nanoWatts/sr/cm^2 |  -1.5*  |  340573*  | Average DNB radiance values.  
`cf_cvg` |  0*  |  58*  | Cloud-free coverages; the total number of observations that went into each pixel. This band can be used to identify areas with low numbers of observations where the quality is reduced.  
* estimated min or max value 
**Terms of Use**
Colorado School of Mines data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')
.filter(ee.Filter.date('2017-05-01','2017-05-31'));
varnighttime=dataset.select('avg_rad');
varnighttimeVis={min:0.0,max:60.0};
Map.setCenter(-77.1056,38.8904,8);
Map.addLayer(nighttime,nighttimeVis,'Nighttime');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)
[ VIIRS Nighttime Day/Night Band Composites Version 1 ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)
Monthly average radiance composite images using nighttime data from the Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB). As these data are composited monthly, there are many areas of the globe where it is impossible to get good quality data coverage for that month. This can be due to …
NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG, dnb,eog,lights,monthly,nighttime,noaa,population,viirs,visible 
2012-04-01T00:00:00Z/2025-03-01T00:00:00Z
-65 -180 75 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://eogdata.mines.edu/products/vnl/#monthly)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)


