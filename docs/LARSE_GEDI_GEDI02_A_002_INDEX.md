 
#  GEDI L2A table index 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LARSE/GEDI/GEDI02_A_002_INDEX](https://developers.google.com/earth-engine/datasets/images/LARSE/LARSE_GEDI_GEDI02_A_002_INDEX_sample.png) 

Dataset Availability
    2019-03-25T00:00:00Z–2023-01-01T00:00:00Z 

Dataset Provider
     [ Indexing: Google and USFS Laboratory for Applications of Remote Sensing in Ecology (LARSE) ](https://www.fs.usda.gov/) [ NASA GEDI mission, accessed through the USGS LP DAAC ](https://lpdaac.usgs.gov/products/gedi02_av002/) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("LARSE/GEDI/GEDI02_A_002_INDEX")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LARSE/LARSE_GEDI_GEDI02_A_002_INDEX)      FeatureView  `    ui.Map.FeatureViewLayer("LARSE/GEDI/GEDI02_A_002_INDEX_FeatureView")   ` 

Tags
     [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [gedi](https://developers.google.com/earth-engine/datasets/tags/gedi) [larse](https://developers.google.com/earth-engine/datasets/tags/larse) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [table](https://developers.google.com/earth-engine/datasets/tags/table) [tree-cover](https://developers.google.com/earth-engine/datasets/tags/tree-cover) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX#citations) More
This is a feature collection created from the geometries of L2A tables in [LARSE/GEDI/GEDI02_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002). Each feature is a polygon footprint of a source table with its asset id and start/end timestamps.
Please see [User Guide](https://lpdaac.usgs.gov/documents/986/GEDI02_UserGuide_V2.pdf) for more information.
The Global Ecosystem Dynamics Investigation [GEDI](https://gedi.umd.edu/) mission aims to characterize ecosystem structure and dynamics to enable radically improved quantification and understanding of the Earth's carbon cycle and biodiversity. The GEDI instrument, attached to the International Space Station (ISS), collects data globally between 51.6° N and 51.6° S latitudes at the highest resolution and densest sampling of the 3-dimensional structure of the Earth. The GEDI instrument consists of three lasers producing a total of eight beam ground transects, which instantaneously sample eight ~25 m footprints spaced approximately every 60 m along-track.
Product | Description  
---|---  
L2A Vector | [LARSE/GEDI/GEDI02_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002)  
L2A Monthly raster | [LARSE/GEDI/GEDI02_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_MONTHLY)  
L2A table index | [LARSE/GEDI/GEDI02_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX)  
L2B Vector | [LARSE/GEDI/GEDI02_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002)  
L2B Monthly raster | [LARSE/GEDI/GEDI02_B_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_MONTHLY)  
L2B table index | [LARSE/GEDI/GEDI02_B_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_B_002_INDEX)  
L4A Biomass Vector | [LARSE/GEDI/GEDI04_A_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002)  
L4A Monthly raster | [LARSE/GEDI/GEDI04_A_002_MONTHLY](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_MONTHLY)  
L4A table index | [LARSE/GEDI/GEDI04_A_002_INDEX](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002_INDEX)  
L4B Biomass | [LARSE/GEDI/GEDI04_B_002](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_B_002)  
**Table Schema**
Name | Type | Description  
---|---|---  
table_id | STRING | GEDI L2A table collection Ids  
time_start | STRING | GEDI L2A table start time in the ISO 8601 format  
time_end | STRING | GEDI L2A table end time in the ISO 8601 format  
**Terms of Use**
This dataset is in the public domain and is available without restriction on use and distribution. See [NASA's Earth Science Data & Information Policy](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy) for additional information.
Citations:
  * GEDI L2A Elevation and Height Metrics Data Global Footprint Level - GEDI02_A Dubayah, R., M. Hofton, J. Blair, J. Armston, H. Tang, S. Luthcke. GEDI L2A Elevation and Height Metrics Data Global Footprint Level V002. 2021, distributed by NASA EOSDIS Land Processes DAAC. Accessed YYYY-MM-DD.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX#code-editor-javascript-sample) More
```
varrectangle=ee.Geometry.Rectangle([
-111.22,24.06,-6.54,51.9
]);
// Filter index by date and location
varfilter_index=ee.FeatureCollection(
'LARSE/GEDI/GEDI02_A_002_INDEX').filter(
'time_start > "2020-10-10T15:57:18Z" && time_end < "2020-10-11T01:20:45Z"')
.filterBounds(rectangle);
Map.addLayer(filter_index);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LARSE/LARSE_GEDI_GEDI02_A_002_INDEX)
[ GEDI L2A table index ](https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX)
This is a feature collection created from the geometries of L2A tables in LARSE/GEDI/GEDI02_A_002. Each feature is a polygon footprint of a source table with its asset id and start/end timestamps. Please see User Guide for more information. The Global Ecosystem Dynamics Investigation GEDI mission aims to characterize ecosystem structure …
LARSE/GEDI/GEDI02_A_002_INDEX, elevation,forest-biomass,gedi,larse,nasa,table,tree-cover,usgs 
2019-03-25T00:00:00Z/2023-01-01T00:00:00Z
-51.6 -180 51.6 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.fs.usda.gov/)
  * [ ](https://doi.org/https://lpdaac.usgs.gov/products/gedi02_av002/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI02_A_002_INDEX)


