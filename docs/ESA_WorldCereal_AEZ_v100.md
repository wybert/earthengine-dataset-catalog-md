 
#  ESA WorldCereal AEZ v100 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![ESA/WorldCereal/AEZ/v100](https://developers.google.com/earth-engine/datasets/images/ESA/ESA_WorldCereal_AEZ_v100_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2022-01-01T00:00:00Z 

Dataset Provider
     [ ESA WorldCereal Consortium ](https://esa-worldcereal.org/en) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("ESA/WorldCereal/AEZ/v100")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ESA/ESA_WorldCereal_AEZ_v100)      FeatureView  `    ui.Map.FeatureViewLayer("ESA/WorldCereal/AEZ/v100_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ESA/ESA_WorldCereal_AEZ_v100_FeatureView) 

Tags
     [agriculture](https://developers.google.com/earth-engine/datasets/tags/agriculture) [boundaries](https://developers.google.com/earth-engine/datasets/tags/boundaries) [crop](https://developers.google.com/earth-engine/datasets/tags/crop) [esa](https://developers.google.com/earth-engine/datasets/tags/esa) [global](https://developers.google.com/earth-engine/datasets/tags/global) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#dois) More
The [European Space Agency (ESA) WorldCereal](https://esa-worldcereal.org/) classification system aims for product generation within one month after the end of a particular growing season. Due to the dynamic nature of these growing seasons across the globe, a global stratification into Agro-Ecological Zones (AEZ) was performed based on the global crop calendars created within the project [1]. The feature collection in this dataset contains the 106 AEZ for which WorldCereal products were generated. Each AEZ has unique crop calendars, described based on their start of season (SOS) and end of season (EOS). SOS and EOS are given in day of year (DOY). More information on the AEZ stratification and the subsequent WorldCereal product generation is described in [2].
AEZ properties:
  * aez_id: the unique ID of each AEZ. WorldCereal products can be filtered based on this ID
  * aez_groupid: the group ID combines several unique AEZ into a group based on crop calendar similarity.
  * tc-annual_sos: SOS of the tc-annual season (DOY)
  * tc-annual_eos: EOS of the tc-annual season (DOY)
  * tc-wintercereals_sos: SOS of the tc-wintercereals season (DOY)
  * tc-wintercereals_eos: EOS of the tc-wintercereals season (DOY)
  * tc-springcereals_sos: SOS of the tc-springcereals season (DOY)
  * tc-springcereals_eos: EOS of the tc-springcereals season (DOY)
  * tc-maize-main_sos: SOS of the tc-maize-main season (DOY)
  * tc-maize-main_eos: EOS of the tc-maize-main season (DOY)
  * tc-maize-second_sos: SOS of the tc-maize-second season (DOY)
  * tc-maize-second_eos: EOS of the tc-maize-second season (DOY)


Missing values of SOS and EOS indicate the absence of the respective growing season in a particular AEZ.
References:
  * [1] [WorldCereal global seasonality paper](https://doi.org/10.1080/15481603.2022.2079273)
  * [2] [WorldCereal methodology and products paper](https://doi.org/10.5194/essd-2023-184)


WorldCereal datasets:
  * Version 100 for year 2021 
    * [ESA/WorldCereal/AEZ/v100](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100)
    * [ESA/WorldCereal/2021/MODELS/v100](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_2021_MODELS_v100)
    * [ESA/WorldCereal/2021/MARKERS/v100](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_2021_MARKERS_v100)


**Table Schema**
Name | Type | Description  
---|---|---  
aez_id | INT | The unique ID of an AEZ.  
aez_groupid | INT | The group ID combines several unique AEZ into a group based on crop calendar similarity.  
tc-annual_sos | INT | SOS of the tc-annual season (DOY).  
tc-annual_eos | INT | EOS of the tc-annual season (DOY).  
tc-wintercereals_sos | INT | SOS of the tc-wintercereals season (DOY).  
tc-wintercereals_eos | INT | EOS of the tc-wintercereals season (DOY).  
tc-springcereals_sos | INT | SOS of the tc-springcereals season (DOY).  
tc-springcereals_eos | INT | EOS of the tc-springcereals season (DOY).  
tc-maize-main_sos | INT | SOS of the tc-maize-main season (DOY).  
tc-maize-main_eos | INT | EOS of the tc-maize-main season (DOY).  
tc-maize-second_sos | INT | SOS of the tc-maize-second season (DOY).  
tc-maize-second_eos | INT | EOS of the tc-maize-second season (DOY).  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Van Tricht, K., Degerickx, J., Gilliams, S., Zanaga, D., Battude, M., Grosu, A., Brombacher, J., Lesiv, M., Bayas, J. C. L., Karanam, S., Fritz, S., Becker-Reshef, I., Franch, B., Mollà-Bononad, B., Boogaard, H., Pratihast, A. K., and Szantoi, Z.: WorldCereal: a dynamic open-source system for global-scale, seasonal, and reproducible crop and irrigation mapping, Earth Syst. Sci. Data Discuss. [preprint], [doi:10.5194/essd-2023-184](https://doi.org/10.5194/essd-2023-184), in review, 2023.,


  * [ https://doi.org/10.5194/essd-2023-184 ](https://doi.org/10.5194/essd-2023-184)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#code-editor-javascript-sample) More
```
varaez=ee.FeatureCollection('ESA/WorldCereal/AEZ/v100');
// Find the AEZs with multiple growing seasons for maize and cereal.
vartwoMaizeAez=
aez.filter(ee.Filter.notNull(['tc-maize-main_eos','tc-maize-second_eos']));
vartwoCerealAez=aez.filter(
ee.Filter.notNull(['tc-wintercereals_eos','tc-springcereals_eos']));
Map.addLayer(
twoMaizeAez.draw('ff0000',1,2),{},'AEZ with two maize seasons');
Map.addLayer(
twoCerealAez.draw('0000ff',1,2),{},'AEZ with two cereal seasons');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ESA/ESA_WorldCereal_AEZ_v100)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100#code-editor-javascript-sample) More
```
varaezLayer=ui.Map.FeatureViewLayer('ESA/WorldCereal/AEZ/v100_FeatureView');
varvisParams={
opacity:0.5,
lineWidth:5,
polygonFillColor:'red'
};
aezLayer.setVisParams(visParams);
aezLayer.setName('Agro-Ecological Zones');
Map.setCenter(15.5,35.5,3);
Map.add(aezLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ESA/ESA_WorldCereal_AEZ_v100_FeatureView)
[ ESA WorldCereal AEZ v100 ](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100)
The European Space Agency (ESA) WorldCereal classification system aims for product generation within one month after the end of a particular growing season. Due to the dynamic nature of these growing seasons across the globe, a global stratification into Agro-Ecological Zones (AEZ) was performed based on the global crop calendars …
ESA/WorldCereal/AEZ/v100, agriculture,boundaries,crop,esa,global,table 
2020-01-01T00:00:00Z/2022-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/essd-2023-184 ](https://doi.org/https://esa-worldcereal.org/en)
  * [ https://doi.org/10.5194/essd-2023-184 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCereal_AEZ_v100)


