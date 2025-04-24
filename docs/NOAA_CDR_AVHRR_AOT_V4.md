 
#  NOAA CDR AVHRR AOT: Daily Aerosol Optical Thickness Over Global Oceans, v04 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/CDR/AVHRR/AOT/V4](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_CDR_AVHRR_AOT_V4_sample.png) 

Dataset Availability
    1981-01-01T00:00:00Z–2024-12-31T00:00:00Z 

Dataset Provider
     [ NOAA ](https://doi.org/10.25921/w3zj-4y48) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/CDR/AVHRR/AOT/V4")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_CDR_AVHRR_AOT_V4) 

Cadence
    1 Day 

Tags
     [aerosol](https://developers.google.com/earth-engine/datasets/tags/aerosol) [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [atmospheric](https://developers.google.com/earth-engine/datasets/tags/atmospheric) [avhrr](https://developers.google.com/earth-engine/datasets/tags/avhrr) [cdr](https://developers.google.com/earth-engine/datasets/tags/cdr) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [optical](https://developers.google.com/earth-engine/datasets/tags/optical) [pollution](https://developers.google.com/earth-engine/datasets/tags/pollution)
aot
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#dois) More
The NOAA Climate Data Record (CDR) of Aerosol Optical Thickness (AOT) is a collection of global daily 0.1 degree derived data from the PATMOS-x AVHRR level-2b channel 1 (0.63 micron) orbital clear-sky radiance. The aerosol product is generated from AVHRR imagery in cloud-free conditions during daytime over oceans.
Due to the relatively large uncertainties associated with surface reflectance over water glint area and land surface as well as limited AVHRR retrieval channels, this dataset only includes retrieval over non-glint water surface (specifically at the anti-solar side of the orbit with viewing angle more than 40 degree away from the specular ray). For more details, see the [Algorithm Description](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Aerosol_Optical_Thickness/AlgorithmDescription_01B-04.pdf).
Image and data processing by NOAA's National Climatic Data Center.
**Pixel Size** 11132 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`aot` |  -0.19*  |  4.95*  | Atmosphere optical thickness; the degree to which aerosols prevent the transmission of light by absorption or scattering of light. A value of 0.01 corresponds to an extremely clean atmosphere, and a value of 0.4 would correspond to a very hazy condition. An average aerosol optical depth for the U.S. is 0.1 to 0.15.  
* estimated min or max value 
**Terms of Use**
The NOAA CDR Program's official distribution point for CDRs is NOAA's National Climatic Data Center which provides sustained, open access and active data management of the CDR packages and related information in keeping with the United States' open data policies and practices as described in the President's Memorandum on "Open Data Policy" and pursuant to the Executive Order of May 9, 2013, "Making Open and Machine Readable the New Default for Government Information". In line with these policies, the CDR data sets are nonproprietary, publicly available, and no restrictions are placed upon their use. For more information, see the [Fair Use of NOAA's CDR Data Sets, Algorithms and Documentation](https://www1.ncdc.noaa.gov/pub/data/sds/cdr/CDRs/Aerosol_Optical_Thickness/UseAgreement_01B-04.pdf) pdf.
Citations:
  * Zhao, Xuepeng; and NOAA CDR Program: NOAA Climate Data Record (CDR) of AVHRR Daily and Monthly Aerosol Optical Thickness (AOT) over Global Oceans, Version 4.0. [indicate subset used]. NOAA National Centers for Environmental Information. [doi:10.25921/w3zj-4y48](https://doi.org/10.25921/w3zj-4y48) [date accessed].


  * [ https://doi.org/10.25921/w3zj-4y48 ](https://doi.org/10.25921/w3zj-4y48)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NOAA/CDR/AVHRR/AOT/V4')
.filter(ee.Filter.date('2018-02-01','2018-03-01'));
varaerosolOpticalThickness=dataset.select('aot');
varvisParams={
min:0.0,
max:0.5,
palette:['800080','0000ff','00ffff','008000','ffff00','ff0000'],
};
Map.setCenter(-88.6,26.4,3);
Map.addLayer(
aerosolOpticalThickness,visParams,
'Aerosol Optical Thickness');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_CDR_AVHRR_AOT_V4)
[ NOAA CDR AVHRR AOT: Daily Aerosol Optical Thickness Over Global Oceans, v04 ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4)
The NOAA Climate Data Record (CDR) of Aerosol Optical Thickness (AOT) is a collection of global daily 0.1 degree derived data from the PATMOS-x AVHRR level-2b channel 1 (0.63 micron) orbital clear-sky radiance. The aerosol product is generated from AVHRR imagery in cloud-free conditions during daytime over oceans. Due to …
NOAA/CDR/AVHRR/AOT/V4, aerosol,atmosphere,atmospheric,avhrr,cdr,daily,noaa,optical,pollution 
1981-01-01T00:00:00Z/2024-12-31T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.25921/w3zj-4y48 ](https://doi.org/https://doi.org/10.25921/w3zj-4y48)
  * [ https://doi.org/10.25921/w3zj-4y48 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_AVHRR_AOT_V4)


