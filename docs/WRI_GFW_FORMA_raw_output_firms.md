 
#  FORMA Raw Output FIRMS 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WRI/GFW/FORMA/raw_output_firms](https://developers.google.com/earth-engine/datasets/images/WRI/WRI_GFW_FORMA_raw_output_firms_sample.png) 

Dataset Availability
    2017-04-08T00:00:00Z–2019-05-18T00:00:00Z 

Dataset Provider
     [ World Resources Institute / Global Forest Watch ](https://www.globalforestwatch.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("WRI/GFW/FORMA/raw_output_firms")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_GFW_FORMA_raw_output_firms) 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [deforestation](https://developers.google.com/earth-engine/datasets/tags/deforestation) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forma](https://developers.google.com/earth-engine/datasets/tags/forma) [gfw](https://developers.google.com/earth-engine/datasets/tags/gfw) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [monitoring](https://developers.google.com/earth-engine/datasets/tags/monitoring) [wri](https://developers.google.com/earth-engine/datasets/tags/wri)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms#terms-of-use) More
**NOTE from WRI** : WRI decided to stop updating FORMA alerts. The goal was to simplify the [Global Forest Watch](https://www.globalforestwatch.org) user experience and reduce redundancy. We found that [Terra-i](http://www.terra-i.org/terra-i.html) and [GLAD](https://glad-forest-alert.appspot.com/) were more frequently used. Moreover, using GLAD as a standard, found that Terra-i outperformed FORMA globally.
FORMA alerts are detected using a combination of two MODIS products: NDVI (Normalized Difference Vegetation Index) and FIRMS (Fires Information for Resource Management System). NDVI updates are processed every 16 days, while fire updates are processed daily. Models are developed individually for each ecogroup to relate the two inputs to the area of clearing, using the Hansen annual tree cover loss data to train the model. The minimum threshold to qualify as an alert is 25% of the pixel cleared, though thresholds vary by ecogroup to minimize false positives. Here is an [example script](https://code.earthengine.google.com/f29b1e4360f3fc36847bd789ceeb20f6) for a quick introduction to the FORMA datasets.
The images in this ImageCollection contain the raw FORMA data calculated after new MODIS FIRMS data becomes available, approximately every day.
Each band gives a percentage of clearing (from 0 to 100) for different accumulation periods. "N" is the number of days between the latest FIRMS update and the previous NDVI update. N is given by the 'date_delta' property.
**Pixel Size** 250 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`nday` | % |  0  |  100  | Percentage of clearing in the last N days  
`delta_nday` | % |  0  |  100  | Percentage of clearing in the last 96+N days  
`near_term_delta_nday` | % |  0  |  100  | Percentage of clearing in the last 32+N days  
**Image Properties**
Name | Type | Description  
---|---|---  
year | INT | Year of the most recent data included in the dataset  
date | STRING | Date, in "YYYY-MM-DD" format, of the last MODIS FIRMS data included in this dataset  
date_delta | INT | The number of days between date and previous_biweekly_date  
previous_biweekly | INT | The biweekly (every 16 days) period of the year associated with the latest MODIS NDVI  
previous_biweekly_date | STRING | The date associated with the latest MODIS NDVI update  
**Terms of Use**
The FORMA datasets are available without restriction on use or distribution. WRI does request that the user give proper attribution and identify WRI and GFW, where applicable, as the source of the data.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('WRI/GFW/FORMA/raw_output_firms')
.filter(ee.Filter.date('2018-08-01','2018-08-15'));
varpercentageOfClearing=dataset.select('nday');
varvisParams={
min:0.0,
max:0.01,
};
Map.setCenter(26,-8,3);
Map.addLayer(percentageOfClearing,visParams,'Percentage of clearing');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_GFW_FORMA_raw_output_firms)
[ FORMA Raw Output FIRMS ](https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms)
NOTE from WRI: WRI decided to stop updating FORMA alerts. The goal was to simplify the Global Forest Watch user experience and reduce redundancy. We found that Terra-i and GLAD were more frequently used. Moreover, using GLAD as a standard, found that Terra-i outperformed FORMA globally. FORMA alerts are detected …
WRI/GFW/FORMA/raw_output_firms, daily,deforestation,fire,forest,forma,gfw,modis,monitoring,wri 
2017-04-08T00:00:00Z/2019-05-18T00:00:00Z
-50 -120 40 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.globalforestwatch.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WRI_GFW_FORMA_raw_output_firms)


