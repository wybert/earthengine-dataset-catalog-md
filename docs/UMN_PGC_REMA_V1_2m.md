 
#  REMA Strips 2m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UMN/PGC/REMA/V1/2m](https://developers.google.com/earth-engine/datasets/images/UMN/UMN_PGC_REMA_V1_2m_sample.png) 

Dataset Availability
    2009-01-01T00:00:00Z–2018-01-01T00:00:00Z 

Dataset Provider
     [ University of Minnesota Polar Geospatial Center ](https://www.pgc.umn.edu/data/arcticdem/) 

Earth Engine Snippet
     `    ee.ImageCollection("UMN/PGC/REMA/V1/2m")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_REMA_V1_2m) 

Tags
     [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [pgc](https://developers.google.com/earth-engine/datasets/tags/pgc) [rema](https://developers.google.com/earth-engine/datasets/tags/rema) [umn](https://developers.google.com/earth-engine/datasets/tags/umn)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#dois) More
The Reference Elevation Model of Antarctica (REMA) is a high resolution, time-stamped Digital Surface Model (DSM) of Antarctica at 2-meter and 8-meter spatial resolutions.
Strip DEM files correspond to the overlapping area of the input stereoscopic imagery pair strips as they are collected by DigitalGlobe's constellation of polar-orbiting satellites. Strip DEM dimensions will vary according to the satellite sensor that acquired the images and the off-nadir angle of collection. Most strips are between 13 km and 17 km in width, and 110 km and 120 km in length.
**Pixel Size** 2 meters 
**Bands**
Name | Units | Description  
---|---|---  
`elevation` | m | Elevation  
`matchtag` | Bitmask raster indicating DEM pixels processing  
Bitmask for matchtag
  * Bit 0: Pixel processing 
    * 0: Pixels have been interpolated
    * 1: Pixels are derived from a stereo match

  
**Terms of Use**
National Science Foundation (PGC's primary funding source) policy requires researchers to acknowledge NSF support in all publications, web pages, and media interviews.
By using PGC data in Earth Engine, users agree to cite PGC and its sponsorship by the NSF. The original source of any third-party data supplied by PGC must also be properly attributed.
For more information see the PGC's [Acknowledgement Policy](https://www.pgc.umn.edu/guides/user-services/acknowledgement-policy/).
Citations:
  * Howat, I. M., Porter, C., Smith, B. E., Noh, M.-J., and Morin, P.: The Reference Elevation Model of Antarctica, The Cryosphere, 13, 665-674, 2019.


  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/10.5194/tc-13-665-2019)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m#code-editor-javascript-sample) More
```
varcollection=ee.ImageCollection('UMN/PGC/REMA/V1/2m');
Map.setCenter(-60,-75,3);
varelevationVis={
bands:['elevation'],
min:-50.0,
max:1000.0,
palette:['0d13d8','60e1ff','ffffff'],
};
Map.addLayer(collection,elevationVis,'REMA_DEM_strips_2m');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_REMA_V1_2m)
[ REMA Strips 2m ](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m)
The Reference Elevation Model of Antarctica (REMA) is a high resolution, time-stamped Digital Surface Model (DSM) of Antarctica at 2-meter and 8-meter spatial resolutions. Strip DEM files correspond to the overlapping area of the input stereoscopic imagery pair strips as they are collected by DigitalGlobe's constellation of polar-orbiting satellites. Strip …
UMN/PGC/REMA/V1/2m, dem,elevation-topography,geophysical,pgc,rema,umn 
2009-01-01T00:00:00Z/2018-01-01T00:00:00Z
-88.3 -180 -53.8 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/https://www.pgc.umn.edu/data/arcticdem/)
  * [ https://doi.org/10.5194/tc-13-665-2019 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_REMA_V1_2m)


