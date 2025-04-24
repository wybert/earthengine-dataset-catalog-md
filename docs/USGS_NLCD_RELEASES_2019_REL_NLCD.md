 
#  NLCD 2019: USGS National Land Cover Database, 2019 release 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/NLCD_RELEASES/2019_REL/NLCD](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_NLCD_RELEASES_2019_REL_NLCD_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2019-01-01T00:00:00Z 

Dataset Provider
     [ USGS ](https://www.mrlc.gov) 

Earth Engine Snippet
     `    ee.ImageCollection("USGS/NLCD_RELEASES/2019_REL/NLCD")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_NLCD_RELEASES_2019_REL_NLCD) 

Tags
     [blm](https://developers.google.com/earth-engine/datasets/tags/blm) [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [mrlc](https://developers.google.com/earth-engine/datasets/tags/mrlc) [nlcd](https://developers.google.com/earth-engine/datasets/tags/nlcd) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#dois) More
NLCD (the National Land Cover Database) is a 30-m Landsat-based land cover database spanning 8 epochs (2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019). A ninth epoch for 2021 is also available [here](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2021_REL_NLCD). The images rely on the imperviousness data layer for the urban classes and on a decision-tree classification for the rest.
This dataset has one image for the continental US for each epoch. Alaska, Hawaii, and Puerto Rico data can be found in the previous [2016 NLCD release](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2016_REL).
NLCD products are created by the Multi-Resolution Land Characteristics (MRLC) Consortium, a partnership of federal agencies led by the U.S. Geological Survey.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`landcover` |  11  |  95  | All images include the landcover classification scheme described in the [Product Legend](https://www.mrlc.gov/data/legends/national-land-cover-database-class-legend-and-description). The legends are also available as metadata on each image. The classes in the product legend are given below.  
`impervious` | % |  0  |  100  | Percent of the pixel covered by developed impervious surface.  
`impervious_descriptor` |  1  |  12  | Defines which impervious layer pixels are roads and provides the best fit description for impervious pixels that are not roads.  
**landcover Class Table**
Value | Color | Description  
---|---|---  
11 | #466b9f | Open water: areas of open water, generally with less than 25% cover of vegetation or soil.  
12 | #d1def8 | Perennial ice/snow: areas characterized by a perennial cover of ice and/or snow, generally greater than 25% of total cover.   
21 | #dec5c5 | Developed, open space: areas with a mixture of some constructed materials, but mostly vegetation in the form of lawn grasses. Impervious surfaces account for less than 20% of total cover. These areas most commonly include large-lot single-family housing units, parks, golf courses, and vegetation planted in developed settings for recreation, erosion control, or aesthetic purposes.   
22 | #d99282 | Developed, low intensity: areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 20% to 49% percent of total cover. These areas most commonly include single-family housing units.   
23 | #eb0000 | Developed, medium intensity: areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 50% to 79% of the total cover. These areas most commonly include single-family housing units.   
24 | #ab0000 | Developed high intensity: highly developed areas where people reside or work in high numbers. Examples include apartment complexes, row houses, and commercial/industrial. Impervious surfaces account for 80% to 100% of the total cover.   
31 | #b3ac9f | Barren land (rock/sand/clay): areas of bedrock, desert pavement, scarps, talus, slides, volcanic material, glacial debris, sand dunes, strip mines, gravel pits, and other accumulations of earthen material. Generally, vegetation accounts for less than 15% of total cover.   
41 | #68ab5f | Deciduous forest: areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species shed foliage simultaneously in response to seasonal change.   
42 | #1c5f2c | Evergreen forest: areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species maintain their leaves all year. Canopy is never without green foliage.   
43 | #b5c58f | Mixed forest: areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. Neither deciduous nor evergreen species are greater than 75% of total tree cover.   
51 | #af963c | Dwarf scrub: Alaska only areas dominated by shrubs less than 20 centimeters tall with shrub canopy typically greater than 20% of total vegetation. This type is often co-associated with grasses, sedges, herbs, and non-vascular vegetation.   
52 | #ccb879 | Shrub/scrub: areas dominated by shrubs less than 5 meters tall with shrub canopy typically greater than 20% of total vegetation. This class includes true shrubs, young trees in an early successional stage, or trees stunted from environmental conditions.   
71 | #dfdfc2 | Grassland/herbaceous: areas dominated by gramanoid or herbaceous vegetation, generally greater than 80% of total vegetation. These areas are not subject to intensive management such as tilling, but can be utilized for grazing.   
72 | #d1d182 | Sedge/herbaceous: Alaska only areas dominated by sedges and forbs, generally greater than 80% of total vegetation. This type can occur with significant other grasses or other grass like plants, and includes sedge tundra and sedge tussock tundra.   
73 | #a3cc51 | Lichens: Alaska only areas dominated by fruticose or foliose lichens generally greater than 80% of total vegetation.   
74 | #82ba9e | Moss: Alaska only areas dominated by mosses, generally greater than 80% of total vegetation.  
81 | #dcd939 | Pasture/hay: areas of grasses, legumes, or grass-legume mixtures planted for livestock grazing or the production of seed or hay crops, typically on a perennial cycle. Pasture/hay vegetation accounts for greater than 20% of total vegetation.   
82 | #ab6c28 | Cultivated crops: areas used for the production of annual crops, such as corn, soybeans, vegetables, tobacco, and cotton, and also perennial woody crops such as orchards and vineyards. Crop vegetation accounts for greater than 20% of total vegetation. This class also includes all land being actively tilled.   
90 | #b8d9eb | Woody wetlands: areas where forest or shrubland vegetation accounts for greater than 20% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.   
95 | #6c9fb8 | Emergent herbaceous wetlands: areas where perennial herbaceous vegetation accounts for greater than 80% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.   
**impervious_descriptor Class Table**
Value | Color | Description  
---|---|---  
0 | #000000 | Unclassified.  
20 | #ff0000 | Primary road. Interstates and other major roads. Pixels were derived from the 2018 NavStreets Street Data.   
21 | #ffff00 | Secondary road. Non-interstate highways. Pixels were derived from the 2018 NavStreets Street Data.   
22 | #0000ff | Tertiary road. Any two-lane road. Pixels were derived from the 2018 NavStreets Street Data.   
23 | #ffffff | Thinned road. Small tertiary roads that generally are not paved and have been removed from the landcover but remain as part of the impervious surface product. Pixels were derived from the 2018 NavStreets Street Data.   
24 | #ffc0c5 | Non-road non-energy impervious. Developed areas that are generally not roads or energy production; includes residential/commercial/industrial areas, parks, and golf courses.   
25 | #eb82eb | Microsoft buildings. Buildings not captured in the NLCD impervious process, and not included in the nonroad impervious surface class. Pixels derived from the Microsoft US Building Footprints dataset.   
26 | #9f1feb | LCMAP impervious. Impervious pixels from LCMAP that were used to fill in gaps left when roads were updated from previous versions of NLCD.   
27 | #40dfd0 | Wind turbines. Pixels derived from the US Wind Turbine Dataset, accessed on 1/9/2020.   
28 | #79ff00 | Well pads. Pixels derived from the 2019 Oil and Natural Gas Wells dataset from the Oak Ridge National Laboratory.   
29 | #005f00 | Other energy production. Areas previously identified as well pads and wind turbines and classified in coordination with the Landfire project.   
**Image Properties**
Name | Type | Description  
---|---|---  
landcover_class_names | DOUBLE | Landcover class names  
landcover_class_palette | DOUBLE | Landcover class palette  
landcover_class_values | DOUBLE | Landcover class values  
impervious_descriptor_class_names | DOUBLE | Impervious descriptor class names  
impervious_descriptor_class_palette | DOUBLE | Impervious descriptor class palette  
impervious_descriptor_class_values | DOUBLE | Impervious descriptor class values  
**Terms of Use**
Most U.S. Geological Survey (USGS) information is federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction. Additional information on [Acknowledging or Crediting USGS as Information Source](https://www.usgs.gov/centers/eros/data-citation) is available.
Citations:
  * Dewitz, J., and U.S. Geological Survey, 2021, National Land Cover Database (NLCD) 2019 Products (ver. 2.0, June 2021): U.S. Geological Survey data release, [doi:10.5066/P9KZCM54](https://doi.org/10.5066/P9KZCM54)


  * [ https://doi.org/10.5066/P9KZCM54 ](https://doi.org/10.5066/P9KZCM54)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD#code-editor-javascript-sample) More
```
// Import the NLCD collection.
vardataset=ee.ImageCollection('USGS/NLCD_RELEASES/2019_REL/NLCD');
// The collection contains images for multiple years and regions in the USA.
print('Products:',dataset.aggregate_array('system:index'));
// Filter the collection to the 2016 product.
varnlcd2016=dataset.filter(ee.Filter.eq('system:index','2016')).first();
// Each product has multiple bands for describing aspects of land cover.
print('Bands:',nlcd2016.bandNames());
// Select the land cover band.
varlandcover=nlcd2016.select('landcover');
// Display land cover on the map.
Map.setCenter(-95,38,5);
Map.addLayer(landcover,null,'Landcover');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_NLCD_RELEASES_2019_REL_NLCD)
[ NLCD 2019: USGS National Land Cover Database, 2019 release ](https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD)
NLCD (the National Land Cover Database) is a 30-m Landsat-based land cover database spanning 8 epochs (2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019). A ninth epoch for 2021 is also available here. The images rely on the imperviousness data layer for the urban classes and on a decision-tree …
USGS/NLCD_RELEASES/2019_REL/NLCD, blm,landcover,landuse-landcover,mrlc,nlcd,usgs 
2001-01-01T00:00:00Z/2019-01-01T00:00:00Z
21.75 -130.24 50 -63.66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5066/P9KZCM54 ](https://doi.org/https://www.mrlc.gov)
  * [ https://doi.org/10.5066/P9KZCM54 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD_RELEASES_2019_REL_NLCD)


