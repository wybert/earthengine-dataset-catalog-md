 
#  European Primary Forest Dataset - Points 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![HU_BERLIN/EPFD/V2/points](https://developers.google.com/earth-engine/datasets/images/HU_BERLIN/HU_BERLIN_EPFD_V2_points_sample.png) 

Dataset Availability
    2000-01-01T01:00:00Z–2019-12-31T16:45:00Z 

Dataset Provider
     [ Geography Department, Humboldt University of Berlin, Berlin, Germany ](https://www.geographie.hu-berlin.de/en/geography_department) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("HU_BERLIN/EPFD/V2/points")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/HU_BERLIN/HU_BERLIN_EPFD_V2_points)      FeatureView  `    ui.Map.FeatureViewLayer("HU_BERLIN/EPFD/V2/points_FeatureView")   ` 

Tags
     [europe](https://developers.google.com/earth-engine/datasets/tags/europe) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points#terms-of-use) More
European primary forest data harmonizes 48 different, mostly field-based datasets of primary forests, and contains 18,411 individual patches (41.1 Mha) spread across 33 countries. It includes includes mainly old-growth, late-successional forests, but also some early seral stages and young forests that originated after natural disturbances and natural regeneration, without subsequent management.
For more information, including a complete list of authors and their affiliations, please see the [dataset documentation](https://www.nature.com/articles/s41597-021-00988-7) This dataset is a point-based, where each point represents the approximate center of a primary forest.
**Table Schema**
Name | Type | Description  
---|---|---  
BIOGEOGRAP | STRING | Biogeographical region is defined by the European Environmental Agency, one of: Alpine, Arctic, Atlantic, Black Sea, Boreal, Continental, Macaronesia, Mediterranean, Pannonian, or Steppic.  
CONTACT_PE | STRING | Contact person  
DOMINANT_1 | STRING | Species (latin name) of the dominant tree species of the overstorey  
DOMINANT_2 | STRING | Species (latin name) of the second dominant tree species of the overstorey (if any)  
DOMINANT_T | STRING | Species (latin name) of the third dominant tree species of the overstorey (if any)  
FOREST_NAM | STRING | Name of the forest stand (if applicable, otherwise can be name of the wider area)  
FOREST_SHA | DOUBLE | Actual share of the polygon covered by forest, assuming that primary forests in high naturalness classes, and having a large extent, may encompass land temporarily or permanently not covered by forest.  
FOREST_TYP | INT | Main forest type according to the forest categories defined by the European Environmental Agency, based on the map of Potential Vegetation type for Europe. Possible values:
  * 1: Boreal
  * 2: Hemiboreal-nemoral
  * 3: Alpine coniferous
  * 4: Acidophilus oak-birch
  * 5: Mesophytic deciduous
  * 6: Lowland beech
  * 7: Montane beech
  * 8: Thermophilus deciduous
  * 9: Broadleaved evergreen
  * 10: Coniferous Mediterranean
  * 11: Mire and swamp
  * 12: Floodplain
  * 13: Non-riverine Alder-birch-aspen

  
FOREST_T_1 | INT | Second main forest type according to the forest categories defined by the European Environmental Agency, based on the map of Potential Vegetation types for Europe  
ID_Dataset | STRING | ID of the data set  
LAST_DISTU | STRING | LAST_DISTURBANCE1_TYPE, type of the last disturbance event. Possible values:
  * 1: Fire
  * 2: Windthrow
  * 3: Flood
  * 4: Landslide Avalanche
  * 5: Logging/harvesting
  * 6: Diseases/insect outbreak
  * 7: OTHER natural
  * 8: OTHER anthropogenic

  
LAST_DIS_1 | INT | LAST_DISTURBANCE1_YEAR, year when disturbance event 1 happened  
LAST_DIS_2 | INT | LAST_DISTURBANCE1_INTENSITY, intensity of disturbance event 1. Possible values:
  * 1: Light (<20% of the stand disturbed)
  * 2: Moderate (20-70% of the stand disturbed)
  * 3: Stand replacing (>70% of the stand disturbed)

  
LAST_DIS_3 | STRING | LAST_DISTURBANCE2_TYPE, type of the penultimate disturbance event Possible values:
  * 1: Fire
  * 2: Windthrow
  * 3: Flood
  * 4: Landslide Avalanche
  * 5: Logging/harvesting
  * 6: Diseases/insect outbreak
  * 7: OTHER natural
  * 8: OTHER anthropogenic

  
LAST_DIS_4 | INT | LAST_DISTURBANCE2_YEAR, year when disturbance event 2 happened  
LAST_DIS_5 | INT | LAST_DISTURBANCE2_INTENSITY, intensity of disturbance event 2. Possible values:
  * 1: Light (<20% of the stand disturbed)
  * 2: Moderate (20-70% of the stand disturbed)
  * 3: Stand replacing (>70% of the stand disturbed)

  
LOCATION | STRING | Municipality, Protected Area, or Region in which the primary forest remnant is located  
NATURALNES | INT | Naturalness level of the primary forest remnant: Possible values:
  * 10: n10 - Primeval Forest
  * 9: n9 - Virgin Forest
  * 8: n8 - Frontier Forest
  * 7: n7 - Near-virgin Forest
  * 6: n6 - Old-growth Forest
  * 5: n5 - Long Untouched Forest
  * 0: UNKNOWN

  
Notes | STRING | Optional additional remarks to the forest points/polygon  
OBJECTID | STRING | Object ID  
PROTECTION | INT | Legal protection status of the forest stand as derived from the World Database of Protected. The original IUCN classification was simplified to three classes:
  * Strictly protected (IUCN category I);
  * Protected (IUCN categories II-VI + not classified);
  * Not protected.

In case more updated/precise information was available from our data contributors, these were given priority. Possible values:
  * 0: Not protected
  * 1: Protected
  * 2: Strictly protected

  
RELEVANT_L | STRING | Any relevant sources of information describing the forest remnant (including journal articles, local reports and websites)  
Source | STRING | Directly attributable source/ownership attribution of the forest remnant data  
THREATS_1 | INT | Threat (if any) that is most likely to endanger the primary forest remnant. Possible values:
  * 1: Plantation development
  * 2: Anthropogenic Fires
  * 3: Tourism/recreation
  * 4: Infrastructure development (including touristic)
  * 5: Mismanagement
  * 6: Illegal logging
  * 7: Timber and fuelwood extraction
  * 8: Non-Timber Forest Products extraction
  * 9: Urbanization and housing construction
  * 10: Climate change
  * 11: Biodiversity loss

  
THREATS_2 | INT | Threat (if any) that is most likely to endanger the primary forest remnant.  
DATA_AVAIL | STRING | Data availability  
FOREST_EXT | DOUBLE | The total extent of the primary forest patch in hectares. This field is only relevant when a polygon feature IS NOT available for the forest patch.  
FOREST_E_1 | INT | The order of magnitude of the extent of a primary forest remnant patch. This field is only relevant when a polygon feature IS NOT available for the forest patch and no precise measurement of the total extent of the forest remnant is available. Possible values:
  * 1: 1-10 ha
  * 2: 11-100 ha
  * 3: 101-1000 ha
  * 4: >1001 ha

  
PUBLICATIO | STRING | Publication  
**Terms of Use**
European primary forest datasets are provided under the CC BY 4.0 license, which allows for most commmercial, noncommercial, and academic uses. See [provider terms of use](https://www.nature.com/articles/s41597-021-00988-7#Tab3:%7E:text=Full%20size%20table-,Rights%20and%20permissions,-Open%20Access%20This).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('HU_BERLIN/EPFD/V2/points');
Map.setCenter(13.64,50.11,4);
varstyleParams={
fillColor:'0F7209',
color:'000000',
width:1.0,
};
dataset=dataset.style(styleParams);
Map.addLayer(dataset,{},'European Primary Forest Points');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/HU_BERLIN/HU_BERLIN_EPFD_V2_points)
[ European Primary Forest Dataset - Points ](https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points)
European primary forest data harmonizes 48 different, mostly field-based datasets of primary forests, and contains 18,411 individual patches (41.1 Mha) spread across 33 countries. It includes includes mainly old-growth, late-successional forests, but also some early seral stages and young forests that originated after natural disturbances and natural regeneration, without subsequent …
HU_BERLIN/EPFD/V2/points, europe,forest,forest-biomass,table 
2000-01-01T01:00:00Z/2019-12-31T16:45:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.geographie.hu-berlin.de/en/geography_department)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_points)


