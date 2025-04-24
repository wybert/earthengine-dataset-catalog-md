 
#  OpenET DisALEXI Monthly Evapotranspiration v2.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![OpenET/DISALEXI/CONUS/GRIDMET/MONTHLY/v2_0](https://developers.google.com/earth-engine/datasets/images/OpenET/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2023-12-01T00:00:00Z 

Dataset Provider
     [ OpenET, Inc. ](https://openetdata.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("OpenET/DISALEXI/CONUS/GRIDMET/MONTHLY/v2_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenET/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0) 

Cadence
    1 Month 

Tags
     [evapotranspiration](https://developers.google.com/earth-engine/datasets/tags/evapotranspiration) [gridmet-derived](https://developers.google.com/earth-engine/datasets/tags/gridmet-derived) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [openet](https://developers.google.com/earth-engine/datasets/tags/openet) [water](https://developers.google.com/earth-engine/datasets/tags/water) [water-vapor](https://developers.google.com/earth-engine/datasets/tags/water-vapor)
[Description](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#dois) More
Atmosphere-Land Exchange Inverse / Disaggregation of the Atmosphere-Land Exchange Inverse (ALEXI/DisALEXI)
DisALEXI was recently ported to Google Earth Engine as part of the OpenET framework and the baseline ALEXI/DisALEXI model structure is described by Anderson et al. (2012, 2018). The ALEXI evapotranspiration (ET) model specifically uses time differential land surface temperature (LST) measurements from geostationary or moderate resolution polar orbiting platforms to generate regional ET maps. DisALEXI then disaggregates the regional ALEXI ET to finer scales using Landsat data (30 m; biweekly) to resolve individual farm fields and other landscape features. [Additional information](https://openetdata.org/methodologies/)
**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`et` | mm | DisALEXI ET value  
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
  * Anderson, M., Gao, F., Knipper, K., Hain, C., Dulaney, W., Baldocchi, D ., Eichelmann, E., Hemes, K., Yang, Y., Medellin-Azuara, J. and Kustas, W., 2018. Field-scale assessment of land and water use change over the California Delta using remote sensing. Remote Sensing, 10(6), p.889. [doi:10.3390/rs10060889](https://doi.org/10.3390/rs10060889)
  * Anderson, M.C., Norman, J.M., Mecikalski, J.R., Otkin, J.A. and Kustas, W.P., 2007. A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 1. Model formulation. Journal of Geophysical Research: Atmospheres, 112(D10). [doi:10.1029/2006JD007506](https://doi.org/10.1029/2006JD007506)


  * [ https://doi.org/10.3390/rs10060889 ](https://doi.org/10.3390/rs10060889)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('OpenET/DISALEXI/CONUS/GRIDMET/MONTHLY/v2_0')
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
Map.addLayer(et,visualization,'OpenET DisALEXI Annual ET');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/OpenET/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0)
[ OpenET DisALEXI Monthly Evapotranspiration v2.0 ](https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0)
Atmosphere-Land Exchange Inverse / Disaggregation of the Atmosphere-Land Exchange Inverse (ALEXI/DisALEXI) DisALEXI was recently ported to Google Earth Engine as part of the OpenET framework and the baseline ALEXI/DisALEXI model structure is described by Anderson et al. (2012, 2018). The ALEXI evapotranspiration (ET) model specifically uses time differential land surface …
OpenET/DISALEXI/CONUS/GRIDMET/MONTHLY/v2_0, evapotranspiration,gridmet-derived,landsat-derived,monthly,openet,water,water-vapor 
2001-01-01T00:00:00Z/2023-12-01T00:00:00Z
25 -126 50 -66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.3390/rs10060889 ](https://doi.org/https://openetdata.org/)
  * [ https://doi.org/10.3390/rs10060889 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0)


