 
#  TIGER: US Census Roads 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![TIGER/2016/Roads](https://developers.google.com/earth-engine/datasets/images/TIGER/TIGER_2016_Roads_sample.png) 

Dataset Availability
    2016-01-01T00:00:00Z–2017-01-02T00:00:00Z 

Dataset Provider
     [ United States Census Bureau ](https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("TIGER/2016/Roads")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2016_Roads)      FeatureView  `    ui.Map.FeatureViewLayer("TIGER/2016/Roads_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2016_Roads_FeatureView) 

Tags
     [census](https://developers.google.com/earth-engine/datasets/tags/census) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [roads](https://developers.google.com/earth-engine/datasets/tags/roads) [table](https://developers.google.com/earth-engine/datasets/tags/table) [tiger](https://developers.google.com/earth-engine/datasets/tags/tiger) [us](https://developers.google.com/earth-engine/datasets/tags/us)
[Description](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#citations) More
This United States Census Bureau TIGER dataset contains all road segments from the 2016 release, containing more than 19 million individual line features covering the United States, the District of Columbia, Puerto Rico, and the [Island Areas](https://www.census.gov/newsroom/releases/archives/2010_census/press-kits/island-areas.html). Each feature represents a road segment geometry (a single navigable linear path connected to at least one intersection).
For full technical details on all TIGER 2016 products, see the [TIGER technical documentation](https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2016/TGRSHP2016_TechDoc.pdf).
**Table Schema**
Name | Type | Description  
---|---|---  
fullname | STRING | A human-readable road name  
linearid | STRING | The primary identifier used to refer to this row in other TIGER products  
mtfcc | STRING | The road [priority code](https://www.census.gov/library/reference/code-lists/mt-feature-class-codes.html), representing, e.g., primary, second, local, etc.  
rttyp | STRING | The route [type code](https://www.census.gov/library/reference/code-lists/route-type-codes.html),  
**Terms of Use**
The U.S. Census Bureau offers some of its public data in machine-readable format via an Application Programming Interface (API). All of the content, documentation, code and related materials made available through the API are subject to [these terms and conditions](https://www.census.gov/data/developers/about/terms-of-service.html).
Citations:
  * For the creation of any reports, publications, new data sets, derived products, or services resulting from the data set, users should [cite the US Census Bureau](https://www.census.gov/about/policies/citation.html).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('TIGER/2016/Roads');
varroads=dataset.style({color:'#4285F4',width:1});
Map.setCenter(-73.99172,40.74101,12);
Map.addLayer(roads,{},'TIGER/2016/Roads');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2016_Roads)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('TIGER/2016/Roads_FeatureView');
varvisParams={
color:'4285f4'
};
fvLayer.setVisParams(visParams);
fvLayer.setName('US census roads');
Map.setCenter(-73.99172,40.74101,14);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2016_Roads_FeatureView)
[ TIGER: US Census Roads ](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads)
This United States Census Bureau TIGER dataset contains all road segments from the 2016 release, containing more than 19 million individual line features covering the United States, the District of Columbia, Puerto Rico, and the Island Areas. Each feature represents a road segment geometry (a single navigable linear path connected …
TIGER/2016/Roads, census,infrastructure-boundaries,roads,table,tiger,us 
2016-01-01T00:00:00Z/2017-01-02T00:00:00Z
-14.69 -180 71.567 -64.435 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/TIGER_2016_Roads)


