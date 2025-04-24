 
#  MCD15A3H.061 MODIS Leaf Area Index/FPAR 4-Day Global 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MCD15A3H](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MCD15A3H_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2025-04-11T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MCD15A3H.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MCD15A3H")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD15A3H) 

Cadence
    4 Days 

Tags
     [fpar](https://developers.google.com/earth-engine/datasets/tags/fpar) [global](https://developers.google.com/earth-engine/datasets/tags/global) [lai](https://developers.google.com/earth-engine/datasets/tags/lai) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [plant-productivity](https://developers.google.com/earth-engine/datasets/tags/plant-productivity) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation)
4-day
mcd15a3h
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#dois) More
The MCD15A3H Version 6.1 Moderate Resolution Imaging Spectroradiometer (MODIS) Level 4, Combined Fraction of Photosynthetically Active Radiation (FPAR), and Leaf Area Index (LAI) product is a 4-day composite data set with 500 meter pixel size. The algorithm chooses the best pixel available from all the acquisitions of both MODIS sensors located on NASA's Terra and Aqua satellites from within the 4-day period.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/624/MOD15_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/90/MOD15_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD15A3H)


**Pixel Size** 500 meters 
**Bands**
Name | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---  
`Fpar` |  0  |  100  | 0.01 | 400-700nm | FPAR absorbed by the green elements of a vegetation canopy  
`Lai` |  0  |  100  | 0.1 | One-sided green leaf area per unit ground area in broadleaf canopies; one-half the total needle surface area per unit ground area in coniferous canopies  
`FparLai_QC` | Quality for Lai and Fpar  
Bitmask for FparLai_QC
  * Bit 0: MODLAND_QC bits 
    * 0: Good quality (main algorithm with or without saturation)
    * 1: Other quality (back-up algorithm or fill values)
  * Bit 1: Sensor 
    * 0: Terra
    * 1: Aqua
  * Bit 2: Dead detector 
    * 0: Detectors apparently fine for up to 50% of channels 1, 2
    * 1: Dead detectors caused >50% adjacent detector retrieval
  * Bits 3-4: Cloud state 
    * 0: Significant clouds NOT present (clear)
    * 1: Significant clouds WERE present
    * 2: Mixed cloud present in pixel
    * 3: Cloud state not defined, assumed clear
  * Bits 5-7: SCF_QC 
    * 0: Main (RT) method used with no saturation, best result possible
    * 1: Main (RT) method used with saturation, good and very usable
    * 2: Main (RT) method failed due to bad geometry, empirical algorithm used
    * 3: Main (RT) method failed due to problems other than geometry, empirical algorithm used
    * 4: Pixel not produced at all, value couldn''t be retrieved (possible reasons: bad L1B data, unusable MOD09GA data)

  
`FparExtra_QC` | Extra detail quality for LAI and FPAR  
Bitmask for FparExtra_QC
  * Bits 0-1: Land-sea pass-thru 
    * 0: LAND
    * 1: SHORE
    * 2: FRESHWATER
    * 3: OCEAN
  * Bit 2: Snow ice 
    * 0: No snow/ice detected
    * 1: Snow/ice detected
  * Bit 3: Aerosol 
    * 0: No or low atmospheric aerosol levels detected
    * 1: Average or high aerosol levels detected
  * Bit 4: Cirrus 
    * 0: No cirrus detected
    * 1: Cirrus detected
  * Bit 5: Internal cloud mask 
    * 0: No clouds
    * 1: Clouds were detected
  * Bit 6: Cloud shadow 
    * 0: No cloud shadow detected
    * 1: Cloud shadow detected
  * Bit 7: SCF biome mask 
    * 0: Biome outside interval <1,4>
    * 1: Biome in interval <1,4>

  
`FparStdDev` |  0  |  100  | 0.01 | Standard deviation of Fpar  
`LaiStdDev` |  0  |  100  | 0.1 | Standard deviation for Lai  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MCD15A3H.061 ](https://doi.org/10.5067/MODIS/MCD15A3H.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MCD15A3H');
vardefaultVisualization=dataset.first().select('Fpar');
vardefaultVisualizationVis={
min:0.0,
max:100.0,
palette:['e1e4b4','999d60','2ec409','0a4b06'],
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(
defaultVisualization,defaultVisualizationVis,'Default visualization');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD15A3H)
[ MCD15A3H.061 MODIS Leaf Area Index/FPAR 4-Day Global 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H)
The MCD15A3H Version 6.1 Moderate Resolution Imaging Spectroradiometer (MODIS) Level 4, Combined Fraction of Photosynthetically Active Radiation (FPAR), and Leaf Area Index (LAI) product is a 4-day composite data set with 500 meter pixel size. The algorithm chooses the best pixel available from all the acquisitions of both MODIS sensors …
MODIS/061/MCD15A3H, fpar,global,lai,modis,nasa,plant-productivity,usgs,vegetation 
2002-07-04T00:00:00Z/2025-04-11T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MCD15A3H.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MCD15A3H.061)
  * [ https://doi.org/10.5067/MODIS/MCD15A3H.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD15A3H)


