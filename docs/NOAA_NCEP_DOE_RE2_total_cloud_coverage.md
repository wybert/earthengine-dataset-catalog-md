 
#  NCEP-DOE Reanalysis 2 (Gaussian Grid), Total Cloud Coverage 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/NCEP_DOE_RE2/total_cloud_coverage](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_NCEP_DOE_RE2_total_cloud_coverage_sample.png) 

Dataset Availability
    1979-01-01T00:00:00Z–2025-03-31T18:00:00Z 

Dataset Provider
     [ NOAA ](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/NCEP_DOE_RE2/total_cloud_coverage")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NCEP_DOE_RE2_total_cloud_coverage) 

Cadence
    6 Hours 

Tags
     [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [cloud](https://developers.google.com/earth-engine/datasets/tags/cloud) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [ncep](https://developers.google.com/earth-engine/datasets/tags/ncep) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [reanalysis](https://developers.google.com/earth-engine/datasets/tags/reanalysis)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage#citations) More
NCEP-DOE Reanalysis 2 project is using a state-of-the-art analysis/forecast system to perform data assimilation using past data from 1979 through the previous year.
**Pixel Size** 278300 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`tcdc` | % |  0*  |  100*  | Total cloud cover  
* estimated min or max value 
**Terms of Use**
There are no restrictions on the use of these datasets.
Citations:
  * [NCEP-DOE AMIP-II Reanalysis (R-2): M. Kanamitsu, W. Ebisuzaki, J. Woollen, S-K Yang, J.J. Hnilo, M. Fiorino, and G. L. Potter. 1631-1643, Nov 2002, Bulletin of the American Meteorological Society.](https://journals.ametsoc.org/view/journals/bams/83/11/bams-83-11-1631.xml).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage#code-editor-javascript-sample) More
```
// Import the dataset, filter the first five months of 2020.
vardataset=ee.ImageCollection('NOAA/NCEP_DOE_RE2/total_cloud_coverage')
.filter(ee.Filter.date('2020-01-01','2020-06-01'));
// Select the total cloud cover band.
vartotalCloudCoverage=dataset.select('tcdc');
// Reduce the image collection to per-pixel mean.
vartotalCloudCoverageMean=totalCloudCoverage.mean();
// Define visualization parameters.
varvis={
min:0,
max:80,// dataset max is 100
palette:['black','white'],
};
// Display the dataset.
Map.setCenter(0,20,2);
Map.addLayer(totalCloudCoverageMean,vis,'Total Cloud Coverage Data',false);
// Display a visualization image with opacity defined by cloud cover.
varvisImg=totalCloudCoverageMean.visualize(vis)
.updateMask(totalCloudCoverageMean.divide(100));
Map.addLayer(visImg,null,'Total Cloud Coverage Vis.',true);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_NCEP_DOE_RE2_total_cloud_coverage)
[ NCEP-DOE Reanalysis 2 (Gaussian Grid), Total Cloud Coverage ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage)
NCEP-DOE Reanalysis 2 project is using a state-of-the-art analysis/forecast system to perform data assimilation using past data from 1979 through the previous year.
NOAA/NCEP_DOE_RE2/total_cloud_coverage, atmosphere,climate,cloud,geophysical,ncep,noaa,reanalysis 
1979-01-01T00:00:00Z/2025-03-31T18:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_NCEP_DOE_RE2_total_cloud_coverage)


