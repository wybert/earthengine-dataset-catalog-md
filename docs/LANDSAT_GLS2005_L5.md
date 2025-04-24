 
#  Landsat Global Land Survey 2005, Landsat 5 scenes 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/GLS2005_L5](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_GLS2005_L5_sample.png) 

Dataset Availability
    2003-08-14T00:00:00Z–2008-05-29T00:00:00Z 

Dataset Provider
     [ USGS ](https://www.usgs.gov/landsat-missions/global-land-survey-gls) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/GLS2005_L5")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_GLS2005_L5) 

Tags
     [etm](https://developers.google.com/earth-engine/datasets/tags/etm) [gls](https://developers.google.com/earth-engine/datasets/tags/gls) [l5](https://developers.google.com/earth-engine/datasets/tags/l5) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5#terms-of-use) More
The GLS2005 data set is a collection of 9500 orthorectified leaf-on medium-resolution satellite images collected between 2004 and 2007 and covering the Earth's land masses. GLS2005 uses mainly Landsat 5 and gap-filled Landsat 7 data with EO-1 ALI and Terra ASTER data filling in any data holes.
This collection contains just the subset of the GLS2005 images from the L5 ETM sensor.
**Bands**
Name | Pixel Size | Wavelength | Description  
---|---|---|---  
`10` |  30 meters  | 0.45 - 0.52 μm | Blue  
`20` |  30 meters  | 0.52 - 0.60 μm | Green  
`30` |  30 meters  | 0.63 - 0.69 μm | Red  
`40` |  30 meters  | 0.76 - 0.90 μm | Near infrared  
`50` |  30 meters  | 1.55 - 1.75 μm | Shortwave infrared 1  
`60` |  60 meters  | 10.40 - 12.50 μm | Thermal Infrared 1. Resampled from 60m to 30m.  
`70` |  30 meters  | 2.08 - 2.35 μm | Shortwave infrared 2  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/GLS2005_L5');
vartrueColor321=dataset.select(['30','20','10']);
Map.setCenter(6.746,46.529,6);
Map.addLayer(trueColor321,{},'True Color (321)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_GLS2005_L5)
[ Landsat Global Land Survey 2005, Landsat 5 scenes ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5)
The GLS2005 data set is a collection of 9500 orthorectified leaf-on medium-resolution satellite images collected between 2004 and 2007 and covering the Earth's land masses. GLS2005 uses mainly Landsat 5 and gap-filled Landsat 7 data with EO-1 ALI and Terra ASTER data filling in any data holes. This collection contains …
LANDSAT/GLS2005_L5, etm,gls,l5,landsat,radiance,satellite-imagery,usgs 
2003-08-14T00:00:00Z/2008-05-29T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/landsat-missions/global-land-survey-gls)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS2005_L5)


