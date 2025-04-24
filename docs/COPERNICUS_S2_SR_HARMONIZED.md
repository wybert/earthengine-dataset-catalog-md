 
#  Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A (SR) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/S2_SR_HARMONIZED](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S2_SR_HARMONIZED_sample.png) 

Dataset Availability
    2017-03-28T00:00:00Z–2025-04-22T14:21:05.411000Z 

Dataset Provider
     [ European Union/ESA/Copernicus ](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-2) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S2_SR_HARMONIZED) 

Revisit Interval
    5 Days 

Tags
     [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [msi](https://developers.google.com/earth-engine/datasets/tags/msi) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [sr](https://developers.google.com/earth-engine/datasets/tags/sr)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#terms-of-use) More
After 2022-01-25, Sentinel-2 scenes with PROCESSING_BASELINE '04.00' or above have their DN (value) range shifted by 1000. The HARMONIZED collection shifts data in newer scenes to be in the same range as in older scenes.
Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.
The Sentinel-2 L2 data are downloaded from CDSE. They were computed by running sen2cor. WARNING: 2017-2018 L2 coverage in the EE collection is not yet global.
The assets contain 12 UINT16 spectral bands representing SR scaled by 10000 (unlike in L1 data, there is no B10). There are also several more L2-specific bands (see band list for details). See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook) for details.
QA60 is a bitmask band that contained rasterized cloud mask polygons until 2022-01-25, when these polygons stopped being produced. Starting 2024-02-28, legacy-consistent QA60 bands are constructed from the MSK_CLASSI cloud classification bands. For more details, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks)
EE asset ids for Sentinel-2 L2 assets have the following format: COPERNICUS/S2_SR/20151128T002653_20151128T102149_T56MNN. Here the first numeric part represents the sensing date and time, the second numeric part represents the product generation date and time, and the final 6-character string is a unique granule identifier indicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).
For datasets to assist with cloud and/or cloud shadow detection, see [COPERNICUS/S2_CLOUD_PROBABILITY](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_CLOUD_PROBABILITY) and [GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED).
For more details on Sentinel-2 radiometric resolution, [see this page](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).
**Bands**
Name | Units | Min | Max | Scale | Pixel Size | Wavelength | Description  
---|---|---|---|---|---|---|---  
`B1` | 0.0001 |  60 meters  | 443.9nm (S2A) / 442.3nm (S2B) | Aerosols  
`B2` | 0.0001 |  10 meters  | 496.6nm (S2A) / 492.1nm (S2B) | Blue  
`B3` | 0.0001 |  10 meters  | 560nm (S2A) / 559nm (S2B) | Green  
`B4` | 0.0001 |  10 meters  | 664.5nm (S2A) / 665nm (S2B) | Red  
`B5` | 0.0001 |  20 meters  | 703.9nm (S2A) / 703.8nm (S2B) | Red Edge 1  
`B6` | 0.0001 |  20 meters  | 740.2nm (S2A) / 739.1nm (S2B) | Red Edge 2  
`B7` | 0.0001 |  20 meters  | 782.5nm (S2A) / 779.7nm (S2B) | Red Edge 3  
`B8` | 0.0001 |  10 meters  | 835.1nm (S2A) / 833nm (S2B) | NIR  
`B8A` | 0.0001 |  20 meters  | 864.8nm (S2A) / 864nm (S2B) | Red Edge 4  
`B9` | 0.0001 |  60 meters  | 945nm (S2A) / 943.2nm (S2B) | Water vapor  
`B11` | 0.0001 |  20 meters  | 1613.7nm (S2A) / 1610.4nm (S2B) | SWIR 1  
`B12` | 0.0001 |  20 meters  | 2202.4nm (S2A) / 2185.7nm (S2B) | SWIR 2  
`AOT` | 0.001 |  10 meters  | Aerosol Optical Thickness  
`WVP` | cm | 0.001 |  10 meters  | Water Vapor Pressure. The height the water would occupy if the vapor were condensed into liquid and spread evenly across the column.  
`SCL` |  1  |  11  |  20 meters  | Scene Classification Map (The "No Data" value of 0 is masked out)  
`TCI_R` |  10 meters  | True Color Image, Red channel  
`TCI_G` |  10 meters  | True Color Image, Green channel  
`TCI_B` |  10 meters  | True Color Image, Blue channel  
`MSK_CLDPRB` |  0  |  100  |  20 meters  | Cloud Probability Map (missing in some products)  
`MSK_SNWPRB` |  0  |  100  |  10 meters  | Snow Probability Map (missing in some products)  
`QA10` |  10 meters  | Always empty  
`QA20` |  20 meters  | Always empty  
`QA60` |  60 meters  | Cloud mask. Masked out between 2022-01-25 to 2024-02-28 inclusive.  
Bitmask for QA60
  * Bits 0-9: Unused 
  * Bit 10: Opaque clouds 
    * 0: No opaque clouds
    * 1: Opaque clouds present
  * Bit 11: Cirrus clouds 
    * 0: No cirrus clouds
    * 1: Cirrus clouds present

  
