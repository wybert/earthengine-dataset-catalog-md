 
#  Sentinel-5P NRTI CLOUD: Near Real-Time Cloud Properties 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/S5P/NRTI/L3_CLOUD](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_CLOUD_sample.png) 

Dataset Availability
    2018-07-05T23:24:16Z–2025-04-21T08:26:30Z 

Dataset Provider
     [ European Union/ESA/Copernicus ](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_CLOUD")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_CLOUD) 

Revisit Interval
    2 Days 

Tags
     [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [cloud](https://developers.google.com/earth-engine/datasets/tags/cloud) [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [dlr](https://developers.google.com/earth-engine/datasets/tags/dlr) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [s5p](https://developers.google.com/earth-engine/datasets/tags/s5p) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [tropomi](https://developers.google.com/earth-engine/datasets/tags/tropomi)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD#terms-of-use) More
### NRTI/L3_CLOUD
This dataset provides near real-time high-resolution imagery of cloud parameters.
The TROPOMI/S5P cloud properties retrieval is based on the OCRA and ROCINN algorithms currently being used in the operational GOME and GOME-2 products. OCRA retrieves the cloud fraction using measurements in the UV/VIS spectral regions and ROCINN retrieves the cloud height (pressure) and optical thickness (albedo) using measurements in and around the oxygen A-band at 760 nm. Version 3.0 of the algorithms are used, which are based on a more realistic treatment of clouds as optically uniform layers of light-scattering particles. Additionally, the cloud parameters are also provided for a cloud model which assumes the cloud to be a Lambertian reflecting boundary. [More information.](http://www.tropomi.eu/data-products/cloud)
### NRTI L3 Product
To make our NRTI L3 products, we use [harpconvert](https://stcorp.github.io/harp/doc/html/harpconvert.html) to grid the data.
Example harpconvert invocation for one tile: `harpconvert --format hdf5 --hdf5-compression 9 -a 'cloud_fraction>50;derive(datetime_stop {time}); bin_spatial(2001, 50.000000, 0.01, 2001, -120.000000, 0.01); keep(cloud_fraction,cloud_top_pressure,cloud_top_height, cloud_base_pressure,cloud_base_height,cloud_optical_depth,surface_albedo, sensor_azimuth_angle,sensor_zenith_angle,solar_azimuth_angle, solar_zenith_angle)' S5P_NRTI_L2__CLOUD__20190208T230503_20190208T231003_06860_01_010105_20190209T005255.nc output.h5`
Assets between the dates 2018-07-10 and 2018-07-18 are missing due to non-standard structure of product files.
**Pixel Size** 1113.2 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`cloud_fraction` | Fraction |  0*  |  1*  | Retrieved effective radiometric cloud fraction  
`cloud_top_pressure` | Pa |  12109*  |  101299*  | Retrieved atmospheric pressure at the level of cloud top  
`cloud_top_height` | m |  9*  |  15471*  | Retrieved altitude of the cloud top  
`cloud_base_pressure` | Pa |  14169*  |  101299*  | Cloud base pressure  
`cloud_base_height` | m |  9*  |  14545*  | Cloud base height  
`cloud_optical_depth` |  1*  |  250*  | Retrieved cloud optical depth  
`surface_albedo` |  0*  |  1*  | Surface albedo  
`sensor_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the satellite at the ground pixel location (WGS84); angle measured East-of-North.  
`sensor_zenith_angle` | deg |  0.09*  |  67*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
`solar_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the Sun at the ground pixel location (WGS84); angle measured East-of-North.  
`solar_zenith_angle` | deg |  8*  |  80*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
ALGORITHM_VERSION | STRING | The algorithm version used in L2 processing. It is separate from the processor (framework) version, to accommodate different release schedules for different products.  
BUILD_DATE | STRING | The date, expressed as milliseconds since 1 Jan 1970, when the software used to perform L2 processing was built.  
HARP_VERSION | INT | The version of the HARP tool used to grid the L2 data into an L3 product.  
INSTITUTION | STRING | The institution where data processing from L1 to L2 was performed.  
L3_PROCESSING_TIME | INT | The date, expressed as milliseconds since 1 Jan 1970, when Google processed the L2 data into L3 using harpconvert.  
LAT_MAX | DOUBLE | The maximum latitude of the asset (degrees).  
LAT_MIN | DOUBLE | The minimum latitude of the asset (degrees).  
LON_MAX | DOUBLE | The maximum longitude of the asset (degrees).  
LON_MIN | DOUBLE | The minimum longitude of the asset (degrees).  
ORBIT | INT | The orbit number of the satellite when the data was acquired.  
PLATFORM | STRING | Name of the platform which acquired the data.  
PROCESSING_STATUS | STRING | The processing status of the product on a global level, mainly based on the availability of auxiliary input data. Possible values are "Nominal" and "Degraded".  
PROCESSOR_VERSION | STRING | The version of the software used for L2 processing, as a string of the form "major.minor.patch".  
PRODUCT_ID | STRING | Id of the L2 product used to generate this asset.  
PRODUCT_QUALITY | STRING | Indicator that specifies whether the product quality is degraded or not. Allowed values are "Degraded" and "Nominal".  
SENSOR | STRING | Name of the sensor which acquired the data.  
SPATIAL_RESOLUTION | STRING | Spatial resolution at nadir. For most products this is `3.5x7 km2`, except for `L2__O3__PR`, which uses `28x21km2`, and `L2__CO____` and `L2__CH4___`, which both use `7x7 km2`. This attribute originates from the CCI standard.  
TIME_REFERENCE_DAYS_SINCE_1950 | INT | Days from 1 Jan 1950 to when the data was acquired.  
TIME_REFERENCE_JULIAN_DAY | DOUBLE | The Julian day number when the data was acquired.  
TRACKING_ID | STRING | UUID for the L2 product file.  
CLOUD_MODE | STRING | Tells which model was used to generate this dataset, the CAL (Clouds As Layers) model or the CRB (Clouds as Reflecting Boundaries) model. Valid values of this property are "cal" or "crb", respectively, with "cal" being the default.  
STATUS_MET_2D | STRING | This dataset uses some dynamic auxiliary data from the European Centre for Medium-Range Weather Forecasts. If the ECMWF data was used, this field will have the value 'Nominal'. If the ECMWF data was not used, a fallback solution was used, and this field will have the value of "Fallback".  
**Terms of Use**
The use of Sentinel data is governed by the [Copernicus Sentinel Data Terms and Conditions.](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice)
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD#code-editor-javascript-sample) More
```
varcollection=ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CLOUD')
.select('cloud_fraction')
.filterDate('2019-06-01','2019-06-02');
varband_viz={
min:0,
max:0.95,
palette:['black','blue','purple','cyan','green','yellow','red']
};
Map.addLayer(collection.mean(),band_viz,'S5P Cloud');
Map.setCenter(-58.14,-10.47,2);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_CLOUD)
[ Sentinel-5P NRTI CLOUD: Near Real-Time Cloud Properties ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD)
NRTI/L3_CLOUD This dataset provides near real-time high-resolution imagery of cloud parameters. The TROPOMI/S5P cloud properties retrieval is based on the OCRA and ROCINN algorithms currently being used in the operational GOME and GOME-2 products. OCRA retrieves the cloud fraction using measurements in the UV/VIS spectral regions and ROCINN retrieves the …
COPERNICUS/S5P/NRTI/L3_CLOUD, atmosphere,cloud,copernicus,dlr,esa,eu,s5p,sentinel,tropomi 
2018-07-05T23:24:16Z/2025-04-21T08:26:30Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_CLOUD)


