 
#  Landsat Collection 2 Tier 1 Level 2 32-Day NBR Composite 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/COMPOSITES/C02/T1_L2_32DAY_NBR](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR_sample.png) 

Dataset Availability
    1984-01-01T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/COMPOSITES/C02/T1_L2_32DAY_NBR")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR) 

Cadence
    32 Days 

Tags
    
landsat
nbrt
usgs
vegetation-indices
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR#terms-of-use) More
These Landsat Collection 2 Tier 1 Level 2 composites are made from Tier 1 Level 2 orthorectified scenes.
The Normalized Burn Ratio Thermal (NBRT) index is generated from the Near-IR, Mid-IR (2215 nm), and Thermal bands, and has a range from -1.0 to 1.0. See [Holden et al. (2005)](https://www.tandfonline.com/doi/abs/10.1080/01431160500239008) for details.
These composites are created from all the scenes in each 32-day period beginning from the first day of the year and continuing to the 352nd day of the year. The last composite of the year, beginning on day 353, will overlap the first composite of the following year by 20 days. All the images from each 32-day period are included in the composite, with the most recent pixel as the composite value.
Notes:
  * Only daytime images with WRS_ROW < 122 are included.
  * For Landsat 7 , images after 2017-01-01 are excluded due to orbital drift.
  * For Landsat 8, images before 2013-05-01 are excluded due to pointing issues.


**Bands**
Name | Pixel Size | Description  
---|---|---  
`NBR` |  30 meters  | Normalized Burn Ratio Thermal  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/COMPOSITES/C02/T1_L2_32DAY_NBR')
.filterDate('2017-01-01','2017-12-31');
varcolorized=dataset.select('NBR');
varcolorizedVis={
min:0.9,
max:1.0,
palette:['000000','ffffff'],
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(colorized,colorizedVis,'Colorized');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR)
[ Landsat Collection 2 Tier 1 Level 2 32-Day NBR Composite ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR)
These Landsat Collection 2 Tier 1 Level 2 composites are made from Tier 1 Level 2 orthorectified scenes. The Normalized Burn Ratio Thermal (NBRT) index is generated from the Near-IR, Mid-IR (2215 nm), and Thermal bands, and has a range from -1.0 to 1.0. See Holden et al. (2005) for …
LANDSAT/COMPOSITES/C02/T1_L2_32DAY_NBR, landsat,nbrt,usgs,vegetation-indices 
1984-01-01T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_NBR)


