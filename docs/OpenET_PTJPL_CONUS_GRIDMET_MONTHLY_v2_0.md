 
#  OpenET PT-JPL Monthly Evapotranspiration v2.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![OpenET/PTJPL/CONUS/GRIDMET/MONTHLY/v2_0](https://developers.google.com/earth-engine/datasets/images/OpenET/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0_sample.png) 

Dataset Availability
    1999-10-01T00:00:00Z–2023-12-01T00:00:00Z 

Dataset Provider
     [ OpenET, Inc. ](https://openetdata.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("OpenET/PTJPL/CONUS/GRIDMET/MONTHLY/v2_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenET/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0) 

Cadence
    1 Month 

Tags
     [evapotranspiration](https://developers.google.com/earth-engine/datasets/tags/evapotranspiration) [gridmet-derived](https://developers.google.com/earth-engine/datasets/tags/gridmet-derived) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [openet](https://developers.google.com/earth-engine/datasets/tags/openet) [water](https://developers.google.com/earth-engine/datasets/tags/water) [water-vapor](https://developers.google.com/earth-engine/datasets/tags/water-vapor)
[Description](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#dois) More
Priestley-Taylor Jet Propulsion Laboratory (PT-JPL)
The core formulation of the PT-JPL model within the OpenET framework has not changed from the original formulation detailed in Fisher et al. (2008). However, enhancements and updates to model inputs and time integration for PT-JPL were made to take advantage of contemporary gridded weather datasets, provide consistency with other models, improve open water evaporation estimates, and account for advection over crop and wetland areas in semiarid and arid environments. These changes include the use of Landsat surface reflectance and thermal radiation for calculating net radiation, photosynthetically active radiation, plant canopy and moisture variables, and use of NLDAS, Spatial CIMIS, and gridMET weather data for estimating insolation and ASCE reference ET. Similar to the implementation of other OpenET models, estimation of daily and monthly time integrated ET is based on the fraction of ASCE reference ET. Open water evaporation is estimated following a surface energy balance approach of Abdelrady et al. (2016) that is specific for water bodies by accounting for water heat flux as opposed to soil heat flux.
[Additional information](https://openetdata.org/methodologies/)
**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`et` | mm | PT-JPL ET value  
`count` | count | Number of cloud free values  
**Image Properties**
Name | Type | Description  
---|---|---  
build_date | STRING | Date assets were built  
cloud_cover_max | DOUBLE | Maximum CLOUD_COVER_LAND percent value for Landsat images included in interpolation  
collections | STRING | List of Landsat collections for Landsat images included in the interpolation  
core_version | STRING | OpenET core library version  
end_date | STRING | End date of month  
et_reference_band | STRING | Band in et_reference_source that contains the daily reference ET data  
et_reference_resample | STRING | Spatial interpolation mode to resample daily reference ET data  
et_reference_source | STRING | Collection ID for the daily reference ET data  
interp_days | DOUBLE | Maximum number of days before and after each image date to include in interpolation  
interp_method | STRING | Method used to interpolate between Landsat model estimates  
interp_source_count | DOUBLE | Number of available images in the interpolation source image collection for the target month  
mgrs_tile | STRING | MGRS grid zone ID  
model_name | STRING | OpenET model name  
model_version | STRING | OpenET model version  
scale_factor_count | DOUBLE | Scaling factor that should be applied to the count band  
scale_factor_et | DOUBLE | Scaling factor that should be applied to the et band  
start_date | STRING | Start date of month  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Fisher, J.B., Tu, K.P. and Baldocchi, D.D., 2008. Global estimates of the land–atmosphere water flux based on monthly AVHRR and ISLSCP-II data, validated at 16 FLUXNET sites. Remote Sensing of Environment, 112(3), pp.901-919. [doi:10.1016/j.rse.2007.06.025](https://doi.org/10.1016/j.rse.2007.06.025)
  * Abdelrady, A., Timmermans, J., Vekerdy, Z. and Salama, M., 2016. Surface energy balance of fresh and saline waters: AquaSEBS. Remote sensing, 8(7), p.583. [doi:10.3390/rs8070583](https://doi.org/10.3390/rs8070583)


  * [ https://doi.org/10.1016/j.rse.2007.06.025 ](https://doi.org/10.1016/j.rse.2007.06.025)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('OpenET/PTJPL/CONUS/GRIDMET/MONTHLY/v2_0')
.filterDate('2020-01-01','2021-01-01');
// Compute the annual evapotranspiration (ET) as the sum of the monthly ET
// images for the year.
varet=dataset.select('et').sum();
varvisualization={
min:0,
max:1400,
palette:[
'9e6212','ac7d1d','ba9829','c8b434','d6cf40','bed44b','9fcb51',
'80c256','61b95c','42b062','45b677','49bc8d','4dc2a2','51c8b8',
'55cece','4db4ba','459aa7','3d8094','356681','2d4c6e',
]
};
Map.setCenter(-100,38,5);
Map.addLayer(et,visualization,'OpenET PT-JPL Annual ET');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenET/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0)
[ OpenET PT-JPL Monthly Evapotranspiration v2.0 ](https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0)
Priestley-Taylor Jet Propulsion Laboratory (PT-JPL) The core formulation of the PT-JPL model within the OpenET framework has not changed from the original formulation detailed in Fisher et al. (2008). However, enhancements and updates to model inputs and time integration for PT-JPL were made to take advantage of contemporary gridded weather …
OpenET/PTJPL/CONUS/GRIDMET/MONTHLY/v2_0, evapotranspiration,gridmet-derived,landsat-derived,monthly,openet,water,water-vapor 
1999-10-01T00:00:00Z/2023-12-01T00:00:00Z
25 -126 50 -66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1016/j.rse.2007.06.025 ](https://doi.org/https://openetdata.org/)
  * [ https://doi.org/10.1016/j.rse.2007.06.025 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/OpenET_PTJPL_CONUS_GRIDMET_MONTHLY_v2_0)


