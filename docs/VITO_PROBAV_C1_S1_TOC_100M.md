 
#  PROBA-V C1 Top Of Canopy Daily Synthesis 100m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![VITO/PROBAV/C1/S1_TOC_100M](https://developers.google.com/earth-engine/datasets/images/VITO/VITO_PROBAV_C1_S1_TOC_100M_sample.png) 

Dataset Availability
    2013-10-17T00:00:00Z–2021-10-31T00:00:00Z 

Dataset Provider
     [ Vito / ESA ](https://proba-v.vgt.vito.be/) 

Earth Engine Snippet
     `    ee.ImageCollection("VITO/PROBAV/C1/S1_TOC_100M")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/VITO/VITO_PROBAV_C1_S1_TOC_100M) 

Cadence
    1 Day 

Tags
     [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [multispectral](https://developers.google.com/earth-engine/datasets/tags/multispectral) [nir](https://developers.google.com/earth-engine/datasets/tags/nir) [proba](https://developers.google.com/earth-engine/datasets/tags/proba) [probav](https://developers.google.com/earth-engine/datasets/tags/probav) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [swir](https://developers.google.com/earth-engine/datasets/tags/swir) [vito](https://developers.google.com/earth-engine/datasets/tags/vito)
[Description](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#citations) More
Proba-V is a satellite mission tasked to map land cover and vegetation growth. It was designed to provide continuity for the VGT optical instrument from the SPOT-4 and SPOT-5 missions.
The sensor collects data in three VNIR (visible and near-infrared) bands and one SWIR (short-wave infrared) spectral band with a 2250km field of view. Global images are produced every 2 days at 300m resolution, and a 100m image from nadir observations every 5 days. These images are later composited to produce this daily synthesis dataset. The description of the compositing and atmospheric correction procedures can be found in the [user manual](https://publications.vito.be/2017-1333-probav-products-user-manual.pdf).
The reflectances provided in this dataset are presented as Digital Count Numbers (DN) and must be converted according to the guidelines in Section 4.6.1 of the [user manual](https://publications.vito.be/2017-1333-probav-products-user-manual.pdf).
**Pixel Size** 100 meters 
**Bands**
Name | Units | Wavelength | Description  
---|---|---|---  
`RED` | 658nm, FWHM: 82nm | Top of canopy reflectance RED channel  
`NIR` | 834nm, FWHM: 121nm | Top of canopy reflectance NIR channel  
`BLUE` | 460nm, FWHM: 42nm | Top of canopy reflectance BLUE channel  
`SWIR` | 1610nm, FWHM: 89nm | Top of canopy reflectance SWIR channel  
`NDVI` | Normalized Difference Vegetation Index  
`SZA` | deg | Solar zenith angle  
`SAA` | deg | Solar azimuth angle  
`SWIRVAA` | deg | Viewing azimuth angles SWIR detector  
`SWIRVZA` | deg | Viewing zenith angle SWIR detector  
`VNIRVAA` | deg | Viewing azimuth angle VNIR detector  
`VNIRVZA` | deg | Viewing zenith angle VNIR detector  
`SM` | Quality / Information band.  
Bitmask for SM
  * Bits 0-2: Cloud/ice snow/shadow flag 
    * 0: Clear
    * 1: Shadow
    * 2: Undefined
    * 3: Cloud
    * 4: Ice
  * Bit 3: Land/sea 
    * 0: Sea
    * 1: Land (pixels with this value may include areas of sea)
  * Bit 4: Radiometric quality SWIR flag 
    * 0: Bad
    * 1: Good
  * Bit 5: Radiometric quality NIR flag 
    * 0: Bad
    * 1: Good
  * Bit 6: Radiometric quality RED flag 
    * 0: Bad
    * 1: Good
  * Bit 7: Radiometric quality BLUE flag 
    * 0: Bad
    * 1: Good

  
`TIME` | min | Time elapsed since the start of image collection of this mosaic  
**Image Properties**
Name | Type | Description  
---|---|---  
ARCHIVING_DATE | STRING | Archiving date  
CLOUD_COVER_PERCENTAGE | DOUBLE | Cloud cover percentage  
LAND_PERCENTAGE | DOUBLE | Land percentage  
MISSING_DATA_PERCENTAGE | DOUBLE | Missing data percentage  
PROBAV_ATMCORR_SMAC_VERSION | STRING | Initial version of the atmospheric correction algorithm  
PROBAV_CLOUDICESNOWDETECTION_VERSION | STRING | Initial version of the cloud and snow/ice detection algorithm  
PROBAV_COMPOSITING_MVC_VERSION | STRING | Initial version of the MVC compositing algorithm  
PROBAV_GEOMODELLING_VERSION | STRING | Initial version of the geometric modelling algorithm  
PROBAV_MAPPING_VERSION | STRING | Initial version of the projection algorithm  
PROBAV_MOSAIC_VERSION | STRING | Initial version of the mosaicking algorithm  
PROBAV_RADIOMODELLING_VERSION | STRING | Initial version of the radiometric modelling algorithm  
PROBAV_SHADOWDETECTION_VERSION | STRING | Initial version of the shadow detection algorithm  
PRODUCT_VERSION | STRING | Product version  
SNOW_COVER_PERCENTAGE | DOUBLE | Snow cover percentage  
**Terms of Use**
PROBA-V 300m and 100m data are freely available for data older than 1 month.
Citations:
  * Copyright ESA-BELSPO, produced by Vito


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('VITO/PROBAV/C1/S1_TOC_100M')
.filter(ee.Filter.date('2018-03-01','2018-04-01'));
varfalseColor=dataset.select(['RED','NIR','BLUE']);
varfalseColorVis={
min:20.0,
max:2000.0,
};
Map.setCenter(17.93,7.71,2);
Map.addLayer(falseColor,falseColorVis,'False Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/VITO/VITO_PROBAV_C1_S1_TOC_100M)
[ PROBA-V C1 Top Of Canopy Daily Synthesis 100m ](https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M)
Proba-V is a satellite mission tasked to map land cover and vegetation growth. It was designed to provide continuity for the VGT optical instrument from the SPOT-4 and SPOT-5 missions. The sensor collects data in three VNIR (visible and near-infrared) bands and one SWIR (short-wave infrared) spectral band with a …
VITO/PROBAV/C1/S1_TOC_100M, esa,multispectral,nir,proba,probav,satellite-imagery,swir,vito 
2013-10-17T00:00:00Z/2021-10-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://proba-v.vgt.vito.be/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/VITO_PROBAV_C1_S1_TOC_100M)


