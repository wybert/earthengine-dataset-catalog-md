 
#  HLSS30: HLS Sentinel-2 Multi-spectral Instrument Surface Reflectance Daily Global 30m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/HLS/HLSS30/v002](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_HLS_HLSS30_v002_sample.png) 

Dataset Availability
    2015-11-28T00:00:00Z–2025-04-18T23:56:31Z 

Dataset Provider
     [ NASA LP DAAC ](https://lpdaac.usgs.gov/products/hlss30v002/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/HLS/HLSS30/v002")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_HLS_HLSS30_v002) 

Tags
     [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#dois) More
The Harmonized Landsat Sentinel-2 (HLS) project provides consistent surface reflectance data from the Operational Land Imager (OLI) aboard the joint NASA/USGS Landsat 8 satellite and the Multi-Spectral Instrument (MSI) aboard Europe's Copernicus Sentinel-2A satellites. The combined measurement enables global observations of the land every 2-3 days at 30-meter (m) spatial resolution. The HLS project uses a set of algorithms to obtain seamless products from OLI and MSI that include atmospheric correction, cloud and cloud-shadow masking, spatial co-registration and common gridding, illumination and view angle normalization, and spectral bandpass adjustment.
The HLS project distributes data as two separate products: HLSL30 (Landsat 8/9) and HLSS30 (Sentinel-2 A/B). They both provide 30m Nadir Bidirectional Reflectance Distribution Function (BRDF), Adjusted Reflectance (NBAR).
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/1698/HLS_User_Guide_V2.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/769/HLS_ATBD_V15_provisional.pdf)
  * [General Documentation](https://lpdaac.usgs.gov/products/hlss30v002/)
  * L30 catalog link: [NASA/HLS/HLSL30/v002](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSL30_v002)

**Note:** The historical assets are currently being ingested and this process is expected to finish in 2025.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`B1` | Coastal Aerosol  
`B2` | Blue  
`B3` | Green  
`B4` | Red  
`B5` | Red-Edge 1  
`B6` | Red-Edge 2  
`B7` | Red-Edge 3  
`B8` | NIR Broad  
`B8A` | NIR Narrow  
`B9` | Water vapor  
`B10` | Cirrus  
`B11` | SWIR 1  
`B12` | SWIR 2  
`Fmask` | Quality Bits  
Bitmask for Fmask
  * Bit 0: Cirrus 
    * 0: Reserved but not used
    * 1: Reserved but not used
  * Bit 1: Cloud 
    * 0: No
    * 1: Yes
  * Bit 2: Adjacent to cloud/shadow 
    * 0: No
    * 1: Yes
  * Bit 3: Cloud shadow 
    * 0: No
    * 1: Yes
  * Bit 4: Snow/ice 
    * 0: No
    * 1: Yes
  * Bit 5: Water 
    * 0: No
    * 1: Yes
  * Bits 6-7: Aerosol level 
    * 0: Climatology aerosol
    * 1: Low aerosol
    * 2: Moderate aerosol
    * 3: High aerosol

  
`SZA` | deg | Sun Zenith Angle  
`SAA` | deg | Sun Azimuth Angle  
`VZA` | deg | View Zenith Angle  
`VAA` | deg | View Azimuth Angle  
**Image Properties**
Name | Type | Description  
---|---|---  
PRODUCT_URI | STRING | The input L1C granule URI, for processing backtracing.  
MGRS_TILE_ID | STRING | The MGRS tile identifier that corresponds to the spatial grid of the observation.  
SENSING_TIME | STRING | The timestamp of when the observation was acquired.  
ADD_OFFSET | DOUBLE | Value added to the spectral data before they are scaled to int16 reflectance data.  
REF_SCALE_FACTOR | DOUBLE | Multiplier to be applied to the int16 reflectance data to get the unscaled reflectance.  
ANG_SCALE_FACTOR | DOUBLE | Multiplier to be applied to the uint16 angle bands to get the angle in degrees.  
MSI_BAND_01_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B01 reflectance in the linear bandpass adjustment.  
MSI_BAND_01_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B01 reflectance in the linear bandpass adjustment.  
MSI_BAND_02_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B02 reflectance in the linear bandpass adjustment.  
MSI_BAND_02_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B02 reflectance in the linear bandpass adjustment.  
MSI_BAND_03_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B03 reflectance in the linear bandpass adjustment.  
MSI_BAND_03_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B03 reflectance in the linear bandpass adjustment.  
MSI_BAND_04_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B04 reflectance in the linear bandpass adjustment.  
MSI_BAND_04_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B04 reflectance in the linear bandpass adjustment.  
MSI_BAND_11_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B11 reflectance in the linear bandpass adjustment.  
MSI_BAND_11_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B11 reflectance in the linear bandpass adjustment.  
MSI_BAND_12_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B12 reflectance in the linear bandpass adjustment.  
MSI_BAND_12_BANDPASS_ADJUSTMENT_OFFSET | DOUBLE | The offset applied to the Sentinel-2 B12 reflectance in the linear bandpass adjustment.  
MSI_BAND_8A_BANDPASS_ADJUSTMENT_SLOPE | DOUBLE | The slope applied to the Sentinel-2 B08A reflectance in the linear bandpass adjustment.  
AROP_AVE_XSHIFT | DOUBLE | AROP-derived average coordinate shift in X direction relative to the reference image. Populated only for Sentinel-2 L1C data prior to processing baseline 2.04.  
AROP_AVE_YSHIFT | DOUBLE | AROP-derived average coordinate shift in Y direction relative to the reference image. Populated only for Sentinel-2 L1C data prior to processing baseline 2.04.  
AROP_NCP | DOUBLE | Number of control points identified by AROP. Populated only for Sentinel-2 L1C data prior to processing baseline 2.04.  
AROP_RMSE | DOUBLE | Root mean squared error in AROP model fitting. Populated only for Sentinel-2 L1C data prior to processing baseline 2.04  
AROP_S2_REFIMG | STRING | Geolocation reference image name. Populated only for Sentinel-2 L1C data prior to processing baseline 2.04.  
ACCODE | STRING | The version of LaSRC used by HLS for S30.  
PROCESSING_BASELINE | STRING_LIST | List of baseline versions of processing applied to the product.  
CLOUD_COVERAGE | DOUBLE | The percentage of cloud and cloud shadow in observation based on Fmask  
HLS_PROCESSING_TIME | STRING | The date and time of HLS processing for this observation  
MEAN_SUN_AZIMUTH_ANGLE | DOUBLE | Mean Sun Azimuth Angle in degree of the input data for HLS L30  
MEAN_SUN_ZENITH_ANGLE | DOUBLE | Mean Sun Zenith Angle in degree of the input data for HLS L30  
MEAN_VIEW_AZIMUTH_ANGLE | DOUBLE | Mean View Azimuth Angle in degree of the input data  
MEAN_VIEW_ZENITH_ANGLE | DOUBLE | Mean View Zenith Angle in degree of the input data  
NBAR_SOLAR_ZENITH | DOUBLE | The solar zenith angle used in NBAR derivation  
SPATIAL_COVERAGE | DOUBLE | The percentage of the tile with data  
**Terms of Use**
NASA promotes the full and open sharing of all data with research and applications communities, private industry, academia, and the general public.
Citations:
  * Masek, J., Ju, J., Roger, J., Skakun, S., Vermote, E., Claverie, M., Dungan, J., Yin, Z., Freitag, B., Justice, C. (2021). HLS Operational Land Imager Surface Reflectance and TOA Brightness Daily Global 30m v2.0 [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2023-09-12 from https://doi.org/10.5067/HLS/HLSL30.002


  * [ https://doi.org/10.5067/HLS/HLSS30.002 ](https://doi.org/10.5067/HLS/HLSS30.002)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002#code-editor-javascript-sample) More
```
varcollection=ee.ImageCollection("NASA/HLS/HLSS30/v002")
.filter(ee.Filter.date('2024-04-25','2024-04-26'))
.filter(ee.Filter.lt('CLOUD_COVERAGE',30));
varvisParams={
bands:['B4','B3','B2'],
min:0.01,
max:0.18,
};
varvisualizeImage=function(image){
varimageRGB=image.visualize(visParams);
returnimageRGB;
};
varrgbCollection=collection.map(visualizeImage);
Map.setCenter(-109.53,29.19,12)
Map.addLayer(rgbCollection,{},'HLS S30 RGB bands');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_HLS_HLSS30_v002)
[ HLSS30: HLS Sentinel-2 Multi-spectral Instrument Surface Reflectance Daily Global 30m ](https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002)
The Harmonized Landsat Sentinel-2 (HLS) project provides consistent surface reflectance data from the Operational Land Imager (OLI) aboard the joint NASA/USGS Landsat 8 satellite and the Multi-Spectral Instrument (MSI) aboard Europe's Copernicus Sentinel-2A satellites. The combined measurement enables global observations of the land every 2-3 days at 30-meter (m) spatial …
NASA/HLS/HLSS30/v002, landsat,nasa,satellite-imagery,sentinel,usgs 
2015-11-28T00:00:00Z/2025-04-18T23:56:31Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/HLS/HLSS30.002 ](https://doi.org/https://lpdaac.usgs.gov/products/hlss30v002/)
  * [ https://doi.org/10.5067/HLS/HLSS30.002 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_HLS_HLSS30_v002)