`MSK_CLASSI_OPAQUE` |  60 meters  | Opaque clouds classification band (0=no clouds, 1=clouds). Masked out before February 2024.  
`MSK_CLASSI_CIRRUS` |  60 meters  | Cirrus clouds classification band (0=no clouds, 1=clouds). Masked out before February 2024.  
`MSK_CLASSI_SNOW_ICE` |  60 meters  | Snow/ice classification band (0=no snow/ice, 1=snow/ice). Masked out before February 2024.  
**SCL Class Table**
Value | Color | Description  
---|---|---  
1 | #ff0004 | Saturated or defective  
2 | #868686 | Dark Area Pixels  
3 | #774b0a | Cloud Shadows  
4 | #10d22c | Vegetation  
5 | #ffff52 | Bare Soils  
6 | #0000ff | Water  
7 | #818181 | Clouds Low Probability / Unclassified  
8 | #c0c0c0 | Clouds Medium Probability  
9 | #f1f1f1 | Clouds High Probability  
10 | #bac5eb | Cirrus  
11 | #52fff9 | Snow / Ice  
**Image Properties**
Name | Type | Description  
---|---|---  
AOT_RETRIEVAL_ACCURACY | DOUBLE | Accuracy of Aerosol Optical thickness model  
CLOUDY_PIXEL_PERCENTAGE | DOUBLE | Granule-specific cloudy pixel percentage taken from the original metadata  
CLOUD_COVERAGE_ASSESSMENT | DOUBLE | Cloudy pixel percentage for the whole archive that contains this granule. Taken from the original metadata  
CLOUDY_SHADOW_PERCENTAGE | DOUBLE | Percentage of pixels classified as cloud shadow  
DARK_FEATURES_PERCENTAGE | DOUBLE | Percentage of pixels classified as dark features or shadows  
DATASTRIP_ID | STRING | Unique identifier of the datastrip Product Data Item (PDI)  
DATATAKE_IDENTIFIER | STRING | Uniquely identifies a given Datatake. The ID contains the Sentinel-2 satellite, start date and time, absolute orbit number, and processing baseline.  
DATATAKE_TYPE | STRING | MSI operation mode  
DEGRADED_MSI_DATA_PERCENTAGE | DOUBLE | Percentage of degraded MSI and ancillary data  
FORMAT_CORRECTNESS | STRING | Synthesis of the On-Line Quality Control (OLQC) checks performed at granule (Product_Syntax) and datastrip (Product Syntax and DS_Consistency) levels  
GENERAL_QUALITY | STRING | Synthesis of the OLQC checks performed at the datastrip level (Relative_Orbit_Number)  
GENERATION_TIME | DOUBLE | Product generation time  
GEOMETRIC_QUALITY | STRING | Synthesis of the OLQC checks performed at the datastrip level (Attitude_Quality_Indicator)  
GRANULE_ID | STRING | Unique identifier of the granule PDI (PDI_ID)  
HIGH_PROBA_CLOUDS_PERCENTAGE | DOUBLE | Percentage of pixels classified as high probability clouds  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B1 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B1 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B2 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B2 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B3 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B3 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B4 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B4 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B5 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B5 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B6 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B6 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B7 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B7 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B8 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B8 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B8a and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B9 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B9 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B10 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B10 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B11 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B11 and for all detectors  
MEAN_INCIDENCE_AZIMUTH_ANGLE_B12 | DOUBLE | Mean value containing viewing incidence azimuth angle average for band B12 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B1 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B1 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B2 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B2 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B3 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B3 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B4 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B4 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B5 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B5 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B6 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B6 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B7 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B7 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B8 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B8 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B8A | DOUBLE | Mean value containing viewing incidence zenith angle average for band B8a and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B9 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B9 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B10 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B10 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B11 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B11 and for all detectors  
MEAN_INCIDENCE_ZENITH_ANGLE_B12 | DOUBLE | Mean value containing viewing incidence zenith angle average for band B12 and for all detectors  
MEAN_SOLAR_AZIMUTH_ANGLE | DOUBLE | Mean value containing sun azimuth angle average for all bands and detectors  
MEAN_SOLAR_ZENITH_ANGLE | DOUBLE | Mean value containing sun zenith angle average for all bands and detectors  
MEDIUM_PROBA_CLOUDS_PERCENTAGE | DOUBLE | Percentage of pixels classified as medium probability clouds  
MGRS_TILE | STRING | US-Military Grid Reference System (MGRS) tile  
NODATA_PIXEL_PERCENTAGE | DOUBLE | Percentage of No Data pixels  
NOT_VEGETATED_PERCENTAGE | DOUBLE | Percentage of pixels classified as non-vegetated  
PROCESSING_BASELINE | STRING | Configuration baseline used at the time of the product generation in terms of processor software version and major Ground Image Processing Parameters (GIPP) version  
PRODUCT_ID | STRING | The full id of the original Sentinel-2 product  
RADIATIVE_TRANSFER_ACCURACY | DOUBLE | Accuracy of radiative transfer model  
RADIOMETRIC_QUALITY | STRING | Based on the OLQC reports contained in the Datastrips/QI_DATA with RADIOMETRIC_QUALITY checklist name  
REFLECTANCE_CONVERSION_CORRECTION | DOUBLE | Earth-Sun distance correction factor  
SATURATED_DEFECTIVE_PIXEL_PERCENTAGE | DOUBLE | Percentage of saturated or defective pixels  
SENSING_ORBIT_DIRECTION | STRING | Imaging orbit direction  
SENSING_ORBIT_NUMBER | DOUBLE | Imaging orbit number  
SENSOR_QUALITY | STRING | Synthesis of the OLQC checks performed at granule (Missing_Lines, Corrupted_ISP, and Sensing_Time) and datastrip (Degraded_SAD and Datation_Model) levels  
SOLAR_IRRADIANCE_B1 | DOUBLE | Mean solar exoatmospheric irradiance for band B1  
SOLAR_IRRADIANCE_B2 | DOUBLE | Mean solar exoatmospheric irradiance for band B2  
SOLAR_IRRADIANCE_B3 | DOUBLE | Mean solar exoatmospheric irradiance for band B3  
SOLAR_IRRADIANCE_B4 | DOUBLE | Mean solar exoatmospheric irradiance for band B4  
SOLAR_IRRADIANCE_B5 | DOUBLE | Mean solar exoatmospheric irradiance for band B5  
SOLAR_IRRADIANCE_B6 | DOUBLE | Mean solar exoatmospheric irradiance for band B6  
SOLAR_IRRADIANCE_B7 | DOUBLE | Mean solar exoatmospheric irradiance for band B7  
SOLAR_IRRADIANCE_B8 | DOUBLE | Mean solar exoatmospheric irradiance for band B8  
SOLAR_IRRADIANCE_B8A | DOUBLE | Mean solar exoatmospheric irradiance for band B8a  
SOLAR_IRRADIANCE_B9 | DOUBLE | Mean solar exoatmospheric irradiance for band B9  
SOLAR_IRRADIANCE_B10 | DOUBLE | Mean solar exoatmospheric irradiance for band B10  
SOLAR_IRRADIANCE_B11 | DOUBLE | Mean solar exoatmospheric irradiance for band B11  
SOLAR_IRRADIANCE_B12 | DOUBLE | Mean solar exoatmospheric irradiance for band B12  
SNOW_ICE_PERCENTAGE | DOUBLE | Percentage of pixels classified as snow or ice  
SPACECRAFT_NAME | STRING | Sentinel-2 spacecraft name: Sentinel-2A, Sentinel-2B  
THIN_CIRRUS_PERCENTAGE | DOUBLE | Percentage of pixels classified as thin cirrus clouds  
UNCLASSIFIED_PERCENTAGE | DOUBLE | Percentage of unclassified pixels  
VEGETATION_PERCENTAGE | DOUBLE | Percentage of pixels classified as vegetation  
WATER_PERCENTAGE | DOUBLE | Percentage of pixels classified as water  
WATER_VAPOUR_RETRIEVAL_ACCURACY | DOUBLE | Declared accuracy of the Water Vapor model  
**Terms of Use**
The use of Sentinel data is governed by the [Copernicus Sentinel Data Terms and Conditions.](https://scihub.copernicus.eu/twiki/pub/SciHubWebPortal/TermsConditions/Sentinel_Data_Terms_and_Conditions.pdf)
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#colab-python-sample) More
```
/**
 * Function to mask clouds using the Sentinel-2 QA band
 * @param {ee.Image} image Sentinel-2 image
 * @return {ee.Image} cloud masked Sentinel-2 image
 */
functionmaskS2clouds(image){
varqa=image.select('QA60');
// Bits 10 and 11 are clouds and cirrus, respectively.
varcloudBitMask=1 << 10;
varcirrusBitMask=1 << 11;
// Both flags should be set to zero, indicating clear conditions.
varmask=qa.bitwiseAnd(cloudBitMask).eq(0)
.and(qa.bitwiseAnd(cirrusBitMask).eq(0));
returnimage.updateMask(mask).divide(10000);
}
vardataset=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
.filterDate('2020-01-01','2020-01-30')
// Pre-filter to get less cloudy granules.
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20))
.map(maskS2clouds);
varvisualization={
min:0.0,
max:0.3,
bands:['B4','B3','B2'],
};
Map.setCenter(83.277,17.7009,12);
Map.addLayer(dataset.mean(),visualization,'RGB');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
defmask_s2_clouds(image):
"""Masks clouds in a Sentinel-2 image using the QA band.
 Args:
   image (ee.Image): A Sentinel-2 image.
 Returns:
   ee.Image: A cloud-masked Sentinel-2 image.
 """
 qa = image.select('QA60')
 # Bits 10 and 11 are clouds and cirrus, respectively.
 cloud_bit_mask = 1 << 10
 cirrus_bit_mask = 1 << 11
 # Both flags should be set to zero, indicating clear conditions.
 mask = (
   qa.bitwiseAnd(cloud_bit_mask)
   .eq(0)
   .And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
 )
 return image.updateMask(mask).divide(10000)

dataset = (
  ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterDate('2020-01-01', '2020-01-30')
  # Pre-filter to get less cloudy granules.
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .map(mask_s2_clouds)
)
visualization = {
  'min': 0.0,
  'max': 0.3,
  'bands': ['B4', 'B3', 'B2'],
}
m = geemap.Map()
m.set_center(83.277, 17.7009, 12)
m.add_layer(dataset.mean(), visualization, 'RGB')
m
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S2_SR_HARMONIZED)
[ Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-2A (SR) ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)
After 2022-01-25, Sentinel-2 scenes with PROCESSING_BASELINE '04.00' or above have their DN (value) range shifted by 1000. The HARMONIZED collection shifts data in newer scenes to be in the same range as in older scenes. Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the …
COPERNICUS/S2_SR_HARMONIZED, copernicus,esa,eu,msi,reflectance,satellite-imagery,sentinel,sr 
2017-03-28T00:00:00Z/2025-04-22T14:21:05.411000Z
-56 -180 83 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-2)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)


