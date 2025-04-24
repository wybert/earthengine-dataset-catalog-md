 
#  Copernicus DEM GLO-30: Global 30m Digital Elevation Model 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![COPERNICUS/DEM/GLO30](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_DEM_GLO30_sample.png) 

Dataset Availability
    2010-12-01T00:00:00Z–2015-01-31T00:00:00Z 

Dataset Provider
     [ Copernicus ](https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model) 

Earth Engine Snippet
     `    ee.ImageCollection("COPERNICUS/DEM/GLO30")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_DEM_GLO30) 

Tags
     [copernicus](https://developers.google.com/earth-engine/datasets/tags/copernicus) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical)
[Description](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30#terms-of-use) More
The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. This DEM is derived from an edited DSM named WorldDEM&trade, i.e. flattening of water bodies and consistent flow of rivers has been included. Editing of shore- and coastlines, special features such as airports and implausible terrain structures has also been applied.
The WorldDEM product is based on the radar satellite data acquired during the TanDEM-X Mission, which is funded by a Public Private Partnership between the German State, represented by the German Aerospace Centre (DLR) and Airbus Defence and Space. More details are available in the dataset [documentation](https://spacedata.copernicus.eu/documents/20123/121239/GEO1988-CopernicusDEM-SPE-002_ProductHandbook_I4.0.pdf).
Earth Engine asset has been ingested from the DGED files.
**Note:** See the code example for the recommended way of computing slope. Unlike most DEMs in Earth Engine, this is an image collection due to multiple resolutions of source files that make it impossible to mosaic them into a single asset, so the slope computations need a reprojection.
**Pixel Size** 30 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`DEM` | Digital Surface Model  
`EDM` |  0  |  13  | The Edit Data Mask indicates all DEM pixels that were modified during the terrain and hydro editing process.  
`FLM` |  0  |  101  | The Filling Mask is created primarily during the terrain editing process.  
`HEM` | The Height Error Mask represents the corresponding height error for each DEM pixel in the form of the standard deviation derived from the interferometric coherence and geometrical considerations.  
`WBM` |  0  |  3  | The Water Body Mask shows all DEM pixels which are classified as water and edited according to the categories Ocean, Lake or River.  
**EDM Class Table**
Value | Color | Description  
---|---|---  
0 | Void (no data)  
1 | Not edited  
2 | Infill of external elevation data  
3 | Interpolated pixels  
4 | Smoothed pixels  
5 | Airport editing  
6 | Raised negative elevation pixels  
7 | Flattened pixels  
8 | Ocean pixels  
9 | Lake pixels  
10 | River pixels  
11 | Shoreline pixels  
12 | Morphed pixels (series of pixels manually set)  
13 | Shifted pixels  
**FLM Class Table**
Value | Color | Description  
---|---|---  
0 | Void (no data)  
1 | Edited (except filled pixels)  
2 | Not edited / not filled  
3 | ASTER  
4 | SRTM90  
5 | SRTM30  
6 | GMTED2010  
7 | SRTM30plus  
8 | TerraSAR-X Radargrammetric DEM  
9 | AW3D30  
100 | Norway DEM  
101 | DSM05 Spain  
**WBM Class Table**
Value | Color | Description  
---|---|---  
0 | No water  
1 | Ocean  
2 | Lake  
3 | River  
**Terms of Use**
The GLO-30 dataset is available worldwide with a free license with the exception of two countries (Armenia and Azerbaijan). [License for Copernicus DEM](https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('COPERNICUS/DEM/GLO30');
varelevation=dataset.select('DEM');
varelevationVis={
min:0.0,
max:1000.0,
palette:['0000ff','00ffff','ffff00','ff0000','ffffff'],
};
Map.setCenter(-6.746,46.529,4);
Map.addLayer(elevation,elevationVis,'DEM');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/COPERNICUS/COPERNICUS_DEM_GLO30)
[ Copernicus DEM GLO-30: Global 30m Digital Elevation Model ](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30)
The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. This DEM is derived from an edited DSM named WorldDEM&trade, i.e. flattening of water bodies and consistent flow of rivers has been included. Editing of shore- and coastlines, special …
COPERNICUS/DEM/GLO30, copernicus,dem,elevation,elevation-topography,geophysical 
2010-12-01T00:00:00Z/2015-01-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30)


