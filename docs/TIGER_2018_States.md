 
#  TIGER: US Census States 2018 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![TIGER/2018/States](https://developers.google.com/earth-engine/datasets/images/TIGER/TIGER_2018_States_sample.png) 

Dataset Availability
    2018-01-01T00:00:00Z–2019-01-01T00:00:00Z 

Dataset Provider
     [ United States Census Bureau ](https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("TIGER/2018/States")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2018_States)      FeatureView  `    ui.Map.FeatureViewLayer("TIGER/2018/States_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2018_States_FeatureView) 

Tags
     [census](https://developers.google.com/earth-engine/datasets/tags/census) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [state](https://developers.google.com/earth-engine/datasets/tags/state) [states](https://developers.google.com/earth-engine/datasets/tags/states) [table](https://developers.google.com/earth-engine/datasets/tags/table) [tiger](https://developers.google.com/earth-engine/datasets/tags/tiger) [us](https://developers.google.com/earth-engine/datasets/tags/us)
[Description](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#citations) More
The United States Census Bureau TIGER dataset contains the 2018 boundaries for the primary governmental divisions of the United States. In addition to the fifty states, the Census Bureau treats the District of Columbia, Puerto Rico, and each of the island areas (American Samoa, the Commonwealth of the Northern Mariana Islands, Guam, and the U.S. Virgin Islands) as the statistical equivalents of States for the purpose of data presentation. Each feature represents a state or state equivalent.
For full technical details on all TIGER 2018 products, see the [TIGER technical documentation](https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2018/TGRSHP2018_TechDoc.pdf).
**Table Schema**
Name | Type | Description  
---|---|---  
ALAND | DOUBLE | Land area  
AWATER | DOUBLE | Water area  
DIVISION | STRING | Division code  
FUNCSTAT | STRING | Functional Status  
GEOID | STRING | State identifier; state FIPS code  
INTPTLAT | STRING | Internal point latitude  
INTPTLON | STRING | Internal point longitude  
LSAD | STRING | Legal/statistical area description for state  
MTFCC | STRING | MAF/TIGER feature class code (=G4000)  
NAME | STRING | State name  
REGION | STRING | Region code  
STATEFP | STRING | State FIPS code  
STATENS | STRING | State GNIS code  
STUSPS | STRING | US Postal Service state abbreviation  
**Terms of Use**
The U.S. Census Bureau offers some of its public data in machine-readable format via an Application Programming Interface (API). All of the content, documentation, code and related materials made available through the API are subject to [these terms and conditions](https://www.census.gov/data/developers/about/terms-of-service.html).
Citations:
  * For the creation of any reports, publications, new data sets, derived products, or services resulting from the data set, users should [cite the US Census Bureau](https://www.census.gov/about/policies/citation.html).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('TIGER/2018/States');
varvisParams={
palette:['purple','blue','green','yellow','orange','red'],
min:500000000.0,
max:5e+11,
opacity:0.8,
};
varimage=ee.Image().float().paint(dataset,'ALAND');
Map.setCenter(-99.844,37.649,5);
Map.addLayer(image,visParams,'TIGER/2018/States');
Map.addLayer(dataset,null,'for Inspector',false);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2018_States)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('TIGER/2018/States_FeatureView');
varvisParams={
opacity:0.8,
color:{
property:'ALAND',
mode:'linear',
palette:['purple','blue','green','yellow','orange','red'],
min:5e8,
max:5e11
}
};
fvLayer.setVisParams(visParams);
fvLayer.setName('US census states');
Map.setCenter(-99.844,37.649,5);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2018_States_FeatureView)
[ TIGER: US Census States 2018 ](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States)
The United States Census Bureau TIGER dataset contains the 2018 boundaries for the primary governmental divisions of the United States. In addition to the fifty states, the Census Bureau treats the District of Columbia, Puerto Rico, and each of the island areas (American Samoa, the Commonwealth of the Northern Mariana …
TIGER/2018/States, census,infrastructure-boundaries,state,states,table,tiger,us 
2018-01-01T00:00:00Z/2019-01-01T00:00:00Z
-14.69 -180 71.567 -64.435 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_States)


