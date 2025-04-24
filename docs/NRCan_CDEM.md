 
#  Canadian Digital Elevation Model 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NRCan/CDEM](https://developers.google.com/earth-engine/datasets/images/NRCan/NRCan_CDEM_sample.png) 

Dataset Availability
    1945-01-01T00:00:00Z–2011-01-01T00:00:00Z 

Dataset Provider
     [ NRCan ](https://open.canada.ca/data/en/dataset/7f245e4d-76c2-4caa-951a-45d1d2051333) 

Earth Engine Snippet
     `    ee.ImageCollection("NRCan/CDEM")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NRCan/NRCan_CDEM) 

Tags
     [canada](https://developers.google.com/earth-engine/datasets/tags/canada) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [topography](https://developers.google.com/earth-engine/datasets/tags/topography)
cdem
nrcan
[Description](https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM#terms-of-use) More
The Canadian Digital Elevation Model (CDEM) is part of Natural Resources Canada's (NRCan) altimetry system and stems from the existing Canadian Digital Elevation Data (CDED). In these data, elevations can be either ground or reflective surface elevations.
The CDEM is comprised of multiple DEMs with varying resolutions. These vary according to latitude and have a base resolution of 0.75 arc-seconds. For more information see the [Product Specifications](https://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/doc/CDEM_product_specs.pdf)
Contains information licensed under the [Open Government Licence - Canada](https://open.canada.ca/en/open-government-licence-canada).
**Pixel Size** 23.19 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`elevation` | m |  -226*  |  5944*  | Elevation  
* estimated min or max value 
**Terms of Use**
Licensed under the [Open Government Licence - Canada](https://open.canada.ca/en/open-government-licence-canada).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NRCan/CDEM');
varelevation=dataset.select('elevation');
varelevationVis={
min:-50.0,
max:1500.0,
palette:['0905ff','ffefc4','ffffff'],
};
Map.setCenter(-139.3643,63.3213,9);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NRCan/NRCan_CDEM)
[ Canadian Digital Elevation Model ](https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM)
The Canadian Digital Elevation Model (CDEM) is part of Natural Resources Canada's (NRCan) altimetry system and stems from the existing Canadian Digital Elevation Data (CDED). In these data, elevations can be either ground or reflective surface elevations. The CDEM is comprised of multiple DEMs with varying resolutions. These vary according …
NRCan/CDEM, canada,dem,elevation,elevation-topography,geophysical,topography 
1945-01-01T00:00:00Z/2011-01-01T00:00:00Z
41 -142 84 -52 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://open.canada.ca/data/en/dataset/7f245e4d-76c2-4caa-951a-45d1d2051333)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NRCan_CDEM)


