 
#  LUCAS Harmonized (Theoretical Location, 2006-2018) V1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![JRC/LUCAS_HARMO/THLOC/V1](https://developers.google.com/earth-engine/datasets/images/JRC/JRC_LUCAS_HARMO_THLOC_V1_sample.png) 

Dataset Availability
    2006-02-05T00:00:00Z–2019-03-14T00:00:00Z 

Dataset Provider
     [ Joint Research Center, Unit D5 ](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUCAS/LUCAS_harmonised/) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("JRC/LUCAS_HARMO/THLOC/V1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_LUCAS_HARMO_THLOC_V1)      FeatureView  `    ui.Map.FeatureViewLayer("JRC/LUCAS_HARMO/THLOC/V1_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_LUCAS_HARMO_THLOC_V1_FeatureView) 

Tags
     [eu](https://developers.google.com/earth-engine/datasets/tags/eu) [jrc](https://developers.google.com/earth-engine/datasets/tags/jrc) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landuse](https://developers.google.com/earth-engine/datasets/tags/landuse) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [lucas](https://developers.google.com/earth-engine/datasets/tags/lucas) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#citations) More
The [Land Use/Cover Area frame Survey (LUCAS)](https://ec.europa.eu/eurostat/web/lucas) in the European Union (EU) was set up to provide statistical information. It represents a triennial in-situ landcover and land-use data-collection exercise that extends over the whole of the EU's territory. LUCAS collects information on land cover and land use, agro-environmental variables, soil, and grassland. The surveys also provide spatial information to analyse the mutual influences between agriculture, environment, and countryside, such as irrigation and land management.
The dataset presented here is the harmonized version of all yearly LUCAS surveys with a total of 106 attributes. Each point's location is using the fields 'th_lat' and 'th_lon', that is, the LUCAS theoretical location (THLOC), as prescribed by the LUCAS grid. For more information please see Citations. Note that not every field is present for every year - see the "Years" section in property descriptions.
The text "C1 (Instructions)" in the table schema descriptions refers to [this document](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUCAS/LUCAS_harmonised/3_supporting/LUCAS2018-C1-Instructions.pdf).
See also [the 2018 LUCAS polygons dataset](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_COPERNICUS_POLYGONS_V1_2018).
**Table Schema**
Name | Type | Description  
---|---|---  
id | INT | Unique row identifier. Source: Added by harmonization process  
point_id | INT | 8-digit unique point identifier, point ID according to the LUCAS grid. Such a point ID can either be part or not of a particular yearly LUCAS survey. Source: C1(Instructions), p.141, sec.9.1.1 Years: all  
year | INT | Year of survey. Source: Added by harmonization process Years: all  
nuts0 | STRING | NUTS 2016 Level 0. Years: all  
nuts1 | STRING | NUTS 2016 Level 1. Years: all  
nuts2 | STRING | NUTS 2016 Level 2. Years: all  
nuts3 | STRING | NUTS 2016 Level 3. Years: 2018  
office_pi | STRING | Whether photo-interpretation has happened in the office for this LUCAS point. If true, then this point_id was not visited by an inspector for this year. Values:
  * true
  * false

Source: C1(Instructions), p.141, sec.9.1.1 Years: 2015, 2018  
ex_ante | STRING | Ex-ante points are points that are parts of the in-situ sample and in principle have to be visited in the field, although there are a posteriori reasons why this is impossible. If true, then this point_id was not visited by an inspector for this year. Values:
  * true
  * false

Source: C1(Instructions), p.16, sec 8.1; C1(Instructions), p.141, sec.9.1.1 Years: 2018  
survey_date | STRING | Date on which the survey was carried out in the format dd/mm/yy Years: all  
car_latitude | DOUBLE | Latitude (WGS84) on which the car was parked. Source: C1(Instructions), p.141, sec.9.1.2 Years: 2018  
car_ew | STRING | GPS Car parking East/West compass setting. Used for knowing when to add a minus to the respective coordinate. Values:
  * East
  * West
  * empty if not relevant

Years: 2018  
car_longitude | DOUBLE | Longitude (WGS84) on which the car was parked. Source: C1(Instructions), p.142, sec.9.1.2 Years: 2018  
gps_proj | STRING | GPS projection. Values:
  * WGS84
  * No GPS signal
  * empty if not relevant

Source: C1(Instructions), p.142, sec.9.1.2 Years: all  
gps_prec | DOUBLE | Average location error as given by GPS receiver (in meters). Source: C1(Instructions), p.142, sec.9.1.2 Years: all  
gps_altitude | DOUBLE | Elevation in m above sea level. Source: C1(Instructions), p.141, sec.9.1.1 Years: 2009, 2012, 2015, 2018  
gps_lat | DOUBLE | GPS latitude of the location from which observation is actually done (WGS84) measured in degrees. Source: C1(Instructions), p.142, sec.9.1.2 Years: all  
gps_ew | STRING | East-west encoding setting for GPS. Values:
  * East
  * West
  * empty if not relevant

Years: all  
gps_long | DOUBLE | GPS longitude of the location from which observation is actually done (WGS84) measured in degrees. Source: C1(Instructions), p.142, sec.9.1.2 Years: all  
obs_dist | DOUBLE | Distance between observation location and the LUCAS point as provided by the GPS receiver (in meters). Years: all  
obs_direct | STRING | Direction of the observation. Values:
  * On the point: Point regularly observed
  * Look to the North: "Look to the North" rule is applied id the point is located on a boundary/ e.g., or a small linear feature (<3 m wide)
  * Look to the East: "Look to the East" rule is applied if he point is located on a boundary/e.g., or a small linear feature (<3 m wide)
  * empty if not relevant

Source: C1(Instructions), p.144, sec.9.1.4 Years: all  
obs_type | STRING | The method of observation for the relevant point. For the availability of LUCAS photos according to obs_type, please check C1(Instructions), sec. 8.15.3. Values:
  * In situ < 100 m
  * In situ > 100 m
  * In situ PI
  * In situ PI not possible
  * Out of national territory
  * In office PI
  * Marine Sea
  * (only 2015)

Find more details check the documentation. Source: C1(Instructions), p.142-144, sec.9.1.4 Years: all  
letter_group | STRING | Which letter group (top tier classification) from the C3 document is the point assigned to. Source: Added by harmonization process Years: all  
lc1 | STRING | Coding of land cover according to harmonized C3 classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: all  
lc1_label | STRING | Label of land cover according to harmonized C3 document. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lc1_spec | STRING | Coding of land cover species according to harmonized C3 classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: 2009, 2012, 2015, 2018  
lc1_spec_label | STRING | Label of land cover species according to harmonized C3 document. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lc1_perc | STRING | The percentage that the assigned land cover type (lc1) occupies on the ground. Values:
  * < 10 %
  * 10 - 25 %
  * 25 - 50 %
  * 50 - 75 %
  * > 75 %
  * empty if not relevant

This coding applies only for the years 2009-2015 . For 2018 the number represents the percentage of land-cover (0-100). The variable does not exist for 2006 Years: 2009, 2012, 2015, 2018  
lc2 | STRING | Coding of land cover according to harmonized C3 classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: all  
lc2_label | STRING | Label of land cover according to harmonized C3 document. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lc2_spec | STRING | Coding of land cover species according to harmonized C3 classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: 2009, 2012, 2015, 2018  
lc2_spec_label | STRING | Label of land cover species according to harmonized C3 document. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lc2_perc | STRING | The percentage that the assigned land cover type (lc2) occupies on the ground. Values:
  * < 10 %
  * 10 - 25 %
  * 25 - 50 %
  * 50 - 75 %
  * > 75 %
  * empty if not relevant

This coding applies only for the years 2009-2015 . For 2018 the number represents the percentage of land-cover (0-100). The variable does not exist for 2006 Years: 2009, 2012, 2015, 2018  
lu1 | STRING | Coding of the land use according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: all  
lu1_label | STRING | Label of the land use according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lu1_type | STRING | Coding of the land use types according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: 2015, 2018  
lu1_type_label | STRING | Label of the land use types according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lu1_perc | STRING | The percentage that the assigned land use type (lu1) occupies on the ground. Values:
  * < 5 %
  * 5 - 10 %
  * 10 - 25 %
  * 25 - 50 %
  * 50 - 75 %
  * 75 - 90 %
  * > 90 %
  * Not Relevant

This coding applies only for the year 2015. For 2018 the number represents the percentage of land-cover (0-100). The variable does not exist for 2006, 2009 and 2012. Years: 2015, 2018  
lu2 | STRING | Coding of the land use according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: all  
lu2_label | STRING | Label of the land use according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lu2_type | STRING | Coding of the land use types according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document Years: 2015, 2018  
lu2_type_label | STRING | Label of the land use types according to Harmonized C3 document classification. Coding and label translation can be found in the [supporting docs](https://figshare.com/s/e6cab3bceaa9a2299237) in file _c3_legends_new.csv_. Source: Harmonized C3 document  
lu2_perc | STRING | The percentage that the assigned land use type (lu2) occupies on the ground. Values:
  * < 5 %
  * 5 - 10 %
  * 10 - 25 %
  * 25 - 50 %
  * 50 - 75 %
  * 75 - 90 %
  * > 90 %
  * Not Relevant

This coding applies only for the year 2015. For 2018 the number represents the percentage of land-cover (0-100). The variable does not exist for 2006, 2009 and 2012. Years: 2015, 2018  
parcel_area_ha | STRING | Size of the surveyed parcel in hectares. Values:
  * < 0.5
  * 0.5 - 1
  * 1 - 10
  * > 10
  * empty if not relevant

Source: C1(Instructions), p.50, sec.8.4.15 Years: 2009, 2012, 2015, 2018  
tree_height_maturity | STRING | Height of trees at maturity. Values:
  * < 5 m
  * > 5 m
  * Not identifiable
  * empty if not relevant

Source: C1(Instructions), p.147, sec.9.1.6 Years: 2012, 2015, 2018  
tree_height_survey | STRING | Height of trees at the moment of survey. Values:
  * < 5 m
  * > 5 m
  * Not identifiable
  * empty if not relevant

Source: C1(Instructions), p.147, sec.9.1.6 Years: 2009, 2012, 2015, 2018  
feature_width | STRING | Width of the feature. Values:
  * < 20 m
  * > 20 m
  * Not identifiable
  * empty if not relevant

Source: C1(Instructions), p.147, sec.9.1.6 Years: 2009, 2012, 2015, 2018  
lm_stone_walls | STRING | Presence of stone walls on the plot. Values:
  * No
  * Stone wall not maintained
  * Stone wall well maintained
  * empty if not relevant

Source: C1(Instructions), p.148, sec.9.1.7 Years: 2018  
crop_residues | STRING | Presence of crop residues on the plot. Values:
  * true
  * false

Source: C1(Instructions), p.51, sec.8.6 Years: 2018  
lm_grass_margins | STRING | Presence of grass margins on the plot. Values:
  * No
  * < 1 m width
  * > 1 m width
  * empty if not relevant

Source: C1(Instructions), p.148, sec.9.1.7 Years: 2018  
grazing | STRING | Signs of grazing on the plot. Values:
  * Signs of grazing
  * No signs of grazing
  * empty if not relevant

Source: C1(Instructions), p.148, sec.9.1.8 Years: 2009, 2012, 2015, 2018  
special_status | STRING | Whether the plot is a part of any specially regulated area. Values:
  * Protected
  * Hunting
  * Protected and hunting
  * No special status
  * empty if not relevant

Source: C1(Instructions), p.149, sec.9.1.8 Years: 2012, 2015, 2018  
lc_lu_special_remark | STRING | Any special remarks on the land cover / land use. Values:
  * Harvested field
  * Tilled/sowed
  * Clear cut
  * Burnt area
  * Fire break
  * Nursery
  * Dump site
  * Temporary dry
  * Temporary flooded
  * No remark
  * empty if not relevant

For more details check the documentation. Source: C1(Instructions), p.149-150, sec.9.1.8 Years: 2012, 2015, 2018  
cprn_cando | STRING | Whether a Copernicus survey can be done on this point. For more information on the Copernicus module and the data created please refer to [d'Andrimont et al, 2021](https://essd.copernicus.org/articles/13/1119/2021/). Values:
  * true
  * false

Source: C1(Instructions), p.58, sec.8.8.1, C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc | STRING | The land cover on the Copernicus points according to the classification scheme at level2. Source: Harmonized C3 document Years: 2018  
cprn_lc_label | STRING | Label of land cover on the Copernicus points according to the classification scheme at level2. Source: Harmonized C3 document  
cprn_lc1n | DOUBLE | The extent (in meters) to which the land cover of the Copernicus point stays the same in direction North. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprnc_lc1e | DOUBLE | The extent (in meters) to which the land cover of the Copernicus point stays the same in direction East. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprnc_lc1s | DOUBLE | The extent (in meters) to which the land cover of the Copernicus point stays the same in direction South. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprnc_lc1w | DOUBLE | The extent (in meters) to which the land cover of the Copernicus point stays the same in direction West. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc1n_brdth | DOUBLE | The breath (in %) to the next Copernicus land cover in direction North. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc1e_brdth | DOUBLE | The breath (in %) to the next Copernicus land cover in direction East. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc1s_brdth | DOUBLE | The breath (in %) to the next Copernicus land cover in direction South. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc1w_brdth | DOUBLE | The breath (in %) to the next Copernicus land cover in direction West. Source: C1(Instructions), p.150, sec.9.1.9 Years: 2018  
cprn_lc1n_next | STRING | The recorded next land cover if a land cover change (LUCAS land cover level 2) occurs within 50m in direction North, regardless of the fact that the next land cover is visible on the landscape photo or not. Any feature less than 3m wide is not taken into account and is not considered a land cover change. Source: Harmonized C3 document Years: 2018  
cprn_lc1s_next | STRING | The recorded next land cover if a land cover change (LUCAS land cover level 2) occurs within 50m in direction South, regardless of the fact that the next land cover is visible on the landscape photo or not. Any feature less than 3m wide is not taken into account and is not considered a land cover change. Source: Harmonized C3 document Years: 2018  
cprn_lc1e_next | STRING | The recorded next land cover if a land cover change (LUCAS land cover level 2) occurs within 50m in direction East, regardless of the fact that the next land cover is visible on the landscape photo or not. Any feature less than 3m wide is not taken into account and is not considered a land cover change. Source: Harmonized C3 document Years: 2018  
cprn_lc1w_next | STRING | The recorded next land cover if a land cover change (LUCAS land cover level 2) occurs within 50m in direction West, regardless of the fact that the next land cover is visible on the landscape photo or not. Any feature less than 3m wide is not taken into account and is not considered a land cover change. Source: Harmonized C3 document Years: 2018  
cprn_urban | STRING | Whether the Copernicus point located in an urban area. Values:
  * true
  * false

Source: C1(Instructions), p.151, sec.9.1.10.1 Years: 2018  
cprn_impervious_perc | DOUBLE | Percentage of impervious surfaces. Source: C1(Instructions), p.151, sec.9.1.10.1 Years: 2018  
inspire_plcc1 | DOUBLE | Percentage of coniferous trees. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc2 | DOUBLE | Percentage of broadleaved trees. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc3 | DOUBLE | Percentage of shrubs. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc4 | DOUBLE | Percentage of herbaceous plants. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc5 | DOUBLE | Percentage of lichens and mosses. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc6 | DOUBLE | Percentage of consolidated (bare) surface (e.g., rock outcrops). Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc7 | DOUBLE | Percentage of unconsolidated (bare) surface (e.g., sand). Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
inspire_plcc8 | DOUBLE | Difference between the sum of all inspire persentage classes and 100%. Source: C1(Instructions), p.151, sec.9.1.10.2 Years: 2015, 2018  
eunis_complex | STRING | EUNIS habitat classification. Values:
  * X06
  * X09
  * Other
  * Unknown
  * empty if not relevant

Source: C1(Instructions), p.152, sec.9.1.11 Years: 2018  
grassland_sample | STRING | Whether the point is a part of the grassland module. Values:
  * true
  * false

Source: C1(Instructions), p.152, sec.9.1.12 Years: 2018  
grass_cando | STRING | Whether a grassland survey is possible. Values:
  * true
  * false

Source: C1(Instructions), p.152, sec.9.1.12 Years: 2018  
wm | STRING | Type of water management present at the point. Values:
  * Irrigation
  * Potential irrigation
  * Drainage
  * Irrigation and drainage
  * No visible water management
  * empty if not relevant

Source: C1(Instructions), p.162, sec.9.1.13 Years: 2009, 2012, 2015, 2018  
wm_source | STRING | Source of the irrigation at the point. Values:
  * Combo - Other/Not Identifiable + Well
  * Combo - Other/Not Identifiable + Pond/Lake/Reservoir
  * Combo - Other/Not Identifiable + Stream/Canal/Ditch
  * Combo - Other/Not Identifiable + Lagoon/Wastewater
  * Combo - Pond/Lake/Reservoir + Stream/Canal/Ditch
  * Lagoon/Wastewater
  * Pond/Lake/Reservoir
  * Stream/Canal/Ditch
  * Well
  * Other/Not Identifiable
  * empty if not relevant

Combo classes exist only for 2009 and were later discontinued. For more details check the documentation. Source: C1(Instructions), p.163, sec.9.1.13 Years: 2009  
wm_type | STRING | The type of irrigation present at the point. Values:
  * Gravity
  * Pressure: Sprinkle irrigation
  * Pressure: Micro-irrigation
  * Gravity/Pressure
  * Other/Non identifiable
  * Combo - Pressure: Sprinkle irrigation + Pressure: Micro-irrigation
  * Combo - Gravity/Pressure + Gravity
  * Combo - Pressure: Sprinkle irrigation + Gravity/Pressure
  * Combo - Pressure: Micro-irrigation + Gravity/Pressure
  * Other/not identifiable
  * Combo - Other/Non identifiable + Gravity
  * Combo - Other/Non identifiable + Gravity/Pressure
  * Combo - Other/Non identifiable + Gravity/Pressure + Pressure: Micro-irrigation
  * empty if not relevant

Combo classes exist only for 2009 and were later discontinued. For more details check the documentation. Source: C1(Instructions), p.162-163, sec.9.1.13 Years: 2009  
wm_delivery | STRING | The irrigation delivery system at the point. Values:
  * Canal
  * Combo - Pipeline + Ditch
  * Combo - Other/Non identifiable + Ditch
  * Combo - Other/Non identifiable + Pipeline
  * Ditch
  * Pipeline
  * Other/Non identifiable
  * Other/Non identifiable + Canal
  * empty if not relevant

Combo classes exist only for 2009 and were later discontinued. For more details check the documentation. Source: C1(Instructions), p.163-164, sec.9.1.13 Years: 2009  
erosion_cando | STRING | Whether a point is foreseen for assessing erosion (true) or not (false). Values:
  * true
  * false

Source: C1(Instructions), p.168, sec.9.1.15 Years: 2018  
soil_stones_perc | STRING | Percentage of stones on the surface (does not include stones covered by soil). Values:
  * < 10 %
  * 10 - 25 %
  * 25 - 50 %
  * > 50 %
  * empty if not relevant

This coding applies only for the years 2009-2015 . For 2018 the number represents the percentage of stones on the surface (0-100). The variable does not exist for 2006. Source: C1(Instructions), p.164, sec.9.1.14.2 Years: 2009, 2012, 2015, 2018  
bio_sample | STRING | Whether the point a biodiversity sample point. Values:
  * true
  * false

Years: 2018  
soil_bio_taken | STRING | Whether a soil-biodiversity sample was taken. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
bulk0_10_sample | STRING | Whether a point is foreseen for collecting the bulk density between the given range. Values:
  * false
  * true

Years: 2018  
soil_blk_0_10_taken | STRING | Whether the soil sample between the given range was taken. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
bulk10_20_sample | STRING | Whether a point is foreseen for collecting the bulk density between the given range. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
soil_blk_10_20_taken | STRING | Whether the soil sample between the given range was taken. Values:
  * Yes
  * No

Source: C1(Instructions) Years: 2018  
bulk20_30_sample | STRING | Whether a point is foreseen for collecting the bulk density between the given range. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
soil_blk_20_30_taken | STRING | Whether the soil sample between the given range was taken. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
standard_sample | STRING | Whether the point is a standard soil point. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
soil_std_taken | STRING | Whether the standard soil sample was taken. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
organic_sample | STRING | Whether the point is an organic sample point. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
soil_org_depth_cando | STRING | Whether depth can be evaluated. Values:
  * true
  * false

Source: C1(Instructions) Years: 2018  
soil_taken | STRING | Has a soil sample been taken (before 2018). Values:
  * Yes
  * Not possible
  * No, already taken
  * No sample required
  * empty if not relevant

Source: C1(Instructions) Years: 2009, 2012, 2015  
soil_crop | STRING | Percentage of residual crop. Values:
  * < 10 %
  * 10 - 25 %
  * 25 - 50 %
  * > 50 %
  * empty if not relevant

Source: C1(Instructions) Years: 2009, 2012, 2015  
photo_point | STRING | Whether a photo on the point was taken. Values:
  * Photo taken
  * Photo not taken
  * empty if not relevant

Source: C1(Instructions) Years: all  
photo_north | STRING | Whether a photo looking north was taken. Values:
  * Photo taken
  * Photo not taken
  * empty if not relevant

Source: C1(Instructions) Years: all  
photo_south | STRING | Whether a photo looking south was taken. Values:
  * Photo taken
  * Photo not taken
  * empty if not relevant

Source: C1(Instructions) Years: all  
photo_east | STRING | Whether a photo looking east was taken. Values:
  * Photo taken
  * Photo not taken
  * empty if not relevant

Source: C1(Instructions) Years: all  
photo_west | STRING | Whether a photo looking west been taken. Values:
  * Photo taken
  * Photo not taken
  * empty if not relevant

Source: C1(Instructions) Years: all  
transect | STRING | The changes in land cover as recorded by the east-facing transect line. Years: 2009, 2012, 2015  
revisit | DOUBLE | Number of visits to the point throughout the survey years. Source: Added by harmonization process  
th_gps_dist | DOUBLE | Calculated distance between theoretical and recorded location. Source: Added by harmonization process  
file_path_gisco_north | STRING | File path to north-facing photo as stored on ESTAT GISCO sever. Source: Added by harmonization process Years: all  
file_path_gisco_south | STRING | File path to south-facing photo as stored on ESTAT GISCO sever. Source: Added by harmonization process Years: all  
file_path_gisco_east | STRING | File path to east-facing photo as stored on ESTAT GISCO sever. Source: Added by harmonization process Years: all  
file_path_gisco_west | STRING | File path to west-facing photo as stored on ESTAT GISCO sever. Source: Added by harmonization process Years: all  
file_path_gisco_point | STRING | File path to point-facing photo as stored on ESTAT GISCO sever. Source: Added by harmonization process Years: all  
obs_radius | DOUBLE | The radius of observation - whether the near or the extended window of observation is applied. Values:
  * 1.5
  * 20
  * null if not relevant

Source: C1(Instructions) Years: 2006, 2009, 2012, 2015  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * d'Andrimont, R., Yordanov, M., Martinez-Sanchez, L. et al. Harmonised LUCAS in-situ land cover and use database for field surveys from 2006 to 2018 in the European Union. Sci Data 7, 352 (2020). [doi:10.1038/s41597-020-00675-z](https://doi.org/10.1038/s41597-020-00675-z)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('JRC/LUCAS_HARMO/THLOC/V1');
// For the Inspector
Map.addLayer(dataset,{},'LUCAS Points (data)',false);
dataset=dataset.style({
color:'489734',
pointSize:3,
});
Map.setCenter(-3.8233,40.609,10);
Map.addLayer(dataset,{},'LUCAS Points (styled green)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_LUCAS_HARMO_THLOC_V1)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('JRC/LUCAS_HARMO/THLOC/V1_FeatureView');
varvisParams={
pointSize:8,
color:'808080',
pointFillColor:{
property:'inspire_plcc4',
mode:'linear',
palette:['ffffcc','c2e699','78c679','238443'],
min:0,
max:100
}
};
fvLayer.setVisParams(visParams);
fvLayer.setName('LUCAS herbaceous cover');
Map.setCenter(-3.8233,40.609,10);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JRC/JRC_LUCAS_HARMO_THLOC_V1_FeatureView)
[ LUCAS Harmonized (Theoretical Location, 2006-2018) V1 ](https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1)
The Land Use/Cover Area frame Survey (LUCAS) in the European Union (EU) was set up to provide statistical information. It represents a triennial in-situ landcover and land-use data-collection exercise that extends over the whole of the EU's territory. LUCAS collects information on land cover and land use, agro-environmental variables, soil, …
JRC/LUCAS_HARMO/THLOC/V1, eu,jrc,landcover,landuse,landuse-landcover,lucas,table 
2006-02-05T00:00:00Z/2019-03-14T00:00:00Z
34.307144 -13.359375 71.187754 34.804688 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUCAS/LUCAS_harmonised/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/JRC_LUCAS_HARMO_THLOC_V1)


