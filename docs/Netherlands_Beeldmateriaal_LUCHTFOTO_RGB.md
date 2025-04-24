 
#  Netherlands orthophotos 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Netherlands/Beeldmateriaal/LUCHTFOTO_RGB](https://developers.google.com/earth-engine/datasets/images/Netherlands/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB_sample.png) 

Dataset Availability
    2021-01-01T00:00:00Z–2022-12-31T00:00:00Z 

Dataset Provider
     [ Beeldmateriaal Nederland ](https://opendata.beeldmateriaal.nl/) 

Earth Engine Snippet
     `    ee.ImageCollection("Netherlands/Beeldmateriaal/LUCHTFOTO_RGB")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Netherlands/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB) 

Tags
     [netherlands](https://developers.google.com/earth-engine/datasets/tags/netherlands) [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB#citations) More
Orthophotos of Netherlands is a set of color orthoimages. Two nationwide aerial photographs are collected per year: a leafless image at 7.5 cm resolution in the spring and one with leaves on trees at 25 cm resolution in the summer.
For more information, please see the [Netherlands orthophotos documentation](https://opendata.beeldmateriaal.nl/)
**Pixel Size** 0.08 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`R` | dn |  0  |  255  | Red  
`G` | dn |  0  |  255  | Green  
`B` | dn |  0  |  255  | Blue  
**Terms of Use**
The images are made available with a CC BY 4.0 license. The user is required to add a reference to the datasource as "opendata.beeldmaterial.nl".
Citations:
  * opendata.beeldmaterial.nl


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Netherlands/Beeldmateriaal/LUCHTFOTO_RGB');
Map.setCenter(5.54,51.88,15);
Map.addLayer(dataset,{},'Netherlands orthophotos RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Netherlands/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB)
[ Netherlands orthophotos ](https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB)
Orthophotos of Netherlands is a set of color orthoimages. Two nationwide aerial photographs are collected per year: a leafless image at 7.5 cm resolution in the spring and one with leaves on trees at 25 cm resolution in the summer. For more information, please see the Netherlands orthophotos documentation
Netherlands/Beeldmateriaal/LUCHTFOTO_RGB, netherlands,orthophotos,rgb 
2021-01-01T00:00:00Z/2022-12-31T00:00:00Z
50.75 3.2 53.7 7.22 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://opendata.beeldmateriaal.nl/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Netherlands_Beeldmateriaal_LUCHTFOTO_RGB)


