 
#  USFS Landscape Change Monitoring System v2023.9 (CONUS and OCONUS) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USFS/GTAC/LCMS/v2023-9](https://developers.google.com/earth-engine/datasets/images/USFS/USFS_GTAC_LCMS_v2023-9_sample.png) 

Dataset Availability
    1985-01-01T00:00:00Z–2023-12-31T00:00:00Z 

Dataset Provider
     [ USDA Forest Service (USFS) Geospatial Technology and Applications Center (GTAC) ](https://apps.fs.usda.gov/lcms-viewer/) 

Earth Engine Snippet
     `    ee.ImageCollection("USFS/GTAC/LCMS/v2023-9")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USFS/USFS_GTAC_LCMS_v2023-9) 

Tags
     [change-detection](https://developers.google.com/earth-engine/datasets/tags/change-detection) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [gtac](https://developers.google.com/earth-engine/datasets/tags/gtac) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [landuse](https://developers.google.com/earth-engine/datasets/tags/landuse) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [sentinel](https://developers.google.com/earth-engine/datasets/tags/sentinel) [time-series](https://developers.google.com/earth-engine/datasets/tags/time-series) [usda](https://developers.google.com/earth-engine/datasets/tags/usda) [usfs](https://developers.google.com/earth-engine/datasets/tags/usfs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#dois) More
This product is part of the Landscape Change Monitoring System (LCMS) data suite. It shows LCMS-modeled change, land cover, and/or land use classes for each year that covers the Conterminous United States (CONUS) and areas outside the CONUS (OCONUS) that include Southeastern Alaska (SEAK), Puerto Rico-US Virgin Islands (PRUSVI), and Hawaii (HI). 
LCMS is a remote sensing-based system for mapping and monitoring landscape change across the United States. Its objective is to develop a consistent approach using the latest technology and advancements in change detection to produce a "best available" map of landscape change.
Outputs include three annual products: change, land cover, and land use. Change relates specifically to vegetation cover and includes slow loss, fast loss (which also includes hydrologic changes such as inundation or desiccation), and gain. These values are predicted for each year of the Landsat time series and serve as the foundational products for LCMS. Land cover and land use maps depict life-form level land cover and broad-level land use for each year.
Because no algorithm performs best in all situations, LCMS uses an ensemble of models as predictors, which improves map accuracy across a range of ecosystems and change processes (Healey et al., 2018). The resulting suite of LCMS change, land cover, and land use maps offer a holistic depiction of landscape change across the United States since 1985.
Predictor layers for the LCMS model include outputs from the LandTrendr and CCDC change detection algorithms, and terrain information. These components are all accessed and processed using Google Earth Engine (Gorelick et al., 2017).
For CCDC, United States Geological Survey (USGS) Collection 2 Landsat Tier 1 surface reflectance data were used for the CONUS, and Landsat Tier 1 top of atmosphere reflectance data for SEAK, PRUSVI and HI. To produce annual composites for LandTrendr, USGS Collection 2 Landsat Tier 1 and Sentinel 2A, 2B Level-1C top of atmosphere reflectance data were used. The cFmask cloud masking algorithm (Foga et al., 2017), which is an implementation of Fmask 2.0 (Zhu and Woodcock, 2012) (Landsat-only), cloudScore (Chastain et al., 2019) (Landsat-only), s2cloudless (Sentinel-Hub, 2021) and Cloud Score plus (Pasquarella et al., 2023) (Sentinel 2-only) are used to mask clouds, while TDOM (Chastain et al., 2019) is used to mask cloud shadows (Landsat and Sentinel 2). For LandTrendr, the annual medoid is then computed to summarize cloud and cloud shadow-free values from each year into a single composite.
The composite time series is temporally segmented using LandTrendr (Kennedy et al., 2010; Kennedy et al., 2018; Cohen et al., 2018).
All cloud and cloud shadow free values are also temporally segmented using the CCDC algorithm (Zhu and Woodcock, 2014).
Predictor data include raw composite values, LandTrendr fitted values, pair-wise differences, segment duration, change magnitude, and slope, and CCDC sine and cosine coefficients (first 3 harmonics), fitted values, and pairwise differences, along with elevation, slope, sine of aspect, cosine of aspect, and topographic position indices (Weiss, 2001) from the 10 m USGS 3D Elevation Program (3DEP) data (U.S. Geological Survey, 2019).
Reference data are collected using TimeSync, a web-based tool that helps analysts visualize and interpret the Landsat data record from 1984-present (Cohen et al., 2010).
Random Forests models (Breiman, 2001) were trained using reference data from TimeSync and predictor data from LandTrendr, CCDC, and terrain indices to predict annual change, land cover, and land use classes. Following modeling, we instituted a series of probability thresholds and rulesets using ancillary datasets to improve qualitative map outputs and reduce commission and omission. More information can be found in the LCMS Methods Brief included in the Description. 
**Additional Resources**
  * [A more detailed code example of using LCMS data](https://github.com/google/earthengine-community/blob/master/datasets/scripts/LCMS_Visualization.js).
  * The [LCMS Data Explorer](https://apps.fs.usda.gov/lcms-viewer) is a web-based application that provides users the ability to view, analyze, summarize and download LCMS data.
  * Please see the [LCMS Methods Brief](https://data.fs.usda.gov/geodata/rastergateway/LCMS/LCMS_v2023-9_Methods.pdf) for more detailed information regarding methods and accuracy assessment, or the [LCMS Geodata Clearinghouse](https://data.fs.usda.gov/geodata/rastergateway/LCMS/index.php) for data downloads, metadata, and support documents.
  * The CONUS land use product was updated on July 2nd 2024, to correct an issue with the developed class.
  * PRUSVI and HI data were released October 1st 2024. 


Contact sm.fs.lcms@usda.gov with any questions or specific data requests.
**Pixel Size** 30 meters 
**Bands**
Name | Description  
---|---  
`Change` | Final thematic LCMS change product. A total of three change classes (slow loss, fast loss, and gain) are mapped for each year. Each class is predicted using a separate Random Forest model, which outputs a probability (proportion of the trees within the Random Forest model) that the pixel belongs to that class. Because of this, individual pixels have three different model outputs for each year. Final classes are assigned to the change class with the highest probability that is also above a specified threshold. Any pixel that does not have any value above each class's respective threshold is assigned to the Stable class. Prior to assigning the change class, a rule was applied to all study areas to prevent change in non-vegetated land cover.   
`Land_Cover` | Final thematic LCMS land cover product. A total of 14 land cover classes are mapped on an annual basis using TimeSync reference data and spectral information derived from Landsat imagery. Each class is predicted using a separate Random Forest model, which outputs a probability (proportion of the trees within the Random Forest model) that the pixel belongs to that class. Because of this, individual pixels have 14 different model outputs for each year, and final classes are assigned to the land cover with the highest probability. For Southeastern Alaska, prior to assigning the land cover class with the highest probability, a land cover rule was implemented to limit tree and snow landcover class commission in the large intertidal zones at sea level. No land cover rules were applied to CONUS, Puerto Rico-US Virgin Islands or Hawaii. Seven of the 14 land cover classes indicate a single land cover, where that land cover type covers most of the pixel's area and no other class covers more than 10% of the pixel. There are also seven mixed classes. These represent pixels in which an additional land cover class covers at least 10% of the pixel.  
`Land_Use` | Final thematic LCMS land use product. A total of 6 land use classes are mapped on an annual basis using TimeSync reference data and spectral information derived from Landsat imagery. Each class is predicted using a separate Random Forest model, which outputs a probability (proportion of the trees within the Random Forest model) that the pixel belongs to that class. Because of this, individual pixels have 6 different model outputs for each year, and final classes are assigned to the land use with the highest probability. Prior to assigning the land use class with the highest probability, a series of probability thresholds and rulesets using ancillary datasets land use rules were applied. More information on the probability thresholds and rulesets can be found in the LCMS Methods Brief included in the Description. The CONUS land use product was updated on July 2nd 2024, to correct an issue with the developed class.   
`Change_Raw_Probability_Slow-Loss` | Raw LCMS modeled probability of Slow Loss. Defined as: Slow Loss includes the following classes from the TimeSync change process interpretation-
  * Structural Decline - Land where trees or other woody vegetation is physically altered by unfavorable growing conditions brought on by non-anthropogenic or non-mechanical factors. This type of loss should generally create a trend in the spectral signal(s) (e.g. NDVI decreasing, Wetness decreasing; SWIR increasing; etc.) however the trend can be subtle. Structural decline occurs in woody vegetation environments, most likely from insects, disease, drought, acid rain, etc. Structural decline can include defoliation events that do not result in mortality such as in Gypsy moth and spruce budworm infestations which may recover within 1 or 2 years.
  * Spectral Decline - A plot where the spectral signal shows a trend in one or more of the spectral bands or indices (e.g. NDVI decreasing, Wetness decreasing; SWIR increasing; etc.). Examples include cases where: a) non-forest/non-woody vegetation shows a trend suggestive of decline (e.g. NDVI decreasing, Wetness decreasing; SWIR increasing; etc.), or b) where woody vegetation shows a decline trend which is not related to the loss of woody vegetation, such as when mature tree canopies close resulting in increased shadowing, when species composition changes from conifer to hardwood, or when a dry period (as opposed to stronger, more acute drought) causes an apparent decline in vigor, but no loss of woody material or leaf area.

  
`Change_Raw_Probability_Fast-Loss` | Raw LCMS modeled probability of Fast Loss. Defined as: Fast Loss includes the following classes from the TimeSync change process interpretation-
  * Fire - Land altered by fire, regardless of the cause of the ignition (natural or anthropogenic), severity, or land use.
  * Harvest - Forest land where trees, shrubs or other vegetation have been severed or removed by anthropogenic means. Examples include clearcutting, salvage logging after fire or insect outbreaks, thinning and other forest management prescriptions (e.g. shelterwood/seedtree harvest).
  * Mechanical - Non-forest land where trees, shrubs or other vegetation has been mechanically severed or removed by chaining, scraping, brush sawing, bulldozing, or any other methods of non-forest vegetation removal.
  * Wind/ice - Land (regardless of use) where vegetation is altered by wind from hurricanes, tornados, storms and other severe weather events including freezing rain from ice storms.
  * Hydrology - Land where flooding has significantly altered woody cover or other Land cover elements regardless of land use (e.g. new mixtures of gravel and vegetation in and around streambeds after a flood).
  * Debris - Land (regardless of use) altered by natural material movement associated with landslides, avalanches, volcanos, debris flows, etc.
  * Other - Land (regardless of use) where the spectral trend or other supporting evidence suggests a disturbance or change event has occurred but the definitive cause cannot be determined or the type of change fails to meet any of the change process categories defined above.

  
`Change_Raw_Probability_Gain` | Raw LCMS modeled probability of Gain. Defined as: Land exhibiting an increase in vegetation cover due to growth and succession over one or more years. Applicable to any areas that may express spectral change associated with vegetation regrowth. In developed areas, growth can result from maturing vegetation and/or newly installed lawns and landscaping. In forests, growth includes vegetation growth from bare ground, as well as the over topping of intermediate and co-dominate trees and/or lower-lying grasses and shrubs. Growth/Recovery segments recorded following forest harvest will likely transition through different land cover classes as the forest regenerates. For these changes to be considered growth/recovery, spectral values should closely adhere to an increasing trend line (e.g. a positive slope that would, if extended to ~20 years, be on the order of .10 units of NDVI) which persists for several years.  
`Land_Cover_Raw_Probability_Trees` | Raw LCMS modeled probability of Trees. Defined as: The majority of the pixel is comprised of live or standing dead trees.  
`Land_Cover_Raw_Probability_Tall-Shrubs-and-Trees-Mix` | Raw LCMS modeled probability of Tall Shrubs and Trees Mix (SEAK Only). Defined as: The majority of the pixel is comprised of shrubs greater than 1m in height and is also comprised of at least 10% live or standing dead trees.  
`Land_Cover_Raw_Probability_Shrubs-and-Trees-Mix` | Raw LCMS modeled probability of Shrubs and Trees Mix. Defined as: The majority of the pixel is comprised of shrubs and is also comprised of at least 10% live or standing dead trees.  
`Land_Cover_Raw_Probability_Grass-Forb-Herb-and-Trees-Mix` | Raw LCMS modeled probability of Grass/Forb/Herb and Trees Mix. Defined as: The majority of the pixel is comprised of perennial grasses, forbs, or other forms of herbaceous vegetation and is also comprised of at least 10% live or standing dead trees.  
`Land_Cover_Raw_Probability_Barren-and-Trees-Mix` | Raw LCMS modeled probability of Barren and Trees Mix. Defined as: The majority of the pixel is comprised of bare soil exposed by disturbance (e.g., soil uncovered by mechanical clearing or forest harvest), as well as perennially barren areas such as deserts, playas, rock outcroppings (including minerals and other geologic materials exposed by surface mining activities), sand dunes, salt flats, and beaches. Roads made of dirt and gravel are also considered barren and is also comprised of at least 10% live or standing dead trees.  
`Land_Cover_Raw_Probability_Tall-Shrubs` | Raw LCMS modeled probability of Tall Shrubs (SEAK Only). Defined as: The majority of the pixel is comprised of shrubs greater than 1m in height.  
`Land_Cover_Raw_Probability_Shrubs` | Raw LCMS modeled probability of Shrubs. Defined as: The majority of the pixel is comprised of shrubs.  
`Land_Cover_Raw_Probability_Grass-Forb-Herb-and-Shrubs-Mix` | Raw LCMS modeled probability of Grass/Forb/Herb and Shrubs Mix. Defined as: The majority of the pixel is comprised of perennial grasses, forbs, or other forms of herbaceous vegetation and is also comprised of at least 10% shrubs.  
`Land_Cover_Raw_Probability_Barren-and-Shrubs-Mix` | Raw LCMS modeled probability of Barren and Shrubs Mix. Defined as: The majority of the pixel is comprised of bare soil exposed by disturbance (e.g., soil uncovered by mechanical clearing or forest harvest), as well as perennially barren areas such as deserts, playas, rock outcroppings (including minerals and other geologic materials exposed by surface mining activities), sand dunes, salt flats, and beaches. Roads made of dirt and gravel are also considered barren and is also comprised of at least 10% shrubs.  
`Land_Cover_Raw_Probability_Grass-Forb-Herb` | Raw LCMS modeled probability of Grass/Forb/Herb. Defined as: The majority of the pixel is comprised of perennial grasses, forbs, or other forms of herbaceous vegetation.  
`Land_Cover_Raw_Probability_Barren-and-Grass-Forb-Herb-Mix` | Raw LCMS modeled probability of Barren and Grass/Forb/Herb Mix. Defined as: The majority of the pixel is comprised of bare soil exposed by disturbance (e.g., soil uncovered by mechanical clearing or forest harvest), as well as perennially barren areas such as deserts, playas, rock outcroppings (including minerals and other geologic materials exposed by surface mining activities), sand dunes, salt flats, and beaches. Roads made of dirt and gravel are also considered barren and is also comprised of at least 10% perennial grasses, forbs, or other forms of herbaceous vegetation.  
`Land_Cover_Raw_Probability_Barren-or-Impervious` | Raw LCMS modeled probability of Barren or Impervious. Defined as: The majority of the pixel is comprised of 1) bare soil exposed by disturbance (e.g., soil uncovered by mechanical clearing or forest harvest), as well as perennially barren areas such as deserts, playas, rock outcroppings (including minerals and other geologic materials exposed by surface mining activities), sand dunes, salt flats, and beaches. Roads made of dirt and gravel are also considered barren or 2) man-made materials that water cannot penetrate, such as paved roads, rooftops, and parking lots.  
`Land_Cover_Raw_Probability_Snow-or-Ice` | Raw LCMS modeled probability of Snow or Ice. Defined as: The majority of the pixel is comprised of snow or ice.  
`Land_Cover_Raw_Probability_Water` | Raw LCMS modeled probability of Water. Defined as: The majority of the pixel is comprised of water.  
`Land_Use_Raw_Probability_Agriculture` | Raw LCMS modeled probability of Agriculture. Defined as: Land used for the production of food, fiber and fuels which is in either a vegetated or non-vegetated state. This includes but is not limited to cultivated and uncultivated croplands, hay lands, orchards, vineyards, confined livestock operations, and areas planted for production of fruits, nuts or berries. Roads used primarily for agricultural use (i.e. not used for public transport from town to town) are considered agriculture land use.  
`Land_Use_Raw_Probability_Developed` | Raw LCMS modeled probability of Developed. Defined as: Land covered by man-made structures (e.g. high density residential, commercial, industrial, mining or transportation), or a mixture of both vegetation (including trees) and structures (e.g., low density residential, lawns, recreational facilities, cemeteries, transportation and utility corridors, etc.), including any land functionally altered by human activity.  
`Land_Use_Raw_Probability_Forest` | Raw LCMS modeled probability of Forest. Defined as: Land that is planted or naturally vegetated and which contains (or is likely to contain) 10% or greater tree cover at some time during a near-term successional sequence. This may include deciduous, evergreen and/or mixed categories of natural forest, forest plantations, and woody wetlands.  
`Land_Use_Raw_Probability_Non-Forest-Wetland` | Raw LCMS modeled probability of Non-Forest Wetland. Defined as: Lands adjacent to or within a visible water table (either permanently or seasonally saturated) dominated by shrubs or persistent emergents. These wetlands may be situated shoreward of lakes, river channels, or estuaries; on river floodplains; in isolated catchments; or on slopes. They may also occur as prairie potholes, drainage ditches and stock ponds in agricultural landscapes and may also appear as islands in the middle of lakes or rivers. Other examples also include marshes, bogs, swamps, quagmires, muskegs, sloughs, fens, and bayous.  
`Land_Use_Raw_Probability_Other` | Raw LCMS modeled probability of Other. Defined as: Land (regardless of use) where the spectral trend or other supporting evidence suggests a disturbance or change event has occurred but the definitive cause cannot be determined or the type of change fails to meet any of the change process categories defined above.  
`Land_Use_Raw_Probability_Rangeland-or-Pasture` | Raw LCMS modeled probability of Rangeland or Pasture. Defined as: This class includes any area that is either a.) Rangeland, where vegetation is a mix of native grasses, shrubs, forbs and grass-like plants largely arising from natural factors and processes such as rainfall, temperature, elevation and fire, although limited management may include prescribed burning as well as grazing by domestic and wild herbivores; or b.) Pasture, where vegetation may range from mixed, largely natural grasses, forbs and herbs to more managed vegetation dominated by grass species that have been seeded and managed to maintain near monoculture.  
`QA_Bits` | Ancillary information on the origin of the annual LCMS product output values.  
Bitmask for QA_Bits
  * Bit 0: Whether the pixel is interpolated. 
    * 0: Interpolated
    * 1: Not interpolated
  * Bits 1-5: Which sensor the pixel came from. 
    * 4: Landsat 4
    * 5: Landsat 5
    * 7: Landsat 7
    * 8: Landsat 8
    * 9: Landsat 9
    * 21: Sentinel 2A
    * 22: Sentinel 2B
  * Bits 6-14: Which Julian day the pixel came from (1-365). 

  
**Change Class Table**
Value | Color | Description  
---|---|---  
1 | #3d4551 | Stable  
2 | #f39268 | Slow Loss  
3 | #d54309 | Fast Loss  
4 | #00a398 | Gain  
5 | #1b1716 | Non-Processing Area Mask  
**Land_Cover Class Table**
Value | Color | Description  
---|---|---  
1 | #005e00 | Trees  
2 | #008000 | Tall Shrubs & Trees Mix (SEAK Only)  
3 | #00cc00 | Shrubs & Trees Mix  
4 | #b3ff1a | Grass/Forb/Herb & Trees Mix  
5 | #99ff99 | Barren & Trees Mix  
6 | #b30088 | Tall Shrubs (SEAK Only)  
7 | #e68a00 | Shrubs  
8 | #ffad33 | Grass/Forb/Herb & Shrubs Mix  
9 | #ffe0b3 | Barren & Shrubs Mix  
10 | #ffff00 | Grass/Forb/Herb  
11 | #aa7700 | Barren & Grass/Forb/Herb Mix  
12 | #d3bf9b | Barren or Impervious  
13 | #ffffff | Snow or Ice  
14 | #4780f3 | Water  
15 | #1b1716 | Non-Processing Area Mask  
**Land_Use Class Table**
Value | Color | Description  
---|---|---  
1 | #efff6b | Agriculture  
2 | #ff2ff8 | Developed  
3 | #1b9d0c | Forest  
4 | #97ffff | Non-Forest Wetland  
5 | #a1a1a1 | Other  
6 | #c2b34a | Rangeland or Pasture  
7 | #1b1716 | Non-Processing Area Mask  
**Image Properties**
Name | Type | Description  
---|---|---  
study_area | STRING | LCMS currently covers the conterminous United States, Southeastern Alaska, Puerto Rico-US Virgin Islands, and Hawaii. This version contains outputs across conterminous United States, Southeastern Alaska, Puerto Rico-US Virgin Islands, and Hawaii. Possible values: 'CONUS, SEAK, PRUSVI, HI'  
year | INT | Year of the product  
**Terms of Use**
The USDA Forest Service makes no warranty, expressed or implied, including the warranties of merchantability and fitness for a particular purpose, nor assumes any legal liability or responsibility for the accuracy, reliability, completeness or utility of these geospatial data, or for the improper or incorrect use of these geospatial data. These geospatial data and related maps or graphics are not legal documents and are not intended to be used as such. The data and maps may not be used to determine title, ownership, legal descriptions or boundaries, legal jurisdiction, or restrictions that may be in place on either public or private land. Natural hazards may or may not be depicted on the data and maps, and land users should exercise due caution. The data are dynamic and may change over time. The user is responsible to verify the limitations of the geospatial data and to use the data accordingly.
These data were collected using funding from the U.S. Government and can be used without additional permissions or fees. If you use these data in a publication, presentation, or other research product please use the following citation:
USDA Forest Service. 2024. USFS Landscape Change Monitoring System v2023.9 (Conterminous United States and Outer Conterminous United States). Salt Lake City, Utah.
Note
  * <https://data.fs.usda.gov/geodata/rastergateway/LCMS/index.php> is the preferred link for citations


Citations:
  * USDA Forest Service. 2024. USFS Landscape Change Monitoring System v2023.9 (Conterminous United States and Outer Conterminous United States). Salt Lake City, Utah.
  * Breiman, L., 2001. Random Forests. In Machine Learning. Springer, 45: 5-32. [doi:10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)
  * Chastain, R., Housman, I., Goldstein, J., Finco, M., and Tenneson, K., 2019. Empirical cross sensor comparison of Sentinel-2A and 2B MSI, Landsat-8 OLI, and Landsat-7 ETM top of atmosphere spectral characteristics over the conterminous United States. In Remote Sensing of Environment. Science Direct, 221: 274-285. [doi:10.1016/j.rse.2018.11.012](https://doi.org/10.1016/j.rse.2018.11.012)
  * Cohen, W. B., Yang, Z., and Kennedy, R., 2010. Detecting trends in forest disturbance and recovery using yearly Landsat time series: 2. TimeSync - Tools for calibration and validation. In Remote Sensing of Environment. Science Direct, 114(12): 2911-2924. [doi:10.1016/j.rse.2010.07.010](https://doi.org/10.1016/j.rse.2010.07.010)
  * Cohen, W. B., Yang, Z., Healey, S. P., Kennedy, R. E., and Gorelick, N., 2018. A LandTrendr multispectral ensemble for forest disturbance detection. In Remote Sensing of Environment. Science Direct, 205: 131-140. [doi:10.1016/j.rse.2017.11.015](https://doi.org/10.1016/j.rse.2017.11.015)
  * Foga, S., Scaramuzza, P.L., Guo, S., Zhu, Z., Dilley, R.D., Beckmann, T., Schmidt, G.L., Dwyer, J.L., Hughes, M.J., Laue, B., 2017. Cloud detection algorithm comparison and validation for operational Landsat data products. In Remote Sensing of Environment. Science Direct, 194: 379-390. [doi:10.1016/j.rse.2017.03.026](http://doi.org/10.1016/j.rse.2017.03.026)
  * U.S. Geological Survey, 2019. USGS 3D Elevation Program Digital Elevation Model, accessed August 2022 at https://developers.google.com/earth-engine/datasets/catalog/USGS_3DEP_10m
  * Healey, S. P., Cohen, W. B., Yang, Z., Kenneth Brewer, C., Brooks, E. B., Gorelick, N., Hernandez, A. J., Huang, C., Joseph Hughes, M., Kennedy, R. E., Loveland, T. R., Moisen, G. G., Schroeder, T. A., Stehman, S. V., Vogelmann, J. E., Woodcock, C. E., Yang, L., and Zhu, Z., 2018. Mapping forest change using stacked generalization: An ensemble approach. In Remote Sensing of Environment. Science Direct, 204: 717-728. [doi:10.1016/j.rse.2017.09.029](https://doi.org/10.1016/j.rse.2017.09.029)
  * Kennedy, R. E., Yang, Z., and Cohen, W. B., 2010. Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr - Temporal segmentation algorithms. In Remote Sensing of Environment. Science Direct, 114(12): 2897-2910. [doi:10.1016/j.rse.2010.07.008](https://doi.org/10.1016/j.rse.2010.07.008)
  * Kennedy, R., Yang, Z., Gorelick, N., Braaten, J., Cavalcante, L., Cohen, W., and Healey, S. 2018. Implementation of the LandTrendr Algorithm on Google Earth Engine. In Remote Sensing. MDPI, 10(5): 691. [doi:10.3390/rs10050691](https://doi.org/10.3390/rs10050691)
  * Pasquarella, V. J., Brown, C. F., Czerwinski, W., and Rucklidge, W. J., 2023. Comprehensive Quality Assessment of Optical Satellite Imagery Using Weakly Supervised Video Learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2124-2134.
  * Sentinel-Hub, 2021. Sentinel 2 Cloud Detector. [Online]. Available at: <https://github.com/sentinel-hub/sentinel2-cloud-detector>
  * Weiss, A.D., 2001. Topographic position and landforms analysis Poster Presentation, ESRI Users Conference, San Diego, CAZhu, Z., and Woodcock, C. E. 2012. Object-based cloud and cloud shadow detection in Landsat imagery. 118: 83-94.
  * Zhu, Z., and Woodcock, C. E., 2012. Object-based cloud and cloud shadow detection in Landsat imagery. In Remote Sensing of Environment. Science Direct, 118: 83-94. [doi:10.1016/j.rse.2011.10.028](https://doi.org/10.1016/j.rse.2011.10.028)
  * Zhu, Z., and Woodcock, C. E., 2014. Continuous change detection and classification of land cover using all available Landsat data. In Remote Sensing of Environment. Science Direct, 144: 152-171. [doi:10.1016/j.rse.2014.01.011](https://doi.org/10.1016/j.rse.2014.01.011)


  * [ https://doi.org/10.1016/j.rse.2010.07.008 ](https://doi.org/10.1016/j.rse.2010.07.008)
  * [ https://doi.org/10.1016/j.rse.2010.07.010 ](https://doi.org/10.1016/j.rse.2010.07.010)
  * [ https://doi.org/10.1016/j.rse.2011.10.028 ](https://doi.org/10.1016/j.rse.2011.10.028)
  * [ https://doi.org/10.1016/j.rse.2014.01.011 ](https://doi.org/10.1016/j.rse.2014.01.011)
  * [ https://doi.org/10.1016/j.rse.2017.03.026 ](https://doi.org/10.1016/j.rse.2017.03.026)
  * [ https://doi.org/10.1016/j.rse.2017.09.029 ](https://doi.org/10.1016/j.rse.2017.09.029)
  * [ https://doi.org/10.1016/j.rse.2017.11.015 ](https://doi.org/10.1016/j.rse.2017.11.015)
  * [ https://doi.org/10.1016/j.rse.2018.11.012 ](https://doi.org/10.1016/j.rse.2018.11.012)
  * [ https://doi.org/10.1023/A:1010933404324 ](https://doi.org/10.1023/A:1010933404324)
  * [ https://doi.org/10.3390/rs10050691 ](https://doi.org/10.3390/rs10050691)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('USFS/GTAC/LCMS/v2023-9');
varlcms=dataset.filterDate('2021','2022')// range: [1985, 2023]
.filter('study_area == "CONUS"')// or "SEAK"; "PRUSVI"; "HAWAII" 
.first();
Map.addLayer(lcms.select('Land_Cover'),{},'Land Cover');
Map.addLayer(lcms.select('Land_Use'),{},'Land Use');
Map.addLayer(lcms.select('Change'),{},'Vegetation Change',false);
Map.setCenter(-98.58,38.14,4);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USFS/USFS_GTAC_LCMS_v2023-9)
[ USFS Landscape Change Monitoring System v2023.9 (CONUS and OCONUS) ](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9)
This product is part of the Landscape Change Monitoring System (LCMS) data suite. It shows LCMS-modeled change, land cover, and/or land use classes for each year that covers the Conterminous United States (CONUS) and areas outside the CONUS (OCONUS) that include Southeastern Alaska (SEAK), Puerto Rico-US Virgin Islands (PRUSVI), and …
USFS/GTAC/LCMS/v2023-9, change-detection,forest,gtac,landcover,landsat,landuse,landuse-landcover,sentinel,time-series,usda,usfs 
1985-01-01T00:00:00Z/2023-12-31T00:00:00Z
20.38379 -135.286387 52.459364 -56.446306 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.3390/rs10050691 ](https://doi.org/https://apps.fs.usda.gov/lcms-viewer/)
  * [ https://doi.org/10.3390/rs10050691 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_LCMS_v2023-9)


