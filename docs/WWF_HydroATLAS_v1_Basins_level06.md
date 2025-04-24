 
#  WWF HydroATLAS Basins Level 06 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WWF/HydroATLAS/v1/Basins/level06](https://developers.google.com/earth-engine/datasets/images/WWF/WWF_HydroATLAS_v1_Basins_level06_sample.png) 

Dataset Availability
    2000-02-22T00:00:00Z–2000-02-22T00:00:00Z 

Dataset Provider
     [ WWF ](https://www.hydrosheds.org/) 

Earth Engine Snippet
     `    ee.FeatureCollection("WWF/HydroATLAS/v1/Basins/level06")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroATLAS_v1_Basins_level06) 

Tags
     [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [hydroatlas](https://developers.google.com/earth-engine/datasets/tags/hydroatlas) [hydrography](https://developers.google.com/earth-engine/datasets/tags/hydrography) [hydrology](https://developers.google.com/earth-engine/datasets/tags/hydrology) [hydrosheds](https://developers.google.com/earth-engine/datasets/tags/hydrosheds) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [table](https://developers.google.com/earth-engine/datasets/tags/table) [water](https://developers.google.com/earth-engine/datasets/tags/water) [watershed](https://developers.google.com/earth-engine/datasets/tags/watershed) [wwf](https://developers.google.com/earth-engine/datasets/tags/wwf)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06#citations) More
BasinATLAS is a component of the [HydroATLAS database](https://www.hydrosheds.org/page/hydroatlas), which is a component of [HydroSHEDS](https://www.hydrosheds.org).
BasinATLAS provides a standardized compendium of hydro-environmental attribute information for all watersheds of the world at high spatial resolution. This dataset includes data for 56 variables, partitioned into 281 attributes and organized in six categories: hydrology; physiography; climate; land cover & use; soils & geology; and anthropogenic influences (see Table 1 in the HydroATLAS documentation linked below).
Watersheds range from level 1 (coarse) to level 12 (detailed), using Pfastetter codes. The underlying watershed deleniation uses the NASA SRTM Digital Elevatin Map (DEM) below 60oN latitude and the USGS HYDRO1k DEM above 60oN.
Technical documentation:
<https://www.hydrosheds.org/images/inpages/HydroATLAS_TechDoc_v10.pdf>
Note that the quality of HydroATLAS data is significantly lower for regions above 60 degrees northern latitude as there is no underlying SRTM elevation data available and thus a coarser-resolution DEM was used (HYDRO1k provided by USGS).
HydroSHEDS was developed by the World Wildlife Fund (WWF) Conservation Science Program in partnership with the U.S. Geological Survey, the International Centre for Tropical Agriculture, The Nature Conservancy, and the Center for Environmental Systems Research of the University of Kassel, Germany.
**Table Schema**
Name | Type | Description  
---|---|---  
HYBAS_ID | INT | First 1 digit represents the region: * 1 = Africa * 2 = Europe * 3 = Siberia * 4 = Asia * 5 = Australia * 6 = South America * 7 = North America * 8 = Arctic (North America) * 9 = Greenland. Next 2 digits define the Pfafstetter level (01-12). The value '00' is used for the 'Level 0' layer that contains all original sub-basins and all Pfafstetter codes (at all levels); 'Level 0' only exists in the standard format of HydroBASINS (without lakes). Next 6 digits represent a unique identifier within the HydroSHEDS network; values larger than 900,000 represent lakes and only occur in the customized format (with lakes) Last 1 digit indicates the side of a sub-basin in relation to the river network (0 = noSide; 1 = Left; 2 = Right). Sides are only defined for the customized format (with lakes).  
COAST | INT | Indicator for lumped coastal basins: 0 = no; 1 = yes. Coastal basins represent conglomerates of small coastal watersheds that drain into the ocean between larger river basins.  
DIST_MAIN | DOUBLE | Distance from polygon outlet to the most downstream sink, in km.  
DIST_SINK | DOUBLE | Distance from polygon outlet to the next downstream sink, in km.  
ENDO | INT | Indicator for endorheic (inland) basins without surface flow connection to the ocean: 0 = not part of an endorheic basin; 1 = part of an endorheic basin; 2 = sink (i.e. most downstream polygon) of an endorheic basin.  
MAIN_BAS | INT | Hybas_id of the most downstream sink, i.e. the outlet of the main river basin.  
NEXT_DOWN | INT | Hybas_id of the next downstream polygon.  
NEXT_SINK | INT | Hybas_id of the next downstream sink.  
PFAF_ID | INT | The Pfafstetter code.  
SORT | INT | Indicator showing the record number (sequence) in which the original polygons are stored in the shapefile (i.e. counting upwards from 1 in the original shapefile). The original polygons are sorted from downstream to upstream. This field can be used to sort the polygons back to their original sequence or to perform topological searches.  
SUB_AREA | DOUBLE | Area of basin, in square kilometers.  
UP_AREA | DOUBLE | Total upstream area, in square kilometers.  
aet_mm_s01 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
aet_mm_s02 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
aet_mm_s03 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
aet_mm_s04 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
aet_mm_s05 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
aet_mm_s06 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
aet_mm_s07 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
aet_mm_s08 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
aet_mm_s09 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
aet_mm_s10 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
aet_mm_s11 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
aet_mm_s12 | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
aet_mm_syr | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
aet_mm_uyr | INT | Actual Evapotranspiration: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
ari_ix_sav | INT | Global Aridity Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
ari_ix_uav | INT | Global Aridity Index: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
cls_cl_smj | INT | Climate Strata: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
cly_pc_sav | INT | Clay Fraction in Soil: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
cly_pc_uav | INT | Clay Fraction in Soil: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
clz_cl_smj | INT | Climate Zones: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
cmi_ix_s01 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
cmi_ix_s02 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
cmi_ix_s03 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
cmi_ix_s04 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
cmi_ix_s05 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
cmi_ix_s06 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
cmi_ix_s07 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
cmi_ix_s08 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
cmi_ix_s09 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
cmi_ix_s10 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
cmi_ix_s11 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
cmi_ix_s12 | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
cmi_ix_syr | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
cmi_ix_uyr | INT | Climate Moisture Index: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
crp_pc_sse | INT | Cropland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
crp_pc_use | INT | Cropland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
dis_m3_pmn | DOUBLE | Natural Discharge: Category = Hydrology; Spatial Extent = {p} at sub-bsin pour point; Dimensions = {mn} annual minimum  
dis_m3_pmx | DOUBLE | Natural Discharge: Category = Hydrology; Spatial Extent = {p} at sub-bsin pour point; Dimensions = {mx} annual maximum  
dis_m3_pyr | DOUBLE | Natural Discharge: Category = Hydrology; Spatial Extent = {p} at sub-bsin pour point; Dimensions = {yr} annual average  
dor_pc_pva | INT | Degree of Regulation: Category = Hydrology; Spatial Extent = {p} at sub-bsin pour point; Dimensions = {va} value  
ele_mt_sav | INT | Elevation: Category = Physiography; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
ele_mt_smn | INT | Elevation: Category = Physiography; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mn} minimum  
ele_mt_smx | INT | Elevation: Category = Physiography; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mx} maximum  
ele_mt_uav | INT | Elevation: Category = Physiography; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
ero_kh_sav | INT | Soil Erosion: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
ero_kh_uav | INT | Soil Erosion: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
fec_cl_smj | INT | Freshwater Ecoregions: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
fmh_cl_smj | INT | Freshwater Major Habitat Types: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
for_pc_sse | INT | Forest Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
for_pc_use | INT | Forest Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
gad_id_smj | INT | Global Administrative Areas: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
gdp_ud_sav | INT | Gross Domestic Product: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
gdp_ud_ssu | INT | Gross Domestic Product: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {su} sum  
gdp_ud_usu | INT | Gross Domestic Product: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
gla_pc_sse | INT | Glacier Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
gla_pc_use | INT | Glacier Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
glc_cl_smj | INT | Land Cover Classes: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
glc_pc_s01 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} % coverage: Tree Cover, broadleaved, evergreen  
glc_pc_s02 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} % coverage: Tree Cover, broadleaved, deciduous, closed  
glc_pc_s03 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} % coverage: Tree Cover, broadleaved, deciduous, open  
glc_pc_s04 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} % coverage: Tree Cover, needle-leaved, evergreen  
glc_pc_s05 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} % coverage: Tree Cover, needle-leaved, deciduous  
glc_pc_s06 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} % coverage: Tree Cover, mixed leaf type  
glc_pc_s07 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} % coverage: Tree Cover, regularly flooded, fresh water (& brackish)  
glc_pc_s08 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} % coverage: Tree Cover, regularly flooded, saline water  
glc_pc_s09 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} % coverage: Mosaic: Tree cover / Other natural vegetation  
glc_pc_s10 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} % coverage: Tree Cover, burnt  
glc_pc_s11 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} % coverage: Shrub Cover, closed-open, evergreen  
glc_pc_s12 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} % coverage: Shrub Cover, closed-open, deciduous  
glc_pc_s13 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {13} % coverage: Herbaceous Cover, closed-open  
glc_pc_s14 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {14} % coverage: Sparse Herbaceous or sparse Shrub Cover  
glc_pc_s15 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {15} % coverage: Regularly flooded Shrub and/or Herbaceous Cover  
glc_pc_s16 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {16} % coverage: Cultivated and managed areas  
glc_pc_s17 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {17} % coverage: Mosaic: Cropland / Tree Cover / Other natural vegetation  
glc_pc_s18 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {18} % coverage: Mosaic: Cropland / Shrub or Grass Cover  
glc_pc_s19 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {19} % coverage: Bare Areas  
glc_pc_s20 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {20} % coverage: Water Bodies  
glc_pc_s21 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {21} % coverage: Snow and Ice  
glc_pc_s22 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {22} % coverage: Artificial surfaces and associated areas  
glc_pc_u01 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {01} % coverage: Tree Cover, broadleaved, evergreen  
glc_pc_u02 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {02} % coverage: Tree Cover, broadleaved, deciduous, closed  
glc_pc_u03 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {03} % coverage: Tree Cover, broadleaved, deciduous, open  
glc_pc_u04 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {04} % coverage: Tree Cover, needle-leaved, evergreen  
glc_pc_u05 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {05} % coverage: Tree Cover, needle-leaved, deciduous  
glc_pc_u06 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {06} % coverage: Tree Cover, mixed leaf type  
glc_pc_u07 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {07} % coverage: Tree Cover, regularly flooded, fresh water (& brackish)  
glc_pc_u08 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {08} % coverage: Tree Cover, regularly flooded, saline water  
glc_pc_u09 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {09} % coverage: Mosaic: Tree cover / Other natural vegetation  
glc_pc_u10 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {10} % coverage: Tree Cover, burnt  
glc_pc_u11 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {11} % coverage: Shrub Cover, closed-open, evergreen  
glc_pc_u12 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {12} % coverage: Shrub Cover, closed-open, deciduous  
glc_pc_u13 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {13} % coverage: Herbaceous Cover, closed-open  
glc_pc_u14 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {14} % coverage: Sparse Herbaceous or sparse Shrub Cover  
glc_pc_u15 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {15} % coverage: Regularly flooded Shrub and/or Herbaceous Cover  
glc_pc_u16 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {16} % coverage: Cultivated and managed areas  
glc_pc_u17 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {17} % coverage: Mosaic: Cropland / Tree Cover / Other natural vegetation  
glc_pc_u18 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {18} % coverage: Mosaic: Cropland / Shrub or Grass Cover  
glc_pc_u19 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {19} % coverage: Bare Areas  
glc_pc_u20 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {20} % coverage: Water Bodies  
glc_pc_u21 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {21} % coverage: Snow and Ice  
glc_pc_u22 | INT | Land Cover Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {22} % coverage: Artificial surfaces and associated areas  
gwt_cm_sav | INT | Groundwater Table Depth: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
hdi_ix_sav | INT | Human Development Index: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
hft_ix_s09 | INT | Human Footprint: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} year 2009  
hft_ix_s93 | INT | Human Footprint: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {93} year 1993  
hft_ix_u09 | INT | Human Footprint: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {09} year 2009  
hft_ix_u93 | INT | Human Footprint: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {93} year 1993  
inu_pc_slt | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {lt} long-term maximum  
inu_pc_smn | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mn} annual minimum  
inu_pc_smx | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mx} annual maximum  
inu_pc_ult | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {lt} long-term maximum  
inu_pc_umn | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {mn} annual minimum  
inu_pc_umx | INT | Inundation Extent: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {mx} annual maximum  
ire_pc_sse | INT | Irrigated Area Extent (Equipped): Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
ire_pc_use | INT | Irrigated Area Extent (Equipped): Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
kar_pc_sse | INT | Karst Area Extent: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
kar_pc_use | INT | Karst Area Extent: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
lit_cl_smj | INT | Lithological Classes: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
lka_pc_sse | INT | Limnicity (Percent Lake Area): Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
lka_pc_use | INT | Limnicity (Percent Lake Area): Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
lkv_mc_usu | INT | Lake Volume: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
nli_ix_sav | INT | Nighttime Lights: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
nli_ix_uav | INT | Nighttime Lights: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
pac_pc_sse | INT | Protected Area Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
pac_pc_use | INT | Protected Area Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
pet_mm_s01 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
pet_mm_s02 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
pet_mm_s03 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
pet_mm_s04 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
pet_mm_s05 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
pet_mm_s06 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
pet_mm_s07 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
pet_mm_s08 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
pet_mm_s09 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
pet_mm_s10 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
pet_mm_s11 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
pet_mm_s12 | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
pet_mm_syr | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
pet_mm_uyr | INT | Potential Evapotranspiration: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
pnv_cl_smj | INT | Potential Natural Vegetation Classes: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
pnv_pc_s01 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} % coverage: Tropical Evergreen Forest/Woodland  
pnv_pc_s02 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} % coverage: Tropical Deciduous Forest/Woodland  
pnv_pc_s03 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} % coverage: Temperate Broadleaf Evergreen Forest/Woodland  
pnv_pc_s04 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} % coverage: Temperate Needleleaf Evergreen Forest/Woodland  
pnv_pc_s05 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} % coverage: Temperate Dciduous Forest/Woodland  
pnv_pc_s06 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} % coverage: Boreal Evergreen Forest/Woodland  
pnv_pc_s07 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} % coverage: Boreal Deciduous Forest/Woodland  
pnv_pc_s08 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} % coverage: Mixed Forest  
pnv_pc_s09 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} % coverage: Savanna  
pnv_pc_s10 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} % coverage: Grassland/Steppe  
pnv_pc_s11 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} % coverage: Dense Shrubland  
pnv_pc_s12 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} % coverage: Open Shrubland  
pnv_pc_s13 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {13} % coverage: Tundra  
pnv_pc_s14 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {14} % coverage: Desert  
pnv_pc_s15 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {15} % coverage: Polar Desert/Rock/Ice  
pnv_pc_u01 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {01} % coverage: Tropical Evergreen Forest/Woodland  
pnv_pc_u02 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {02} % coverage: Tropical Deciduous Forest/Woodland  
pnv_pc_u03 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {03} % coverage: Temperate Broadleaf Evergreen Forest/Woodland  
pnv_pc_u04 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {04} % coverage: Temperate Needleleaf Evergreen Forest/Woodland  
pnv_pc_u05 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {05} % coverage: Temperate Dciduous Forest/Woodland  
pnv_pc_u06 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {06} % coverage: Boreal Evergreen Forest/Woodland  
pnv_pc_u07 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {07} % coverage: Boreal Deciduous Forest/Woodland  
pnv_pc_u08 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {08} % coverage: Mixed Forest  
pnv_pc_u09 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {09} % coverage: Savanna  
pnv_pc_u10 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {10} % coverage: Grassland/Steppe  
pnv_pc_u11 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {11} % coverage: Dense Shrubland  
pnv_pc_u12 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {12} % coverage: Open Shrubland  
pnv_pc_u13 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {13} % coverage: Tundra  
pnv_pc_u14 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {14} % coverage: Desert  
pnv_pc_u15 | INT | Potential Natural Vegetation Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {15} % coverage: Polar Desert/Rock/Ice  
pop_ct_ssu | DOUBLE | Population Count: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {su} sum  
pop_ct_usu | DOUBLE | Population Count: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
ppd_pk_sav | DOUBLE | Population Density: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
ppd_pk_uav | DOUBLE | Population Density: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
pre_mm_s01 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
pre_mm_s02 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
pre_mm_s03 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
pre_mm_s04 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
pre_mm_s05 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
pre_mm_s06 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
pre_mm_s07 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
pre_mm_s08 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
pre_mm_s09 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
pre_mm_s10 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
pre_mm_s11 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
pre_mm_s12 | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
pre_mm_syr | INT | Precipitation: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
pre_mm_uyr | INT | Precipitation: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
prm_pc_sse | INT | Permafrost Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
prm_pc_use | INT | Permafrost Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
pst_pc_sse | INT | Pasture Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {se} spatial extent (%)  
pst_pc_use | INT | Pasture Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
rdd_mk_sav | INT | Road Density: Category = Anthropogenic; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
rdd_mk_uav | INT | Road Density: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
rev_mc_usu | INT | Reservoir Volume: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
ria_ha_ssu | DOUBLE | River Area: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {su} sum  
ria_ha_usu | DOUBLE | River Area: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
riv_tc_ssu | DOUBLE | River Volume: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {su} sum  
riv_tc_usu | DOUBLE | River Volume: Category = Hydrology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {su} sum  
run_mm_syr | INT | Land Surface Runoff: Category = Hydrology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
sgr_dk_sav | INT | Stream Gradient: Category = Physiography; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
slp_dg_sav | INT | Terrain Slope: Category = Physiography; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
slp_dg_uav | INT | Terrain Slope: Category = Physiography; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
slt_pc_sav | INT | Silt Fraction in Soil: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
slt_pc_uav | INT | Silt Fraction in Soil: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
snd_pc_sav | INT | Sand Fraction in Soil: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
snd_pc_uav | INT | Sand Fraction in Soil: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
snw_pc_s01 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
snw_pc_s02 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
snw_pc_s03 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
snw_pc_s04 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
snw_pc_s05 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
snw_pc_s06 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
snw_pc_s07 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
snw_pc_s08 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
snw_pc_s09 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
snw_pc_s10 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
snw_pc_s11 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
snw_pc_s12 | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
snw_pc_smx | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mx} annual maximum  
snw_pc_syr | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
snw_pc_uyr | INT | Snow Cover Extent: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
soc_th_sav | INT | Organic Carbon Content in Soil: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {av} average  
soc_th_uav | INT | Organic Carbon Content in Soil: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {av} average  
swc_pc_s01 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
swc_pc_s02 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
swc_pc_s03 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
swc_pc_s04 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
swc_pc_s05 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
swc_pc_s06 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
swc_pc_s07 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
swc_pc_s08 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
swc_pc_s09 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
swc_pc_s10 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
swc_pc_s11 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
swc_pc_s12 | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
swc_pc_syr | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
swc_pc_uyr | INT | Soil Water Content: Category = Soils & Geology; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
tbi_cl_smj | INT | Terrestrial Biomes: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
tec_cl_smj | INT | Terrestrial Ecoregions: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
tmp_dc_s01 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} January  
tmp_dc_s02 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} February  
tmp_dc_s03 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} March  
tmp_dc_s04 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} April  
tmp_dc_s05 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} May  
tmp_dc_s06 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} June  
tmp_dc_s07 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} July  
tmp_dc_s08 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} August  
tmp_dc_s09 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} September  
tmp_dc_s10 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {10} October  
tmp_dc_s11 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {11} November  
tmp_dc_s12 | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {12} December  
tmp_dc_smn | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mn} annual minimum  
tmp_dc_smx | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mx} annual maximum  
tmp_dc_syr | INT | Air Temperature: Category = Climate; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {yr} annual average  
tmp_dc_uyr | INT | Air Temperature: Category = Climate; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {yr} annual average  
urb_pc_sse | INT | Urban Extent: Category = Anthropogenic; Spatial Extent = {s} in reach catchment; Dimensions = {se} spatial extent (%)  
urb_pc_use | INT | Urban Extent: Category = Anthropogenic; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {se} spatial extent (%)  
wet_cl_smj | INT | Wetland Classes: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {mj} spatial majority  
wet_pc_s01 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {01} Wetland class #1: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s02 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {02} Wetland class #2: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s03 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {03} Wetland class #3: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s04 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {04} Wetland class #4: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s05 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {05} Wetland class #5: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s06 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {06} Wetland class #6: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s07 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {07} Wetland class #7: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s08 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {08} Wetland class #8: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_s09 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {09} Wetland class #9: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_sg1 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {g1} Wetland class grouping; see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_sg2 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {s} at sub-bsin pour point; Dimensions = {g2} Wetland class grouping; see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u01 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {01} Wetland class #1: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u02 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {02} Wetland class #2: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u03 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {03} Wetland class #3: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u04 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {04} Wetland class #4: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u05 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {05} Wetland class #5: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u06 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {06} Wetland class #6: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u07 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {07} Wetland class #7: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u08 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {08} Wetland class #8: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_u09 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {09} Wetland class #9: see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_ug1 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {g1} Wetland class grouping; see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
wet_pc_ug2 | INT | Wetland Extent: Category = Landcover; Spatial Extent = {u} in total watershed upstream of sub-basin pour point; Dimensions = {g2} Wetland class grouping; see https://www.worldwildlife.org/pages/global-lakes-and-wetlands-database  
**Terms of Use**
'The HydroATLAS database is licensed under a Creative Commons Attribution (CC-BY) 4.0 International License. Please also refer to the HydroATLAS [Technical Documentation](https://data.hydrosheds.org/file/technical-documentation/HydroATLAS_TechDoc_v10.pdf) for more details on the license and requested citations.
By downloading and using the data the user agrees to the terms and conditions of this license.'
Citations:
  * 'Linke, S., Lehner, B., Ouellet Dallaire, C., Ariwi, J., Grill, G., Anand, M., Beames, P., Burchard-Levine, V., Maxwell, S., Moidu, H., Tan, F., Thieme, M. (2019). Global hydro-environmental sub-basin and river reach characteristics at high spatial resolution. Scientific Data 6: 283. [DOI:10.1038/s41597-019-0300-6](https://doi.org/10.1038/s41597-019-0300-6).'
  * [doi:10.6084/m9.figshare.9890531](https://doi.org/10.6084/m9.figshare.9890531)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06#code-editor-javascript-sample) More
```
// Load the HydroATLAS dataset.
varbasinATLAS=ee.FeatureCollection('WWF/HydroATLAS/v1/Basins/level06');
// Set visualization to show upstream drainage area.
varupstreamDrainageArea=ee.Image().byte().paint({
featureCollection:basinATLAS,
color:'UP_AREA',
});
// Set map extent to show the Nile and surrounding basins.
Map.setCenter(-43.50,-24.70,6);
// Create a viridis colormap.
varviridis=[
'481567','482677','453781','404788','39568c','33638d','2d708e',
'287d8e','238a8d','1f968b','20a387','29af7f','3cbb75','55c667',
'73d055','95d840','b8de29','dce319','fde725'];
// View the continent of South America.
varregion=ee.Geometry.BBox(-80,-60,-20,20);
Map.addLayer(upstreamDrainageArea.clip(region),{palette:viridis,max:5e5},
'Upstream Drainage Area [mm]',true,0.8);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroATLAS_v1_Basins_level06)
[ WWF HydroATLAS Basins Level 06 ](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06)
BasinATLAS is a component of the HydroATLAS database, which is a component of HydroSHEDS. BasinATLAS provides a standardized compendium of hydro-environmental attribute information for all watersheds of the world at high spatial resolution. This dataset includes data for 56 variables, partitioned into 281 attributes and organized in six categories: hydrology; …
WWF/HydroATLAS/v1/Basins/level06, geophysical,hydroatlas,hydrography,hydrology,hydrosheds,srtm,surface-ground-water,table,water,watershed,wwf 
2000-02-22T00:00:00Z/2000-02-22T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.hydrosheds.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroATLAS_v1_Basins_level06)


