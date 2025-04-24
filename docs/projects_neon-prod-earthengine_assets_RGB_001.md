 
#  NEON RGB Camera Imagery 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![projects/neon-prod-earthengine/assets/RGB/001](https://developers.google.com/earth-engine/datasets/images/neon-prod-earthengine/projects_neon-prod-earthengine_assets_RGB_001_sample.png)
info
This dataset is part of a Publisher Catalog, and not managed by Google Earth Engine. Contact listaopgee@battelleecology.org for bugs or [view more datasets](https://developers.google.com/earth-engine/datasets/publisher/neon-prod-earthengine) from the National Ecological Observatory Network Catalog. [Learn more about Publisher datasets](https://developers.google.com/earth-engine/datasets/publisher). 
[ ![Catalog Owner Logo](https://developers.google.com/static/earth-engine/datasets/logos/neon-prod-earthengine_logo.png) ](https://www.neonscience.org/data-collection/airborne-remote-sensing) 

Catalog Owner
    National Ecological Observatory Network 

Dataset Availability
    2013-01-01T00:00:00Z–2024-09-08T16:03:42Z 

Dataset Provider
     [ NEON ](https://data.neonscience.org/data-products/DP3.30010.001) 

Earth Engine Snippet
     `    ee.ImageCollection("projects/neon-prod-earthengine/assets/RGB/001")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/neon-prod-earthengine/projects_neon-prod-earthengine_assets_RGB_001) 

Tags
     [airborne](https://developers.google.com/earth-engine/datasets/tags/airborne) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [highres](https://developers.google.com/earth-engine/datasets/tags/highres) [neon](https://developers.google.com/earth-engine/datasets/tags/neon) [neon-prod-earthengine](https://developers.google.com/earth-engine/datasets/tags/neon-prod-earthengine) [orthophoto](https://developers.google.com/earth-engine/datasets/tags/orthophoto) [publisher-dataset](https://developers.google.com/earth-engine/datasets/tags/publisher-dataset) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation)
[Description](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#citations) More
High resolution Red-Green-Blue (RGB) orthorectified camera images mosaicked and output onto a fixed, uniform spatial grid using nearest-neighbor resampling; spatial resolution is 0.1 m. The digital camera is part of a suite of instruments on the NEON Airborne Observation Platform (AOP) that also includes a full-waveform LiDAR system and the NEON Imaging Spectrometer. In the orthorectification process, the digital imagery is re-mapped to the same geographic projection as the LiDAR and imaging spectrometer data that is acquired simultaneously. The resulting images share the same map projection grid space as the orthorectified spectrometer and LiDAR imagery. Since the digital camera imagery is acquired at higher spatial resolution than the imaging spectrometer data, it can aid in identifying features in the spectrometer images including manmade features (e.g., roads, fence lines, and buildings) that are indicative of land-use change. Availability in GEE may not represent full availability in the NEON Data Portal (linked below). Additional sites and years can be added to GEE upon request by emailing listaopgee@battelleecology.org.
See [NEON Data Product DP3.30010.001](https://data.neonscience.org/data-products/DP3.30010.001) for more details.
Documentation: [NEON DP3.30010.001 Camera imagery mosaic Quick Start Guide](https://data.neonscience.org/api/v0/documents/quick-start-guides/NEON.QSG.DP3.30010.001v1?inline=true&fallback=html)
Get started by exploring the [Intro to AOP Data in Google Earth Engine Tutorial Series](https://www.neonscience.org/resources/learning-hub/tutorials/intro-aop-data-google-earth-engine-tutorial-series)
Browse and interact with AOP data in the [NEON AOP GEE Data Viewer App](https://neon-prod-earthengine.projects.earthengine.app/view/neon-aop-gee-data-viewer---desktop)
**Pixel Size** 0.1 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`R` | dn |  0  |  255  | Red  
`G` | dn |  0  |  255  | Green  
`B` | dn |  0  |  255  | Blue  
**Image Properties**
Name | Type | Description  
---|---|---  
AOP_VISIT_NUMBER | INT | Unique visit number to the NEON site.  
CITATION | STRING | Data citation. See [NEON Data Policies and Citation Guidelines](https://www.neonscience.org/data-samples/data-policies-citation).  
DOI | STRING | Digital Object Identifier. NEON data that have been released are assigned a DOI.  
FLIGHT_YEAR | INT | Year the data were collected.  
NEON_DOMAIN | STRING | NEON eco-climatic domain code, "D01" to "D20". See [NEON Field Sites and Domains](https://www.neonscience.org/field-sites/about-field-sites).  
NEON_SITE | STRING | NEON four-digit site code. See [NEON Field Sites](https://www.neonscience.org/field-sites/).  
NEON_SITE_NAME | STRING | Full name of the NEON site. See [NEON Field Sites](https://www.neonscience.org/field-sites/).  
NEON_DATA_PROD_URL | STRING | NEON data product url. Always set to: <https://data.neonscience.org/data-products/DP3.30010.001>.  
SENSOR_NAME | STRING | Make and model of the camera sensor: "Phase One D8900", "Phase One IQ180", "Phase One iX-RS 1000", "Phase One iXM-RS 150F".  
SENSOR_SERIAL | STRING | Serial number of the camera sensor: "EH021537", "EH021656", "EH021554", "FT010031", "MM010175", "MM010176", "YC030119", "YC030129".  
PROVISIONAL_RELEASED | STRING | Whether the data are Provisional or Released. See [NEON Data Revisions and Releases](https://www.neonscience.org/data-samples/data-management/data-revisions-releases).  
RELEASE_YEAR | INT | If data are released, the year of the NEON Release Tag.  
**Terms of Use**
All data collected by NEON and provided as data products, with the exception of data related to rare, threatened, or endangered (RTE) species, are released to the public domain under [Creative Commons CC0 1.0 "No Rights Reserved"](https://creativecommons.org/publicdomain/zero/1.0/). No copyright has been applied to NEON data; any person may copy, modify, or distribute the data, for commercial or non-commercial purposes, without asking for permission. NEON data may still be subject to other laws or rights such as for privacy, and NEON makes no warranties about the data and disclaims all liability. When using or citing NEON data, no implication should be made about endorsement by NEON. In most countries, data and facts are not copyrightable. By putting NEON data into the public domain, we encourage broad use, particularly in scientific analyses and data aggregations. However, please be aware of the following scholarly norms: NEON data should be used in a way that is mindful of the limitations of the data, using the documentation associated with the data packages as a guide. Please refer to [NEON Data Guidelines and Policies](https://www.neonscience.org/data-samples/guidelines-policies) for detailed information on how to properly use and cite NEON data, as well as best practices for publishing research that uses NEON data.
Citations:
  * See [NEON citation guidelines](https://www.neonscience.org/data-samples/guidelines-policies/citing)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001#code-editor-javascript-sample) More
```
// Read in the NEON AOP RGB Camera Image Collection
varrgb=ee.ImageCollection(
"projects/neon-prod-earthengine/assets/RGB/001");
// Display available images in the RGB/001 Image Collection
print('NEON RGB Camera Images',rgb.aggregate_array('system:index'))
// Specify the start and end dates and filter by date range
varstartDate=ee.Date('2021-01-01');
varendDate=startDate.advance(1,'year');
varrgb2021=rgb.filterDate(startDate,endDate);
// Filter by NEON site name (see https://www.neonscience.org/field-sites/explore-field-sites)
varrgbABBY_2021=rgb2021.filter('NEON_SITE == "ABBY"').mosaic();
// Add the RGB Camera layer to the Map and center on the site
Map.addLayer(rgbABBY_2021,{min:40,max:200,gamma:0.65},'ABBY 2021 RGB Camera Imagery');
Map.setCenter(-122.341,45.75,15);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/neon-prod-earthengine/projects_neon-prod-earthengine_assets_RGB_001)
[ NEON RGB Camera Imagery ](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001)
High resolution Red-Green-Blue (RGB) orthorectified camera images mosaicked and output onto a fixed, uniform spatial grid using nearest-neighbor resampling; spatial resolution is 0.1 m. The digital camera is part of a suite of instruments on the NEON Airborne Observation Platform (AOP) that also includes a full-waveform LiDAR system and the …
projects/neon-prod-earthengine/assets/RGB/001, airborne,forest,highres,neon,neon-prod-earthengine,orthophoto,publisher-dataset,rgb,satellite-imagery,vegetation 
2013-01-01T00:00:00Z/2024-09-08T16:03:42Z
16 -170 73 -66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://data.neonscience.org/data-products/DP3.30010.001)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_RGB_001)


