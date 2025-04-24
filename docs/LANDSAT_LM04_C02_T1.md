 
#  USGS Landsat 4 MSS Collection 2 Tier 1 Raw Scenes 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/LM04/C02/T1](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_LM04_C02_T1_sample.png) 

Dataset Availability
    1982-08-14T18:22:17Z–1992-08-28T07:14:35Z 

Dataset Provider
     [ USGS ](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/LM04/C02/T1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LM04_C02_T1) 

Revisit Interval
    16 Days 

Tags
     [c2](https://developers.google.com/earth-engine/datasets/tags/c2) [global](https://developers.google.com/earth-engine/datasets/tags/global) [l4](https://developers.google.com/earth-engine/datasets/tags/l4) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [lm4](https://developers.google.com/earth-engine/datasets/tags/lm4) [mss](https://developers.google.com/earth-engine/datasets/tags/mss) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [t1](https://developers.google.com/earth-engine/datasets/tags/t1) [tier1](https://developers.google.com/earth-engine/datasets/tags/tier1) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1#terms-of-use) More
Landsat 4 MSS Collection 2 Tier 1 DN values, representing scaled, calibrated at-sensor radiance.
Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The georegistration of Tier 1 scenes will be consistent and within prescribed tolerances [<=12 m root mean square error (RMSE)]. All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of sensor) across the full collection. See more information [in the USGS docs](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collections).
**Bands**
Name | Pixel Size | Wavelength | Description  
---|---|---|---  
`B1` |  60 meters  | 0.5 - 0.6 μm | Green  
`B2` |  60 meters  | 0.6 - 0.7 μm | Red  
`B3` |  60 meters  | 0.7 - 0.8 μm | Near Infrared 1  
`B4` |  30 meters  | 0.8 - 1.1 μm | Near Infrared 2  
`QA_PIXEL` |  30 meters  | Landsat Collection 2 MSS QA Bitmask  
Bitmask for QA_PIXEL
  * Bit 0: Fill 
    * 0: Image data
    * 1: Fill data
  * Bits 1-2: Unused 
  * Bit 3: Cloud 
    * 0: Not likely to exist
    * 1: Likely to exist
  * Bits 4-7: Unused 
  * Bits 8-9: Cloud Confidence 
    * 0: No confidence level set
    * 1: Low confidence
    * 2: Unused
    * 3: High confidence

  
`QA_RADSAT` |  30 meters  | Radiometric saturation QA  
Bitmask for QA_RADSAT
  * Bit 0: Band 1 data saturated 
  * Bit 1: Band 2 data saturated 
  * Bit 2: Band 3 data saturated 
  * Bit 3: Band 4 data saturated 
  * Bit 4: Band 5 data saturated 
  * Bit 5: Band 6 data saturated 
  * Bits 6-8: Unused 
  * Bit 9: Dropped pixel 
    * 0: Pixel present
    * 1: Detector does not have a value

  
