 
#  NAIP: National Agriculture Imagery Program 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USDA/NAIP/DOQQ](https://developers.google.com/earth-engine/datasets/images/USDA/USDA_NAIP_DOQQ_sample.png) 

Dataset Availability
    2002-06-15T00:00:00Z–2023-11-17T00:00:00Z 

Dataset Provider
     [ USDA Farm Production and Conservation - Business Center, Geospatial Enterprise Operations ](https://naip-usdaonline.hub.arcgis.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("USDA/NAIP/DOQQ")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDA/USDA_NAIP_DOQQ) 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [highres](https://developers.google.com/earth-engine/datasets/tags/highres) [imagery](https://developers.google.com/earth-engine/datasets/tags/imagery) [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [usda](https://developers.google.com/earth-engine/datasets/tags/usda)
aerial
fpac
naip
[Description](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ#citations) More
The National Agriculture Imagery Program (NAIP) acquires aerial imagery during the agricultural growing seasons in the continental U.S.
NAIP projects are contracted each year based upon available funding and the imagery acquisition cycle. Beginning in 2003, NAIP was acquired on a 5-year cycle. 2008 was a transition year, and a three-year cycle began in 2009.
NAIP imagery is acquired at a one-meter ground sample distance (GSD) with a horizontal accuracy that matches within six meters of photo-identifiable ground control points, which are used during image inspection.
Older images were collected using 3 bands (Red, Green, and Blue: RGB), but newer imagery is usually collected with an additional near-infrared band (RGBN). RGB asset ids begin with 'n _', NRG asset ids begin with 'c_ ', RGBN asset ids begin with 'm_'.
Some older images have GSD of 2 meters.
**Pixel Size** 0.6 meters 
**Bands**
Name | Units | Description  
---|---|---  
`R` | dn | Red  
`G` | dn | Green  
`B` | dn | Blue  
`N` | dn | Near infrared  
**Terms of Use**
Most information presented on the FSA Web site is considered public domain information. Public domain information may be freely distributed or copied, but use of appropriate byline/photo/image credits is requested. For more information visit the [FSA Policies and Links](https://www.fsa.usda.gov/help/policies-and-links) website.
Users should acknowledge USDA Farm Production and Conservation - Business Center, Geospatial Enterprise Operations when using or distributing this data set.
Citations:
  * USDA Farm Production and Conservation - Business Center, Geospatial Enterprise Operations


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('USDA/NAIP/DOQQ')
.filter(ee.Filter.date('2017-01-01','2018-12-31'));
vartrueColor=dataset.select(['R','G','B']);
vartrueColorVis={
min:0,
max:255,
};
Map.setCenter(-73.9958,40.7278,15);
Map.addLayer(trueColor,trueColorVis,'True Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDA/USDA_NAIP_DOQQ)
[ NAIP: National Agriculture Imagery Program ](https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ)
The National Agriculture Imagery Program (NAIP) acquires aerial imagery during the agricultural growing seasons in the continental U.S. NAIP projects are contracted each year based upon available funding and the imagery acquisition cycle. Beginning in 2003, NAIP was acquired on a 5-year cycle. 2008 was a transition year, and a …
USDA/NAIP/DOQQ, agriculture,highres,imagery,orthophotos,usda 
2002-06-15T00:00:00Z/2023-11-17T00:00:00Z
24.42 -124.84 49.72 -64.82 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://naip-usdaonline.hub.arcgis.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USDA_NAIP_DOQQ)


