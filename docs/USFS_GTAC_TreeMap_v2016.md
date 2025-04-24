 
#  USFS TreeMap v2016 (Conterminous United States) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USFS/GTAC/TreeMap/v2016](https://developers.google.com/earth-engine/datasets/images/USFS/USFS_GTAC_TreeMap_v2016_sample.png) 

Dataset Availability
    2016-01-01T00:00:00Z–2017-01-01T00:00:00Z 

Dataset Provider
     [ USDA Forest Service (USFS) Geospatial Technology and Applications Center (GTAC) ](https://data.fs.usda.gov/geodata/rastergateway/treemap/) 

Earth Engine Snippet
     `    ee.ImageCollection("USFS/GTAC/TreeMap/v2016")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USFS/USFS_GTAC_TreeMap_v2016) 

Tags
     [biomass](https://developers.google.com/earth-engine/datasets/tags/biomass) [carbon](https://developers.google.com/earth-engine/datasets/tags/carbon) [climate-change](https://developers.google.com/earth-engine/datasets/tags/climate-change) [conus](https://developers.google.com/earth-engine/datasets/tags/conus) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [gtac](https://developers.google.com/earth-engine/datasets/tags/gtac) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landfire](https://developers.google.com/earth-engine/datasets/tags/landfire) [redcastle-resources](https://developers.google.com/earth-engine/datasets/tags/redcastle-resources) [tree-cover](https://developers.google.com/earth-engine/datasets/tags/tree-cover) [usfs](https://developers.google.com/earth-engine/datasets/tags/usfs) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation)
forest-inventory-and-analysis
forest-type
treemap
[Description](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#citations) More
This product is part of the TreeMap data suite. It provides detailed spatial information on forest characteristics including number of live and dead trees, biomass, and carbon across the entire forested extent of the continental United States in 2016.
TreeMap v2016 contains one image, a 22-band 30 x 30m resolution gridded map of the forests of the continental United States circa 2016, with each band representing an attribute derived from select FIA data (and one band representing the TreeMap ID). Examples of attributes include forest type, canopy cover percent, live tree stocking, live/dead tree biomass, and carbon in live/dead trees.
TreeMap products are the output of a random forest machine learning algorithm that assigns the most similar Forest Inventory Analysis (FIA) plot to each pixel of gridded LANDFIRE input data. The objective is to combine the complimentary strengths of detailed-but-spatially-sparse FIA data with less-detailed-but-spatially-comprehensive LANDFIRE data to produce better estimations of forest characteristics at a variety of scales. TreeMap is being used in both the private and public sectors for projects including fuel treatment planning, snag hazard mapping, and estimation of terrestrial carbon resources.
TreeMap is distinct from other imputed forest vegetation products in that it provides an FIA plot identifier to each pixel whereas other datasets provide forest characteristics such as live basal area (e.g., Ohmann and Gregory 2002; Pierce Jr et al. 2009; Wilson, Lister, and Riemann 2012). The FIA plot identifier can be linked to the hundreds of variables and attributes recorded for each tree and plot in the FIA DataMart, FIA's public repository of plot information (Forest Inventory Analysis 2022a).
The 2016 methodology includes disturbance as a response variable, resulting in increased accuracy in mapping disturbed areas. Within-class accuracy was over 90% for forest cover, height, vegetation group, and disturbance code when compared to LANDFIRE maps. At least one pixel within the radius of validation plots matched the class of predicted values in 57.5% of cases for forest cover, 80.0% for height, 80.0% for tree species with highest basal area, and 87.4% for disturbance.
**Additional Resources**
  * Please see the [TreeMap 2016 Publication](https://www.fs.usda.gov/research/treesearch/65597) for more detailed information regarding methods and accuracy assessment.
  * The [TreeMap 2016 Data Explorer](https://apps.fs.usda.gov/lcms-viewer/treemap.html) is a web-based application that provides users the ability to view and download TreeMap attribute data.
  * The [TreeMap Research Data Archive](https://www.fs.usda.gov/rds/archive/Catalog/RDS-2021-0074) for the full dataset download, metadata, and support documents.
  * [TreeMap Raster Data Gateway](https://data.fs.usda.gov/geodata/rastergateway/treemap/) for TreeMap attribute data downloads, metadata, and support documents.
  * [FIA Database Manual version 8](https://www.fia.fs.usda.gov/library/database-documentation/current/ver80/FIADB%20User%20Guide%20P2_8-0.pdf) for more detailed information on the attributes included in TreeMap 2016.


Contact sm.fs.treemaphelp@usda.gov with any questions or specific data requests.
  * **Forest Inventory Analysis. 2022a.** Forest Inventory Analysis DataMart. Forest Inventory Analysis DataMart FIADB_1.9.0. 2022. <https://apps.fs.usda.gov/fia/datamart/datamart.html>.
  * **Ohmann, Janet L and Matthew J Gregory. 2002.** Predictive Mapping of Forest Composition and Structure with Direct Gradient Analysis and Nearest- Neighbor Imputation in Coastal Oregon, USA. Can. J. For. Res. 32:725-741. [doi: 10.1139/X02-011](https://doi.org/10.1139/X02-011).
  * **Pierce, Kenneth B Jr, Janet L Ohmann, Michael C Wimberly, Matthew J Gregory, and Jeremy S Fried. 2009.** Mapping Wildland Fuels and Forest Structure for Land Management: A Comparison of Nearest Neighbor Imputation and Other Methods. Can. J. For. Res. 39: 1901-1916. [doi:10.1139/X09-102](https://doi.org/10.1139/X09-102).
  * **Wilson, B Tyler, Andrew J Lister, and Rachel I Riemann. 2012.** A Nearest-Neighbor Imputation Approach to Mapping Tree Species over Large Areas Using Forest Inventory Plots and Moderate Resolution Raster Data. Forest Ecol. Manag. 271:182-198. [doi: 10.1016/j. foreco.2012.02.002](https://doi.org/10.1016/j.foreco.2012.02.002).


**Pixel Size** 30 meters 
**Bands**
Name | Units | Description  
---|---|---  
`ALSTK` | % | All-Live-Tree Stocking. The sum of stocking percent values of all live trees on the condition.  
`BALIVE` | ft^2/acre | Live Tree Basal Area. Basal area in square feet per acre of all live trees ≥1.0 inch d.b.h./d.r.c. sampled in the condition.  
`CANOPYPCT` | % | Live Canopy Cover. Derived from the Forest Vegetation Simulator.  
`CARBON_D` | tons/acre | Carbon, Standing Dead. Calculated via the following FIA query: Sum (DRYBIO_BOLE, DRYBIO_TOP, DRYBIO_STUMP, DRYBIO_SAPLING, DRYBIO_WDLD_SPP) / 2 /2000*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=2) AND ((TREE.DIA)>=5) AND ((TREE.STANDING_DEAD_CD)=1))  
`CARBON_DWN` | tons/acre | Carbon, Down Dead. Carbon (tons per acre) of woody material >3 inches in diameter on the ground, and stumps and their roots >3 inches in diameter. Estimated from models based on geographic area, forest type, and live tree carbon density (Smith and Heath 2008).  
`CARBON_L` | tons/acre | Carbon, Live Above Ground. Calculated via the following FIA query: Sum (DRYBIO_BOLE, DRYBIO_TOP, DRYBIO_STUMP, DRYBIO_SAPLING, DRYBIO_WDLD_SPP) / 2 /2000*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=1))  
`DRYBIO_D` | tons/acre | Dry Standing Dead Tree Biomass, Above Ground. Calculated via the following FIA query: Sum (DRYBIO_BOLE, DRYBIO_TOP, DRYBIO_STUMP, DRYBIO_SAPLING, DRYBIO_WDLD_SPP) /2000*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=2) AND ((TREE.DIA)>=5) AND ((TREE.STANDING_DEAD_CD)=1))  
`DRYBIO_L` | tons/acre | Dry Live Tree Biomass, Above Ground. Calculated via the following FIA query: Sum (DRYBIO_BOLE, DRYBIO_TOP, DRYBIO_STUMP, DRYBIO_SAPLING, DRYBIO_WDLD_SPP) /2000*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=1))  
`FLDSZCD` | Field Stand-Size Class Code - Field-assigned classification of the predominant (based on stocking) diameter class of live trees within the condition.  
`FLDTYPCD` | Field Forest Type Code - A code indicating the forest type, assigned by the field crew, based on the tree species or species groups forming a plurality of all live stocking. The field crew assesses the forest type based on the acre of forest land around the plot, in addition to the species sampled on the condition.  
`FORTYPCD` | Algorithm Forest Type Code - This is the forest type used for reporting purposes. It is primarily derived using a computer algorithm, except when less than 25 percent of the plot samples a particular forest condition or in a few other cases.  
`GSSTK` | % | Growing-Stock Stocking. The sum of stocking percent values of all growing-stock trees on the condition.  
`QMD_RMRS` | in | Stand Quadratic Mean Diameter. Rocky Mountain Research Station. The quadratic mean diameter, or the diameter of the tree of average basal area, on the condition. Based on live trees ≥1.0 inch d.b.h./d.r.c. Only collected by certain FIA work units.  
`SDIPCT_RMRS` | % | Stand Density Index. Rocky Mountain Research Station. A relative measure of stand density for live trees (≥1.0 inch d.b.h./d.r.c.) on the condition, expressed as a percentage of the maximum stand density index (SDI). Only collected by certain FIA work units.  
`STANDHT` | ft | Height of dominant trees. Derived from the Forest Vegetation Simulator.  
`STDSZCD` | Algorithm Stand-Size Class Code - A classification of the predominant (based on stocking) diameter class of live trees within the condition assigned using an algorithm.  
`TPA_DEAD` | count/acre | Dead Trees Per Acre. Number of dead standing trees per acre (DIA >= 5”). Calculated via the following FIA query: Sum TREE.TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=2) AND ((TREE.DIA)>=5) AND ((TREE.STANDING_DEAD_CD)=1))  
`TPA_LIVE` | count/acre | Live Trees Per Acre. Number of live trees per acre (DIA > 1"). Calculated via the following FIA query: Sum TREE.TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=1) AND ((TREE.DIA)>=1))  
`Value` | Raw TreeMap identifier dataset values. This dataset is useful to see spatial groupings of individual modeled plot values.  
`VOLBFNET_L` | sawlog-board-ft/acre | Volume, Live (log rule: Int’l ¼ inch). Calculated via the following FIA query: Sum VOLBFNET * TPA_UNADJ WHERE (((TREE.TREECLCD)=2) AND ((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=1))  
`VOLCFNET_D` | ft^3/acre | Volume, Standing Dead. Calculated via the following FIA query: Sum VOLCFNET*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=2) AND ((TREE.DIA)>=5) AND ((TREE.STANDING_DEAD_CD)=1))  
`VOLCFNET_L` | ft^3/acre | Volume, Live. Calculated via the following FIA query: Sum VOLCFNET*TPA_UNADJ WHERE (((COND.COND_STATUS_CD)=1) AND ((TREE.STATUSCD)=1))  
**FLDSZCD Class Table**
Value | Color | Description  
---|---|---  
0 | #c62363 | Nonstocked - Meeting the definition of accessible land and one of the following applies (1) less than 10 percent stocked by trees, seedlings, and saplings and not classified as cover trees, or (2) for several woodland species where stocking standards are not available, less than 10 percent canopy cover of trees, seedlings, and saplings.  
1 | #feba12 | ≤4.9 inches (seedlings/saplings). At least 10 percent stocking (or 10 percent canopy cover if stocking standards are not available) in trees, seedlings, and saplings, and at least 2/3 of the canopy cover is in trees less than 5.0 inches d.b.h./d.r.c.  
2 | #ffff00 | 5.0-8.9 inches (softwoods)/ 5.0-10.9 inches (hardwoods). At least 10 percent stocking (or 10 percent canopy cover if stocking standards are not available) in trees, seedlings, and saplings; and at least one-third of the canopy cover is in trees greater than 5.0 inches d.b.h./d.r.c. and the plurality of the canopy cover is in softwoods 5.0-8.9 inches diameter and/or hardwoods 5.0-10.9 inches d.b.h., and/or woodland trees 5.0-8.9 inches d.r.c.  
3 | #38a800 | 9.0-19.9 inches (softwoods)/ 11.0-19.9 inches (hardwoods). At least 10 percent stocking (or 10 percent canopy cover if stocking standards are not available) in trees, seedlings, and sapling; and at least one-third of the canopy cover is in trees greater than 5.0 inches d.b.h./d.r.c. and the plurality of the canopy cover is in softwoods 9.0-19.9 inches diameter and/or hardwoods between 11.0-19.9 inches d.b.h., and/or woodland trees 9.0-19.9 inches d.r.c.  
4 | #73dfff | 20.0-39.9 inches. At least 10 percent stocking (or 10 percent canopy cover if stocking standards are not available) in trees, seedlings, and saplings; and at least one-third of the canopy cover is in trees greater than 5.0 inches d.b.h./d.r.c. and the plurality of the canopy cover is in trees 20.0-39.9 inches d.b.h.  
5 | #5c09fc | 40.0+ inches. At least 10 percent stocking (or 10 percent canopy cover if stocking standards are not available) in trees, seedlings, and saplings; and at least one-third of the canopy cover is in trees greater than 5.0 inches d.b.h./d.r.c. and the plurality of the canopy cover is in trees greater than or equal to 40.0 inches d.b.h.  
**FLDTYPCD Class Table**
Value | Color | Description  
---|---|---  
101 | #6e26ec | Jack pine  
102 | #c765ec | Red pine  
103 | #efdbcc | Eastern white pine  
104 | #a8a9f2 | Eastern white pine / eastern hemlock  
105 | #d0ce83 | Eastern hemlock  
121 | #47d0b6 | Balsam fir  
122 | #9d86a6 | White spruce  
123 | #a5f77a | Red spruce  
124 | #dcf4d9 | Red spruce / balsam fir  
125 | #64e1f7 | Black spruce  
126 | #afa9b0 | Tamarack  
127 | #f2c531 | Northern white-cedar  
128 | #87cc75 | Fraser fir  
141 | #84d7eb | Longleaf pine  
142 | #ef4677 | Slash pine  
161 | #97f2ad | Loblolly pine  
162 | #d45549 | Shortleaf pine  
163 | #63f3ac | Virginia pine  
164 | #f58de4 | Sand pine  
165 | #e9c991 | Table Mountain pine  
166 | #ddbef2 | Pond pine  
167 | #bba847 | Pitch pine  
171 | #95eacd | Eastern redcedar  
182 | #a6827b | Rocky Mountain juniper  
184 | #bca28a | Juniper woodland  
185 | #cff3f4 | Pinyon / juniper woodland  
201 | #c1ded5 | Douglas-fir  
202 | #948ee9 | Port-Orford-cedar  
221 | #d0ef5b | Ponderosa pine  
222 | #e29af0 | Incense-cedar  
224 | #c34bc3 | Sugar pine  
225 | #e6acb8 | Jeffrey pine  
226 | #ea3b34 | Coulter pine  
241 | #724353 | Western white pine  
261 | #f2c7a0 | White fir  
262 | #6ab27f | Red fir  
263 | #f1f3d3 | Noble fir  
264 | #ea5aba | Pacific silver fir  
265 | #edc7e1 | Engelmann spruce  
266 | #4965e2 | Engelmann spruce / subalpine fir  
267 | #a0f4c4 | Grand fir  
268 | #5697de | Subalpine fir  
269 | #5defc4 | Blue spruce  
270 | #e8f384 | Mountain hemlock  
271 | #cc63bd | Alaska-yellow-cedar  
281 | #e16f3d | Lodgepole pine  
301 | #f5da68 | Western hemlock  
304 | #a63bcf | Western redcedar  
305 | #51d0dd | Sitka spruce  
321 | #6bc5b6 | Western larch  
341 | #f2f4a5 | Redwood  
361 | #576abe | Knobcone pine  
362 | #b56f7c | Southwestern white pine  
365 | #dca5ca | Foxtail pine / bristlecone pine  
366 | #67eff4 | Limber pine  
367 | #ca5483 | Whitebark pine  
368 | #a8bf86 | Miscellaneous western softwoods  
369 | #aff6e9 | Western juniper  
371 | #a53394 | California mixed conifer  
381 | #e9e2eb | Scotch pine  
383 | #d0cfad | Other exotic softwoods  
384 | #eee1b3 | Norway spruce  
385 | #e4db79 | Introduced larch  
401 | #ec42f6 | Eastern white pine / northern red oak / white ash  
402 | #7e9f81 | Eastern redcedar / hardwood  
403 | #4a7196 | Longleaf pine / oak  
404 | #5cd76e | Shortleaf pine / oak  
405 | #37999a | Virginia pine / southern red oak  
406 | #ed54dd | Loblolly pine / hardwood  
407 | #6792f0 | Slash pine / hardwood  
409 | #82eb3e | Other pine / hardwood  
501 | #b8db98 | Post oak / blackjack oak  
502 | #bccc4b | Chestnut oak  
503 | #f22ab1 | White oak / red oak / hickory  
504 | #f6e095 | White oak  
505 | #77989d | Northern red oak  
506 | #718640 | Yellow-poplar / white oak / northern red oak  
507 | #9d4f8d | Sassafras / persimmon  
508 | #c376e4 | Sweetgum / yellow-poplar  
509 | #7cb133 | Bur oak  
510 | #5fa7cc | Scarlet oak  
511 | #9ae6e8 | Yellow-poplar  
512 | #def3b1 | Black walnut  
513 | #b88bf2 | Black locust  
514 | #a5f031 | Southern scrub oak  
515 | #eeafa3 | Chestnut oak / black oak / scarlet oak  
516 | #9bd763 | Cherry / white ash / yellow-poplar  
517 | #b838ee | Elm / ash / black locust  
519 | #e88fbb | Red maple / oak  
520 | #cce5b9 | Mixed upland hardwoods  
601 | #ed8a9c | Swamp chestnut oak / cherrybark oak  
602 | #c8ed2d | Sweetgum / Nuttall oak / willow oak  
605 | #f0bd53 | Overcup oak / water hickory  
606 | #60dad1 | Atlantic white-cedar  
607 | #c790c1 | Baldcypress / water tupelo  
608 | #54c7ef | Sweetbay / swamp tupelo / red maple  
609 | #8e6a31 | Baldcypress / pondcypress  
701 | #cecceb | Black ash / American elm / red maple  
702 | #b1bef2 | River birch / sycamore  
703 | #f077ef | Cottonwood  
704 | #969aca | Willow  
705 | #c4ec84 | Sycamore / pecan / American elm  
706 | #efadec | Sugarberry / hackberry / elm / green ash  
707 | #da23cf | Silver maple / American elm  
708 | #e4c3c0 | Red maple / lowland  
709 | #bf90e1 | Cottonwood / willow  
722 | #52f3eb | Oregon ash  
801 | #a2c9eb | Sugar maple / beech / yellow birch  
802 | #3ff451 | Black cherry  
805 | #6ab7f2 | Hard maple / basswood  
809 | #b3714c | Red maple / upland  
901 | #d28f25 | Aspen  
902 | #f59550 | Paper birch  
903 | #dd82c7 | Gray birch  
904 | #c5f2a0 | Balsam poplar  
905 | #e3f2e7 | Pin cherry  
911 | #b2c2b1 | Red alder  
912 | #4ff389 | Bigleaf maple  
921 | #8772e8 | Gray pine  
922 | #bb24a1 | California black oak  
923 | #c7f7cd | Oregon white oak  
924 | #8fc3c6 | Blue oak  
931 | #f13896 | Coast live oak  
933 | #efe92f | Canyon live oak  
934 | #6c48ae | Interior live oak  
935 | #b3e8cd | California white oak (valley oak)  
941 | #e8a882 | Tanoak  
942 | #b3e0f0 | California laurel  
943 | #6a48de | Giant chinkapin  
961 | #c3ab6e | Pacific madrone  
962 | #f5f169 | Other hardwoods  
971 | #f3c66f | Deciduous oak woodland  
972 | #4ecb89 | Evergreen oak woodland  
973 | #60b0c2 | Mesquite woodland  
974 | #76e45f | Cercocarpus (mountain brush) woodland  
975 | #b3c5ce | Intermountain maple woodland  
976 | #ee73af | Miscellaneous woodland hardwoods  
982 | #9473b4 | Mangrove  
983 | #80d9a8 | Palms  
995 | #e67774 | Other exotic hardwoods  
**FORTYPCD Class Table**
Value | Color | Description  
---|---|---  
101 | #6e26ec | Jack pine  
102 | #c765ec | Red pine  
103 | #efdbcc | Eastern white pine  
104 | #a8a9f2 | Eastern white pine / eastern hemlock  
105 | #d0ce83 | Eastern hemlock  
121 | #47d0b6 | Balsam fir  
122 | #9d86a6 | White spruce  
123 | #a5f77a | Red spruce  
124 | #dcf4d9 | Red spruce / balsam fir  
125 | #64e1f7 | Black spruce  
126 | #afa9b0 | Tamarack  
127 | #f2c531 | Northern white-cedar  
141 | #84d7eb | Longleaf pine  
142 | #ef4677 | Slash pine  
161 | #97f2ad | Loblolly pine  
162 | #d45549 | Shortleaf pine  
163 | #63f3ac | Virginia pine  
164 | #f58de4 | Sand pine  
165 | #e9c991 | Table Mountain pine  
166 | #ddbef2 | Pond pine  
167 | #bba847 | Pitch pine  
171 | #95eacd | Eastern redcedar  
182 | #a6827b | Rocky Mountain juniper  
184 | #bca28a | Juniper woodland  
185 | #cff3f4 | Pinyon / juniper woodland  
201 | #c1ded5 | Douglas-fir  
202 | #948ee9 | Port-Orford-cedar  
221 | #d0ef5b | Ponderosa pine  
222 | #e29af0 | Incense-cedar  
224 | #c34bc3 | Sugar pine  
225 | #e6acb8 | Jeffrey pine  
226 | #ea3b34 | Coulter pine  
241 | #724353 | Western white pine  
261 | #f2c7a0 | White fir  
262 | #6ab27f | Red fir  
263 | #f1f3d3 | Noble fir  
264 | #ea5aba | Pacific silver fir  
265 | #edc7e1 | Engelmann spruce  
266 | #4965e2 | Engelmann spruce / subalpine fir  
267 | #a0f4c4 | Grand fir  
268 | #5697de | Subalpine fir  
269 | #5defc4 | Blue spruce  
270 | #e8f384 | Mountain hemlock  
271 | #cc63bd | Alaska-yellow-cedar  
281 | #e16f3d | Lodgepole pine  
301 | #f5da68 | Western hemlock  
304 | #a63bcf | Western redcedar  
305 | #51d0dd | Sitka spruce  
321 | #6bc5b6 | Western larch  
341 | #f2f4a5 | Redwood  
361 | #576abe | Knobcone pine  
362 | #b56f7c | Southwestern white pine  
365 | #dca5ca | Foxtail pine / bristlecone pine  
366 | #67eff4 | Limber pine  
367 | #ca5483 | Whitebark pine  
368 | #a8bf86 | Miscellaneous western softwoods  
369 | #aff6e9 | Western juniper  
371 | #a53394 | California mixed conifer  
381 | #e9e2eb | Scotch pine  
383 | #d0cfad | Other exotic softwoods  
384 | #eee1b3 | Norway spruce  
385 | #e4db79 | Introduced larch  
401 | #ec42f6 | Eastern white pine / northern red oak / white ash  
402 | #7e9f81 | Eastern redcedar / hardwood  
403 | #4a7196 | Longleaf pine / oak  
404 | #5cd76e | Shortleaf pine / oak  
405 | #37999a | Virginia pine / southern red oak  
406 | #ed54dd | Loblolly pine / hardwood  
407 | #6792f0 | Slash pine / hardwood  
409 | #82eb3e | Other pine / hardwood  
501 | #b8db98 | Post oak / blackjack oak  
502 | #bccc4b | Chestnut oak  
503 | #f22ab1 | White oak / red oak / hickory  
504 | #f6e095 | White oak  
505 | #77989d | Northern red oak  
506 | #718640 | Yellow-poplar / white oak / northern red oak  
507 | #9d4f8d | Sassafras / persimmon  
508 | #c376e4 | Sweetgum / yellow-poplar  
509 | #7cb133 | Bur oak  
510 | #5fa7cc | Scarlet oak  
511 | #9ae6e8 | Yellow-poplar  
512 | #def3b1 | Black walnut  
513 | #b88bf2 | Black locust  
514 | #a5f031 | Southern scrub oak  
515 | #eeafa3 | Chestnut oak / black oak / scarlet oak  
516 | #9bd763 | Cherry / white ash / yellow-poplar  
517 | #b838ee | Elm / ash / black locust  
519 | #e88fbb | Red maple / oak  
520 | #cce5b9 | Mixed upland hardwoods  
601 | #ed8a9c | Swamp chestnut oak / cherrybark oak  
602 | #c8ed2d | Sweetgum / Nuttall oak / willow oak  
605 | #f0bd53 | Overcup oak / water hickory  
606 | #60dad1 | Atlantic white-cedar  
607 | #c790c1 | Baldcypress / water tupelo  
608 | #54c7ef | Sweetbay / swamp tupelo / red maple  
609 | #8e6a31 | Baldcypress / pondcypress  
701 | #cecceb | Black ash / American elm / red maple  
702 | #b1bef2 | River birch / sycamore  
703 | #f077ef | Cottonwood  
704 | #969aca | Willow  
705 | #c4ec84 | Sycamore / pecan / American elm  
706 | #efadec | Sugarberry / hackberry / elm / green ash  
707 | #da23cf | Silver maple / American elm  
708 | #e4c3c0 | Red maple / lowland  
709 | #bf90e1 | Cottonwood / willow  
722 | #52f3eb | Oregon ash  
801 | #a2c9eb | Sugar maple / beech / yellow birch  
802 | #3ff451 | Black cherry  
805 | #6ab7f2 | Hard maple / basswood  
809 | #b3714c | Red maple / upland  
901 | #d28f25 | Aspen  
902 | #f59550 | Paper birch  
903 | #dd82c7 | Gray birch  
904 | #c5f2a0 | Balsam poplar  
905 | #e3f2e7 | Pin cherry  
911 | #b2c2b1 | Red alder  
912 | #4ff389 | Bigleaf maple  
921 | #8772e8 | Gray pine  
922 | #bb24a1 | California black oak  
923 | #c7f7cd | Oregon white oak  
924 | #8fc3c6 | Blue oak  
931 | #f13896 | Coast live oak  
933 | #efe92f | Canyon live oak  
934 | #6c48ae | Interior live oak  
935 | #b3e8cd | California white oak (valley oak)  
941 | #e8a882 | Tanoak  
942 | #b3e0f0 | California laurel  
943 | #6a48de | Giant chinkapin  
961 | #c3ab6e | Pacific madrone  
962 | #f5f169 | Other hardwoods  
971 | #f3c66f | Deciduous oak woodland  
972 | #4ecb89 | Evergreen oak woodland  
973 | #60b0c2 | Mesquite woodland  
974 | #76e45f | Cercocarpus (mountain brush) woodland  
975 | #b3c5ce | Intermountain maple woodland  
976 | #ee73af | Miscellaneous woodland hardwoods  
982 | #9473b4 | Mangrove  
983 | #80d9a8 | Palms  
991 | #e6a25e | Paulownia  
992 | #f8f3b7 | Melaleuca  
995 | #e67774 | Other exotic hardwoods  
999 | #d5cc36 | Nonstocked  
**STDSZCD Class Table**
Value | Color | Description  
---|---|---  
1 | #38a800 | Large diameter - Stands with an all live stocking value of at least 10 (base 100); with more than 50 percent of the stocking in medium and large diameter trees; and with the stocking of large diameter trees equal to or greater than the stocking of medium diameter trees.  
2 | #ffff00 | Medium diameter - Stands with an all live stocking value of at least 10 (base 100); with more than 50 percent of the stocking in medium and large diameter trees; and with the stocking of large diameter trees less than the stocking of medium diameter trees.  
3 | #feba12 | Small diameter - Stands with an all live stocking value of at least 10 (base 100) on which at least 50 percent of the stocking is in small diameter trees.  
5 | #c62363 | Nonstocked - Forest land with all live stocking value less than 10.  
**Image Properties**
Name | Type | Description  
---|---|---  
year | INT | Year of the product.  
landfire_ver | STRING | Landfire version used as reference and target data for imputation.  
**Terms of Use**
The USDA Forest Service makes no warranty, expressed or implied, including the warranties of merchantability and fitness for a particular purpose, nor assumes any legal liability or responsibility for the accuracy, reliability, completeness or utility of these geospatial data, or for the improper or incorrect use of these geospatial data. These geospatial data and related maps or graphics are not legal documents and are not intended to be used as such. The data and maps may not be used to determine title, ownership, legal descriptions or boundaries, legal jurisdiction, or restrictions that may be in place on either public or private land. Natural hazards may or may not be depicted on the data and maps, and land users should exercise due caution. The data are dynamic and may change over time. The user is responsible to verify the limitations of the geospatial data and to use the data accordingly.
These data were collected using funding from the U.S. Government and can be used without additional permissions or fees. If you use these data in a publication, presentation, or other research product please use the appropriate citation.
Citations:
  * Riley, Karin L.; Grenfell, Isaac C.; Finney, Mark A.; Shaw, John D. 2021. TreeMap 2016: A tree-level model of the forests of the conterminous United States circa 2016. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2021-0074.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016#code-editor-javascript-sample) More
```
// Load the full dataset
vardataset=ee.ImageCollection('USFS/GTAC/TreeMap/v2016');
// Get the 2016 image
vartm2016=dataset.filterDate('2016','2017').first();
// 'Official' TreeMap 2016 palettes
varbamako=['00404d','134b42','265737','3a652a','52741c','71870b','969206','c5ae32','e7cd68','ffe599'];
varbamako_r=JSON.parse(JSON.stringify(bamako)).reverse();
varlajolla=['ffffcc','fbec9a','f4cc68','eca855','e48751','d2624d','a54742','73382f','422818','1a1a01'];
varlajolla_r=JSON.parse(JSON.stringify(lajolla)).reverse();
varimola=['1a33b3','2446a9','2e599f','396b94','497b85','60927b','7bae74','98cb6d','c4ea67','ffff66'];
varimola_r=JSON.parse(JSON.stringify(imola)).reverse();
// Select all 22 attributes
varalstk=tm2016.select('ALSTK');
varbalive=tm2016.select('BALIVE');
varcanopypct=tm2016.select('CANOPYPCT');
varcarbon_d=tm2016.select('CARBON_D');
varcarbon_dwn=tm2016.select('CARBON_DWN');
varcarbon_l=tm2016.select('CARBON_L');
vardrybio_d=tm2016.select('DRYBIO_D');
vardrybio_l=tm2016.select('DRYBIO_L');
varfldszcd=tm2016.select('FLDSZCD');
varfldtypcd=tm2016.select('FLDTYPCD');
varfortypcd=tm2016.select('FORTYPCD');
vargsstk=tm2016.select('GSSTK');
varqmd_rmrs=tm2016.select('QMD_RMRS');
varsdipct_rmrs=tm2016.select('SDIPCT_RMRS');
varstandht=tm2016.select('STANDHT');
varstdszcd=tm2016.select('STDSZCD');
vartpa_dead=tm2016.select('TPA_DEAD');
vartpa_live=tm2016.select('TPA_LIVE');
varvalue=tm2016.select('Value');
varvolbfnet_l=tm2016.select('VOLBFNET_L');
varvolcfnet_d=tm2016.select('VOLCFNET_D');
varvolcfnet_l=tm2016.select('VOLCFNET_L');
// Add all attributes to the map with the 'official' visualization
Map.addLayer(alstk,{'min':0,'max':100,'palette':bamako_r},'ALSTK: All-Live-Tree Stocking (percent)',false);
Map.addLayer(balive,{'min':24,'max':217,'palette':bamako_r},'BALIVE: Live Tree Basal Area (ft²)',false);
Map.addLayer(canopypct,{'min':0,'max':100,'palette':bamako_r},'CANOPYPCT: Live Canopy Cover (percent)',false);
Map.addLayer(carbon_d,{'min':0,'max':9,'palette':lajolla},'CARBON_D: Carbon, Standing Dead (tons/acre)',false);
Map.addLayer(carbon_dwn,{'min':0,'max':7,'palette':lajolla},'CARBON_DWN: Carbon, Down Dead (tons/acre)',false);
Map.addLayer(carbon_l,{'min':2,'max':59,'palette':lajolla_r},'CARBON_L: Carbon, Live Above Ground (tons/acre)',false);
Map.addLayer(drybio_d,{'min':0,'max':10,'palette':lajolla},'DRYBIO_D: Dry Standing Dead Tree Biomass, Above Ground (tons/acre)',false);
Map.addLayer(drybio_l,{'min':4,'max':118,'palette':lajolla_r},'DRYBIO_L: Dry Live Tree Biomass, Above Ground (tons/acre)',false);
Map.addLayer(fldszcd,{},'FLDSZCD: Field Stand-Size Class Code',false);
Map.addLayer(fldtypcd,{},'FLDTYPCD: Field Forest Type Code');
Map.addLayer(fortypcd,{},'FORTYPCD: Algorithm Forest Type Code',false);
Map.addLayer(gsstk,{'min':0,'max':100,'palette':bamako_r},'GSSTK: Growing-Stock Stocking (percent)',false);
Map.addLayer(qmd_rmrs,{'min':2,'max':25,'palette':bamako_r},'QMD_RMRS: Stand Quadratic Mean Diameter (in)',false);
Map.addLayer(sdipct_rmrs,{'min':6,'max':99,'palette':bamako_r},'SDIPCT_RMRS: Stand Density Index (percent of maximum)',false);
Map.addLayer(standht,{'min':23,'max':194,'palette':bamako_r},'STANDHT: Height of Dominant Trees (ft)',false);
Map.addLayer(stdszcd,{},'STDSZCD: Algorithm Stand-Size Class Code',false);
Map.addLayer(tpa_dead,{'min':38,'max':126,'palette':bamako},'TPA_DEAD: Dead Trees Per Acre',false);
Map.addLayer(tpa_live,{'min':252,'max':1666,'palette':bamako_r},'TPA_LIVE: Live Trees Per Acre',false);
Map.addLayer(value.randomVisualizer(),{},'Value: TreeMap ID',false);
Map.addLayer(volbfnet_l,{'min':441,'max':36522,'palette':imola_r},'VOLBFNET_L: Volume, Live (sawlog-board-ft/acre)',false);
Map.addLayer(volcfnet_d,{'min':5,'max':1326,'palette':imola_r},'VOLCFNET_D: Volume, Standing Dead (ft³/acre)',false);
Map.addLayer(volcfnet_l,{'min':137,'max':5790,'palette':imola_r},'VOLCFNET_L: Volume, Live (ft³/acre)',false);
// Set basemap
Map.setOptions('TERRAIN');
// Center map on CONUS
Map.setCenter(-95.712891,38,5);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USFS/USFS_GTAC_TreeMap_v2016)
[ USFS TreeMap v2016 (Conterminous United States) ](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016)
This product is part of the TreeMap data suite. It provides detailed spatial information on forest characteristics including number of live and dead trees, biomass, and carbon across the entire forested extent of the continental United States in 2016. TreeMap v2016 contains one image, a 22-band 30 x 30m resolution …
USFS/GTAC/TreeMap/v2016, biomass,carbon,climate-change,conus,forest,forest-biomass,gtac,landcover,landfire,redcastle-resources,tree-cover,usfs,vegetation 
2016-01-01T00:00:00Z/2017-01-01T00:00:00Z
22.76862 -128.97722 51.64968 -65.25445 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://data.fs.usda.gov/geodata/rastergateway/treemap/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_TreeMap_v2016)