**Image Properties**
Name | Type | Description  
---|---|---  
CLOUD_COVER | DOUBLE | Percentage cloud cover (0-100), -1 = not calculated.  
CLOUD_COVER_LAND | DOUBLE | Percentage cloud cover over land (0-100), -1 = not calculated.  
COLLECTION_CATEGORY | STRING | Tier of scene. (T1 or T2)  
COLLECTION_NUMBER | DOUBLE | Number of collection.  
CORRECTION_GAIN_BAND_1 | STRING | Internal calibration gain method for band 1.  
CORRECTION_GAIN_BAND_2 | STRING | Internal calibration gain method for band 2.  
CORRECTION_GAIN_BAND_3 | STRING | Internal calibration gain method for band 3.  
CORRECTION_GAIN_BAND_4 | STRING | Internal calibration gain method for band 4.  
DATA_SOURCE_ELEVATION | STRING | Indicates the source of the DEM used in the correction process. Possible values: "GLS2000", "RAMP", "GTOPO30".'  
DATA_TYPE_L0RP | STRING | Data type identifier string used to create the L0RP product.  
DATE_ACQUIRED | STRING | Image acquisition date. "YYYY-MM-DD"  
DATE_PRODUCT_GENERATED | INT | Product generation epoch.  
DATUM | STRING | Datum used in image creation.  
EARTH_SUN_DISTANCE | DOUBLE | Earth sun distance in astronomical units (AU).  
ELLIPSOID | STRING | Ellipsoid used in image creation.  
EPHEMERIS_TYPE | STRING | Ephemeris data type used to perform geometric correction. (Definitive or Predictive)  
GAIN_BAND_1 | STRING | Gain state for Band 1. (L = Low gain, H = High)  
GAIN_BAND_2 | STRING | Gain state for Band 2. (L = Low gain, H = High)  
GAIN_BAND_3 | STRING | Gain state for Band 3. (L = Low gain, H = High)  
GAIN_BAND_4 | STRING | Gain state for Band 4. (L = Low gain, H = High)  
GEOMETRIC_RMSE_MODEL | DOUBLE | Combined Root Mean Square Error (RMSE) of the geometric residuals (meters) in both across-track and along-track directions measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_X | DOUBLE | RMSE of the X direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_Y | DOUBLE | RMSE of the Y direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_VERIFY | DOUBLE | RMSE of the geometric residuals (pixels) in both line and sample directions measured on the terrain-corrected product independently using GLS2000.  
GEOMETRIC_RMSE_VERIFY_QUAD_LL | DOUBLE | RMSE of the geometric residuals (pixels) of the lower-left quadrant measured on the terrain-corrected product independently using GLS2000.  
GEOMETRIC_RMSE_VERIFY_QUAD_LR | DOUBLE | RMSE of the geometric residuals (pixels) of the lower-right quadrant measured on the terrain-corrected product independently using GLS2000.  
GEOMETRIC_RMSE_VERIFY_QUAD_UL | DOUBLE | RMSE of the geometric residuals (pixels) of the upper-left quadrant measured on the terrain-corrected product independently using GLS2000.  
GEOMETRIC_RMSE_VERIFY_QUAD_UR | DOUBLE | RMSE of the geometric residuals (pixels) of the upper-right quadrant measured on the terrain-corrected product independently using GLS2000.  
GRID_CELL_SIZE_REFLECTIVE | DOUBLE | Grid cell size used in creating the image for the reflective band.  
GROUND_CONTROL_POINTS_MODEL | DOUBLE | The number of ground control points used. Not used in L1GT products. Values: 0 - 999 (0 is used for L1T products that have used Multi-scene refinement).  
GROUND_CONTROL_POINTS_VERIFY | DOUBLE | The number of ground control points used in the verification of the terrain corrected product. Values: -1 to 1615 (-1 = not available)  
GROUND_CONTROL_POINTS_VERSION | DOUBLE | The number of ground control points used in the verification of the terrain corrected product. Values: -1 to 1615 (-1 = not available)  
IMAGE_QUALITY | DOUBLE | Image quality, 0 = worst, 9 = best, -1 = quality not calculated  
LANDSAT_PRODUCT_ID | STRING | The naming convention of each Landsat Collection 1 Level-1 image based on acquisition parameters and processing parameters. Format: LXSS_LLLL_PPPRRR_YYYYMMDD_yyyymmdd_CC_TX
  * L = Landsat
  * X = Sensor (O = Operational Land Imager, T = Thermal Infrared Sensor, C = Combined OLI/TIRS)
  * SS = Satellite (08 = Landsat 8)
  * LLLL = Processing Correction Level (L1TP = precision and terrain, L1GT = systematic terrain, L1GS = systematic)
  * PPP = WRS Path
  * RRR = WRS Row
  * YYYYMMDD = Acquisition Date expressed in Year, Month, Day
  * yyyymmdd = Processing Date expressed in Year, Month, Day
  * CC = Collection Number (01)
  * TX = Collection Category (RT = Real Time, T1 = Tier 1, T2 = Tier 2)

  
LANDSAT_SCENE_ID | STRING | The Pre-Collection naming convention of each image is based on acquisition parameters. This was the naming convention used prior to Collection 1. Format: LXSPPPRRRYYYYDDDGSIVV
  * L = Landsat
  * X = Sensor (O = Operational Land Imager, T = Thermal Infrared Sensor, C = Combined OLI/TIRS)
  * S = Satellite (08 = Landsat 8)
  * PPP = WRS Path
  * RRR = WRS Row
  * YYYY = Year of Acquisition
  * DDD = Julian Day of Acquisition
  * GSI = Ground Station Identifier
  * VV = Version

  
