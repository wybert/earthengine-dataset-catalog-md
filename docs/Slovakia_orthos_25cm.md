 
#  Slovakia orthophotos 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Slovakia/orthos/25cm](https://developers.google.com/earth-engine/datasets/images/Slovakia/Slovakia_orthos_25cm_sample.png) 

Dataset Availability
    2017-01-01T00:00:00Z–2020-01-01T00:00:00Z 

Dataset Provider
     [ Slovakia orthophotomosaic ](https://www.geoportal.sk/en/zbgis/orthophotomosaic/) 

Earth Engine Snippet
     `    ee.ImageCollection("Slovakia/orthos/25cm")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Slovakia/Slovakia_orthos_25cm) 

Tags
     [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm#citations) More
Orthophotomosaic of the Slovak Republic is a set of color orthoimages without overlaps, gaps and visible brightness and color differences along the connecting lines.
For more information, please see the [Slovakia orthophotos documentation](https://www.geoportal.sk/files/zbgis/orto/technicka_sprava_ortofotomozaika_sr_2017-2019.pdf)
**Pixel Size** 0.25 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`R` | dn |  0  |  255  | Red  
`G` | dn |  0  |  255  | Green  
`B` | dn |  0  |  255  | Blue  
**Terms of Use**
The User is entitled to combine the Source Data with other data, use it in the creation of his/her own work for commercial and non-commercial purposes, create a new work, publish the work on the Internet, publish the Source Data as a base map, publish the Source Data in connection with other data/thematic layers through web apps. The User is obliged to provide the name of the Author of the Source Data when creating his/her own work and when publishing it as follows: "GKÚ Bratislava, NLC".
For more details, see [Terms of use](https://www.geoportal.sk/files/zbgis/orto/licencne_podmienky_orto.zip)
Citations:
  * GKU Bratislava, NLC


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Slovakia/orthos/25cm');
Map.setCenter(19.163,48.751,15);
Map.addLayer(dataset,{},'Slovakia orthophotos RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Slovakia/Slovakia_orthos_25cm)
[ Slovakia orthophotos ](https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm)
Orthophotomosaic of the Slovak Republic is a set of color orthoimages without overlaps, gaps and visible brightness and color differences along the connecting lines. For more information, please see the Slovakia orthophotos documentation
Slovakia/orthos/25cm, orthophotos,rgb 
2017-01-01T00:00:00Z/2020-01-01T00:00:00Z
47.44 16.5 49.36 22.33 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.geoportal.sk/en/zbgis/orthophotomosaic/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Slovakia_orthos_25cm)


