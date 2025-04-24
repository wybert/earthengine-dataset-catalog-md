 
#  Hansen Global Forest Change v1.11 (2000-2023) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UMD/hansen/global_forest_change_2023_v1_11](https://developers.google.com/earth-engine/datasets/images/UMD/UMD_hansen_global_forest_change_2023_v1_11_sample.png) 

Dataset Availability
    2000-01-01T00:00:00Z–2023-12-31T00:00:00Z 

Dataset Provider
     [ Hansen/UMD/Google/USGS/NASA ](https://glad.earthengine.app/view/global-forest-change) 

Earth Engine Snippet
     `    ee.Image("UMD/hansen/global_forest_change_2023_v1_11")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMD/UMD_hansen_global_forest_change_2023_v1_11) 

Tags
     [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [umd](https://developers.google.com/earth-engine/datasets/tags/umd)
hansen
[Description](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#dois) More
Results from time-series analysis of Landsat images in characterizing global forest extent and change.
The 'first' and 'last' bands are reference multispectral imagery from the first and last available years for Landsat spectral bands corresponding to red, NIR, SWIR1, and SWIR2. Reference composite imagery represents median observations from a set of quality-assessed growing-season observations for each of these bands.
Please see the [User Notes](https://storage.googleapis.com/earthenginepartners-hansen/GFC-2023-v1.11/download.html) for this Version 1.11 update, as well as the associated journal article: Hansen, Potapov, Moore, Hancher et al. "High-resolution global maps of 21st-century forest cover change." Science 342.6160 (2013): 850-853.
**Pixel Size** 30.92 meters 
**Bands**
Name | Units | Min | Max | Wavelength | Description  
---|---|---|---|---|---  
`treecover2000` | % |  0  |  100  | Tree canopy cover for year 2000, defined as canopy closure for all vegetation taller than 5m in height.  
`loss` | Forest loss during the study period, defined as a stand-replacement disturbance (a change from a forest to non-forest state).  
Bitmask for loss
  * Bit 0: Forest loss during the study period. 
    * 0: Not loss
    * 1: Loss

  
`gain` | Forest gain during the period 2000-2012, defined as the inverse of loss (a non-forest to forest change entirely within the study period). Note that this has not been updated in subsequent versions.  
Bitmask for gain
  * Bit 0: Forest gain during the period 2000-2012. 
    * 0: No gain
    * 1: Gain

  
`first_b30` | 0.63-0.69µm | Landsat Red cloud-free image composite (corresponding to Landsat 5/7 band 3 and Landsat 8/9 band 4). Reference multispectral imagery from the first available year, typically 2000.  
`first_b40` | 0.77-0.90µm | Landsat NIR cloud-free image composite (corresponding to Landsat 5/7 band 4 and Landsat 8/9 band 5). Reference multispectral imagery from the first available year, typically 2000.  
`first_b50` | 1.55-1.75µm | Landsat SWIR1 cloud-free image composite (corresponding to Landsat 5/7 band 5 and Landsat 8/9 band 6). Reference multispectral imagery from the first available year, typically 2000.  
`first_b70` | 2.09-2.35µm | Landsat SWIR2 cloud-free image composite (corresponding to Landsat 5/7 band 7 and Landsat 8/9 band 7). Reference multispectral imagery from the first available year, typically 2000.  
`last_b30` | 0.63-0.69µm | Landsat Red cloud-free image composite (corresponding to Landsat 5/7 band 3 and Landsat 8/9 band 4). Reference multispectral imagery from the last available year, typically the last year of the study period.  
`last_b40` | 0.77-0.90µm | Landsat NIR cloud-free image composite (corresponding to Landsat 5/7 band 4 and Landsat 8/9 band 5). Reference multispectral imagery from the last available year, typically the last year of the study period.  
`last_b50` | 1.55-1.75µm | Landsat SWIR1 cloud-free image composite (corresponding to Landsat 5/7 band 5 and Landsat 8/9 band 6). Reference multispectral imagery from the last available year, typically the last year of the study period.  
`last_b70` | 2.09-2.35µm | Landsat SWIR2 cloud-free image composite (corresponding to Landsat 5/7 band 7 and Landsat 8/9 band 7). Reference multispectral imagery from the last available year, typically the last year of the study period.  
`datamask` | Three values representing areas of no data, mapped land surface, and permanent water bodies.  
Bitmask for datamask
  * Bits 0-1: Three values representing areas of no data, mapped land surface, and permanent water bodies. 
    * 0: No data
    * 1: Mapped land surface
    * 2: Permanent water bodies

  
`lossyear` |  0  |  23  | Year of gross forest cover loss event. Forest loss during the study period, defined as a stand-replacement disturbance, or a change from a forest to non-forest state. Encoded as either 0 (no loss) or else a value in the range 1-23, representing loss detected primarily in the year 2001-2023, respectively.  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013. "High-Resolution Global Maps of 21st-Century Forest Cover Change." Science 342 (15 November): 850-53. [10.1126/science.1244693](https://doi.org/10.1126/science.1244693) Data available on-line at: <https://glad.earthengine.app/view/global-forest-change>.


  * [ https://doi.org/10.1126/science.1244693 ](https://doi.org/10.1126/science.1244693)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11#code-editor-javascript-sample) More
```
vardataset=ee.Image('UMD/hansen/global_forest_change_2023_v1_11');
vartreeCoverVisParam={
bands:['treecover2000'],
min:0,
max:100,
palette:['black','green']
};
Map.addLayer(dataset,treeCoverVisParam,'tree cover 2000');
vartreeLossVisParam={
bands:['lossyear'],
min:0,
max:23,
palette:['yellow','red']
};
Map.addLayer(dataset,treeLossVisParam,'tree loss year');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMD/UMD_hansen_global_forest_change_2023_v1_11)
[ Hansen Global Forest Change v1.11 (2000-2023) ](https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11)
Results from time-series analysis of Landsat images in characterizing global forest extent and change. The 'first' and 'last' bands are reference multispectral imagery from the first and last available years for Landsat spectral bands corresponding to red, NIR, SWIR1, and SWIR2. Reference composite imagery represents median observations from a set …
UMD/hansen/global_forest_change_2023_v1_11, forest,forest-biomass,geophysical,landsat-derived,umd 
2000-01-01T00:00:00Z/2023-12-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1126/science.1244693 ](https://doi.org/https://glad.earthengine.app/view/global-forest-change)
  * [ https://doi.org/10.1126/science.1244693 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2023_v1_11)