MAP_PROJECTION | STRING | Projection used to represent the 3-dimensional surface of the earth for the Level-1 product.  
MAP_PROJECTION_L0RA | STRING | L0RA map projection selectively applied to HDTs based on geographic location. Used for processed archive data.  
ORIENTATION | STRING | Orientation used in creating the image. Values: NOMINAL = Nominal Path, NORTH_UP = North Up, TRUE_NORTH = True North, USER = User  
PRESENT_BAND_1 | STRING | Presence of Band 1 (Y = Yes, N = No, M = Missing, I = Unknown)  
PRESENT_BAND_2 | STRING | Presence of Band 2 (Y = Yes, N = No, M = Missing, I = Unknown)  
PRESENT_BAND_3 | STRING | Presence of Band 3 (Y = Yes, N = No, M = Missing, I = Unknown)  
PRESENT_BAND_4 | STRING | Presence of Band 4 (Y = Yes, N = No, M = Missing, I = Unknown)  
PROCESSING_LEVEL | DOUBLE | One of L1GS, L1GT, or L1TP.  
PROCESSING_SOFTWARE_VERSION | STRING | Name and version of the processing software used to generate the L1 product.  
RADIANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 1.  
RADIANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 2.  
RADIANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 3.  
RADIANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 4.  
RADIANCE_MULT_BAND_1 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 1 DN to radiance.  
RADIANCE_MULT_BAND_2 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 2 DN to radiance.  
RADIANCE_MULT_BAND_3 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 3 DN to radiance.  
RADIANCE_MULT_BAND_4 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 4 DN to radiance.  
REFLECTANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTANCE_MULT_BAND_1 | DOUBLE | Multiplicative factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_MULT_BAND_2 | DOUBLE | Multiplicative factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_MULT_BAND_3 | DOUBLE | Multiplicative factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_MULT_BAND_4 | DOUBLE | Multiplicative factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTIVE_LINES | DOUBLE | Number of product lines for the reflective bands.  
REFLECTIVE_SAMPLES | DOUBLE | Number of product samples for the reflective bands.  
REQUEST_ID | STRING | Request id, nnnyymmdd0000_0000
  * nnn = node number
  * yy = year
  * mm = month
  * dd = day

  
RESAMPLING_OPTION | STRING | Resampling option used in creating the image.  
SATURATION_BAND_1 | STRING | Flag indicating saturated pixels for band 1 ('Y'/'N')  
SATURATION_BAND_2 | STRING | Flag indicating saturated pixels for band 2 ('Y'/'N')  
SATURATION_BAND_3 | STRING | Flag indicating saturated pixels for band 3 ('Y'/'N')  
SATURATION_BAND_4 | STRING | Flag indicating saturated pixels for band 4 ('Y'/'N')  
SCENE_CENTER_TIME | STRING | Scene center time of acquired image. HH:MM:SS.SSSSSSSZ
  * HH = Hour (00-23)
  * MM = Minutes
  * SS.SSSSSSS = Fractional seconds
  * Z = "Zulu" time (same as GMT)

  
SENSOR_ID | STRING | Sensor used to capture data.  
SPACECRAFT_ID | STRING | Spacecraft identification.  
STATION_ID | STRING | Ground Station/Organisation that received the data.  
SUN_AZIMUTH | DOUBLE | Sun azimuth angle in degrees for the image center location at the image center acquisition time.  
SUN_ELEVATION | DOUBLE | Sun elevation angle in degrees for the image center location at the image center acquisition time.  
UTM_ZONE | DOUBLE | UTM zone number used in product map projection.  
WRS_PATH | DOUBLE | The WRS orbital path number (001 - 251).  
WRS_ROW | DOUBLE | Landsat satellite WRS row (001-248).  
WRS_TYPE | DOUBLE | World Reference System (WRS) type used for the collection of this scene.  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/LM04/C02/T1')
.filterDate('1989-01-01','1992-12-31');
varnearInfrared321=dataset.select(['B3','B2','B1']);
varnearInfrared321Vis={};
Map.setCenter(6.746,46.529,6);
Map.addLayer(nearInfrared321,nearInfrared321Vis,'Near Infrared (321)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LM04_C02_T1)
[ USGS Landsat 4 MSS Collection 2 Tier 1 Raw Scenes ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1)
Landsat 4 MSS Collection 2 Tier 1 DN values, representing scaled, calibrated at-sensor radiance. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are …
LANDSAT/LM04/C02/T1, c2,global,l4,landsat,lm4,mss,radiance,satellite-imagery,t1,tier1,usgs 
1982-08-14T18:22:17Z/1992-08-28T07:14:35Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM04_C02_T1)


