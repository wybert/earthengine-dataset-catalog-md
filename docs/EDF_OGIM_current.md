 
#  OGIM: Oil and Gas Infrastructure Mapping Database v2.5.1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![EDF/OGIM/current](https://developers.google.com/earth-engine/datasets/images/EDF/EDF_OGIM_current_sample.png) 

Dataset Availability
    2024-05-15T00:00:00Z–2024-05-15T00:00:00Z 

Dataset Provider
     [ Environmental Defense Fund - MethaneSAT ](https://methanesat.org) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("EDF/OGIM/current")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EDF/EDF_OGIM_current)      FeatureView  `    ui.Map.FeatureViewLayer("EDF/OGIM/current_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EDF/EDF_OGIM_current_FeatureView) 

Tags
     [edf](https://developers.google.com/earth-engine/datasets/tags/edf) [emissions](https://developers.google.com/earth-engine/datasets/tags/emissions) [ghg](https://developers.google.com/earth-engine/datasets/tags/ghg) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [methane](https://developers.google.com/earth-engine/datasets/tags/methane) [methaneair](https://developers.google.com/earth-engine/datasets/tags/methaneair) [methanesat](https://developers.google.com/earth-engine/datasets/tags/methanesat) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#dois) More
This dataset provides the locations of oil and gas (O&G) related infrastructure globally.
The Oil and Gas Infrastructure Mapping (OGIM) database is a project developed by the Environmental Defense Fund (EDF) and [MethaneSAT LLC](https://www.methanesat.org/), a wholly-owned subsidiary of EDF. The primary objective of developing a standardized O&G infrastructure database such as OGIM is to support MethaneSAT's emission quantification, source characterization, and other scientific- or advocacy-relevant analyses of methane emissions from the oil and gas sector. The OGIM database is developed based on the acquisition, analysis, and quality assurance of publicly available geospatial data sources of O&G facilities, which are combined within one standard data schema and coordinate reference system.
This dataset contains the spatial locations of the following types of infrastructure assets:
  * oil and natural gas wells,
  * oil and gas pipelines,
  * natural gas compressor stations,
  * gathering and processing facilities,
  * tank batteries,
  * offshore platforms,
  * liquefied natural gas (LNG) facilities,
  * crude oil refineries,
  * petroleum terminals,
  * injection and disposal facilities,
  * equipment and component locations,
  * satellite detections of oil and gas flares,
  * and "other" oil and gas related infrastructure, such as metering stations


Records in the OGIM are consolidated from numerous publicly-available governmental and academic sources. This list of sources is available [in the OGIM_v2.5.1_Data_Source_References.pdf](https://zenodo.org/records/13259749) document. For more information on each source, refer to the "Data_Catalog" table that accompanies [Omara et al (2023)](https://doi.org/10.5194/essd-15-3761-2023).
Important notes about the attributes associated with these facility locations:
  * Missing values (i.e., values missing or not reported by the original data source) are handled by assigning "N/A" to string attributes, -999 to numerical attributes, and a generic date of "1900-01-01" to date/datetime attributes.
  * Facility operator names have not been altered in any way from the original source of data and are assumed to be accurate as of the original source's publication date.


For more information about the OGIM database, including methods used in its development and key applications of the database, please refer to the recent publication by [Omara et al, 2023](https://doi.org/10.5194/essd-15-3761-2023).
Contact the data provider for more information about the project at this link: <https://www.methanesat.org/contact/>
This dataset will be updated in-place with the new versions.
**Table Schema**
Name | Type | Description  
---|---|---  
CATEGORY | STRING | Category of O&G infrastructure to which the facility belongs. Values:
  * CRUDE OIL REFINERIES
  * EQUIPMENT AND COMPONENTS
  * INJECTION AND DISPOSAL
  * GATHERING AND PROCESSING
  * LNG FACILITIES
  * NATURAL GAS COMPRESSOR STATION
  * NATURAL GAS FLARING DETECTIONS
  * OFFSHORE PLATFORMS
  * OIL AND NATURAL GAS WELLS
  * OIL AND NATURAL GAS PIPELINES
  * PETROLEUM TERMINALS
  * STATIONS - OTHER
  * TANK BATTERIES

  
OGIM_ID | INT | Unique identifier for each facility in the dataset. Values do not repeat across infrastructure categories.  
SRC_DATE | STRING | Original publication date of the data source from which the record was acquired, in YYYY-MM-DD format.  
SRC_REF_ID | INT | ID number(s) linking the record to its corresponding original data source(s). To look up the citation for a given SRC_REF_ID value, refer to the [Data Source Reference list](https://zenodo.org/records/13259749), or the "Data_Catalog" table in the GeoPackage that accompanies [Omara et al (2023)](https://doi.org/10.5194/essd-15-3761-2023).  
COUNTRY | STRING | Country in which the record resides. Where possible, country name matches the UN Member State list. If features are located in more than one country, COUNTRY field contains a comma-separated list of these countries in alphabetical order.  
STATE_PROV | STRING | State or province in which the facility resides.  
FAC_ID | STRING | Unique ID used by the original source agency to identify the facility.  
FAC_NAME | STRING | Name of the facility.  
FAC_STATUS | STRING | Operational status of the infrastructure asset, according to the original source e.g. 'ACTIVE'; 'SUSPENDED'; 'TEMPORARILY CLOSED'. FAC_STATUS of "N/A" cannot be assumed to mean active or inactive.  
FAC_TYPE | STRING | Detailed information on type of facility.  
OGIM_STATUS | STRING | Standardized version of the facility status reported by the original data source. The original statuses were binned into one of 12 categories defined by EDF.  
OPERATOR | STRING | Name of the facility's operator, according to the original source at time of publication.  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Omara, M., Gautam, R., O'Brien, M., Himmelberger, A., Franco, A., Meisenhelder, K., Hauser, G., Lyon, D., Chulakadaba, A., Miller, C. and Franklin, J., 2023. Developing a spatially explicit global oil and gas infrastructure database for characterizing methane emission sources at high resolution. Earth System Science Data Discussions, 2023, pp.1-35. [doi:10.5194/essd-15-3761-2023](https://doi.org/10.5194/essd-15-3761-2023),


  * [ https://doi.org/10.5194/essd-15-3761-2023 ](https://doi.org/10.5194/essd-15-3761-2023)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection("EDF/OGIM/current");
vardatasetVis=dataset.style({
color:'black',
fillColor:'yellow',
pointSize:2,
width:0.5
});
Map.setCenter(-96,40,4);
Map.setOptions("SATELLITE");
Map.addLayer(datasetVis,{},'oil and gas infrastructure');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EDF/EDF_OGIM_current)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('EDF/OGIM/current_FeatureView');
varvisParams={
pointSize:2,
width:0.5,
color:{
property:'CATEGORY',
categories:[
['GATHERING AND PROCESSING','red'],
['NATURAL GAS COMPRESSOR STATION','green'],
['NATURAL GAS FLARING DETECTIONS','blue'],
['OIL AND NATURAL GAS WELLS','purple'],
['OFFSHORE PLATFORMS','yellow']
],
defaultValue:'white'
}
};
fvLayer.setVisParams(visParams);
fvLayer.setName('Oil and gas infrastructure database');
Map.setCenter(-96,40,4);
Map.setOptions("SATELLITE");
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EDF/EDF_OGIM_current_FeatureView)
[ OGIM: Oil and Gas Infrastructure Mapping Database v2.5.1 ](https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current)
This dataset provides the locations of oil and gas (O&G) related infrastructure globally. The Oil and Gas Infrastructure Mapping (OGIM) database is a project developed by the Environmental Defense Fund (EDF) and MethaneSAT LLC, a wholly-owned subsidiary of EDF. The primary objective of developing a standardized O&G infrastructure database such …
EDF/OGIM/current, edf,emissions,ghg,infrastructure-boundaries,methane,methaneair,methanesat,table 
2024-05-15T00:00:00Z/2024-05-15T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/essd-15-3761-2023 ](https://doi.org/https://methanesat.org)
  * [ https://doi.org/10.5194/essd-15-3761-2023 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/EDF_OGIM_current)


