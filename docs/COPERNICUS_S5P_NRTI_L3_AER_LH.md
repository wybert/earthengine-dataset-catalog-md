 
#  Sentinel-5P NRTI AER LH: Near Real-Time UV Aerosol Layer Height 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/S5P/NRTI/L3_AER_LH](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_AER_LH_sample.png) 

Dataset Availability
    2018-07-10T11:17:44Z–2025-04-21T08:26:30Z 

Dataset Provider
     [ European Union/ESA/Copernicus ](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_AER_LH")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_AER_LH) 

Revisit Interval
    2 Days 

Tags
     [aerosol](https://developers.google.com/earth-engine/datasets/tags/aerosol) [air-quality](https://developers.google.com/earth-engine/datasets/tags/air-quality) [alh](https://developers.google.com/earth-engine/datasets/tags/alh) [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [knmi](https://developers.google.com/earth-engine/datasets/tags/knmi) [pollution](https://developers.google.com/earth-engine/datasets/tags/pollution) [s5p](https://developers.google.com/earth-engine/datasets/tags/s5p) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [tropomi](https://developers.google.com/earth-engine/datasets/tags/tropomi) [uvai](https://developers.google.com/earth-engine/datasets/tags/uvai)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH#terms-of-use) More
### NRTI/L3_AER_LH
This dataset provides offline high-resolution imagery of the UV Aerosol Index (UVAI), also called the Absorbing Layer Height (ALH).
The ALH is very sensitive to cloud contamination. However, aerosols and clouds can be difficult to distinguish, and ALH is computed for all FRESCO effective cloud fractions smaller than 0.05. Cloud masks are available from FRESCO and VIIRS, and are strongly recommended to filter for residual clouds. A sunglint mask is also available to screen sunglint regions, which are not filtered beforehand.
It is known that high surface albedos negatively influence the ALH, biasing the ALH towards the surface. In general, the ALH over (dark) oceans is considered reliable to within the requirement of 1000 m or 100 hPa. Over land, especially bright surfaces, the accuracy may be lower, and the use of the ALH product over bright surfaces like deserts is not advisable.
For this L3 AER_LH product, the aerosol_mid_pressure is calculated with a pair of measurements at the 354 nm and 388 nm wavelengths. The [COPERNICUS/S5P/OFFL/L3_SO2](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_SO2) product has the absorbing_aerosol_index calculated using the 340 nm and 380 nm wavelengths.
Example harpconvert invocation for one tile: `harpconvert --format hdf5 --hdf5-compression 9 -a 'aerosol_height_validity>50;derive(datetime_stop {time}); bin_spatial(2001, 50.000000, 0.01, 2001, -120.000000, 0.01); keep(aerosol_height,aerosol_pressure,aerosol_optical_depth,    sensor_zenith_angle,sensor_azimuth_angle,solar_azimuth_angle,solar_zenith_angle)' S5P_NRTI_L2__AER_LH_20191202T233055_20191202T233555_11074_01_010302_20191203T012120.nc output.h5`
### Sentinel-5 Precursor
Sentinel-5 Precursor is a satellite launched on 13 October 2017 by the European Space Agency to monitor air pollution. The onboard sensor is frequently referred to as Tropomi (TROPOspheric Monitoring Instrument).
All of the S5P datasets, except CH4, have two versions: Near Real-Time (NRTI) and Offline (OFFL). CH4 is available as OFFL only. The NRTI assets cover a smaller area than the OFFL assets, but appear more quickly after acquisition. The OFFL assets contain data from a single orbit (which, due to half the earth being dark, contains data only for a single hemisphere).
Because of noise in the data, negative vertical column values are often observed in particular over clean regions or for low SO2 emissions. It is recommended not to filter these values except for outliers, i.e. for vertical columns lower than -0.001 mol/m^2.
The original Sentinel 5P Level 2 (L2) data is binned by time, not by latitude/longitude. To make it possible to ingest the data into Earth Engine, each Sentinel 5P L2 product is converted to L3, keeping a single grid per orbit (that is, no aggregation across products is performed).
Source products spanning the antimeridian are ingested as two Earth Engine assets, with suffixes _1 and _2.
The conversion to L3 is done by the [harpconvert](https://cdn.rawgit.com/stcorp/harp/master/doc/html/harpconvert.html) tool using the `bin_spatial` operation. The source data is filtered to remove pixels with QA values less than:
  * 80% for AER_AI
  * 75% for the tropospheric_NO2_column_number_density band of NO2
  * 50% for all other datasets except for O3 and SO2


The O3_TCL product is ingested directly (without running harpconvert).
**Pixel Size** 1113.2 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`aerosol_height` | m |  -81.17*  |  67622.6*  | The aerosol layer pressure is converted into an aerosol layer altitude using an appropriate temperature profile, i.e. the temperature profile used in the retrieval. The value is given relative to the geoid.  
`aerosol_pressure` | Pa |  2.69*  |  102886*  | Pressure of an aerosol layer with an assumed pressure thickness of (currently) 50 hPa and a constant aerosol volume extinction coefficient and single scattering albedo.  
`aerosol_optical_depth` | Pa |  -0.6*  |  37.42*  | Aerosol optical thickness τ of the assumed aerosol layer. The optical thickness holds for 760 nm.  
`sensor_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the satellite at the ground pixel location (WGS84); angle measured East-of-North.  
`sensor_zenith_angle` | deg |  0.098*  |  66.87*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
`solar_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the Sun at the ground pixel location (WGS84); angle measured East-of-North.  
`solar_zenith_angle` | deg |  12.93*  |  74.7*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
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
**Terms of Use**
The use of Sentinel data is governed by the [Copernicus Sentinel Data Terms and Conditions.](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice)
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH#code-editor-javascript-sample) More
```
varcollection=ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_AER_LH')
.select('aerosol_height')
.filterDate('2019-06-01','2019-06-06');
varband_viz={
min:-81.17,
max:67622.56,
palette:['blue','purple','cyan','green','yellow','red']
};
Map.addLayer(collection.mean(),band_viz,'S5P Aerosol Height');
Map.setCenter(44.09,24.27,4);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_AER_LH)
[ Sentinel-5P NRTI AER LH: Near Real-Time UV Aerosol Layer Height ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH)
NRTI/L3_AER_LH This dataset provides offline high-resolution imagery of the UV Aerosol Index (UVAI), also called the Absorbing Layer Height (ALH). The ALH is very sensitive to cloud contamination. However, aerosols and clouds can be difficult to distinguish, and ALH is computed for all FRESCO effective cloud fractions smaller than 0.05. …
COPERNICUS/S5P/NRTI/L3_AER_LH, aerosol,air-quality,alh,atmosphere,copernicus,esa,eu,knmi,pollution,s5p,sentinel,tropomi,uvai 
2018-07-10T11:17:44Z/2025-04-21T08:26:30Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_AER_LH)


