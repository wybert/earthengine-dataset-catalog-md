 
#  LSIB 2017: Large Scale International Boundary Polygons, Simplified 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USDOS/LSIB_SIMPLE/2017](https://developers.google.com/earth-engine/datasets/images/USDOS/USDOS_LSIB_SIMPLE_2017_sample.png) 

Dataset Availability
    2017-03-30T00:00:00Z–2017-03-30T00:00:00Z 

Dataset Provider
     [ United States Department of State, Office of the Geographer ](https://geonode.state.gov/layers/catalog:geonode:LSIB) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDOS/USDOS_LSIB_SIMPLE_2017)      FeatureView  `    ui.Map.FeatureViewLayer("USDOS/LSIB_SIMPLE/2017_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDOS/USDOS_LSIB_SIMPLE_2017_FeatureView) 

Tags
     [borders](https://developers.google.com/earth-engine/datasets/tags/borders) [countries](https://developers.google.com/earth-engine/datasets/tags/countries) [dos](https://developers.google.com/earth-engine/datasets/tags/dos) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [political](https://developers.google.com/earth-engine/datasets/tags/political) [table](https://developers.google.com/earth-engine/datasets/tags/table) [usdos](https://developers.google.com/earth-engine/datasets/tags/usdos)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017#terms-of-use) More
The United States Office of the Geographer provides the Large Scale International Boundary (LSIB) dataset. The detailed version (2013) is derived from two other datasets: a LSIB line vector file and the World Vector Shorelines (WVS) from the National Geospatial-Intelligence Agency (NGA). The interior boundaries reflect U.S. government policies on boundaries, boundary disputes, and sovereignty. The exterior boundaries are derived from the WVS; however, the WVS coastline data is outdated and generally shifted from between several hundred meters to over a kilometer. Each feature is the polygonal area enclosed by interior boundaries and exterior coastlines where applicable, and many countries consist of multiple features, one per disjoint region.
Compared with the detailed LSIB, in this simplified dataset some disjointed regions of each country have been reduced to a single feature. Furthermore, it excludes medium and smaller islands. The resulting simplified boundary lines are rarely shifted by more than 100 meters from the detailed LSIB lines. Each of the 312 features is a part of the geometry of one of the 284 countries described in this dataset.
**Table Schema**
Name | Type | Description  
---|---|---  
abbreviati | STRING | Country abbreviation  
country_co | STRING | [Two-letter FIPS country code](https://en.wikipedia.org/wiki/List_of_FIPS_country_codes)  
country_na | STRING | US-recognized country name  
wld_rgn | STRING | Continental region, e.g. South America  
**Terms of Use**
There are no restrictions on use of this US public domain data.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
varstyleParams={
fillColor:'b5ffb4',
color:'00909F',
width:3,
};
varcountries=dataset.style(styleParams);
Map.setCenter(16.35,48.83,4);
Map.addLayer(countries,{},'USDOS/LSIB_SIMPLE/2017',true,0.8);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDOS/USDOS_LSIB_SIMPLE_2017)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('USDOS/LSIB_SIMPLE/2017_FeatureView');
varvisParams={
color:'00909F',
fillColor:'b5ffb4',
width:3,
opacity:1
};
fvLayer.setVisParams(visParams);
fvLayer.setName('USDOS/LSIB_SIMPLE/2017');
Map.setCenter(16.35,48.83,4);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USDOS/USDOS_LSIB_SIMPLE_2017_FeatureView)
[ LSIB 2017: Large Scale International Boundary Polygons, Simplified ](https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017)
The United States Office of the Geographer provides the Large Scale International Boundary (LSIB) dataset. The detailed version (2013) is derived from two other datasets: a LSIB line vector file and the World Vector Shorelines (WVS) from the National Geospatial-Intelligence Agency (NGA). The interior boundaries reflect U.S. government policies on …
USDOS/LSIB_SIMPLE/2017, borders,countries,dos,infrastructure-boundaries,political,table,usdos 
2017-03-30T00:00:00Z/2017-03-30T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://geonode.state.gov/layers/catalog:geonode:LSIB)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USDOS_LSIB_SIMPLE_2017)


