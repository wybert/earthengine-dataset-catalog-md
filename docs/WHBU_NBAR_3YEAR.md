 
#  MODIS 3-year Nadir BRDF-Adjusted Reflectance (NBAR) Mosaic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WHBU/NBAR_3YEAR](https://developers.google.com/earth-engine/datasets/images/WHBU/WHBU_NBAR_3YEAR_sample.png) 

Dataset Availability
    2002-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ Baccini, A. (Woods Hole Research Center), Sulla-Menashe, D. (Boston University) ](https://doi.org/10.1088/1748-9326/3/4/045011) 

Earth Engine Snippet
     `    ee.ImageCollection("WHBU/NBAR_3YEAR")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WHBU/WHBU_NBAR_3YEAR) 

Cadence
    1 Year 

Tags
    
albedo
annual
bu
mcd43a4
modis-derived
nbar
reflectance
satellite-imagery
whrc
[Description](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#dois) More
The mosaics are created by using the MODIS 8-Day 500 meter BRDF-Albedo Quality product. Data Quality flags are used to select the best observations from the MODIS 8-day 500 meter Nadir BRDF-Adjusted Reflectance imagery product. This specific mosaic picks observations from the three highest quality categories over a 3-year period of MODIS data.
The MODIS NBAR annual mosaics have been used by government agencies and NGOs in tropical countries as input to generate aboveground biomass/carbon maps. The Woods Hole Research Center has been using the dataset for country capacity building and technical training workshops in tropical countries.
**Pixel Size** 463 meters 
**Bands**
Name | Wavelength | Description  
---|---|---  
`Nadir_Reflectance_Band1` | 620-670nm | Best NBAR at local solar noon for band 1  
`Nadir_Reflectance_Band2` | 841-876nm | Best NBAR at local solar noon for band 2  
`Nadir_Reflectance_Band3` | 459-479nm | Best NBAR at local solar noon for band 3  
`Nadir_Reflectance_Band4` | 545-565nm | Best NBAR at local solar noon for band 4  
`Nadir_Reflectance_Band5` | 1230-1250nm | Best NBAR at local solar noon for band 5  
`Nadir_Reflectance_Band6` | 1628-1652nm | Best NBAR at local solar noon for band 6  
`Nadir_Reflectance_Band7` | 2105-2155nm | Best NBAR at local solar noon for band 7  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Baccini, A., Laporte, N., Goetz, S. J., Sun, M., & Dong, H. (2008). A first map of tropical Africa's above-ground biomass derived from satellite imagery. Environmental Research Letters, 3(4), 045011. [doi:10.1088/1748-9326/3/4/045011](https://doi.org/10.1088/1748-9326/3/4/045011)


  * [ https://doi.org/10.1088/1748-9326/3/4/045011 ](https://doi.org/10.1088/1748-9326/3/4/045011)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('WHBU/NBAR_3YEAR');
Map.addLayer(dataset.mean(),{min:0,max:7000});
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WHBU/WHBU_NBAR_3YEAR)
[ MODIS 3-year Nadir BRDF-Adjusted Reflectance (NBAR) Mosaic ](https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR)
The mosaics are created by using the MODIS 8-Day 500 meter BRDF-Albedo Quality product. Data Quality flags are used to select the best observations from the MODIS 8-day 500 meter Nadir BRDF-Adjusted Reflectance imagery product. This specific mosaic picks observations from the three highest quality categories over a 3-year period …
WHBU/NBAR_3YEAR, albedo,annual,bu,mcd43a4,modis-derived,nbar,reflectance,satellite-imagery 
2002-01-01T00:00:00Z/2017-01-01T00:00:00Z
-60.1 -180 60.1 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1088/1748-9326/3/4/045011 ](https://doi.org/https://doi.org/10.1088/1748-9326/3/4/045011)
  * [ https://doi.org/10.1088/1748-9326/3/4/045011 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WHBU_NBAR_3YEAR)


