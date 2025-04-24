 
#  WRI Aqueduct Baseline Monthly Version 4.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WRI/Aqueduct_Water_Risk/V4/baseline_monthly](https://developers.google.com/earth-engine/datasets/images/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_monthly_sample.png) 

Dataset Availability
    2010-01-01T00:00:00Z–2080-12-31T23:59:59Z 

Dataset Provider
     [ World Resources Institute ](https://www.wri.org/data/aqueduct-global-maps-40-data) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("WRI/Aqueduct_Water_Risk/V4/baseline_monthly")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_monthly)      FeatureView  `    ui.Map.FeatureViewLayer("WRI/Aqueduct_Water_Risk/V4/baseline_monthly_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_monthly_FeatureView) 

Tags
     [aqueduct](https://developers.google.com/earth-engine/datasets/tags/aqueduct) [flood](https://developers.google.com/earth-engine/datasets/tags/flood) [monitoring](https://developers.google.com/earth-engine/datasets/tags/monitoring) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [table](https://developers.google.com/earth-engine/datasets/tags/table) [wri](https://developers.google.com/earth-engine/datasets/tags/wri)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly#terms-of-use) More
Aqueduct 4.0 is the latest iteration of WRI's water risk framework designed to translate complex hydrological data into intuitive indicators of water related risk. This dataset has curated 13 water risk indicators for quantity, quality and reputational concerns into a comprehensive framework. For 5 of the 13 indicators, a global hydrological model called PCR-GLOBWB 2 has been used to generate novel datasets on sub-basic water supply. The PCR-GLOBWB 2 model is also used to project future sub-basin water conditions using CMIP6 climate forcings. The projections center around three periods (2030, 2050, and 2080) under three future scenarios (business-as-usual SSP 3 RCP 7.0, optimistic SSP 1 RCP 2.6, and pessimistic SSP 5 RCP 8.5).
The water risk indicators have been aggregated by category (quantity, quality, reputational, and overall) into composite risk scores using sector-specific weighting schemes. In addition, select sub-basin scores have been aggregated into country and provincial administrative boundaries using a weighted average approach, where sub-basins with more demand have a higher influence over the final administrative score.
The WRI Aqueduct baseline monthly dataset provides monthly data on key water risk indicators which includes indicators such as baseline water stress, baseline water depletion and interannual variability.This monthly data allows for a more detailed analysis of water risk dynamics throughout the year, which is crucial for understanding seasonal water scarcity, planning for water management interventions, and adapting to changing water availability patterns.
This [technical note](https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators) explains in detail the framework, methodology, and data used in developing Aqueduct Floods.
**Table Schema**
Name | Type | Description  
---|---|---  
fid_1 | INT | Feature Id  
pfaf_id | INT | Six digit Pfafstetter code for the [hydrological basin](https://hydrosheds.org/page/hydrobasins)  
bwd_01_cat | INT | Baseline water depletion category for January  
bwd_01_label | STRING | Baseline water depletion label for January  
bwd_01_raw | DOUBLE | Baseline water depletion raw value for January  
bwd_01_score | DOUBLE | Baseline water depletion score for January  
bwd_02_cat | INT | Baseline water depletion category for February  
bwd_02_label | STRING | Baseline water depletion label for February  
bwd_02_raw | DOUBLE | Baseline water depletion raw value for February  
bwd_02_score | DOUBLE | Baseline water depletion score for February  
bwd_03_cat | INT | Baseline water depletion category for March  
bwd_03_label | STRING | Baseline water depletion label for March  
bwd_03_raw | DOUBLE | Baseline water depletion raw value for March  
bwd_03_score | DOUBLE | Baseline water depletion score for March  
bwd_04_cat | INT | Baseline water depletion category for April  
bwd_04_label | STRING | Baseline water depletion label for April  
bwd_04_raw | DOUBLE | Baseline water depletion raw value for April  
bwd_04_score | DOUBLE | Baseline water depletion score for April  
bwd_05_cat | INT | Baseline water depletion category for May  
bwd_05_label | STRING | Baseline water depletion label for May  
bwd_05_raw | DOUBLE | Baseline water depletion raw value for May  
bwd_05_score | DOUBLE | Baseline water depletion score for May  
bwd_06_cat | INT | Baseline water depletion category for June  
bwd_06_label | STRING | Baseline water depletion label for June  
bwd_06_raw | DOUBLE | Baseline water depletion raw value for June  
bwd_06_score | DOUBLE | Baseline water depletion score for June  
bwd_07_cat | INT | Baseline water depletion category for July  
bwd_07_label | STRING | Baseline water depletion label for July  
bwd_07_raw | DOUBLE | Baseline water depletion raw value for July  
bwd_07_score | DOUBLE | Baseline water depletion score for July  
bwd_08_cat | INT | Baseline water depletion category for August  
bwd_08_label | STRING | Baseline water depletion label for August  
bwd_08_raw | DOUBLE | Baseline water depletion raw value for August  
bwd_08_score | DOUBLE | Baseline water depletion score for August  
bwd_09_cat | INT | Baseline water depletion category for September  
bwd_09_label | STRING | Baseline water depletion label for September  
bwd_09_raw | DOUBLE | Baseline water depletion raw value for September  
bwd_09_score | DOUBLE | Baseline water depletion score for September  
bwd_10_cat | INT | Baseline water depletion category for October  
bwd_10_label | STRING | Baseline water depletion label for October  
bwd_10_raw | DOUBLE | Baseline water depletion raw value for October  
bwd_10_score | DOUBLE | Baseline water depletion score for October  
bwd_11_cat | INT | Baseline water depletion category for November  
bwd_11_label | STRING | Baseline water depletion label for November  
bwd_11_raw | DOUBLE | Baseline water depletion raw value for November  
bwd_11_score | DOUBLE | Baseline water depletion score for November  
bwd_12_cat | INT | Baseline water depletion category for December  
bwd_12_label | STRING | Baseline water depletion label for December  
bwd_12_raw | DOUBLE | Baseline water depletion raw value for December  
bwd_12_score | DOUBLE | Baseline water depletion score for December  
bws_01_cat | INT | Baseline water stress category for January  
bws_01_label | STRING | Baseline water stress label for January  
bws_01_raw | DOUBLE | Baseline water stress raw value for January  
bws_01_score | DOUBLE | Baseline water stress score for January  
bws_02_cat | INT | Baseline water stress category for February  
bws_02_label | STRING | Baseline water stress label for February  
bws_02_raw | DOUBLE | Baseline water stress raw value for February  
bws_02_score | DOUBLE | Baseline water stress score for February  
bws_03_cat | INT | Baseline water stress category for March  
bws_03_label | STRING | Baseline water stress label for March  
bws_03_raw | DOUBLE | Baseline water stress raw value for March  
bws_03_score | DOUBLE | Baseline water stress score for March  
bws_04_cat | INT | Baseline water stress category for April  
bws_04_label | STRING | Baseline water stress label for April  
bws_04_raw | DOUBLE | Baseline water stress raw value for April  
bws_04_score | DOUBLE | Baseline water stress score for April  
bws_05_cat | INT | Baseline water stress category for May  
bws_05_label | STRING | Baseline water stress label for May  
bws_05_raw | DOUBLE | Baseline water stress raw value for May  
bws_05_score | DOUBLE | Baseline water stress score for May  
bws_06_cat | INT | Baseline water stress category for June  
bws_06_label | STRING | Baseline water stress label for June  
bws_06_raw | DOUBLE | Baseline water stress raw value for June  
bws_06_score | DOUBLE | Baseline water stress score for June  
bws_07_cat | INT | Baseline water stress category for July  
bws_07_label | STRING | Baseline water stress label for July  
bws_07_raw | DOUBLE | Baseline water stress raw value for July  
bws_07_score | DOUBLE | Baseline water stress score for July  
bws_08_cat | INT | Baseline water stress category for August  
bws_08_label | STRING | Baseline water stress label for August  
bws_08_raw | DOUBLE | Baseline water stress raw value for August  
bws_08_score | DOUBLE | Baseline water stress score for August  
bws_09_cat | INT | Baseline water stress category for September  
bws_09_label | STRING | Baseline water stress label for September  
bws_09_raw | DOUBLE | Baseline water stress raw value for September  
bws_09_score | DOUBLE | Baseline water stress score for September  
bws_10_cat | INT | Baseline water stress category for October  
bws_10_label | STRING | Baseline water stress label for October  
bws_10_raw | DOUBLE | Baseline water stress raw value for October  
bws_10_score | DOUBLE | Baseline water stress score for October  
bws_11_cat | INT | Baseline water stress category for November  
bws_11_label | STRING | Baseline water stress label for November  
bws_11_raw | DOUBLE | Baseline water stress raw value for November  
bws_11_score | DOUBLE | Baseline water stress score for November  
bws_12_cat | INT | Baseline water stress category for December  
bws_12_label | STRING | Baseline water stress label for December  
bws_12_raw | DOUBLE | Baseline water stress raw value for December  
bws_12_score | DOUBLE | Baseline water stress score for December  
iav_01_cat | INT | Interannual variability category for January  
iav_01_label | STRING | Interannual variability label for January  
iav_01_raw | DOUBLE | Interannual variability raw value for January  
iav_01_score | DOUBLE | Interannual variability score for January  
iav_02_cat | INT | Interannual variability category for February  
iav_02_label | STRING | Interannual variability label for February  
iav_02_raw | DOUBLE | Interannual variability raw value for February  
iav_02_score | DOUBLE | Interannual variability score for February  
iav_03_cat | INT | Interannual variability category for March  
iav_03_label | STRING | Interannual variability label for March  
iav_03_raw | DOUBLE | Interannual variability raw value for March  
iav_03_score | DOUBLE | Interannual variability score for March  
iav_04_cat | INT | Interannual variability category for April  
iav_04_label | STRING | Interannual variability label for April  
iav_04_raw | DOUBLE | Interannual variability raw value for April  
iav_04_score | DOUBLE | Interannual variability score for April  
iav_05_cat | INT | Interannual variability category for May  
iav_05_label | STRING | Interannual variability label for May  
iav_05_raw | DOUBLE | Interannual variability raw value for May  
iav_05_score | DOUBLE | Interannual variability score for May  
iav_06_cat | INT | Interannual variability category for June  
iav_06_label | STRING | Interannual variability label for June  
iav_06_raw | DOUBLE | Interannual variability raw value for June  
iav_06_score | DOUBLE | Interannual variability score for June  
iav_07_cat | INT | Interannual variability category for July  
iav_07_label | STRING | Interannual variability label for July  
iav_07_raw | DOUBLE | Interannual variability raw value for July  
iav_07_score | DOUBLE | Interannual variability score for July  
iav_08_cat | INT | Interannual variability category for August  
iav_08_label | STRING | Interannual variability label for August  
iav_08_raw | DOUBLE | Interannual variability raw value for August  
iav_08_score | DOUBLE | Interannual variability score for August  
iav_09_cat | INT | Interannual variability category for September  
iav_09_label | STRING | Interannual variability label for September  
iav_09_raw | DOUBLE | Interannual variability raw value for September  
iav_09_score | DOUBLE | Interannual variability score for September  
iav_10_cat | INT | Interannual variability category for October  
iav_10_label | STRING | Interannual variability label for October  
iav_10_raw | DOUBLE | Interannual variability raw value for October  
iav_10_score | DOUBLE | Interannual variability score for October  
iav_11_cat | INT | Interannual variability category for November  
iav_11_label | STRING | Interannual variability label for November  
iav_11_raw | DOUBLE | Interannual variability raw value for November  
iav_11_score | DOUBLE | Interannual variability score for November  
iav_12_cat | INT | Interannual variability category for December  
iav_12_label | STRING | Interannual variability label for December  
iav_12_raw | DOUBLE | Interannual variability raw value for December  
iav_12_score | DOUBLE | Interannual variability score for December  
**Terms of Use**
The WRI datasets are available without restriction on use or distribution. WRI does request that the user give proper attribution and identify WRI, where applicable, as the source of the data. For more information check [WRI's open data commitment](https://www.wri.org/data/open-data-commitment),
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly#code-editor-javascript-sample) More
```
vardataset=
ee.FeatureCollection('WRI/Aqueduct_Water_Risk/V4/baseline_monthly');
varreds=ee.List([
'67000D','9E0D14','E32F27','F6553D','FCA082','FEE2D5'
]);
functionnormalize(value,min,max){
returnvalue.subtract(min).divide(ee.Number(max).subtract(min));
}
functionsetColor(feature,property,min,max,palette){
varvalue=normalize(feature.getNumber(property),min,max)
.multiply(palette.size())
.min(palette.size().subtract(1))
.max(0);
returnfeature.set({style:{color:palette.get(value.int())}});
}
varbws_cat_style=function(f){
returnsetColor(f,'bws_01_cat',-1,4,reds);
};
varwaterLand=ee.Image('NOAA/NGDC/ETOPO1').select('bedrock').gt(0.0);
varwaterLandBackground=
waterLand.visualize({palette:['cadetblue','lightgray']});
Map.addLayer(waterLandBackground);
// Baseline water stress
varpolygons=dataset.filter('bws_01_cat > -2').map(bws_cat_style);
Map.setCenter(10,20,4);
Map.addLayer(polygons.style({styleProperty:'style',pointSize:3}));
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_monthly)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer(
'WRI/Aqueduct_Water_Risk/V4/baseline_monthly_FeatureView');
varvisParams={
isVisible:false,
pointSize:20,
rules:[{
// Baseline water stress with low category in January
filter:ee.Filter.eq('bws_01_cat',-1),
isVisible:true,
pointFillColor:{
property:'bws_01_cat',
mode:'linear',
palette:['f1eef6','d7b5d8','df65b0','ce1256'],
min:-1,
max:100
}
}]
};
fvLayer.setVisParams(visParams);
fvLayer.setName('Low Water Stress January');
Map.setCenter(-10,25,5);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_monthly_FeatureView)
[ WRI Aqueduct Baseline Monthly Version 4.0 ](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly)
Aqueduct 4.0 is the latest iteration of WRI's water risk framework designed to translate complex hydrological data into intuitive indicators of water related risk. This dataset has curated 13 water risk indicators for quantity, quality and reputational concerns into a comprehensive framework. For 5 of the 13 indicators, a global …
WRI/Aqueduct_Water_Risk/V4/baseline_monthly, aqueduct,flood,monitoring,surface-ground-water,table,wri 
2010-01-01T00:00:00Z/2080-12-31T23:59:59Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.wri.org/data/aqueduct-global-maps-40-data)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_monthly)


