 
#  SRTM Digital Elevation Data Version 4 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CGIAR/SRTM90_V4](https://developers.google.com/earth-engine/datasets/images/CGIAR/CGIAR_SRTM90_V4_sample.png) 

Dataset Availability
    2000-02-11T00:00:00Z–2000-02-22T00:00:00Z 

Dataset Provider
     [ NASA/CGIAR ](https://srtm.csi.cgiar.org/) 

Earth Engine Snippet
     `    ee.Image("CGIAR/SRTM90_V4")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CGIAR/CGIAR_SRTM90_V4) 

Tags
     [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm) [topography](https://developers.google.com/earth-engine/datasets/tags/topography)
cgiar
[Description](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#citations) More
The Shuttle Radar Topography Mission (SRTM) digital elevation dataset was originally produced to provide consistent, high-quality elevation data at near global scope. This version of the SRTM digital elevation data has been processed to fill data voids, and to facilitate its ease of use.
**Bands**
Name | Units | Min | Max | Pixel Size | Description  
---|---|---|---|---|---  
`elevation` | m |  -444*  |  8806*  |  90 meters  | Elevation  
* estimated min or max value 
**Terms of Use**
DISTRIBUTION. Users are prohibited from any commercial, non-free resale, or redistribution without explicit written permission from CIAT. Users should acknowledge CIAT as the source used in the creation of any reports, publications, new datasets, derived products, or services resulting from the use of this dataset. CIAT also request reprints of any publications and notification of any redistributing efforts. For commercial access to the data, send requests to Andy Jarvis.
NO WARRANTY OR LIABILITY. CIAT provides these data without any warranty of any kind whatsoever, either express or implied, including warranties of merchantability and fitness for a particular purpose. CIAT shall not be liable for incidental, consequential, or special damages arising out of the use of any data.
ACKNOWLEDGMENT AND CITATION. Any users are kindly asked to cite this data in any published material produced using this data, and if possible link web pages to the [CIAT-CSI SRTM website](https://srtm.csi.cgiar.org).
Citations:
  * Jarvis, A., H.I. Reuter, A. Nelson, E. Guevara. 2008. Hole-filled SRTM for the globe Version 4, available from the CGIAR-CSI SRTM 90m Database: <https://srtm.csi.cgiar.org>.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4#colab-python-sample) More
```
vardataset=ee.Image('CGIAR/SRTM90_V4');
varelevation=dataset.select('elevation');
varslope=ee.Terrain.slope(elevation);
Map.setCenter(-112.8598,36.2841,10);
Map.addLayer(slope,{min:0,max:60},'slope');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
dataset = ee.Image('CGIAR/SRTM90_V4')
elevation = dataset.select('elevation')
slope = ee.Terrain.slope(elevation)
m = geemap.Map()
m.set_center(-112.8598, 36.2841, 10)
m.add_layer(slope, {'min': 0, 'max': 60}, 'slope')
m
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CGIAR/CGIAR_SRTM90_V4)
[ SRTM Digital Elevation Data Version 4 ](https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4)
The Shuttle Radar Topography Mission (SRTM) digital elevation dataset was originally produced to provide consistent, high-quality elevation data at near global scope. This version of the SRTM digital elevation data has been processed to fill data voids, and to facilitate its ease of use.
CGIAR/SRTM90_V4, dem,elevation,elevation-topography,geophysical,srtm,topography 
2000-02-11T00:00:00Z/2000-02-22T00:00:00Z
-56 -180 60 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://srtm.csi.cgiar.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4)


