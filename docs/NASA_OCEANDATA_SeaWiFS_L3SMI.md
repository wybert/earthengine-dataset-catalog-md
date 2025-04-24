 
#  Ocean Color SMI: Standard Mapped Image SeaWiFS Data 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/OCEANDATA/SeaWiFS/L3SMI](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_OCEANDATA_SeaWiFS_L3SMI_sample.png) 

Dataset Availability
    1997-09-04T15:26:33Z–2010-12-10T19:42:17Z 

Dataset Provider
     [ NASA OB.DAAC at NASA Goddard Space Flight Center ](https://oceancolor.gsfc.nasa.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/OCEANDATA/SeaWiFS/L3SMI")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_OCEANDATA_SeaWiFS_L3SMI) 

Cadence
    1 Day 

Tags
     [biology](https://developers.google.com/earth-engine/datasets/tags/biology) [chlorophyll](https://developers.google.com/earth-engine/datasets/tags/chlorophyll) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceandata](https://developers.google.com/earth-engine/datasets/tags/oceandata) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [temperature](https://developers.google.com/earth-engine/datasets/tags/temperature) [weather](https://developers.google.com/earth-engine/datasets/tags/weather)
seawifs
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#dois) More
This level 3 product includes ocean color and satellite ocean biology data produced or collected under [EOSDIS](https://earthdata.nasa.gov/about).
This dataset may be used for studying the biology and hydrology of coastal zones, changes in the diversity and geographical distribution of coastal marine habitats, biogeochemical fluxes and their influence in Earth's oceans and climate over time, and finally the impact of climate and environmental variability and change on ocean ecosystems and the biodiversity they support.
Scale factor and offset are already applied.
Documentation:
  * [Ocean Color Forum](https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl)
  * [Chlorophyll Forum](https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl)
  * [Algorithm Theoretical Basis Document (Chlorophyll)](https://oceancolor.gsfc.nasa.gov/resources/atbd/chlor_a)
  * [Algorithm Theoretical Basis Document (Fluorescence Line Height)](https://oceancolor.gsfc.nasa.gov/resources/atbd/nflh)
  * [Algorithm Theoretical Basis Document (Particulate Organic Carbon)](https://oceancolor.gsfc.nasa.gov/resources/atbd/poc)
  * [Algorithm Theoretical Basis Document (Remote-Sensing Reflectance)](https://oceancolor.gsfc.nasa.gov/resources/atbd/rrs)
  * [Processing History](https://oceancolor.gsfc.nasa.gov/data/reprocessing)
  * There are number of missing data dates in this dataset. For example, most dates are missing between 2009-04-29 and 2009-12-01.
  * The estimated values for POC might be a result of the data being generated without a scale. For more information, visit the [SeaWiFS OceanData](https://oceancolor.gsfc.nasa.gov/about/missions/seawifs)


**Pixel Size** 9200 meters 
**Bands**
Name | Units | Min | Max | Wavelength | Description  
---|---|---|---|---|---  
`chlor_a` | mg/m^3 |  0*  |  99.99*  | Chlorophyll a concentration  
`poc` | mg/m^3 | Particulate organic carbon  
`Rrs_412` | sr-1 |  0*  |  0.11*  | 412nm | Remote sensing reflectance at band 412nm  
`Rrs_443` | sr-1 |  0*  |  0.11*  | 443nm | Remote sensing reflectance at band 443nm  
`Rrs_490` | sr-1 |  0*  |  0.11*  | 490nm | Remote sensing reflectance at band 469nm  
`Rrs_510` | sr-1 |  0*  |  0.11*  | 510nm | Remote sensing reflectance at band 488nm  
`Rrs_555` | sr-1 |  0*  |  0.11*  | 555nm | Remote sensing reflectance at band 555nm  
`Rrs_670` | sr-1 |  0*  |  0.11*  | 670nm | Remote sensing reflectance at band 531nm  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
Rrs_412_lastModified | STRING | Last date this product was modified  
Rrs_412_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_412_software_version | STRING | Version of the software used to create this product  
Rrs_443_lastModified | STRING | Last date this product was modified  
Rrs_443_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_443_software_version | STRING | Version of the software used to create this product  
Rrs_555_lastModified | STRING | Last date this product was modified  
Rrs_555_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_555_software_version | STRING | Version of the software used to create this product  
chlor_a_lastModified | STRING | Last date this product was modified  
chlor_a_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
chlor_a_software_version | STRING | Version of the software used to create this product  
poc_lastModified | STRING | Last date this product was modified  
poc_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
poc_software_version | STRING | Version of the software used to create this product  
Rrs_490_lastModified | STRING | Last date this product was modified  
Rrs_490_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_490_software_version | STRING | Version of the software used to create this product  
Rrs_510_lastModified | STRING | Last date this product was modified  
Rrs_510_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_510_software_version | STRING | Version of the software used to create this product  
Rrs_670_lastModified | STRING | Last date this product was modified  
Rrs_670_software_name | STRING | 'smigen' or 'l3mapgen'; name of the software used to create this product  
Rrs_670_software_version | STRING | Version of the software used to create this product  
**Terms of Use**
This dataset is in the public domain and is available without restriction on use and distribution. See [NASA's Earth Science Data & Information Policy](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy) for additional information.
Citations:
  * NASA Goddard Space Flight Center, Ocean Ecology Laboratory, Ocean Biology Processing Group. Sea-viewing Wide Field-of-view Sensor (SeaWiFS) Data, NASA OB.DAAC, Greenbelt, MD, USA. [doi:10.5067/ORBVIEW-2/SEAWIFS/L1/DATA/1](https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L1/DATA/1)
  * NASA Ocean Biology Processing Group. (2018). _SEAWIFS-ORBVIEW-2 Level 3 Mapped Particulate Organic Carbon Data Version R2018.0_ [Data set]. NASA Ocean Biology DAAC.
  * NASA Ocean Biology Processing Group. (2018). _SEAWIFS-ORBVIEW-2 Level 3 Mapped Remote-Sensing Reflectance Data Version R2018.0_ [Data set]. NASA Ocean Biology DAAC.


  * [ https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/CHL/2018 ](https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/CHL/2018)
  * [ https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/POC/2018 ](https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/POC/2018)
  * [ https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/RRS/2018 ](https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/RRS/2018)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/OCEANDATA/SeaWiFS/L3SMI')
.filter(ee.Filter.date('2009-07-01','2009-08-30'));
varremoteSensingReflectance=
dataset.select(['Rrs_670','Rrs_555','Rrs_443']);
varremoteSensingReflectanceVis={
min:0.0,
max:0.03,
};
Map.setCenter(-52.12,-46.13,1);
Map.addLayer(
remoteSensingReflectance,remoteSensingReflectanceVis,
'Remote Sensing Reflectance');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_OCEANDATA_SeaWiFS_L3SMI)
[ Ocean Color SMI: Standard Mapped Image SeaWiFS Data ](https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI)
This level 3 product includes ocean color and satellite ocean biology data produced or collected under EOSDIS. This dataset may be used for studying the biology and hydrology of coastal zones, changes in the diversity and geographical distribution of coastal marine habitats, biogeochemical fluxes and their influence in Earth's oceans …
NASA/OCEANDATA/SeaWiFS/L3SMI, biology,chlorophyll,nasa,ocean,oceandata,oceans,reflectance,temperature,weather 
1997-09-04T15:26:33Z/2010-12-10T19:42:17Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/RRS/2018 ](https://doi.org/https://oceancolor.gsfc.nasa.gov/)
  * [ https://doi.org/10.5067/ORBVIEW-2/SEAWIFS/L3M/RRS/2018 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_OCEANDATA_SeaWiFS_L3SMI)


