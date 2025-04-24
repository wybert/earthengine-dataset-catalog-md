 
#  REMA Mosaic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UMN/PGC/REMA/V1_1/8m](https://developers.google.com/earth-engine/datasets/images/UMN/UMN_PGC_REMA_V1_1_8m_sample.png) 

Dataset Availability
    2009-01-01T00:00:00Z–2018-01-01T00:00:00Z 

Dataset Provider
     [ University of Minnesota Polar Geospatial Center ](https://www.pgc.umn.edu/data/arcticdem/) 

Earth Engine Snippet
     `    ee.Image("UMN/PGC/REMA/V1_1/8m")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_REMA_V1_1_8m) 

Tags
     [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [pgc](https://developers.google.com/earth-engine/datasets/tags/pgc) [rema](https://developers.google.com/earth-engine/datasets/tags/rema) [umn](https://developers.google.com/earth-engine/datasets/tags/umn)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#dois) More
The Reference Elevation Model of Antarctica (REMA) is a high resolution, time-stamped Digital Surface Model (DSM) of Antarctica at 2-meter and 8-meter spatial resolutions.
Mosaicked DEM files are compiled from multiple strips that have been co-registered, blended, and feathered to reduce edge-matching artifacts.
**Pixel Size** 8 meters 
**Bands**
Name | Units | Description  
---|---|---  
`elevation` | m | Elevation  
**Terms of Use**
National Science Foundation (PGC's primary funding source) policy requires researchers to acknowledge NSF support in all publications, web pages, and media interviews.
By using PGC data in Earth Engine, users agree to cite PGC and its sponsorship by the NSF. The original source of any third-party data supplied by PGC must also be properly attributed.
For more information see the PGC's [Acknowledgement Policy](https://www.pgc.umn.edu/guides/user-services/acknowledgement-policy/).
Citations:
  * Howat, I. M., Porter, C., Smith, B. E., Noh, M.-J., and Morin, P.: The Reference Elevation Model of Antarctica, The Cryosphere, 13, 665-674, 2019.


  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/10.5194/tc-13-665-2019)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m#code-editor-javascript-sample) More
```
varmosaic=ee.Image('UMN/PGC/REMA/V1_1/8m');
Map.setCenter(-61,-75,3);
varelevationVis={
bands:['elevation'],
min:-50.0,
max:1000.0,
palette:['0d13d8','60e1ff','ffffff'],
};
Map.addLayer(mosaic,elevationVis,'REMA_DEM_mosaic_8m');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_REMA_V1_1_8m)
[ REMA Mosaic ](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m)
The Reference Elevation Model of Antarctica (REMA) is a high resolution, time-stamped Digital Surface Model (DSM) of Antarctica at 2-meter and 8-meter spatial resolutions. Mosaicked DEM files are compiled from multiple strips that have been co-registered, blended, and feathered to reduce edge-matching artifacts.
UMN/PGC/REMA/V1_1/8m, dem,elevation-topography,geophysical,pgc,rema,umn 
2009-01-01T00:00:00Z/2018-01-01T00:00:00Z
-88.3 -180 -53.8 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/https://www.pgc.umn.edu/data/arcticdem/)
  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_1_8m)


