 
#  Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-1C (TOA) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/S2_HARMONIZED](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S2_HARMONIZED_sample.png) 

Dataset Availability
    2015-06-27T00:00:00Z–2025-04-22T14:21:06.986000Z 

Dataset Provider
     [ European Union/ESA/Copernicus ](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-1) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/S2_HARMONIZED")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S2_HARMONIZED) 

Revisit Interval
    5 Days 

Tags
     [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [msi](https://developers.google.com/earth-engine/datasets/tags/msi) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#terms-of-use) More
After 2022-01-25, Sentinel-2 scenes with PROCESSING_BASELINE '04.00' or above have their DN (value) range shifted by 1000. The HARMONIZED collection shifts data in newer scenes to be in the same range as in older scenes.
Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.
The Sentinel-2 data contain 13 UINT16 spectral bands representing TOA reflectance scaled by 10000. See the [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook) for details. QA60 is a bitmask band that contained rasterized cloud mask polygons until Feb 2022, when these polygons stopped being produced. Starting in February 2024, legacy-consistent QA60 bands are constructed from the MSK_CLASSI cloud classification bands. For more details, [see the full explanation of how cloud masks are computed.](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks).
Each Sentinel-2 product (zip archive) may contain multiple granules. Each granule becomes a separate Earth Engine asset. EE asset ids for Sentinel-2 assets have the following format: COPERNICUS/S2/20151128T002653_20151128T102149_T56MNN. Here the first numeric part represents the sensing date and time, the second numeric part represents the product generation date and time, and the final 6-character string is a unique granule identifier indicating its UTM grid reference (see [MGRS](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)).
The Level-2 data produced by ESA can be found in the collection [COPERNICUS/S2_SR](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR).
For datasets to assist with cloud and/or cloud shadow detection, see [COPERNICUS/S2_CLOUD_PROBABILITY](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_CLOUD_PROBABILITY) and [GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED).
For more details on Sentinel-2 radiometric resolution, [see this page](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric).
**Bands**
Name | Scale | Pixel Size | Wavelength | Description  
---|---|---|---|---  
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
`B10` | 0.0001 |  60 meters  | 1373.5nm (S2A) / 1376.9nm (S2B) | Cirrus  
`B11` | 0.0001 |  20 meters  | 1613.7nm (S2A) / 1610.4nm (S2B) | SWIR 1  
`B12` | 0.0001 |  20 meters  | 2202.4nm (S2A) / 2185.7nm (S2B) | SWIR 2  
`QA10` |  10 meters  | Always empty  
`QA20` |  20 meters  | Always empty  
`QA60` |  60 meters  | Cloud mask. Masked out between February 2022 and February 2024.  
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
**Image Properties**
Name | Type | Description  
---|---|---  
CLOUDY_PIXEL_PERCENTAGE | DOUBLE | Granule-specific cloudy pixel percentage taken from the original metadata  
CLOUD_COVERAGE_ASSESSMENT | DOUBLE | Cloudy pixel percentage for the whole archive that contains this granule. Taken from the original metadata  
DATASTRIP_ID | STRING | Unique identifier of the datastrip Product Data Item (PDI)  
DATATAKE_IDENTIFIER | STRING | Uniquely identifies a given Datatake. The ID contains the Sentinel-2 satellite, start date and time, absolute orbit number, and processing baseline.  
DATATAKE_TYPE | STRING | MSI operation mode  
DEGRADED_MSI_DATA_PERCENTAGE | DOUBLE | Percentage of degraded MSI and ancillary data  
FORMAT_CORRECTNESS | STRING | Synthesis of the On-Line Quality Control (OLQC) checks performed at granule (Product_Syntax) and datastrip (Product Syntax and DS_Consistency) levels  
GENERAL_QUALITY | STRING | Synthesis of the OLQC checks performed at the datastrip level (Relative_Orbit_Number)  
GENERATION_TIME | DOUBLE | Product generation time  
GEOMETRIC_QUALITY | STRING | Synthesis of the OLQC checks performed at the datastrip level (Attitude_Quality_Indicator)  
GRANULE_ID | STRING | Unique identifier of the granule PDI (PDI_ID)  
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
MGRS_TILE | STRING | US-Military Grid Reference System (MGRS) tile  
PROCESSING_BASELINE | STRING | Configuration baseline used at the time of the product generation in terms of processor software version and major Ground Image Processing Parameters (GIPP) version  
PRODUCT_ID | STRING | The full id of the original Sentinel-2 product  
RADIOMETRIC_QUALITY | STRING | Based on the OLQC reports contained in the Datastrips/QI_DATA with RADIOMETRIC_QUALITY checklist name  
REFLECTANCE_CONVERSION_CORRECTION | DOUBLE | Earth-Sun distance correction factor  
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
SPACECRAFT_NAME | STRING | Sentinel-2 spacecraft name: Sentinel-2A, Sentinel-2B  
**Terms of Use**
The use of Sentinel data is governed by the [Copernicus Sentinel Data Terms and Conditions.](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice)
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED#colab-python-sample) More
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
// Map the function over a month of data and take the median.
// Load Sentinel-2 TOA reflectance data (adjusted for processing changes
// that occurred after 2022-01-25).
vardataset=ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
.filterDate('2022-01-01','2022-01-31')
// Pre-filter to get less cloudy granules.
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20))
.map(maskS2clouds);
varrgbVis={
min:0.0,
max:0.3,
bands:['B4','B3','B2'],
};
Map.setCenter(-9.1695,38.6917,12);
Map.addLayer(dataset.median(),rgbVis,'RGB');
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
  ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
  .filterDate('2022-01-01', '2022-01-31')
  # Pre-filter to get less cloudy granules.
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .map(mask_s2_clouds)
)
rgb_vis = {
  'min': 0.0,
  'max': 0.3,
  'bands': ['B4', 'B3', 'B2'],
}
m = geemap.Map()
m.set_center(-9.1695, 38.6917, 12)
m.add_layer(dataset.median(), rgb_vis, 'RGB')
m
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_S2_HARMONIZED)
[ Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-1C (TOA) ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED)
After 2022-01-25, Sentinel-2 scenes with PROCESSING_BASELINE '04.00' or above have their DN (value) range shifted by 1000. The HARMONIZED collection shifts data in newer scenes to be in the same range as in older scenes. Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the …
COPERNICUS/S2_HARMONIZED, copernicus,esa,eu,msi,radiance,satellite-imagery,sentinel 
2015-06-27T00:00:00Z/2025-04-22T14:21:06.986000Z
-56 -180 83 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-1)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED)


