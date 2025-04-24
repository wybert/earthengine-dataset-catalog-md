 
#  Landsat Global Land Survey 1975 Mosaic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/GLS1975_MOSAIC](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_GLS1975_MOSAIC_sample.png) 

Dataset Availability
    1975-01-01T00:00:00Z–1976-01-01T00:00:00Z 

Dataset Provider
     [ USGS ](https://www.usgs.gov/landsat-missions/global-land-survey-gls) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/GLS1975_MOSAIC")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_GLS1975_MOSAIC) 

Cadence
    1 Year 

Tags
    
gls
landsat
radiance
satellite-imagery
usgs
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC#terms-of-use) More
The Global Land Survey (GLS) 1975 is a global collection of imagery from the Landsat Multispectral Scanner (MSS). Most scenes were acquired by Landsat 1–3 during the years from 1972–1983. A few gaps in the Landsat 1–3 data have been filled with scenes acquired by Landsat 4–5 during the years 1982–1987.
These data contain 4 spectral bands: Green, Red, an NIR band, and a SWIR band. In the typical false-color presentation the images appear red because the NIR band, displayed as red, highlights vegetation.
All scenes in the collection are included in this composite image.
**Pixel Size** 60 meters 
**Bands**
Name | Wavelength | Description  
---|---|---  
`10` | 0.50 - 0.60 μm | Green  
`20` | 600-700 μm | Red  
`30` | 0.70-0.80 μm | Near infrared  
`40` | 0.80-1.10 μm | Short-wavelength infrared  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/GLS1975_MOSAIC');
varfalseColor=dataset.select(['30','20','10']);
varfalseColorVis={
gamma:1.6,
};
Map.setCenter(44.517,25.998,5);
Map.addLayer(falseColor,falseColorVis,'False Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_GLS1975_MOSAIC)
[ Landsat Global Land Survey 1975 Mosaic ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC)
The Global Land Survey (GLS) 1975 is a global collection of imagery from the Landsat Multispectral Scanner (MSS). Most scenes were acquired by Landsat 1–3 during the years from 1972–1983. A few gaps in the Landsat 1–3 data have been filled with scenes acquired by Landsat 4–5 during the years …
LANDSAT/GLS1975_MOSAIC, gls,landsat,radiance,satellite-imagery,usgs 
1975-01-01T00:00:00Z/1976-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/landsat-missions/global-land-survey-gls)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_GLS1975_MOSAIC)


