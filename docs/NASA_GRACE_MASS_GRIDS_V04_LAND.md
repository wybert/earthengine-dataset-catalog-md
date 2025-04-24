 
#  GRACE Monthly Mass Grids Release 06 Version 04 - Land 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/GRACE/MASS_GRIDS_V04/LAND](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_GRACE_MASS_GRIDS_V04_LAND_sample.png) 

Dataset Availability
    2002-04-01T00:00:00Z–2017-01-07T00:00:00Z 

Dataset Provider
     [ NASA Jet Propulsion Laboratory ](https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-land/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/GRACE/MASS_GRIDS_V04/LAND")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GRACE_MASS_GRIDS_V04_LAND) 

Tags
     [crs](https://developers.google.com/earth-engine/datasets/tags/crs) [gfz](https://developers.google.com/earth-engine/datasets/tags/gfz) [grace](https://developers.google.com/earth-engine/datasets/tags/grace) [gravity](https://developers.google.com/earth-engine/datasets/tags/gravity) [jpl](https://developers.google.com/earth-engine/datasets/tags/jpl) [land](https://developers.google.com/earth-engine/datasets/tags/land) [mass](https://developers.google.com/earth-engine/datasets/tags/mass) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [tellus](https://developers.google.com/earth-engine/datasets/tags/tellus) [water](https://developers.google.com/earth-engine/datasets/tags/water)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#dois) More
The monthly land mass grids contain water mass anomalies given as equivalent water thickness derived from GRACE & GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. The equivalent water thickness represents the total terrestrial water storage anomalies from soil moisture, snow, surface water (incl. rivers, lakes, reservoirs etc.), as well as groundwater and aquifers. A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Version 04 (v04) of the terrestrial water storage data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change.
The GRACE Tellus (GRCTellus) Monthly Mass Grids dataset is produced by three centers: CSR (U. Texas / Center for Space Research), GFZ (GeoForschungsZentrum Potsdam), and JPL (NASA Jet Propulsion Laboratory). Each center is a part of the GRACE Ground System and generates Level-2 data (spherical harmonic fields) used in this dataset. The output includes spherical harmonic coefficients of the gravity field and of the dealiasing fields used to compute them. Since each center independently produces the coefficients, the results may be slightly different. It is recommended for most users to use the mean of all three datasets. See the provider's [choosing a solution](https://grace.jpl.nasa.gov/data/choosing-a-solution/) page for more details.
**Pixel Size** 111320 meters 
**Bands**
Name | Units | Description  
---|---|---  
`lwe_thickness_csr` | cm | Equivalent liquid water thickness in centimeters calculated by CSR.  
`lwe_thickness_gfz` | cm | Equivalent liquid water thickness in centimeters calculated by GFZ.  
`lwe_thickness_jpl` | cm | Equivalent liquid water thickness in centimeters calculated by JPL.  
`uncertainty_csr` | Error estimation by CSR.  
`uncertainty_gfz` | Error estimation by GFZ.  
`uncertainty_jpl` | Error estimation by JPL.  
**Image Properties**
Name | Type | Description  
---|---|---  
CSR_END_TIME | DOUBLE | End date in milliseconds of spherical harmonics solution from CSR.  
CSR_START_TIME | DOUBLE | Start date in milliseconds of spherical harmonics solution from CSR.  
GFZ_END_TIME | DOUBLE | End date in milliseconds of spherical harmonics solution from GFZ.  
GFZ_START_TIME | DOUBLE | Start date in milliseconds of spherical harmonics solution from GFZ.  
JPL_END_TIME | DOUBLE | End date in milliseconds of spherical harmonics solution from JPL.  
JPL_START_TIME | DOUBLE | Start date in milliseconds of spherical harmonics solution from JPL.  
**Terms of Use**
All NASA-produced data from the GRACE mission is made freely available for the public to use. When using any of the GRCTellus data, please add an acknowledgment: "GRACE land are available at <https://grace.jpl.nasa.gov>, supported by the NASA MEaSUREs Program." and cite with the citations provided.
Citations:
  * Felix Landerer. 2021. TELLUS_GRAC_L3_JPL_RL06_LND_v04. Ver. RL06 v04. PO.DAAC, CA, USA. Dataset accessed [YYYY-MM-DD] at <https://doi.org/10.5067/TELND-3AJ64>.
  * Landerer F.W. and S. C. Swenson, Accuracy of scaled GRACE terrestrial water storage estimates. Water Resources Research, Vol 48, W04531, 11 PP, [doi:10.1029/2011WR011453](https://doi.org/10.1029/2011WR011453), 2012.
  * Swenson, S. C. and J. Wahr, Post-processing removal of correlated errors in GRACE data, Geophys. Res. Lett., 33, L08402, [doi:10.1029/2005GL025285](https://doi.org/10.1029/2005GL025285), 2006.


  * [ https://doi.org/10.1029/2005GL025285 ](https://doi.org/10.1029/2005GL025285)
  * [ https://doi.org/10.1029/2011WR011453 ](https://doi.org/10.1029/2011WR011453)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND#code-editor-javascript-sample) More
```
vardataset=ee.Image('NASA/GRACE/MASS_GRIDS_V04/LAND/20170501_20170522');
varlwe_thickness=dataset.select('lwe_thickness_csr');
varpalette=['001137','01abab','e7eb05','620500'];
varequivalentWaterThicknessCsrVis={
palette:palette,
min:-0.7845402964290882,
max:0.5693220260300134
};
Map.setCenter(6.746,46.529,2);
Map.addLayer(
lwe_thickness,equivalentWaterThicknessCsrVis,
'Equivalent Water Thickness CSR');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GRACE_MASS_GRIDS_V04_LAND)
[ GRACE Monthly Mass Grids Release 06 Version 04 - Land ](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND)
The monthly land mass grids contain water mass anomalies given as equivalent water thickness derived from GRACE & GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. The equivalent water thickness represents the total terrestrial water storage anomalies from soil moisture, snow, surface …
NASA/GRACE/MASS_GRIDS_V04/LAND, crs,gfz,grace,gravity,jpl,land,mass,nasa,surface-ground-water,tellus,water 
2002-04-01T00:00:00Z/2017-01-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1029/2011WR011453 ](https://doi.org/https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-land/)
  * [ https://doi.org/10.1029/2011WR011453 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_V04_LAND)


