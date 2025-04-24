 
#  NASA SRTM Digital Elevation 30m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/SRTMGL1_003](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_SRTMGL1_003_sample.png) 

Dataset Availability
    2000-02-11T00:00:00Z–2000-02-22T00:00:00Z 

Dataset Provider
     [ NASA / USGS / JPL-Caltech ](https://doi.org/10.5067/MEaSUREs/SRTM/SRTMGL1_NC.003) 

Earth Engine Snippet
     `    ee.Image("USGS/SRTMGL1_003")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_SRTMGL1_003) 

Tags
     [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm) [topography](https://developers.google.com/earth-engine/datasets/tags/topography) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003#citations) More
The Shuttle Radar Topography Mission (SRTM, see [Farr et al. 2007](https://onlinelibrary.wiley.com/doi/10.1029/2005RG000183/full)) digital elevation data is an international research effort that obtained digital elevation models on a near-global scale. This SRTM V3 product (SRTM Plus) is provided by NASA JPL at a resolution of 1 arc-second (approximately 30m).
This dataset has undergone a void-filling process using open-source data (ASTER GDEM2, GMTED2010, and NED), as opposed to other versions that contain voids or have been void-filled with commercial sources. For more information on the different versions see the [SRTM Quick Guide](https://lpdaac.usgs.gov/documents/13/SRTM_Quick_Guide.pdf).
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/179/SRTM_User_Guide_V3.pdf)
  * [General Documentation](https://lpdaac.usgs.gov/documents/13/SRTM_Quick_Guide.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://doi.org/10.1029/2005RG000183)


**Bands**
Name | Units | Min | Max | Pixel Size | Description  
---|---|---|---|---|---  
`elevation` | m |  -10*  |  6500*  |  30 meters  | Elevation  
* estimated min or max value 
**Terms of Use**
Unless otherwise noted, images and video on JPL public web sites (public sites ending with a jpl.nasa.gov address) may be used for any purpose without prior permission. For more information and exceptions visit the [JPL Image Use Policy site](https://www.jpl.nasa.gov/imagepolicy/).
Citations:
  * Farr, T.G., Rosen, P.A., Caro, E., Crippen, R., Duren, R., Hensley, S., Kobrick, M., Paller, M., Rodriguez, E., Roth, L., Seal, D., Shaffer, S., Shimada, J., Umland, J., Werner, M., Oskin, M., Burbank, D., and Alsdorf, D.E., 2007, The shuttle radar topography mission: Reviews of Geophysics, v. 45, no. 2, RG2004, at <https://doi.org/10.1029/2005RG000183>.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003#code-editor-javascript-sample) More
```
vardataset=ee.Image('USGS/SRTMGL1_003');
varelevation=dataset.select('elevation');
varslope=ee.Terrain.slope(elevation);
Map.setCenter(-112.8598,36.2841,10);
Map.addLayer(slope,{min:0,max:60},'slope');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_SRTMGL1_003)
[ NASA SRTM Digital Elevation 30m ](https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003)
The Shuttle Radar Topography Mission (SRTM, see Farr et al. 2007) digital elevation data is an international research effort that obtained digital elevation models on a near-global scale. This SRTM V3 product (SRTM Plus) is provided by NASA JPL at a resolution of 1 arc-second (approximately 30m). This dataset has …
USGS/SRTMGL1_003, dem,elevation,elevation-topography,geophysical,nasa,srtm,topography,usgs 
2000-02-11T00:00:00Z/2000-02-22T00:00:00Z
-56 -180 60 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://doi.org/10.5067/MEaSUREs/SRTM/SRTMGL1_NC.003)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003)


