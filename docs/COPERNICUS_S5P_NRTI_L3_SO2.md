 
#  Sentinel-5P NRTI SO2: Near Real-Time Sulfur Dioxide 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/S5P/NRTI/L3_SO2](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_SO2_sample.png) 

Dataset Availability
    2018-07-10T11:17:44Z–2025-04-21T08:26:30Z 

Dataset Provider
     [ European Union/ESA/Copernicus ](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_SO2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_SO2) 

Revisit Interval
    2 Days 

Tags
     [air-quality](https://developers.google.com/earth-engine/datasets/tags/air-quality) [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [bira](https://developers.google.com/earth-engine/datasets/tags/bira) [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [dlr](https://developers.google.com/earth-engine/datasets/tags/dlr) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [pollution](https://developers.google.com/earth-engine/datasets/tags/pollution) [s5p](https://developers.google.com/earth-engine/datasets/tags/s5p) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [so2](https://developers.google.com/earth-engine/datasets/tags/so2) [sulfur-dioxide](https://developers.google.com/earth-engine/datasets/tags/sulfur-dioxide) [tropomi](https://developers.google.com/earth-engine/datasets/tags/tropomi)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2#terms-of-use) More
### NRTI/L3_SO2
This dataset provides near real-time high-resolution imagery of atmospheric sulfur dioxide (SO2) concentrations.
Sulfur dioxide (SO2) enters the Earth's atmosphere through both natural and anthropogenic processes. It plays a role in chemistry on a local and global scale and its impact ranges from short-term pollution to effects on climate. Only about 30% of the emitted SO2 comes from natural sources; the majority is of anthropogenic origin. SO2 emissions adversely affect human health and air quality. SO2 has an effect on climate through radiative forcing, via the formation of sulfate aerosols. Volcanic SO2 emissions can also pose a threat to aviation, along with volcanic ash. S5P/TROPOMI samples the Earth's surface with a revisit time of one day with unprecedented spatial resolution of 3.5 x 7 km which allows the resolution of fine details including the detection of much smaller SO2 plumes. [More information.](https://www.tropomi.eu/data-products/sulfur-dioxide)
### NRTI L3 Product
To make our NRTI L3 products, we use [harpconvert](https://stcorp.github.io/harp/doc/html/harpconvert.html) to grid the data.
The qa value is adjusted before running harpconvert to satisfy all of the following criteria:
  * snow_ice < 0.5
  * sulfurdioxide_total_air_mass_factor_polluted > 0.1
  * sulfurdioxide_total_vertical_column > -0.001
  * qa_value > 0.5
  * cloud_fraction_crb < 0.3
  * solar_zenith_angle < 60


The 15km SO2 band is ingested only when solar_zenith_angle < 70.
Example harpconvert invocation for one tile: `harpconvert --format hdf5 --hdf5-compression 9 -a 'SO2_column_number_density_validity>50;derive(datetime_stop {time}); bin_spatial(2001, 50.000000, 0.01, 2001, -120.000000, 0.01); keep(SO2_column_number_density,SO2_column_number_density_amf,    SO2_slant_column_number_density,cloud_fraction, sensor_altitude,    sensor_azimuth_angle, sensor_zenith_angle,solar_azimuth_angle,    solar_zenith_angle)' S5P_NRTI_L2__SO2____20190129T101503_20190129T102003_06711_01_010105_20190129T111328.nc output.h5`
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
`SO2_column_number_density` | mol/m^2 |  -48*  |  0.24*  | SO2 vertical column density at ground level, calculated using the DOAS technique.  
`SO2_column_number_density_amf` | mol/m^2 |  0.1*  |  3.397*  | Weighted mean of cloudy and clear air mass factor (amf) weighted by intensity-weighted cloud fraction.  
`SO2_slant_column_number_density` | mol/m^2 |  -0.147*  |  0.162*  | SO2 ring corrected slant column number density  
`cloud_fraction` | Fraction |  0*  |  1*  | Effective cloud fraction. See the [Sentinel 5P L2 Input/Output Data Definition Spec](https://sentinels.copernicus.eu/documents/247904/3119978/Sentinel-5P-Level-2-Input-Output-Data-Definition), p.220.  
`sensor_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the satellite at the ground pixel location (WGS84); angle measured East-of-North.  
`sensor_zenith_angle` | deg |  0.09*  |  67*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
`solar_azimuth_angle` | deg |  -180*  |  180*  | Azimuth angle of the Sun at the ground pixel location (WGS84); angle measured East-of-North.  
`solar_zenith_angle` | deg |  8*  |  80*  | Zenith angle of the satellite at the ground pixel location (WGS84); angle measured away from the vertical.  
`SO2_column_number_density_15km` | mol/m^2 | SO2 vertical column density at 15km, calculated using the DOAS technique.  
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
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2#code-editor-javascript-sample) More
```
varcollection=ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_SO2')
.select('SO2_column_number_density')
.filterDate('2019-06-01','2019-06-11');
varband_viz={
min:0.0,
max:0.0005,
palette:['black','blue','purple','cyan','green','yellow','red']
};
Map.addLayer(collection.mean(),band_viz,'S5P SO2');
Map.setCenter(0.0,0.0,2);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S5P_NRTI_L3_SO2)
[ Sentinel-5P NRTI SO2: Near Real-Time Sulfur Dioxide ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2)
NRTI/L3_SO2 This dataset provides near real-time high-resolution imagery of atmospheric sulfur dioxide (SO2) concentrations. Sulfur dioxide (SO2) enters the Earth's atmosphere through both natural and anthropogenic processes. It plays a role in chemistry on a local and global scale and its impact ranges from short-term pollution to effects on climate. …
COPERNICUS/S5P/NRTI/L3_SO2, air-quality,atmosphere,bira,copernicus,dlr,esa,eu,pollution,s5p,sentinel,so2,sulfur-dioxide,tropomi 
2018-07-10T11:17:44Z/2025-04-21T08:26:30Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_SO2)


