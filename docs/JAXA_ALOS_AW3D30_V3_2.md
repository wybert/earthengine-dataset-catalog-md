 
#  ALOS DSM: Global 30m v3.2 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JAXA/ALOS/AW3D30/V3_2](https://developers.google.com/earth-engine/datasets/images/JAXA/JAXA_ALOS_AW3D30_V3_2_sample.png) 

Dataset Availability
    2006-01-24T00:00:00Z–2011-05-12T00:00:00Z 

Dataset Provider
     [ JAXA Earth Observation Research Center ](https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm) 

Earth Engine Snippet
     `    ee.ImageCollection("JAXA/ALOS/AW3D30/V3_2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_AW3D30_V3_2) 

Tags
     [alos](https://developers.google.com/earth-engine/datasets/tags/alos) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [jaxa](https://developers.google.com/earth-engine/datasets/tags/jaxa) [topography](https://developers.google.com/earth-engine/datasets/tags/topography)
[Description](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2#citations) More
ALOS World 3D - 30m (AW3D30) is a global digital surface model (DSM) dataset with a horizontal resolution of approximately 30 meters (1 arcsec mesh). The dataset is based on the DSM dataset (5-meter mesh version) of the [World 3D Topographic Data](https://www.aw3d.jp/en/). More details are available in the dataset [documentation](https://www.eorc.jaxa.jp/ALOS/en/aw3d30/aw3d30v11_format_e.pdf).
Version 3.2, released in January 2021, is an improved version created by reconsidering the format in the high latitude area, auxiliary data, and processing method. Different pixel spacing for each latitude zone was adopted at high latitude area. Coastline data, which is one of the auxiliary datasets, was changed, and new supplementary data was used. In addition, as a source data for Japan, AW3D version 3 was also used. Furthermore, the method of detecting anomalous values in the process was improved.
**Note:** See the code example for the recommended way of computing slope. Unlike most DEMs in Earth Engine, this is an image collection due to multiple resolutions of source files that make it impossible to mosaic them into a single asset, so the slope computations need a reprojection.
The AW3D DSM elevation is calculated by an image matching process that uses a stereo pair of optical images. Clouds, snow, and ice are automatically identified during processing and applied the mask information. However, mismatched points sometimes remain especially surrounding (or at the edges of) clouds, snow, and ice areas, which cause some height errors in the final DSM.
Here are some example areas with data values outside of valid elevation range. Impossibly low negative values are concentrated in Antarctica around (-63.77, -61.660), (-77.22, -150.27), and (-73.29, 168.14); in Indonesia around (-5.36, 134.55); in Brazil around (-1.667113844, -50.6269684); and in Peru around (-10.45048137, -75.39459876) with approximate values of -1013, -998, -635, and -610 respectively. Impossibly high positive values are found in several locations in the Arctic around (79.83, -77.67) and (69.54, -75.42); in Fiji around (-16.58, 179.44) and (-18.96, 178.39); and in Nepal around (28.50, 84.56) with approximate values of 15369, 15213, and 10900 respectively.
**Pixel Size** 30 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`DSM` |  -433*  |  8768*  | Height above sea level. Signed 16 bits. Elevation (in meter) converted from the ellipsoidal height based on ITRF97 and GRS80, using EGM96†1 geoid model.  
`STK` |  1*  |  54*  | Stacking number of the scene unit DSM used in producing DSM. The band is derived by resampling the stacking number for 5m resolution DSM to 30m resolution.  
`MSK` | 8-bit mask for the band.  
Bitmask for MSK
  * Bits 0-7: Generated from resampled DSM. 
    * 0: Valid
    * 1: Cloud and snow mask (invalid).
    * 2: Land water and low correlation mask (valid).
    * 3: Sea mask (valid).
    * 4: Void filled with GSI DTM (valid).
    * 8: Void filled with Shuttle Radar Topography Mission SRTM-1 Version 3 (valid).
    * 12: Void filled with PRISM DSM (valid).
    * 16: Void filled with ViewFinder Panoramas DEM (valid).
    * 24: Void filled with ASTER GDEM v2 (valid).
    * 28: Void filled with ArcticDEM v2 (valid).
    * 32: Void filled with TanDEM-X 90m DEM (valid).
    * 36: Void filled with ArcticDEM v3 (valid).
    * 40: Void filled with ASTER GDEM v3 (valid).
    * 44: Void filled with REMA v1.1 (valid).
    * 252: Void filled with applied IDW method (gdal_fillnodata) (valid)

  
* estimated min or max value 
**Terms of Use**
This dataset is available to use with no charge under the conditions specified in the [Terms of use for ALOS Global Digital Surface Model](https://earth.jaxa.jp/en/data/policy/).
Citations:
  * 

T. Tadono, H. Ishida, F. Oda, S. Naito, K. Minakawa, H. Iwamoto
    Precise Global DEM Generation By ALOS PRISM, ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Vol.II-4, pp.71-76, 2014. [PDF file](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/II-4/71/2014/isprsannals-II-4-71-2014.pdf)
  * J. Takaku, T. Tadono, K. Tsutsui : Generation of High Resolution Global DSM from ALOS PRISM, The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Vol. XL-4, pp.243-248, ISPRS, 2014. [PDF file](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XL-4/243/2014/isprsarchives-XL-4-243-2014.pdf)
  * J. Takaku, T. Tadono, K. Tsutsui, M. Ichikawa : Validation of 'AW3D' Global DSM Generated from ALOS PRISM, ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Vol.III-4, pp.25-31, 2016. [PDF file](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/III-4/25/2016/isprs-annals-III-4-25-2016.pdf)
  * T. Tadono, H. Nagai, H. Ishida, F. Oda, S. Naito, K. Minakawa, H. Iwamoto : Initial Validation of the 30 m-mesh Global Digital Surface Model Generated by ALOS PRISM, The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, ISPRS, Vol. XLI-B4, pp.157-162, 2016. [PDF file](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLI-B4/157/2016/isprs-archives-XLI-B4-157-2016.pdf)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('JAXA/ALOS/AW3D30/V3_2');
varelevation=dataset.select('DSM');
varelevationVis={
min:0,
max:5000,
palette:['0000ff','00ffff','ffff00','ff0000','ffffff']
};
Map.setCenter(138.73,35.36,11);
Map.addLayer(elevation,elevationVis,'Elevation');
// Reproject an image mosaic using a projection from one of the image tiles,
// rather than using the default projection returned by .mosaic().
varproj=elevation.first().select(0).projection();
varslopeReprojected=ee.Terrain.slope(elevation.mosaic()
.setDefaultProjection(proj));
Map.addLayer(slopeReprojected,{min:0,max:45},'Slope');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_AW3D30_V3_2)
[ ALOS DSM: Global 30m v3.2 ](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2)
ALOS World 3D - 30m (AW3D30) is a global digital surface model (DSM) dataset with a horizontal resolution of approximately 30 meters (1 arcsec mesh). The dataset is based on the DSM dataset (5-meter mesh version) of the World 3D Topographic Data. More details are available in the dataset documentation. …
JAXA/ALOS/AW3D30/V3_2, alos,dem,elevation,elevation-topography,geophysical,jaxa,topography 
2006-01-24T00:00:00Z/2011-05-12T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/aw3d30_e.htm)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2)


