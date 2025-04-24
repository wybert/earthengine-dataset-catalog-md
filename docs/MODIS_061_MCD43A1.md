 
#  MCD43A1.061 MODIS BRDF-Albedo Model Parameters Daily 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MCD43A1](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MCD43A1_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MCD43A1.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MCD43A1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD43A1) 

Cadence
    1 Day 

Tags
     [albedo](https://developers.google.com/earth-engine/datasets/tags/albedo) [brdf](https://developers.google.com/earth-engine/datasets/tags/brdf) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
mcd43a1
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#dois) More
The MCD43A1 V6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameters dataset is a 500 meter daily 16-day product. The Julian date represents the 9th day of the 16-day retrieval period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The MCD43A1 algorithm, as is with all combined products, chooses the best representative pixel from a pool that includes all the acquisitions from both the Terra and Aqua sensors from the retrieval period.
The MCD43A1 provides the three model weighting parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible (vis), near infrared (nir), and shortwave bands used to derive the Albedo and BRDF products (MCD43A3 and MCD43A4). The Mandatory Quality layers for each of the 10 bands are supplied as well.
Documentation:
  * [User's Guide](https://www.umb.edu/spectralmass/v006/)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43A1)


**Pixel Size** 500 meters 
**Bands**
Name | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---  
`BRDF_Albedo_Parameters_Band1_iso` |  0  |  32766  | 0.001 | 620-670nm | BDRF/Albedo isotropic parameter for band 1  
`BRDF_Albedo_Parameters_Band1_vol` |  0  |  32766  | 0.001 | 620-670nm | BDRF/Albedo volumetric parameter for band 1  
`BRDF_Albedo_Parameters_Band1_geo` |  0  |  32766  | 0.001 | 620-670nm | BDRF/Albedo geometric parameter for band 1  
`BRDF_Albedo_Parameters_Band2_iso` |  0  |  32766  | 0.001 | 841-876nm | BDRF/Albedo isotropic parameter for band 2  
`BRDF_Albedo_Parameters_Band2_vol` |  0  |  32766  | 0.001 | 841-876nm | BDRF/Albedo volumetric parameter for band 2  
`BRDF_Albedo_Parameters_Band2_geo` |  0  |  32766  | 0.001 | 841-876nm | BDRF/Albedo geometric parameter for band 2  
`BRDF_Albedo_Parameters_Band3_iso` |  0  |  32766  | 0.001 | 459-479nm | BDRF/Albedo isotropic parameter for band 3  
`BRDF_Albedo_Parameters_Band3_vol` |  0  |  32766  | 0.001 | 459-479nm | BDRF/Albedo volumetric parameter for band 3  
`BRDF_Albedo_Parameters_Band3_geo` |  0  |  32766  | 0.001 | 459-479nm | BDRF/Albedo geometric parameter for band 3  
`BRDF_Albedo_Parameters_Band4_iso` |  0  |  32766  | 0.001 | 545-565nm | BDRF/Albedo isotropic parameter for band 4  
`BRDF_Albedo_Parameters_Band4_vol` |  0  |  32766  | 0.001 | 545-565nm | BDRF/Albedo volumetric parameter for band 4  
`BRDF_Albedo_Parameters_Band4_geo` |  0  |  32766  | 0.001 | 545-565nm | BDRF/Albedo geometric parameter for band 4  
`BRDF_Albedo_Parameters_Band5_iso` |  0  |  32766  | 0.001 | 1230-1250nm | BDRF/Albedo isotropic parameter for band 5  
`BRDF_Albedo_Parameters_Band5_vol` |  0  |  32766  | 0.001 | 1230-1250nm | BDRF/Albedo volumetric parameter for band 5  
`BRDF_Albedo_Parameters_Band5_geo` |  0  |  32766  | 0.001 | 1230-1250nm | BDRF/Albedo geometric parameter for band 5  
`BRDF_Albedo_Parameters_Band6_iso` |  0  |  32766  | 0.001 | 1628-1652nm | BDRF/Albedo isotropic parameter for band 6  
`BRDF_Albedo_Parameters_Band6_vol` |  0  |  32766  | 0.001 | 1628-1652nm | BDRF/Albedo volumetric parameter for band 6  
`BRDF_Albedo_Parameters_Band6_geo` |  0  |  32766  | 0.001 | 1628-1652nm | BDRF/Albedo geometric parameter for band 6  
`BRDF_Albedo_Parameters_Band7_iso` |  0  |  32766  | 0.001 | 2105-2155nm | BDRF/Albedo isotropic parameter for band 7  
`BRDF_Albedo_Parameters_Band7_vol` |  0  |  32766  | 0.001 | 2105-2155nm | BDRF/Albedo volumetric parameter for band 7  
`BRDF_Albedo_Parameters_Band7_geo` |  0  |  32766  | 0.001 | 2105-2155nm | BDRF/Albedo geometric parameter for band 7  
`BRDF_Albedo_Parameters_vis_iso` |  0  |  32766  | 0.001 | BDRF/Albedo isotropic parameter for the visible band  
`BRDF_Albedo_Parameters_vis_vol` |  0  |  32766  | 0.001 | BDRF/Albedo volumetric parameter for the visible band  
`BRDF_Albedo_Parameters_vis_geo` |  0  |  32766  | 0.001 | BDRF/Albedo geometric parameter for the visible band  
`BRDF_Albedo_Parameters_nir_iso` |  0  |  32766  | 0.001 | 858nm | BDRF/Albedo isotropic parameter for the NIR band  
`BRDF_Albedo_Parameters_nir_vol` |  0  |  32766  | 0.001 | 858nm | BDRF/Albedo volumetric parameter for the NIR band  
`BRDF_Albedo_Parameters_nir_geo` |  0  |  32766  | 0.001 | 858nm | BDRF/Albedo geometric parameter for the NIR band  
`BRDF_Albedo_Parameters_shortwave_iso` |  0  |  32766  | 0.001 | BDRF/Albedo isotropic parameter for the shortwave band  
`BRDF_Albedo_Parameters_shortwave_vol` |  0  |  32766  | 0.001 | BDRF/Albedo volumetric parameter for the shortwave band  
`BRDF_Albedo_Parameters_shortwave_geo` |  0  |  32766  | 0.001 | BDRF/Albedo geometric parameter for the shortwave band  
`BRDF_Albedo_Band_Mandatory_Quality_Band1` | BRDF albedo mandatory quality for band 1  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band1
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band2` | BRDF albedo mandatory quality for band 2  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band2
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band3` | BRDF albedo mandatory quality for band 3  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band3
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band4` | BRDF albedo mandatory quality for band 4  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band4
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band5` | BRDF albedo mandatory quality for band 5  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band5
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band6` | BRDF albedo mandatory quality for band 6  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band6
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_Band7` | BRDF albedo mandatory quality for band 7  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_Band7
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_vis` | BRDF albedo mandatory quality for visible broadband  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_vis
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_nir` | BRDF albedo mandatory quality for NIR broadband  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_nir
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
`BRDF_Albedo_Band_Mandatory_Quality_shortwave` | BRDF albedo mandatory quality for shortwave broadband  
Bitmask for BRDF_Albedo_Band_Mandatory_Quality_shortwave
  * Bit 0: Mandatory QA bit index 
    * 0: Processed, good quality (full BRDF inversions)
    * 1: Processed, see other QA (magnitude BRDF inversions)

  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MCD43A1.061 ](https://doi.org/10.5067/MODIS/MCD43A1.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MCD43A1')
.filter(ee.Filter.date('2018-05-01','2018-07-01'));
vardefaultVisualization=dataset.select([
'BRDF_Albedo_Parameters_Band1_iso','BRDF_Albedo_Parameters_Band4_iso',
'BRDF_Albedo_Parameters_Band3_iso'
]);
vardefaultVisualizationVis={
min:0.0,
max:1400.0,
gamma:2.0,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(
defaultVisualization,defaultVisualizationVis,'Default visualization');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MCD43A1)
[ MCD43A1.061 MODIS BRDF-Albedo Model Parameters Daily 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1)
The MCD43A1 V6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameters dataset is a 500 meter daily 16-day product. The Julian date represents the 9th day of the 16-day retrieval period, and consequently the observations are weighted to estimate the BRDF/Albedo for that day. The MCD43A1 algorithm, as is …
MODIS/061/MCD43A1, albedo,brdf,daily,global,modis,nasa,reflectance,satellite-imagery,usgs 
2000-02-24T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MCD43A1.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MCD43A1.061)
  * [ https://doi.org/10.5067/MODIS/MCD43A1.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD43A1)


