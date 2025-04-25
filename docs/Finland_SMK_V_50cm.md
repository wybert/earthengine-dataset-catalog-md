 
#  Finland RGB NLS orthophotos 50 cm by SMK 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Finland/SMK/V/50cm](https://developers.google.com/earth-engine/datasets/images/Finland/Finland_SMK_V_50cm_sample.png) 

Dataset Availability
    2015-01-01T00:00:00Z–2023-01-01T00:00:00Z 

Dataset Provider
     [ NLS orthophotos ](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/orthophotos) 

Earth Engine Snippet
     `    ee.ImageCollection("Finland/SMK/V/50cm")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Finland/Finland_SMK_V_50cm) 

Tags
     [finland](https://developers.google.com/earth-engine/datasets/tags/finland) [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb) [smk](https://developers.google.com/earth-engine/datasets/tags/smk)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm#citations) More
NLS Orthophotos are an aerial photo dataset covering the whole of Finland. This data is provided by SMK([The Energy Agency](https://energiavirasto.fi/etusivu), formerly abbreviated SMK). An orthophoto is a combination of several individual aerial photos. The aerial photo data set in orthophoto format is available as the most recent data set consisting of the most recent aerial photos available. The most recent data is usually 1-3 years old. NLS Orthophotos are updated every 3 years (in Northern Lapland 12 years).
(In Dataset id, V stands for "väri", which means "color" as opposed to "false color") For more information, please see the [NLS orthophotos documentation](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/orthophotos)
**Pixel Size** 0.5 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`R` |  0  |  255  | Red  
`G` |  0  |  255  | Green  
`B` |  0  |  255  | Blue  
**Terms of Use**
Mention the name of the Licensor (the National Land Survey of Finland), the name of the dataset(s) and the time when the National Land Survey has delivered the dataset(s) (e.g.: contains data from the National Land Survey of Finland Topographic Database 06/2014). please see the [Terms of use](https://creativecommons.org/licenses/by/4.0/)
Citations:
  * The National Land Survey of Finland


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Finland/SMK/V/50cm');
Map.setCenter(24.9,60.2,17);
Map.addLayer(dataset,null,'Finland 50 cm(color)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Finland/Finland_SMK_V_50cm)
[ Finland RGB NLS orthophotos 50 cm by SMK ](https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm)
NLS Orthophotos are an aerial photo dataset covering the whole of Finland. This data is provided by SMK(The Energy Agency, formerly abbreviated SMK). An orthophoto is a combination of several individual aerial photos. The aerial photo data set in orthophoto format is available as the most recent data set consisting …
Finland/SMK/V/50cm, finland,orthophotos,rgb,smk 
2015-01-01T00:00:00Z/2023-01-01T00:00:00Z
59 18 69.4 29.2 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/orthophotos)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Finland_SMK_V_50cm)


