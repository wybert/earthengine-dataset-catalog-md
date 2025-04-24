 
#  Global Map of Oil Palm Plantations 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![BIOPAMA/GlobalOilPalm/v1](https://developers.google.com/earth-engine/datasets/images/BIOPAMA/BIOPAMA_GlobalOilPalm_v1_sample.png) 

Dataset Availability
    2019-01-01T00:00:00Z–2019-12-31T00:00:00Z 

Dataset Provider
     [ Biopama programme ](https://doi.org/10.5281/zenodo.4473715) 

Earth Engine Snippet
     `    ee.ImageCollection("BIOPAMA/GlobalOilPalm/v1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/BIOPAMA/BIOPAMA_GlobalOilPalm_v1) 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [biodiversity](https://developers.google.com/earth-engine/datasets/tags/biodiversity) [conservation](https://developers.google.com/earth-engine/datasets/tags/conservation) [crop](https://developers.google.com/earth-engine/datasets/tags/crop) [global](https://developers.google.com/earth-engine/datasets/tags/global) [landuse](https://developers.google.com/earth-engine/datasets/tags/landuse) [palm](https://developers.google.com/earth-engine/datasets/tags/palm) [plantation](https://developers.google.com/earth-engine/datasets/tags/plantation)
biopama
[Description](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#dois) More
The dataset is a 10m global industrial and smallholder oil palm map for 2019. It covers areas where oil palm plantations were detected. The classified images are the output of a convolutional neural network based on Sentinel-1 and Sentinel-2 half-year composites.
See [article](https://essd.copernicus.org/articles/13/1211/2021/) for additional information.
**Bands**
Name | Pixel Size | Description  
---|---|---  
`classification` |  10 meters  | Oil Palm class description  
**classification Class Table**
Value | Color | Description  
---|---|---  
1 | #ff0000 | Industrial closed-canopy oil palm plantations  
2 | #ef00ff | Smallholder closed-canopy oil palm plantations  
3 | #696969 | Other land covers and/or uses that are not closed-canopy oil palm.  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Adrià, D., Serge, W., Erik, M., David, G., Stephen, P., & Zoltan, S. (2021). High resolution global industrial and smallholder oil palm map for 2019 (Version v1) [Data set]. Zenodo. [doi:10.5281/zenodo.4473715](https://doi.org/10.5281/zenodo.4473715)


  * [ https://doi.org/10.5281/zenodo.4473715 ](https://doi.org/10.5281/zenodo.4473715)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1#code-editor-javascript-sample) More
```
// Import the dataset; a collection of composite granules from 2019.
vardataset=ee.ImageCollection('BIOPAMA/GlobalOilPalm/v1');
// Select the classification band.
varopClass=dataset.select('classification');
// Mosaic all of the granules into a single image.
varmosaic=opClass.mosaic();
// Define visualization parameters.
varclassificationVis={
min:1,
max:3,
palette:['ff0000','ef00ff','696969']
};
// Create a mask to add transparency to non-oil palm plantation class pixels.
varmask=mosaic.neq(3);
mask=mask.where(mask.eq(0),0.6);
// Display the data on the map.
Map.addLayer(mosaic.updateMask(mask),
classificationVis,'Oil palm plantation type',true);
Map.setCenter(-3.0175,5.2745,12);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/BIOPAMA/BIOPAMA_GlobalOilPalm_v1)
[ Global Map of Oil Palm Plantations ](https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1)
The dataset is a 10m global industrial and smallholder oil palm map for 2019. It covers areas where oil palm plantations were detected. The classified images are the output of a convolutional neural network based on Sentinel-1 and Sentinel-2 half-year composites. See article for additional information.
BIOPAMA/GlobalOilPalm/v1, agriculture,biodiversity,conservation,crop,global,landuse,palm,plantation 
2019-01-01T00:00:00Z/2019-12-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5281/zenodo.4473715 ](https://doi.org/https://doi.org/10.5281/zenodo.4473715)
  * [ https://doi.org/10.5281/zenodo.4473715 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/BIOPAMA_GlobalOilPalm_v1)


