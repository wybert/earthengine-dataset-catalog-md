 
#  GRACE Monthly Mass Grids - Ocean EOFR 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/GRACE/MASS_GRIDS/OCEAN_EOFR](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR_sample.png) 

Dataset Availability
    2002-12-31T00:00:00Z–2016-12-10T00:00:00Z 

Dataset Provider
     [ NASA Jet Propulsion Laboratory ](https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-ocean/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/GRACE/MASS_GRIDS/OCEAN_EOFR")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR) 

Tags
     [crs](https://developers.google.com/earth-engine/datasets/tags/crs) [gfz](https://developers.google.com/earth-engine/datasets/tags/gfz) [grace](https://developers.google.com/earth-engine/datasets/tags/grace) [gravity](https://developers.google.com/earth-engine/datasets/tags/gravity) [jpl](https://developers.google.com/earth-engine/datasets/tags/jpl) [mass](https://developers.google.com/earth-engine/datasets/tags/mass) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans) [tellus](https://developers.google.com/earth-engine/datasets/tags/tellus) [water](https://developers.google.com/earth-engine/datasets/tags/water)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#dois) More
GRACE Tellus Monthly Mass Grids provides monthly gravitational anomalies relative to a 2004-2010 time-mean baseline. The data contained in this dataset are units of "Equivalent Water Thickness" which represent the deviations of mass in terms of vertical extent of water in centimeters. See the provider's [Monthly Mass Grids Overview](https://grace.jpl.nasa.gov/data/monthly-mass-grids/) for more details.
This dataset is a filtered version of the GRACE Tellus (GRCTellus) Ocean dataset. The 'EOFR' bottom pressure (OBP) grids are obtained by projecting the data from the regular GRC Ocean grids product onto the Empirical Orthogonal Functions (EOFs) of the Ocean Model for Circulation and Tides (OMCT). This effectively filters out signals in the GRACE data that are inconsistent with the physics and OBP variations in the OMCT ocean model.
The EOFR filtered reconstructed OBP fields agree better with radar altimetric sea surface height, reduce leakage around ice sheets and glaciers, and reduce noise in the mid latitudes where OBP variability is lower. [(Chambers and Willis, 2010)](https://doi.org/10.1175/2010JTECHO738.1)
**Note**
  * The GRCTellus Ocean datasets are optimized to examine regional ocean bottom pressure, but NOT intended to be spatially averaged to determine global mean ocean mass.


**Pixel Size** 111320 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`lwe_thickness_csr` | cm |  -18.46*  |  12.29*  | Equivalent liquid water thickness in centimeters calculated by CSR.  
`lwe_thickness_gfz` | cm |  -15.37*  |  14.56*  | Equivalent liquid water thickness in centimeters calculated by GFZ.  
`lwe_thickness_jpl` | cm |  -16.59*  |  11.7*  | Equivalent liquid water thickness in centimeters calculated by JPL.  
* estimated min or max value 
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
  * D.P. Chambers. 2012. GRACE MONTHLY OCEAN MASS GRIDS NETCDF RELEASE 5.0. Ver. 5.0. PO.DAAC, CA, USA. Dataset accessed [YYYY-MM-DD] at [doi:10.5067/TEOCN-0N005](https://doi.org/10.5067/TEOCN-0N005).
  * Chambers, D.P. and J.A. Bonin: Evaluation of Release 05 time-variable gravity coefficients over the ocean. Ocean Science 8, 859-868, 2012. [doi:10.5194/os-8-859-2012](https://doi.org/10.5194/os-8-859-2012).
  * Chambers D.P. and J. K. Willis: A Global Evaluation of Ocean Bottom Pressure from GRACE, OMCT, and Steric-Corrected Altimetry. J. of Oceanic and Atmosph. Technology, vol 27, pp 1395-1402, 2010.. [doi:10.1175/2010JTECHO738.1](https://doi.org/10.1175/2010JTECHO738.1)


  * [ https://doi.org/10.1175/2010JTECHO738.1 ](https://doi.org/10.1175/2010JTECHO738.1)
  * [ https://doi.org/10.5194/os-8-859-2012 ](https://doi.org/10.5194/os-8-859-2012)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/GRACE/MASS_GRIDS/OCEAN_EOFR')
.filter(ee.Filter.date('2016-08-01','2016-08-30'));
varequivalentWaterThicknessCsr=dataset.select('lwe_thickness_csr');
varequivalentWaterThicknessCsrVis={
min:-10.0,
max:10.0,
};
Map.setCenter(6.746,46.529,1);
Map.addLayer(
equivalentWaterThicknessCsr,equivalentWaterThicknessCsrVis,
'Equivalent Water Thickness CSR');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR)
[ GRACE Monthly Mass Grids - Ocean EOFR ](https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR)
GRACE Tellus Monthly Mass Grids provides monthly gravitational anomalies relative to a 2004-2010 time-mean baseline. The data contained in this dataset are units of "Equivalent Water Thickness" which represent the deviations of mass in terms of vertical extent of water in centimeters. See the provider's Monthly Mass Grids Overview for …
NASA/GRACE/MASS_GRIDS/OCEAN_EOFR, crs,gfz,grace,gravity,jpl,mass,nasa,ocean,oceans,tellus,water 
2002-12-31T00:00:00Z/2016-12-10T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5194/os-8-859-2012 ](https://doi.org/https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-ocean/)
  * [ https://doi.org/10.5194/os-8-859-2012 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_GRACE_MASS_GRIDS_OCEAN_EOFR)


