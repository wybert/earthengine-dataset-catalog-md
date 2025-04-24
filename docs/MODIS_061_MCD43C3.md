 
#  MCD43C3.061 BRDF/Albedo Daily L3 0.05 Deg CMG 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MCD43C3](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MCD43C3_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MCD43C3.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MCD43C3")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD43C3) 

Cadence
    1 Day 

Tags
     [albedo](https://developers.google.com/earth-engine/datasets/tags/albedo) [black-sky](https://developers.google.com/earth-engine/datasets/tags/black-sky) [brdf](https://developers.google.com/earth-engine/datasets/tags/brdf) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [white-sky](https://developers.google.com/earth-engine/datasets/tags/white-sky)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#dois) More
The MCD43C3 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Albedo dataset is produced daily using 16 days of Terra and Aqua MODIS data in a 0.05 degree (5,600 meters at the equator) Climate Modeling Grid (CMG). Data are temporally weighted to the ninth day of the retrieval period which is reflected in the Julian date in the file name. This CMG product covers the entire globe for use in climate simulation models.
MCD43C3 provides black-sky albedo (directional hemispherical reflectance) and white-sky albedo (bihemispherical reflectance) at local solar noon. Black-sky albedo and white-sky albedo values are available as a separate layer for MODIS spectral bands 1 through 7 as well as the visible, near infrared (NIR), and shortwave bands. Along with the 20 albedo layers are ancillary layers for quality, local solar noon, percent finer resolution inputs, snow cover, and uncertainty.
See [dataset user guide](https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43c3) for more information.
**Pixel Size** 5600 meters 
**Bands**
Name | Units | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---|---  
`Albedo_BSA_Band1` |  0  |  32766  | 0.001 | 620-670nm | Black-sky albedo for band 1  
`Albedo_BSA_Band2` |  0  |  32766  | 0.001 | 841-876nm | Black-sky albedo for band 2  
`Albedo_BSA_Band3` |  0  |  32766  | 0.001 | 459-479nm | Black-sky albedo for band 3  
`Albedo_BSA_Band4` |  0  |  32766  | 0.001 | 545-565nm | Black-sky albedo for band 4  
`Albedo_BSA_Band5` |  0  |  32766  | 0.001 | 1230-1250nm | Black-sky albedo for band 5  
`Albedo_BSA_Band6` |  0  |  32766  | 0.001 | 1628-1652nm | Black-sky albedo for band 6  
`Albedo_BSA_Band7` |  0  |  32766  | 0.001 | 2105-2155nm | Black-sky albedo for band 7  
`Albedo_BSA_vis` |  0  |  32766  | 0.001 | Black-sky albedo for visible brodband  
`Albedo_BSA_nir` |  0  |  32766  | 0.001 | 858nm | Black-sky albedo for NIR broadband  
`Albedo_BSA_shortwave` |  0  |  32766  | 0.001 | Black-sky albedo for shortwave broadband  
`Albedo_WSA_Band1` |  0  |  32766  | 0.001 | 620-670nm | White-sky albedo for band 1  
`Albedo_WSA_Band2` |  0  |  32766  | 0.001 | 841-876nm | White-sky albedo for band 2  
`Albedo_WSA_Band3` |  0  |  32766  | 0.001 | 459-479nm | White-sky albedo for band 3  
`Albedo_WSA_Band4` |  0  |  32766  | 0.001 | 545-565nm | White-sky albedo for band 4  
`Albedo_WSA_Band5` |  0  |  32766  | 0.001 | 1230-1250nm | White-sky albedo for band 5  
`Albedo_WSA_Band6` |  0  |  32766  | 0.001 | 1628-1652nm | White-sky albedo for band 6  
`Albedo_WSA_Band7` |  0  |  32766  | 0.001 | 2105-2155nm | White-sky albedo for band 7  
`Albedo_WSA_vis` |  0  |  32766  | 0.001 | White-sky albedo for visible broadband  
`Albedo_WSA_nir` |  0  |  32766  | 0.001 | 858nm | White-sky albedo for NIR broadband  
`Albedo_WSA_shortwave` |  0  |  32766  | 0.001 | White-sky albedo for shortwave broadband  
`BRDF_Quality` | Global albedo quality  
Bitmask for BRDF_Quality
  * Bits 0-2: BRDF and albedo quality information 
    * 0: best quality, 100% with full inversions
    * 1: good quality, 75% or more with best full inversions and 90% or more with full inversions
    * 2: relative good quality, 75% or more with full inversions
    * 3: mixed, 75% or less full inversions and 25% or less fill values
    * 4: all magnitude inversions or 50% or less fill values
    * 5: all magnitude inversions or 50% or less fill values

  
`Local_Solar_Noon` | deg |  0  |  90  | Local solar noon zenith angle  
`Percent_Inputs` | % |  0  |  100  | Percent of the processed finer resolution data which contributed to this CMG pixel  
`Percent_Snow` | % |  0  |  100  | Percent of underlying data flagged as snow  
`BRDF_Albedo_Uncertainty` |  0  |  32766  | 0.001 | BRDF inversion information. Weights of determination (WoD) of the white sky albedo (see Lucht, W., & Lewis, P. (2000). Theoretical noise sensitivity of BRDF and albedo retrieval from the EOS-MODIS and MISR sensors with respect to angular sampling. International Journal of Remote Sensing, 21(1), 81-98). WoDs give a measure of the uncertainty due to the angular sampling of the inputs available for each retrieval.  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MCD43C3.061 ](https://doi.org/10.5067/MODIS/MCD43C3.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MCD43C3')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
varblackSkyAlbedo=dataset.select('Albedo_BSA_Band1');
varblackSkyAlbedoVis={
min:0.0,
max:400.0,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(blackSkyAlbedo,blackSkyAlbedoVis,'Black-Sky Albedo');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD43C3)
[ MCD43C3.061 BRDF/Albedo Daily L3 0.05 Deg CMG ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3)
The MCD43C3 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Albedo dataset is produced daily using 16 days of Terra and Aqua MODIS data in a 0.05 degree (5,600 meters at the equator) Climate Modeling Grid (CMG). Data are temporally weighted to the ninth day of the retrieval period …
MODIS/061/MCD43C3, albedo,black-sky,brdf,daily,global,modis,nasa,satellite-imagery,usgs,white-sky 
2000-02-24T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MCD43C3.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MCD43C3.061)
  * [ https://doi.org/10.5067/MODIS/MCD43C3.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43C3)


