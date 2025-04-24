 
#  Murray Global Intertidal Change QA Pixel Count 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UQ/murray/Intertidal/v1_1/qa_pixel_count](https://developers.google.com/earth-engine/datasets/images/UQ/UQ_murray_Intertidal_v1_1_qa_pixel_count_sample.png) 

Dataset Availability
    1984-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ Murray/UQ/Google/USGS/NASA ](https://intertidal.app) 

Earth Engine Snippet
     `    ee.ImageCollection("UQ/murray/Intertidal/v1_1/qa_pixel_count")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UQ/UQ_murray_Intertidal_v1_1_qa_pixel_count) 

Cadence
    3 Years 

Tags
     [coastal](https://developers.google.com/earth-engine/datasets/tags/coastal) [google](https://developers.google.com/earth-engine/datasets/tags/google) [intertidal](https://developers.google.com/earth-engine/datasets/tags/intertidal) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [murray](https://developers.google.com/earth-engine/datasets/tags/murray) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [tidal-flats](https://developers.google.com/earth-engine/datasets/tags/tidal-flats) [uq](https://developers.google.com/earth-engine/datasets/tags/uq)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#dois) More
The Murray Global Intertidal Change Dataset contains global maps of tidal flat ecosystems produced via a supervised classification of 707,528 Landsat Archive images. Each pixel was classified into tidal flat, permanent water or other with reference to a globally distributed set of training data.
The classification was implemented along the entire global coastline between 60° North and 60° South from 1 January 1984 to 31 December 2016. The image collection consists consists of a time-series of 11 global maps of tidal flats at 30m pixel resolution for set time-periods (1984-1986; 1987-1989; 1990-1992; 1993-1995; 1996-1998; 1999-2001; 2002-2004; 2005-2007; 2008-2010; 2011-2013; 2014-2016)
The number of Landsat images used to develop the Landsat covariate layers in each time step of the tidal flat classification. Each image in the image collection refers to a single time step.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`pixel_count` | count |  0  |  400  | Input image count.  
**Terms of Use**
This work is licensed under a Creative Commons Attribution 4.0 International License.
Any use of the intertidal data must include proper acknowledgement, including citing the associated journal article.
Citations:
  * Murray, N.J., Phinn, S.R., DeWitt, M., Ferrari, R., Johnston, R., Lyons, M.B., Clinton, N., Thau, D. & Fuller, R.A. (2019) The global distribution and trajectory of tidal flats. Nature, 565, 222-225.


  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/10.1038/s41586-018-0805-8)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('UQ/murray/Intertidal/v1_1/qa_pixel_count');
varvisualization={
bands:['pixel_count'],
min:0,
max:300,
palette:['000000','ffffff']
};
Map.setCenter(126.6339,37.4394,10);
Map.addLayer(dataset,visualization,'QA Pixel Count');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UQ/UQ_murray_Intertidal_v1_1_qa_pixel_count)
[ Murray Global Intertidal Change QA Pixel Count ](https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count)
The Murray Global Intertidal Change Dataset contains global maps of tidal flat ecosystems produced via a supervised classification of 707,528 Landsat Archive images. Each pixel was classified into tidal flat, permanent water or other with reference to a globally distributed set of training data. The classification was implemented along the …
UQ/murray/Intertidal/v1_1/qa_pixel_count, coastal,google,intertidal,landsat-derived,murray,surface-ground-water,tidal-flats,uq 
1984-01-01T00:00:00Z/2017-01-01T00:00:00Z
-60 -180 60 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/https://intertidal.app)
  * [ https://doi.org/10.1038/s41586-018-0805-8 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UQ_murray_Intertidal_v1_1_qa_pixel_count)


