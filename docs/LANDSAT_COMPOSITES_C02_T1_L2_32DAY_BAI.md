 
#  Landsat Collection 2 Tier 1 Level 2 32-Day BAI Composite 
Stay organized with collections  Save and categorize content based on your preferences. 
![LANDSAT/COMPOSITES/C02/T1_L2_32DAY_BAI](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_BAI_sample.png) 

Dataset Availability
    1984-01-01T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ Google ](https://earthengine.google.com) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/COMPOSITES/C02/T1_L2_32DAY_BAI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_BAI) 

Cadence
    32 Days 

Tags
    
bai
landsat
usgs
vegetation-indices
#### Description
These Landsat Collection 2 Tier 1 Level 2 composites are made from Tier 1 Level 2 orthorectified scenes.
The Burn Area Index (BAI) is generated from the Red and Near-IR bands, and measures the spectral distance of each pixel from a reference spectral point (the measured reflectance of charcoal). This index is intended to emphasize the charcoal signal in post-fire images. See [Chuvieco et al. (2002)](https://www.tandfonline.com/doi/abs/10.1080/01431160210153129) for details.
These composites are created from all the scenes in each 32-day period beginning from the first day of the year and continuing to the 352nd day of the year. The last composite of the year, beginning on day 353, will overlap the first composite of the following year by 20 days. All the images from each 32-day period are included in the composite, with the most recent pixel as the composite value.
Notes:
  * Only daytime images with WRS_ROW < 122 are included.
  * For Landsat 7 , images after 2017-01-01 are excluded due to orbital drift.
  * For Landsat 8, images before 2013-05-01 are excluded due to pointing issues.


### Bands
**Bands**
Name | Pixel Size | Description  
---|---|---  
`BAI` |  30 meters  | Burn Area Index  
### Terms of Use
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
### Code Editor (JavaScript)
```
vardataset=ee.ImageCollection('LANDSAT/COMPOSITES/C02/T1_L2_32DAY_BAI')
.filterDate('2023-01-01','2023-03-01');
varburnedArea=dataset.select('BAI');
varburnedAreaVis={
min:0.0,
max:100.0,
};
Map.setCenter(21.6,-18,8);
Map.addLayer(burnedArea,burnedAreaVis,'Burned Area');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_BAI)
[ Landsat Collection 2 Tier 1 Level 2 32-Day BAI Composite ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_BAI)
These Landsat Collection 2 Tier 1 Level 2 composites are made from Tier 1 Level 2 orthorectified scenes. The Burn Area Index (BAI) is generated from the Red and Near-IR bands, and measures the spectral distance of each pixel from a reference spectral point (the measured reflectance of charcoal). This …
LANDSAT/COMPOSITES/C02/T1_L2_32DAY_BAI, bai,landsat,usgs,vegetation-indices 
1984-01-01T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://earthengine.google.com)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_COMPOSITES_C02_T1_L2_32DAY_BAI)


