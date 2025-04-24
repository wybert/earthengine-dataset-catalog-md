 
#  ASTER L1T Radiance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![ASTER/AST_L1T_003](https://developers.google.com/earth-engine/datasets/images/ASTER/ASTER_AST_L1T_003_sample.png) 

Dataset Availability
    2000-03-04T00:00:00Z–2025-04-18T22:27:11Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/ASTER/AST_L1T.003) 

Earth Engine Snippet
     `    ee.ImageCollection("ASTER/AST_L1T_003")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ASTER/ASTER_AST_L1T_003) 

Revisit Interval
    16 Days 

Tags
     [aster](https://developers.google.com/earth-engine/datasets/tags/aster) [imagery](https://developers.google.com/earth-engine/datasets/tags/imagery) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [nir](https://developers.google.com/earth-engine/datasets/tags/nir) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [swir](https://developers.google.com/earth-engine/datasets/tags/swir) [terra](https://developers.google.com/earth-engine/datasets/tags/terra) [thermal](https://developers.google.com/earth-engine/datasets/tags/thermal) [toa](https://developers.google.com/earth-engine/datasets/tags/toa) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
eos
tir
vnir
[Description](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#dois) More
**Note:** Data collection has been paused as of November 28, 2024, due to technical issues with the ASTER instrument. See the USGS [announcement](https://lpdaac.usgs.gov/news/terra-aster-safe-mode-alert/) for more information.
The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) is a multispectral imager that was launched on board NASA's Terra spacecraft in December, 1999. ASTER can collect data in 14 spectral bands from the visible to the thermal infrared. Each scene covers an area of 60 x 60 km. These scenes, produced by the USGS, contain calibrated at-sensor radiance, ortho-rectified and terrain corrected.
Not all 14 bands were collected in each scene. An asset property named ORIGINAL_BANDS_PRESENT contains the list of bands that are present in each scene.
To convert from Digital Numbers (DN) to radiance at the sensor, the unit conversion coefficients are available in the metadata. See [ASTER L1T Product Users' Guide](https://lpdaac.usgs.gov/documents/647/AST__L1T_User_Guide_V3.pdf) and [ASTER L1T Product Specification](https://lpdaac.usgs.gov/documents/300/ASTER_L1T_Product_Specification.pdf) for more information.
Documentation:
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/72/AST_L1T_ATBD.pdf)
  * [User's Guide](https://lpdaac.usgs.gov/documents/647/AST__L1T_User_Guide_V3.pdf)
  * [ASTER Level-1T Product Specification](https://lpdaac.usgs.gov/documents/300/ASTER_L1T_Product_Specification.pdf)
  * [ASTER L1T Quick Reference Guide](https://lpdaac.usgs.gov/documents/174/AST_L1T_Quick_Reference_Guide.pdf)


**Bands**
Name | Min | Max | Pixel Size | Wavelength | Description  
---|---|---|---|---|---  
`B01` |  1  |  255  |  15 meters  | 0.520-0.600μm | VNIR_Band1 (visible green/yellow)  
`B02` |  1  |  255  |  15 meters  | 0.630-0.690μm | VNIR_Band2 (visible red)  
`B3N` |  1  |  255  |  15 meters  | 0.780-0.860μm | VNIR_Band3N (near infrared, nadir pointing)  
`B04` |  1  |  255  |  30 meters  | 1.600-1.700μm | SWIR_Band4 (short-wave infrared)  
`B05` |  1  |  255  |  30 meters  | 2.145-2.185μm | SWIR_Band5 (short-wave infrared)  
`B06` |  1  |  255  |  30 meters  | 2.185-2.225μm | SWIR_Band6 (short-wave infrared)  
`B07` |  1  |  255  |  30 meters  | 2.235-2.285μm | SWIR_Band7 (short-wave infrared)  
`B08` |  1  |  255  |  30 meters  | 2.295-2.365μm | SWIR_Band8 (short-wave infrared)  
`B09` |  1  |  255  |  30 meters  | 2.360-2.430μm | SWIR_Band9 (short-wave infrared)  
`B10` |  1  |  4095  |  90 meters  | 8.125-8.475μm | TIR_Band10 (thermal infrared)  
`B11` |  1  |  4095  |  90 meters  | 8.475-8.825μm | TIR_Band11 (thermal infrared)  
`B12` |  1  |  4095  |  90 meters  | 8.925-9.275μm | TIR_Band12 (thermal infrared)  
`B13` |  1  |  4095  |  90 meters  | 10.250-10.950μm | TIR_Band13 (thermal infrared)  
`B14` |  1  |  4095  |  90 meters  | 10.950-11.650μm | TIR_Band14 (thermal infrared)  
**Image Properties**
Name | Type | Description  
---|---|---  
BAD_PIXELS_B01 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B02 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B03 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B04 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B05 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B06 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B07 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B08 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B09 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B10 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B11 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B12 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B13 | DOUBLE | Number of bad pixels  
BAD_PIXELS_B14 | DOUBLE | Number of bad pixels  
CLOUDCOVER | DOUBLE | Cloud coverage  
COARSE_DEM_DATE | STRING | Coarse DEM issuance date  
COARSE_DEM_NOTE | STRING | Coarse DEM comments  
COARSE_DEM_VERSION | STRING | Coarse DEM version number  
FLYING_DIRECTION | STRING | The satellite flight direction when observation is done: 'AS' - ascending direction, 'DE' - descending direction  
GAIN_COEFFICIENT_B01 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B02 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B03 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B04 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B05 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B06 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B07 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B08 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B09 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B10 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B11 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B12 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B13 | DOUBLE | Coefficient used for radiance conversion  
GAIN_COEFFICIENT_B14 | DOUBLE | Coefficient used for radiance conversion  
GAIN_SETTING_B01 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B02 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B03 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B04 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B05 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B06 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B07 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B08 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B09 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B10 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B11 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B12 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B13 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GAIN_SETTING_B14 | STRING | Band gain setting: 'HGH' - high, 'NOR' - normal, 'LOW' - low, 'LO1' - low 1, or 'LO2' - low 2  
GCP_CHIPS_CORRELATED | DOUBLE | How many chips correlated during correlation statistics creation  
GEOMETRIC_DB_DATE | STRING | Geometric correction data issuance date  
GEOMETRIC_DB_VERSION | STRING | Geometric correction data version number  
GRANULE_REPROCESSING | STRING | What reprocessing has been performed on the granule: 'not reprocessed', 'reprocessed once', 'reprocessed twice', or 'reprocessing n times'  
ORBIT_NUMBER | DOUBLE | The orbit number of the satellite when data is acquired  
ORIGINAL_BANDS_PRESENT | DOUBLE | List of bands that are present in each scene  
PGE_VERSION | STRING | The version of PGE  
PRODUCTION_TIME | DOUBLE | Generation time of this product  
QA_PERCENT_INTERPOLATED_DATA | DOUBLE | The percentage of interpolated data in the scene  
QA_PERCENT_MISSING_DATA | DOUBLE | The percentage of missing data in the scene  
QA_PERCENT_OUT_OF_BOUNDS_DATA | DOUBLE | The percentage of out of bounds data in the scene  
RADIOMETRIC_DB_DATE | STRING | Radiometric correction data issuance date  
RADIOMETRIC_DB_VERSION | STRING | Radiometric correction data version number  
RESAMPLING_METHOD_B01 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B02 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B03 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B04 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B05 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B06 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B07 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B08 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B09 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B10 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B11 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B12 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B13 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
RESAMPLING_METHOD_B14 | STRING | Resampling method: 'BL', 'NN', or 'CC'  
SATELLITE_RECURRENT_CYCLENUMBER | DOUBLE | The satellite recurrent cycle number  
SATELLITE_REVOLUTION_NUMBER | DOUBLE | The satellite revolution number in the cycle  
SCENE_PATH | DOUBLE | Scene path  
SCENE_ROW | DOUBLE | Scene row  
SCENE_VIEW | DOUBLE | Scene view  
SOLAR_AZIMUTH | DOUBLE | Sun direction as seen from the scene center; azimuth angle in degrees measured eastward from North (0.0<az<360)  
SOLAR_ELEVATION | DOUBLE | Sun direction as seen from the scene center; elevation angle in degrees (-90.0<el<90.0)  
SOURCE_DATA_GRANULE | STRING | ID of input AST_L1A data granule used for generating this product  
SWIR_POINTING_ANGLE | DOUBLE | Pointing angle in degrees  
TIR_POINTING_ANGLE | DOUBLE | Pointing angle in degrees  
VNIR_POINTING_ANGLE | DOUBLE | Pointing angle in degrees  
**Terms of Use**
ASTER data and products distributed by the LP DAAC, with the exception of the ASTER Global Digital Elevation Model (GDEM) dataset (ASTGTM) version 2 (v2), have no restrictions on data use, sale, or subsequent redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/ASTER/AST_L1T.003 ](https://doi.org/10.5067/ASTER/AST_L1T.003)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('ASTER/AST_L1T_003')
.filter(ee.Filter.date('2018-01-01','2018-08-15'));
varfalseColor=dataset.select(['B3N','B02','B01']);
varfalseColorVis={
min:0.0,
max:255.0,
};
Map.setCenter(-122.0272,39.6734,11);
Map.addLayer(falseColor.median(),falseColorVis,'False Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ASTER/ASTER_AST_L1T_003)
[ ASTER L1T Radiance ](https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003)
Note: Data collection has been paused as of November 28, 2024, due to technical issues with the ASTER instrument. See the USGS announcement for more information. The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) is a multispectral imager that was launched on board NASA's Terra spacecraft in December, 1999. …
ASTER/AST_L1T_003, aster,imagery,nasa,nir,radiance,satellite-imagery,swir,terra,thermal,toa,usgs 
2000-03-04T00:00:00Z/2025-04-18T22:27:11Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/ASTER/AST_L1T.003 ](https://doi.org/https://doi.org/10.5067/ASTER/AST_L1T.003)
  * [ https://doi.org/10.5067/ASTER/AST_L1T.003 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ASTER_AST_L1T_003)


