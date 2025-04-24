 
#  WRI Aqueduct Baseline Annual Version 4.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WRI/Aqueduct_Water_Risk/V4/baseline_annual](https://developers.google.com/earth-engine/datasets/images/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_annual_sample.png) 

Dataset Availability
    2010-01-01T00:00:00Z–2080-12-31T23:59:59Z 

Dataset Provider
     [ World Resources Institute ](https://www.wri.org/data/aqueduct-global-maps-40-data) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("WRI/Aqueduct_Water_Risk/V4/baseline_annual")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_annual)      FeatureView  `    ui.Map.FeatureViewLayer("WRI/Aqueduct_Water_Risk/V4/baseline_annual_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_annual_FeatureView) 

Tags
     [aqueduct](https://developers.google.com/earth-engine/datasets/tags/aqueduct) [flood](https://developers.google.com/earth-engine/datasets/tags/flood) [monitoring](https://developers.google.com/earth-engine/datasets/tags/monitoring) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [table](https://developers.google.com/earth-engine/datasets/tags/table) [wri](https://developers.google.com/earth-engine/datasets/tags/wri)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual#terms-of-use) More
Aqueduct 4.0 is the latest iteration of WRI's water risk framework designed to translate complex hydrological data into intuitive indicators of water related risk. This dataset has curated 13 water risk indicators for quantity, quality and reputational concerns into a comprehensive framework. For 5 of the 13 indicators, a global hydrological model called PCR-GLOBWB 2 has been used to generate novel datasets on sub-basic water supply. The PCR-GLOBWB 2 model is also used to project future sub-basin water conditions using CMIP6 climate forcings. The projections center around three periods (2030, 2050, and 2080) under three future scenarios (business-as-usual SSP 3 RCP 7.0, optimistic SSP 1 RCP 2.6, and pessimistic SSP 5 RCP 8.5).
The water risk indicators have been aggregated by category (quantity, quality, reputational, and overall) into composite risk scores using sector-specific weighting schemes. In addition, select sub-basin scores have been aggregated into country and provincial administrative boundaries using a weighted average approach, where sub-basins with more demand have a higher influence over the final administrative score.
The WRI Aqueduct baseline annual dataset provides a comprehensive overview of water-related risks on an annual basis which includes indicators such as baseline water stress, baseline water depletion and interannual variability. This annual data is essential for understanding long-term trends in water risk, assessing the cumulative impacts of human activities on water resources, and developing long-term water management strategies.
This [technical note](https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators) explains in detail the framework, methodology, and data used in developing Aqueduct Floods.
**Table Schema**
Name | Type | Description  
---|---|---  
aq30_id | INT | Unique identifier in numeric format  
aqid | INT | Identifier for groundwater aquifers based on WHYMAP  
area_km2 | DOUBLE | Area of the geometry in km2 (union of sub-basin, province and groundwater aquifer)  
gid_0 | STRING | ISO A3 country code based on [GADM](https://gadm.org/data.html)  
gid_1 | STRING | Identifier for sub-national units based on the [GADM](https://gadm.org/data.html) dataset. It contains the ISO A3 country code, followed by numeric values separated by underscores for each sub-national unit.  
name_0 | STRING | National or political entity name based on [GADM](https://gadm.org/data.html)  
name_1 | STRING | Sub-national or political entity name based on [GADM](https://gadm.org/data.html)  
pfaf_id | INT | Six digit Pfafstetter code for the [hydrological basin](https://hydrosheds.org/page/hydrobasins)  
string_id | STRING | Unique string for each geometry. Geometries are the union of hydrological basins, provinces and groundwater aquifers. The string_id is a combination of pfaf_id-gid_1-aqid. See the description of those columns.  
bws_cat | INT | Baseline water stress category  
bws_label | STRING | Baseline water stress label  
bws_raw | DOUBLE | Baseline water stress raw value  
bws_score | DOUBLE | Baseline water stress score  
bwd_cat | INT | Baseline water depletion category  
bwd_label | STRING | Baseline water depletion label  
bwd_raw | DOUBLE | Baseline water depletion raw value  
bwd_score | DOUBLE | Baseline water depletion score  
iav_cat | INT | Interannual variability category  
iav_label | STRING | Interannual variability label  
iav_raw | DOUBLE | Interannual variability raw value  
iav_score | DOUBLE | Interannual variability score  
sev_cat | INT | Seasonal variability category  
sev_label | STRING | Seasonal variability label  
sev_raw | DOUBLE | Seasonal variability raw value  
sev_score | DOUBLE | Seasonal variability score  
gtd_cat | INT | Groundwater table decline category  
gtd_label | STRING | Groundwater table decline label  
gtd_raw | DOUBLE | Groundwater table decline raw value  
gtd_score | DOUBLE | Groundwater table decline score  
rfr_cat | INT | Riverine flood risk category  
rfr_label | STRING | Riverine flood risk label  
rfr_raw | DOUBLE | Riverine flood risk raw value  
rfr_score | DOUBLE | Riverine flood risk score  
cfr_cat | INT | Coastal flood risk category  
cfr_label | STRING | Coastal flood risk label  
cfr_raw | DOUBLE | Coastal flood risk raw value  
cfr_score | DOUBLE | Coastal flood risk score  
drr_cat | INT | Drought risk category  
drr_label | STRING | Drought risk label  
drr_raw | DOUBLE | Drought risk raw value  
drr_score | DOUBLE | Drought risk score  
ucw_cat | INT | Untreated connected wastewater category  
ucw_label | STRING | Untreated connected wastewater label  
ucw_raw | DOUBLE | Untreated connected wastewater raw value  
ucw_score | DOUBLE | Untreated connected wastewater score  
udw_cat | INT | Unimproved/no drinking water category  
udw_label | STRING | Unimproved/no drinking water label  
udw_raw | DOUBLE | Unimproved/no drinking water raw value  
udw_score | DOUBLE | Unimproved/no drinking water score  
usa_cat | INT | Unimproved/no sanitation category  
usa_label | STRING | Unimproved/no sanitation label  
usa_raw | DOUBLE | Unimproved/no sanitation raw value  
usa_score | DOUBLE | Unimproved/no sanitation score  
cep_cat | INT | Coastal eutrophication potential category  
cep_label | STRING | Coastal eutrophication potential label  
cep_raw | DOUBLE | Coastal eutrophication potential raw value  
cep_score | DOUBLE | Coastal eutrophication potential score  
rri_cat | INT | Peak RepRisk country ESG risk index category  
rri_label | STRING | Peak RepRisk country ESG risk index label  
rri_raw | DOUBLE | Peak RepRisk country ESG risk index raw value  
rri_score | DOUBLE | Peak RepRisk country ESG risk index score  
w_awr_def_qan_cat | INT | Default weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_def_qan_label | STRING | Default weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_def_qan_raw | DOUBLE | Default weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_def_qan_score | DOUBLE | Default weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_def_qal_cat | INT | Default weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_def_qal_label | STRING | Default weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_def_qal_raw | DOUBLE | Default weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_def_qal_score | DOUBLE | Default weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_def_rrr_cat | INT | Default weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_def_rrr_label | STRING | Default weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_def_rrr_raw | DOUBLE | Default weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_def_rrr_score | DOUBLE | Default weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_def_tot_cat | INT | Default weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_def_tot_label | STRING | Default weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_def_tot_raw | DOUBLE | Default weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_def_tot_score | DOUBLE | Default weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_agr_qan_cat | INT | Agriculture weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_agr_qan_label | STRING | Agriculture weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_agr_qan_raw | DOUBLE | Agriculture weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_agr_qan_score | DOUBLE | Agriculture weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_agr_qal_cat | INT | Agriculture weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_agr_qal_label | STRING | Agriculture weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_agr_qal_raw | DOUBLE | Agriculture weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_agr_qal_score | DOUBLE | Agriculture weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_agr_rrr_cat | INT | Agriculture weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_agr_rrr_label | STRING | Agriculture weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_agr_rrr_raw | DOUBLE | Agriculture weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_agr_rrr_score | DOUBLE | Agriculture weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_agr_tot_cat | INT | Agriculture weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_agr_tot_label | STRING | Agriculture weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_agr_tot_raw | DOUBLE | Agriculture weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_agr_tot_score | DOUBLE | Agriculture weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_che_qan_cat | INT | Chemicals weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_che_qan_label | STRING | Chemicals weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_che_qan_raw | DOUBLE | Chemicals weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_che_qan_score | DOUBLE | Chemicals weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_che_qal_cat | INT | Chemicals weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_che_qal_label | STRING | Chemicals weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_che_qal_raw | DOUBLE | Chemicals weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_che_qal_score | DOUBLE | Chemicals weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_che_rrr_cat | INT | Chemicals weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_che_rrr_label | STRING | Chemicals weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_che_rrr_raw | DOUBLE | Chemicals weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_che_rrr_score | DOUBLE | Chemicals weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_che_tot_cat | INT | Chemicals weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_che_tot_label | STRING | Chemicals weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_che_tot_raw | DOUBLE | Chemicals weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_che_tot_score | DOUBLE | Chemicals weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_con_qan_cat | INT | Construction materials weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_con_qan_label | STRING | Construction materials weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_con_qan_raw | DOUBLE | Construction materials weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_con_qan_score | DOUBLE | Construction materials weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_con_qal_cat | INT | Construction materials weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_con_qal_label | STRING | Construction materials weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_con_qal_raw | DOUBLE | Construction materials weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_con_qal_score | DOUBLE | Construction materials weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_con_rrr_cat | INT | Construction materials weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_con_rrr_label | STRING | Construction materials weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_con_rrr_raw | DOUBLE | Construction materials weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_con_rrr_score | DOUBLE | Construction materials weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_con_tot_cat | INT | Construction materials weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_con_tot_label | STRING | Construction materials weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_con_tot_raw | DOUBLE | Construction materials weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_con_tot_score | DOUBLE | Construction materials weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_elp_qan_cat | INT | Electric power weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_elp_qan_label | STRING | Electric power weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_elp_qan_raw | DOUBLE | Electric power weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_elp_qan_score | DOUBLE | Electric power weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_elp_qal_cat | INT | Electric power weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_elp_qal_label | STRING | Electric power weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_elp_qal_raw | DOUBLE | Electric power weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_elp_qal_score | DOUBLE | Electric power weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_elp_rrr_cat | INT | Electric power weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_elp_rrr_label | STRING | Electric power weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_elp_rrr_raw | DOUBLE | Electric power weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_elp_rrr_score | DOUBLE | Electric power weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_elp_tot_cat | INT | Electric power weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_elp_tot_label | STRING | Electric power weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_elp_tot_raw | DOUBLE | Electric power weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_elp_tot_score | DOUBLE | Electric power weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_fnb_qan_cat | INT | Food & beverage weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_fnb_qan_label | STRING | Food & beverage weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_fnb_qan_raw | DOUBLE | Food & beverage weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_fnb_qan_score | DOUBLE | Food & beverage weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_fnb_qal_cat | INT | Food & beverage weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_fnb_qal_label | STRING | Food & beverage weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_fnb_qal_raw | DOUBLE | Food & beverage weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_fnb_qal_score | DOUBLE | Food & beverage weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_fnb_rrr_cat | INT | Food & beverage weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_fnb_rrr_label | STRING | Food & beverage weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_fnb_rrr_raw | DOUBLE | Food & beverage weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_fnb_rrr_score | DOUBLE | Food & beverage weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_fnb_tot_cat | INT | Food & beverage weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_fnb_tot_label | STRING | Food & beverage weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_fnb_tot_raw | DOUBLE | Food & beverage weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_fnb_tot_score | DOUBLE | Food & beverage weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_min_qan_cat | INT | Mining weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_min_qan_label | STRING | Mining weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_min_qan_raw | DOUBLE | Mining weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_min_qan_score | DOUBLE | Mining weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_min_qal_cat | INT | Mining weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_min_qal_label | STRING | Mining weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_min_qal_raw | DOUBLE | Mining weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_min_qal_score | DOUBLE | Mining weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_min_rrr_cat | INT | Mining weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_min_rrr_label | STRING | Mining weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_min_rrr_raw | DOUBLE | Mining weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_min_rrr_score | DOUBLE | Mining weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_min_tot_cat | INT | Mining weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_min_tot_label | STRING | Mining weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_min_tot_raw | DOUBLE | Mining weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_min_tot_score | DOUBLE | Mining weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_ong_qan_cat | INT | Oil & gas weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_ong_qan_label | STRING | Oil & gas weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_ong_qan_raw | DOUBLE | Oil & gas weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_ong_qan_score | DOUBLE | Oil & gas weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_ong_qal_cat | INT | Oil & gas weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_ong_qal_label | STRING | Oil & gas weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_ong_qal_raw | DOUBLE | Oil & gas weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_ong_qal_score | DOUBLE | Oil & gas weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_ong_rrr_cat | INT | Oil & gas weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_ong_rrr_label | STRING | Oil & gas weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_ong_rrr_raw | DOUBLE | Oil & gas weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_ong_rrr_score | DOUBLE | Oil & gas weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_ong_tot_cat | INT | Oil & gas weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_ong_tot_label | STRING | Oil & gas weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_ong_tot_raw | DOUBLE | Oil & gas weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_ong_tot_score | DOUBLE | Oil & gas weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_smc_qan_cat | INT | Semiconductor weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_smc_qan_label | STRING | Semiconductor weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_smc_qan_raw | DOUBLE | Semiconductor weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_smc_qan_score | DOUBLE | Semiconductor weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_smc_qal_cat | INT | Semiconductor weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_smc_qal_label | STRING | Semiconductor weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_smc_qal_raw | DOUBLE | Semiconductor weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_smc_qal_score | DOUBLE | Semiconductor weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_smc_rrr_cat | INT | Semiconductor weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_smc_rrr_label | STRING | Semiconductor weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_smc_rrr_raw | DOUBLE | Semiconductor weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_smc_rrr_score | DOUBLE | Semiconductor weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_smc_tot_cat | INT | Semiconductor weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_smc_tot_label | STRING | Semiconductor weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_smc_tot_raw | DOUBLE | Semiconductor weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_smc_tot_score | DOUBLE | Semiconductor weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_tex_qan_cat | INT | Textile weighting scheme is used to aggregate the category for the physical risk quantity group  
w_awr_tex_qan_label | STRING | Textile weighting scheme is used to aggregate the label for the physical risk quantity group  
w_awr_tex_qan_raw | DOUBLE | Textile weighting scheme is used to aggregate the raw value for the physical risk quantity group  
w_awr_tex_qan_score | DOUBLE | Textile weighting scheme is used to aggregate the score for the physical risk quantity group  
w_awr_tex_qal_cat | INT | Textile weighting scheme is used to aggregate the category for the physical risk quality group  
w_awr_tex_qal_label | STRING | Textile weighting scheme is used to aggregate the label for the physical risk quality group  
w_awr_tex_qal_raw | DOUBLE | Textile weighting scheme is used to aggregate the raw value for the physical risk quality group  
w_awr_tex_qal_score | DOUBLE | Textile weighting scheme is used to aggregate the score for the physical risk quality group  
w_awr_tex_rrr_cat | INT | Textile weighting scheme is used to aggregate the category for the regulatory and reputational risk group  
w_awr_tex_rrr_label | STRING | Textile weighting scheme is used to aggregate the label for the regulatory and reputational risk group  
w_awr_tex_rrr_raw | DOUBLE | Textile weighting scheme is used to aggregate the raw value for the regulatory and reputational risk group  
w_awr_tex_rrr_score | DOUBLE | Textile weighting scheme is used to aggregate the score for the regulatory and reputational risk group  
w_awr_tex_tot_cat | INT | Textile weighting scheme is used to aggregate the category for the total, overall water risk group  
w_awr_tex_tot_label | STRING | Textile weighting scheme is used to aggregate the label for the total, overall water risk group  
w_awr_tex_tot_raw | DOUBLE | Textile weighting scheme is used to aggregate the raw value for the total, overall water risk group  
w_awr_tex_tot_score | DOUBLE | Textile weighting scheme is used to aggregate the score for the total, overall water risk group  
w_awr_def_tot_weight_fraction | DOUBLE | Default weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_agr_tot_weight_fraction | DOUBLE | Agriculture weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_che_tot_weight_fraction | DOUBLE | Chemicals weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_con_tot_weight_fraction | DOUBLE | Construction materials weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_elp_tot_weight_fraction | DOUBLE | Electric power weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_fnb_tot_weight_fraction | DOUBLE | Food & beverage weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_min_tot_weight_fraction | DOUBLE | Mining weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_ong_tot_weight_fraction | DOUBLE | Oil & gas weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_smc_tot_weight_fraction | DOUBLE | Semiconductor weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
w_awr_tex_tot_weight_fraction | DOUBLE | Textile weighting scheme is used to aggregate the weight fraction for the total, overall water risk group  
**Terms of Use**
The WRI datasets are available without restriction on use or distribution. WRI does request that the user give proper attribution and identify WRI, where applicable, as the source of the data. For more information check [WRI's open data commitment](https://www.wri.org/data/open-data-commitment),
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual#code-editor-javascript-sample) More
```
vardataset=
ee.FeatureCollection('WRI/Aqueduct_Water_Risk/V4/baseline_annual');
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
returnsetColor(f,'bws_cat',-1,4,reds);
};
varwaterLand=ee.Image('NOAA/NGDC/ETOPO1').select('bedrock').gt(0.0);
varwaterLandBackground=
waterLand.visualize({palette:['cadetblue','lightgray']});
Map.addLayer(waterLandBackground);
// Baseline water stress
varpolygons=dataset.filter('bws_cat > -2').map(bws_cat_style);
Map.setCenter(10,20,4);
Map.addLayer(polygons.style({styleProperty:'style',pointSize:3}));
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_annual)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer(
'WRI/Aqueduct_Water_Risk/V4/baseline_annual_FeatureView');
varvisParams={
isVisible:false,
pointSize:20,
rules:[{
// Baseline water stress with low category
filter:ee.Filter.eq('bws_cat',-1),
isVisible:true,
pointFillColor:{
property:'bws_cat',
mode:'linear',
palette:['f1eef6','d7b5d8','df65b0','ce1256'],
min:-1,
max:100
}
}]
};
fvLayer.setVisParams(visParams);
fvLayer.setName('Low Water Stress');
Map.setCenter(-10,25,5);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WRI/WRI_Aqueduct_Water_Risk_V4_baseline_annual_FeatureView)
[ WRI Aqueduct Baseline Annual Version 4.0 ](https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual)
Aqueduct 4.0 is the latest iteration of WRI's water risk framework designed to translate complex hydrological data into intuitive indicators of water related risk. This dataset has curated 13 water risk indicators for quantity, quality and reputational concerns into a comprehensive framework. For 5 of the 13 indicators, a global …
WRI/Aqueduct_Water_Risk/V4/baseline_annual, aqueduct,flood,monitoring,surface-ground-water,table,wri 
2010-01-01T00:00:00Z/2080-12-31T23:59:59Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.wri.org/data/aqueduct-global-maps-40-data)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Water_Risk_V4_baseline_annual)


