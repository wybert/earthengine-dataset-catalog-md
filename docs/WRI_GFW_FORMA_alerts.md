 
#  FORMA Alerts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WRI/GFW/FORMA/alerts](https://developers.google.com/earth-engine/datasets/images/WRI/WRI_GFW_FORMA_alerts_sample.png) 

Dataset Availability
    2012-01-01T00:00:00Z–2019-05-18T00:00:00Z 

Dataset Provider
     [ World Resources Institute / Global Forest Watch ](https://www.globalforestwatch.org/) 

Earth Engine Snippet
     `    ee.Image("WRI/GFW/FORMA/alerts")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_GFW_FORMA_alerts) 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [deforestation](https://developers.google.com/earth-engine/datasets/tags/deforestation) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forma](https://developers.google.com/earth-engine/datasets/tags/forma) [gfw](https://developers.google.com/earth-engine/datasets/tags/gfw) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [monitoring](https://developers.google.com/earth-engine/datasets/tags/monitoring) [wri](https://developers.google.com/earth-engine/datasets/tags/wri)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts#terms-of-use) More
**NOTE from WRI** : WRI decided to stop updating FORMA alerts. The goal was to simplify the [Global Forest Watch](https://www.globalforestwatch.org) user experience and reduce redundancy. We found that [Terra-i](http://www.terra-i.org/terra-i.html) and [GLAD](https://glad-forest-alert.appspot.com/) were more frequently used. Moreover, using GLAD as a standard, found that Terra-i outperformed FORMA globally.
FORMA alerts are detected using a combination of two MODIS products: NDVI (Normalized Difference Vegetation Index) and FIRMS (Fires Information for Resource Management System). NDVI updates are processed every 16 days, while fire updates are processed daily. Models are developed individually for each ecogroup to relate the two inputs to the area of clearing, using the Hansen annual tree cover loss data to train the model. The minimum threshold to qualify as an alert is 25% of the pixel cleared, though thresholds vary by ecogroup to minimize false positives. Here is an [example script](https://code.earthengine.google.com/f29b1e4360f3fc36847bd789ceeb20f6) for a quick introduction to the FORMA datasets.
The percentage of clearing takes a value of 0, no clearing detected, or in the range [ecogroup_bound:100), where ecogroup_bound is given by WRI/GFW/FORMA/thresholds . The time periods over which data is collected varies by N-days, where N is the number of days between the alert_date and the last MODIS NDVI update.
**Pixel Size** 250 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`alert_delta` | % |  0  |  100  | Percentage of clearing which during the 6 MODIS periods (96 + N days) preceding the corresponding alert_date value for the pixel  
`alert_date` | ms | Timestamp in milliseconds since 1970/01/01  
**Terms of Use**
The FORMA datasets are available without restriction on use or distribution. WRI does request that the user give proper attribution and identify WRI and GFW, where applicable, as the source of the data.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts#code-editor-javascript-sample) More
```
vardataset=ee.Image('WRI/GFW/FORMA/alerts');
varformaAlerts=dataset.select('alert_delta');
varformaAlertsVis={
min:25,
max:75,
palette:['d65898','da68a2'],
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(formaAlerts,formaAlertsVis,'FORMA Alerts');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_GFW_FORMA_alerts)
[ FORMA Alerts ](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts)
NOTE from WRI: WRI decided to stop updating FORMA alerts. The goal was to simplify the Global Forest Watch user experience and reduce redundancy. We found that Terra-i and GLAD were more frequently used. Moreover, using GLAD as a standard, found that Terra-i outperformed FORMA globally. FORMA alerts are detected …
WRI/GFW/FORMA/alerts, daily,deforestation,fire,forest,forma,gfw,modis,monitoring,wri 
2012-01-01T00:00:00Z/2019-05-18T00:00:00Z
-50 -120 40 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.globalforestwatch.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_alerts)


