 
#  Brandenburg (Germany) RGBN orthophotos 20 cm 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Germany/Brandenburg/orthos/20cm](https://developers.google.com/earth-engine/datasets/images/Germany/Germany_Brandenburg_orthos_20cm_sample.png) 

Dataset Availability
    2021-08-23T00:00:00Z–2023-01-20T00:00:00Z 

Dataset Provider
     [ Brandenburg orthophotos ](https://geobasis-bb.de/lgb/de/geodaten/luftbilder/luftbilder-aktuell) 

Earth Engine Snippet
     `    ee.ImageCollection("Germany/Brandenburg/orthos/20cm")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Germany/Germany_Brandenburg_orthos_20cm) 

Tags
     [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos)
brandenburg
germany
rgbn
[Description](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm#citations) More
Orthophotos are an aerial photo dataset covering the Brandenburg state of Germany. This data is provided by State government of Brandenburg ([LGB](https://geobasis-bb.de/lgb/de/)). Digital orthophotos are digitally corrected aerial photos and show all objects that are visible from the air at the time of recording in a parallel perspective. They have a high density of information on ecological, phenological, geographical and other topics.
For more information, please see the [Brandenburg orthophotos documentation](https://geobasis-bb.de/lgb/de/geodaten/luftbilder/luftbilder-aktuell/)
**Pixel Size** 0.2 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`N` |  0  |  255  | Near infrared  
`R` |  0  |  255  | Red  
`G` |  0  |  255  | Green  
`B` |  0  |  255  | Blue  
**Terms of Use**
The user must ensure that the source note contains the following information:
  1. the name of the provider,
  2. the annotation "Data licence Germany - attribution - Version 2.0" or "dl-de/by-2-0" referring to the licence text available at www.govdata.de/dl-de/by-2-0, and
  3. a reference to the dataset (URI). This applies only if the entity keeping the data provides the pieces of information 1-3 for the source note.


Changes, editing, new designs or other amendments must be marked as such in the source note.
For more details please see the [Terms of use](https://www.govdata.de/dl-de/by-2-0)
Citations:
  * Data License Germany - Attribution - Version 2.0


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm#code-editor-javascript-sample) More
```
vardataset=ee.Image('Germany/Brandenburg/orthos/20cm');
Map.setCenter(13.386091,52.507899,18);
Map.addLayer(dataset,null,'Brandenburg 20cm');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Germany/Germany_Brandenburg_orthos_20cm)
[ Brandenburg (Germany) RGBN orthophotos 20 cm ](https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm)
Orthophotos are an aerial photo dataset covering the Brandenburg state of Germany. This data is provided by State government of Brandenburg (LGB). Digital orthophotos are digitally corrected aerial photos and show all objects that are visible from the air at the time of recording in a parallel perspective. They have …
Germany/Brandenburg/orthos/20cm, orthophotos 
2021-08-23T00:00:00Z/2023-01-20T00:00:00Z
51.28 11 53.7 15 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://geobasis-bb.de/lgb/de/geodaten/luftbilder/luftbilder-aktuell)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Germany_Brandenburg_orthos_20cm)


