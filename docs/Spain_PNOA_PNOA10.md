 
#  Spain RGB orthophotos 10 cm 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Spain/PNOA/PNOA10](https://developers.google.com/earth-engine/datasets/images/Spain/Spain_PNOA_PNOA10_sample.png) 

Dataset Availability
    2007-01-01T00:00:00Z–2019-01-01T00:00:00Z 

Dataset Provider
     [ Spain orthophotos ](https://pnoa.ign.es/web/portal/pnoa-imagen/productos-a-descarga) 

Earth Engine Snippet
     `    ee.ImageCollection("Spain/PNOA/PNOA10")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Spain/Spain_PNOA_PNOA10) 

Tags
     [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb)
pnoa
spain
[Description](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10#citations) More
Mosaics of orthophotos from flights carried out between 2007 and 2018 by various public administration bodies at 10cm pixel resolution. This data is provided by National Plan for Aerial Orthophotography Spain ([PNOA](https://pnoa.ign.es)).
For more information, please see the [Spain orthophotos documentation](https://pnoa.ign.es/web/portal/pnoa-imagen/proceso-fotogrametrico)
**Pixel Size** 0.1 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`R` | dn |  0  |  255  | Red  
`G` | dn |  0  |  255  | Green  
`B` | dn |  0  |  255  | Blue  
**Terms of Use**
The data is free and free use for any legitimate purpose, the only strict obligation being that of acknowledging and mentioning the origin and ownership of the geographic information products and services licensed as National Geographic Institute.
For more details, see [Terms of use](http://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf)
Citations:
  * National Geographic Institute Spain


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Spain/PNOA/PNOA10');
Map.setCenter(-1.859852,38.983734,19);
Map.addLayer(dataset,{},'Spain RGB (10cm)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Spain/Spain_PNOA_PNOA10)
[ Spain RGB orthophotos 10 cm ](https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10)
Mosaics of orthophotos from flights carried out between 2007 and 2018 by various public administration bodies at 10cm pixel resolution. This data is provided by National Plan for Aerial Orthophotography Spain (PNOA). For more information, please see the Spain orthophotos documentation
Spain/PNOA/PNOA10, orthophotos,rgb 
2007-01-01T00:00:00Z/2019-01-01T00:00:00Z
36.11 -9.32 43.48 4.7 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://pnoa.ign.es/web/portal/pnoa-imagen/productos-a-descarga)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Spain_PNOA_PNOA10)


