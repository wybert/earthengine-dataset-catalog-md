 
#  LANDFIRE EVT (Existing Vegetation Type) v1.4.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDFIRE/Vegetation/EVT/v1_4_0](https://developers.google.com/earth-engine/datasets/images/LANDFIRE/LANDFIRE_Vegetation_EVT_v1_4_0_sample.png) 

Dataset Availability
    2014-09-01T00:00:00Z–2014-09-01T00:00:00Z 

Dataset Provider
     [ U.S. Department of Agriculture's (USDA), U.S. Forest Service (USFS), U.S. Department of the Interior's Geological Survey (USGS), and The Nature Conservancy. ](https://landfire.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDFIRE/Vegetation/EVT/v1_4_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Vegetation_EVT_v1_4_0) 

Tags
     [doi](https://developers.google.com/earth-engine/datasets/tags/doi) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [landfire](https://developers.google.com/earth-engine/datasets/tags/landfire) [nature-conservancy](https://developers.google.com/earth-engine/datasets/tags/nature-conservancy) [usda](https://developers.google.com/earth-engine/datasets/tags/usda) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation) [wildfire](https://developers.google.com/earth-engine/datasets/tags/wildfire)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#citations) More
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.
LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees.
LANDFIRE's (LF) Existing Vegetation Type (EVT) represents the current distribution of the terrestrial ecological systems classification, developed by NatureServe for the western hemisphere, through 2016. A terrestrial ecological system is defined as a group of plant community types (associations) that tend to co-occur within landscapes with similar ecological processes, substrates, and/or environmental gradients.
*The LF Ecological Systems Descriptions for CONUS provides descriptions for each Ecological System including species, distribution and classification information.
EVT also includes ruderal or semi-natural vegetation types within the U.S. National Vegetation Classification. The LF Ruderal NVC Groups Descriptions for CONUS provides descriptions for each ruderal NVC Group including species, distribution, and classification information.
EVT is mapped using decision tree models, field data, Landsat imagery, elevation, and biophysical gradient data.
  * Decision tree models are developed separately for each of the three lifeforms-tree, shrub, and herbaceous and are then used to generate lifeform specific EVT layers.
  * Disturbance products are included in LF Remap products to describe areas on the landscape that have experienced change within the previous 10-year period.
  * The EVT product is reconciled through QA/QC measures to ensure life-form is synchronized with both Existing Vegetation Cover and Existing Vegetation Height.


The LANDIFRE Vegetation datasets include:
  * Biophysical Settings (BPS)
  * Environmental Site Potential (ESP)
  * Existing Vegetation Canopy Cover (EVC)
  * Existing Vegetation Height (EVH).
  * Existing Vegetation Type (EVT) These layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees.


**Pixel Size** 30 meters 
**Bands**
Name | Description  
---|---  
`EVT` | Existing Vegetation Type  
**EVT Class Table**
Value | Color | Description  
---|---|---  
3001 | #000000 | Inter-Mountain Basins Sparsely Vegetated Systems  
3002 | #000000 | Mediterranean California Sparsely Vegetated Systems  
3003 | #000000 | North Pacific Sparsely Vegetated Systems  
3004 | #000000 | North American Warm Desert Sparsely Vegetated Systems  
3006 | #000000 | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
3007 | #000000 | Western Great Plains Sparsely Vegetated Systems  
3008 | #000100 | North Pacific Oak Woodland  
3009 | #000100 | Northwestern Great Plains Aspen Forest and Parkland  
3011 | #000100 | Rocky Mountain Aspen Forest and Woodland  
3012 | #000100 | Rocky Mountain Bigtooth Maple Ravine Woodland  
3013 | #000000 | Western Great Plains Dry Bur Oak Forest and Woodland  
3014 | #000100 | Central and Southern California Mixed Evergreen Woodland  
3015 | #000100 | California Coastal Redwood Forest  
3016 | #000100 | Colorado Plateau Pinyon-Juniper Woodland  
3017 | #000100 | Columbia Plateau Western Juniper Woodland and Savanna  
3018 | #000100 | East Cascades Mesic Montane Mixed-Conifer Forest and Woodland  
3019 | #000100 | Great Basin Pinyon-Juniper Woodland  
3020 | #000100 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
3021 | #000100 | Klamath-Siskiyou Lower Montane Serpentine Mixed Conifer Woodland  
3022 | #000000 | Klamath-Siskiyou Upper Montane Serpentine Mixed Conifer Woodland  
3023 | #000000 | Madrean Encinal  
3024 | #000000 | Madrean Lower Montane Pine-Oak Forest and Woodland  
3025 | #000100 | Madrean Pinyon-Juniper Woodland  
3026 | #000000 | Madrean Upper Montane Conifer-Oak Forest and Woodland  
3027 | #000000 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
3028 | #000000 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
3029 | #000000 | Mediterranean California Mixed Oak Woodland  
3030 | #000000 | Mediterranean California Lower Montane Conifer Forest and Woodland  
3031 | #000000 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
3032 | #000000 | Mediterranean California Red Fir Forest  
3033 | #000000 | Mediterranean California Subalpine Woodland  
3034 | #000000 | Mediterranean California Mesic Serpentine Woodland and Chaparral  
3035 | #000000 | North Pacific Dry Douglas-fir(-Madrone) Forest and Woodland  
3036 | #000000 | North Pacific Hypermaritime Seasonal Sitka Spruce Forest  
3037 | #000000 | North Pacific Maritime Dry-Mesic Douglas-fir-Western Hemlock Forest  
3038 | #000000 | North Pacific Maritime Mesic Subalpine Parkland  
3039 | #000000 | North Pacific Maritime Mesic-Wet Douglas-fir-Western Hemlock Forest  
3041 | #000000 | North Pacific Mountain Hemlock Forest  
3042 | #000000 | North Pacific Mesic Western Hemlock-Silver Fir Forest  
3043 | #000000 | Mediterranean California Mixed Evergreen Forest  
3044 | #000000 | Northern California Mesic Subalpine Woodland  
3045 | #000000 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
3046 | #000100 | Northern Rocky Mountain Subalpine Woodland and Parkland  
3047 | #000100 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest  
3048 | #000000 | Northwestern Great Plains Highland White Spruce Woodland  
3049 | #000000 | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
3050 | #000000 | Rocky Mountain Lodgepole Pine Forest  
3051 | #000000 | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
3052 | #000000 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
3053 | #000100 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna  
3054 | #000100 | Southern Rocky Mountain Ponderosa Pine Woodland  
3055 | #000000 | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
3056 | #000000 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
3057 | #000100 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
3058 | #000000 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland  
3059 | #000100 | Southern Rocky Mountain Pinyon-Juniper Woodland  
3060 | #000100 | East Cascades Ponderosa Pine Forest and Woodland  
3061 | #000100 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
3062 | #000000 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland  
3063 | #000000 | North Pacific Broadleaf Landslide Forest and Shrubland  
3064 | #000000 | Colorado Plateau Mixed Low Sagebrush Shrubland  
3065 | #000000 | Columbia Plateau Scabland Shrubland  
3066 | #000000 | Inter-Mountain Basins Mat Saltbush Shrubland  
3067 | #010000 | Mediterranean California Alpine Fell-Field  
3068 | #000000 | North Pacific Dry and Mesic Alpine Dwarf-Shrubland or Fell-field or Meadow  
3070 | #000000 | Rocky Mountain Alpine Dwarf-Shrubland  
3071 | #010000 | Sierra Nevada Alpine Dwarf-Shrubland  
3072 | #000000 | Wyoming Basins Dwarf Sagebrush Shrubland and Steppe  
3074 | #000000 | Chihuahuan Creosotebush Desert Scrub  
3075 | #000000 | Chihuahuan Mixed Salt Desert Scrub  
3076 | #000000 | Chihuahuan Stabilized Coppice Dune and Sand Flat Scrub  
3077 | #000000 | Chihuahuan Succulent Desert Scrub  
3078 | #000000 | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
3079 | #000000 | Great Basin Xeric Mixed Sagebrush Shrubland  
3080 | #000000 | Inter-Mountain Basins Big Sagebrush Shrubland  
3081 | #000000 | Inter-Mountain Basins Mixed Salt Desert Scrub  
3082 | #000000 | Mojave Mid-Elevation Mixed Desert Scrub  
3083 | #000000 | North Pacific Avalanche Chute Shrubland  
3084 | #000000 | North Pacific Montane Shrubland  
3085 | #000000 | Northwestern Great Plains Shrubland  
3086 | #000000 | Rocky Mountain Lower Montane-Foothill Shrubland  
3087 | #000000 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
3088 | #000000 | Sonora-Mojave Mixed Salt Desert Scrub  
3090 | #000000 | Sonoran Granite Outcrop Desert Scrub  
3091 | #000000 | Sonoran Mid-Elevation Desert Scrub  
3092 | #000000 | Southern California Coastal Scrub  
3093 | #000000 | Southern Colorado Plateau Sand Shrubland  
3094 | #000000 | Western Great Plains Sandhill Shrubland  
3095 | #000000 | Apacherian-Chihuahuan Mesquite Upland Scrub  
3096 | #000000 | California Maritime Chaparral  
3097 | #000000 | California Mesic Chaparral  
3098 | #000000 | California Montane Woodland and Chaparral  
3099 | #000000 | California Xeric Serpentine Chaparral  
3100 | #000000 | Chihuahuan Mixed Desert and Thornscrub  
3101 | #000000 | Madrean Oriental Chaparral  
3103 | #000000 | Great Basin Semi-Desert Chaparral  
3104 | #000000 | Mogollon Chaparral  
3105 | #000000 | Northern and Central California Dry-Mesic Chaparral  
3106 | #000000 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
3107 | #000000 | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
3108 | #000000 | Sonora-Mojave Semi-Desert Chaparral  
3109 | #000000 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
3110 | #000000 | Southern California Dry-Mesic Chaparral  
3111 | #000000 | Western Great Plains Mesquite Woodland  
3112 | #000000 | California Central Valley Mixed Oak Savanna  
3113 | #000000 | California Coastal Live Oak Woodland and Savanna  
3114 | #000000 | California Lower Montane Foothill Pine Woodland and Savanna  
3115 | #000100 | Inter-Mountain Basins Juniper Savanna  
3116 | #000000 | Madrean Juniper Savanna  
3117 | #000100 | Southern Rocky Mountain Ponderosa Pine Savanna  
3118 | #000000 | Southern California Oak Woodland and Savanna  
3119 | #000100 | Southern Rocky Mountain Juniper Woodland and Savanna  
3120 | #000100 | Willamette Valley Upland Prairie and Savanna  
3121 | #010000 | Apacherian-Chihuahuan Semi-Desert Shrubland  
3122 | #010000 | Chihuahuan Gypsophilous Grassland and Steppe  
3123 | #000000 | Columbia Plateau Steppe and Grassland  
3124 | #000000 | Columbia Plateau Low Sagebrush Steppe  
3125 | #000000 | Inter-Mountain Basins Big Sagebrush Steppe  
3126 | #000000 | Inter-Mountain Basins Montane Sagebrush Steppe  
3127 | #000000 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
3128 | #000000 | Northern California Coastal Scrub  
3129 | #010000 | California Central Valley and Southern Coastal Grassland  
3130 | #010000 | California Mesic Serpentine Grassland  
3131 | #010000 | California Northern Coastal Grassland  
3132 | #010000 | Central Mixedgrass Prairie Grassland  
3133 | #010000 | Chihuahuan Sandy Plains Semi-Desert Grassland  
3134 | #010000 | Columbia Basin Foothill and Canyon Dry Grassland  
3135 | #010000 | Inter-Mountain Basins Semi-Desert Grassland  
3136 | #010000 | Mediterranean California Alpine Dry Tundra  
3137 | #010000 | Mediterranean California Subalpine Meadow  
3138 | #010000 | North Pacific Montane Grassland  
3139 | #010000 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
3140 | #010000 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
3141 | #010000 | Northwestern Great Plains Mixedgrass Prairie  
3142 | #010000 | Columbia Basin Palouse Prairie  
3143 | #000000 | Rocky Mountain Alpine Fell-Field  
3144 | #000000 | Rocky Mountain Alpine Turf  
3145 | #010000 | Rocky Mountain Subalpine-Montane Mesic Meadow  
3146 | #000000 | Southern Rocky Mountain Montane-Subalpine Grassland  
3147 | #010000 | Western Great Plains Foothill and Piedmont Grassland  
3148 | #010000 | Western Great Plains Sand Prairie Grassland  
3149 | #010000 | Western Great Plains Shortgrass Prairie  
3150 | #010000 | Western Great Plains Tallgrass Prairie  
3151 | #000000 | California Central Valley Riparian Forest and Woodland  
3152 | #000000 | California Montane Riparian Systems  
3153 | #000000 | Inter-Mountain Basins Greasewood Flat  
3154 | #000000 | Inter-Mountain Basins Montane Riparian Forest and Woodland  
3155 | #000000 | North American Warm Desert Riparian Forest and Woodland  
3156 | #000000 | North Pacific Lowland Riparian Forest and Shrubland  
3157 | #000000 | North Pacific Swamp Systems  
3158 | #000000 | North Pacific Montane Riparian Woodland and Shrubland  
3159 | #000000 | Rocky Mountain Montane Riparian Forest and Woodland  
3160 | #000000 | Rocky Mountain Subalpine/Upper Montane Riparian Forest and Woodland  
3161 | #000000 | Northern Rocky Mountain Conifer Swamp  
3162 | #000000 | Western Great Plains Floodplain Forest and Woodland  
3163 | #010000 | Pacific Coastal Marsh Systems  
3164 | #000000 | Rocky Mountain Wetland-Herbaceous  
3165 | #000000 | Northern Rocky Mountain Foothill Conifer Wooded Steppe  
3166 | #000000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
3167 | #000000 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
3168 | #000000 | Northern Rocky Mountain Avalanche Chute Shrubland  
3169 | #000000 | Northern Rocky Mountain Subalpine Deciduous Shrubland  
3170 | #000000 | Klamath-Siskiyou Xeromorphic Serpentine Savanna and Chaparral  
3171 | #010000 | North Pacific Alpine and Subalpine Dry Grassland  
3172 | #000000 | Sierran-Intermontane Desert Western White Pine-White Fir Woodland  
3173 | #000000 | North Pacific Wooded Volcanic Flowage  
3174 | #000000 | North Pacific Dry-Mesic Silver Fir-Western Hemlock-Douglas-fir Forest  
3177 | #000000 | California Coastal Closed-Cone Conifer Forest and Woodland  
3178 | #000000 | North Pacific Hypermaritime Western Red-cedar-Western Hemlock Forest  
3179 | #000100 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna  
3180 | #010000 | Introduced Riparian Forest and Woodland  
3181 | #010000 | Introduced Upland Vegetation-Annual Grassland  
3182 | #010000 | Introduced Upland Vegetation-Perennial Grassland and Forbland  
3183 | #010000 | Introduced Upland Vegetation-Annual and Biennial Forbland  
3184 | #010000 | California Annual Grassland  
3185 | #000000 | Introduced Forest Wetland  
3186 | #010000 | Introduced Upland Vegetation-Shrub  
3187 | #010000 | Introduced Upland Vegetation-Treed  
3191 | #010000 | Recently Logged-Herb and Grass Cover  
3192 | #010000 | Recently Logged-Shrub Cover  
3193 | #010000 | Recently Logged-Tree Cover  
3194 | #010000 | Ruderal Upland-Treed  
3195 | #010000 | Recently Burned-Herb and Grass Cover  
3196 | #000000 | Introduced Shrub Wetland  
3199 | #000000 | Introduced Herbaceous Wetland  
3200 | #000000 | Coastal Douglas-fir Woodland  
3201 | #000100 | Quercus garryana Woodland Alliance  
3202 | #000100 | Juniperus occidentalis Wooded Herbaceous Alliance  
3203 | #000000 | Juniperus occidentalis Woodland Alliance  
3204 | #000000 | Western Great Plains Mesquite Shrubland  
3205 | #000000 | Tsuga mertensiana-Abies amabilis Woodland Alliance  
3206 | #000000 | Pseudotsuga menziesii Giant Forest Alliance  
3207 | #010000 | Central Mixedgrass Prairie Shrubland  
3208 | #000000 | Abies concolor Forest Alliance  
3209 | #010000 | Western Great Plains Sand Prairie Shrubland  
3210 | #000000 | Coleogyne ramosissima Shrubland Alliance  
3211 | #000000 | Grayia spinosa Shrubland Alliance  
3212 | #000000 | Western Great Plains Sandhill Grassland  
3213 | #000000 | Quercus havardii Shrubland Alliance  
3214 | #000000 | Arctostaphylos patula Shrubland Alliance  
3215 | #000000 | Quercus turbinella Shrubland Alliance  
3216 | #000000 | Cercocarpus montanus Shrubland Alliance  
3217 | #000000 | Quercus gambelii Shrubland Alliance  
3218 | #000000 | North American Warm Desert Sparsely Vegetated Systems II  
3219 | #000000 | Inter-Mountain Basins Sparsely Vegetated Systems II  
3220 | #000000 | Artemisia tridentata ssp. vaseyana Shrubland Alliance  
3221 | #000000 | Mediterranean California Sparsely Vegetated Systems II  
3222 | #000000 | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems II  
3223 | #000000 | Sonoran Desert Sparsely Vegetated  
3227 | #000000 | Dry-mesic Montane Douglas-fir Forest  
3228 | #000100 | Dry-mesic Montane Western Larch Forest  
3229 | #000100 | Pinus albicaulis Woodland Alliance  
3230 | #000000 | Pinus sabiniana Woodland Alliance  
3231 | #000000 | Sequoiadendron giganteum Forest Alliance  
3232 | #000100 | Abies grandis Forest Forest  
3233 | #000000 | Subalpine Douglas-fir Forest  
3234 | #000000 | Mesic Montane Douglas-fir Forest  
3235 | #000000 | Xeric Montane Douglas-fir Forest  
3236 | #000100 | Subalpine Western Larch Forest  
3237 | #000100 | Mesic Montane Western Larch Forest  
3238 | #000000 | Laurentian-Acadian Northern Oak Forest  
3239 | #000000 | Laurentian-Acadian Northern Pine-Oak Forest  
3240 | #000000 | Laurentian-Acadian Hardwood Forest  
3241 | #000000 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
3242 | #000000 | Laurentian Oak Barrens  
3243 | #000000 | Laurentian Pine-Oak Barrens  
3244 | #000000 | Boreal Hardwood Forest  
3245 | #000000 | Boreal White Spruce-Fir-Hardwood Forest  
3247 | #000000 | Southern Appalachian Grass Bald  
3248 | #010000 | Northern Atlantic Coastal Plain Dune and Swale Grassland  
3249 | #000000 | Atlantic Coastal Plain Peatland Pocosin and Canebrake Shrubland  
3250 | #000000 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Shrubland  
3251 | #000000 | Rocky Mountain Montane Riparian Shrubland  
3252 | #000000 | Rocky Mountain Subalpine/Upper Montane Riparian Shrubland  
3253 | #000000 | Western Great Plains Floodplain Shrubland  
3254 | #000000 | Western Great Plains Floodplain Herbaceous  
3255 | #000000 | Inter-Mountain Basins Montane Riparian Shrubland  
3256 | #010000 | Apacherian-Chihuahuan Semi-Desert Grassland  
3257 | #000000 | California Central Valley Riparian Herbaceous  
3258 | #000000 | North American Warm Desert Riparian Herbaceous  
3259 | #010000 | Introduced Riparian Shrubland  
3260 | #000000 | Mediterranean California Lower Montane Black Oak Forest and Woodland  
3261 | #000000 | Mediterranean California Lower Montane Black Oak - Conifer Forest and Woodland  
3262 | #000100 | East Cascades Oak Forest and Woodland  
3263 | #000100 | East Cascades Oak - Ponderosa Pine Forest and Woodland  
3264 | #000000 | California Lower Montane Blue Oak Forest and Woodland  
3265 | #000000 | California Lower Montane Blue Oak-Foothill Pine Forest and Woodland  
3266 | #000000 | Oregon White Oak Woodland  
3267 | #000000 | Douglas-fir - Oregon White Oak Woodland  
3268 | #000100 | Eastern Great Plains Tallgrass Aspen Shrubland  
3269 | #000000 | Laurentian Shrubland Barrens  
3270 | #010000 | North-Central Interior Sand and Gravel Shrubland  
3271 | #000000 | Eastern Boreal Floodplain Herbaceous  
3272 | #000000 | Eastern Boreal Floodplain Shrubland  
3273 | #000000 | Eastern Great Plains Floodplain Herbaceous  
3274 | #000000 | Central Interior and Appalachian Floodplain Herbaceous  
3275 | #000000 | Central Interior and Appalachian Floodplain Shrubland  
3276 | #000000 | Laurentian-Acadian Floodplain Herbaceous  
3277 | #000000 | Laurentian-Acadian Floodplain Shrubland  
3278 | #000000 | Boreal Acidic Peatland Herbaceous  
3279 | #000000 | Boreal Acidic Peatland Shrubland  
3280 | #000000 | Central Interior and Appalachian Swamp Shrubland  
3281 | #000000 | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp Shrubland  
3282 | #010000 | Great Lakes Coastal Marsh Shrubland  
3283 | #000000 | Central Interior and Appalachian Shrub Wetlands  
3284 | #010000 | Laurentian-Acadian Herbaceous Wetlands  
3285 | #010000 | Laurentian-Acadian Shrub Wetlands  
3286 | #000000 | Paleozoic Plateau Bluff and Talus Herbaceous  
3287 | #010000 | Modified/Managed Northern Tallgrass Shrubland  
3288 | #000000 | Central Appalachian Rocky Shrubland  
3289 | #000000 | Acadian-Appalachian Subalpine Heath-Krummholz  
3290 | #000000 | North-Central Oak Barrens Herbaceous  
3291 | #010000 | Central Interior Highlands Calcareous Glade and Barrens Herbaceous  
3292 | #000001 | Open Water  
3293 | #000000 | Snow-Ice  
3294 | #000000 | Barren  
3295 | #000000 | Quarries-Strip Mines-Gravel Pits  
3296 | #010000 | Developed-Low Intensity  
3297 | #000000 | Developed-Medium Intensity  
3298 | #000000 | Developed-High Intensity  
3299 | #010101 | Developed-Roads  
3300 | #000000 | Central Interior and Appalachian Riparian Herbaceous  
3301 | #000100 | Boreal Aspen-Birch Forest  
3302 | #000100 | Laurentian-Acadian Northern Hardwoods Forest  
3303 | #000000 | Northeastern Interior Dry-Mesic Oak Forest  
3304 | #000000 | Ozark-Ouachita Dry-Mesic Oak Forest  
3305 | #000000 | Southern Interior Low Plateau Dry-Mesic Oak Forest  
3306 | #000000 | East Gulf Coastal Plain Northern Loess Plain Oak-Hickory Upland  
3307 | #000000 | East Gulf Coastal Plain Northern Dry Upland Hardwood Forest  
3308 | #000000 | Crosstimbers Oak Forest and Woodland  
3309 | #000000 | Southern Appalachian Northern Hardwood Forest  
3310 | #000000 | North-Central Interior Dry-Mesic Oak Forest and Woodland  
3311 | #000000 | North-Central Interior Dry Oak Forest and Woodland  
3312 | #000000 | Ouachita Montane Oak Forest  
3313 | #000000 | North-Central Interior Beech-Maple Forest  
3314 | #000100 | North-Central Interior Maple-Basswood Forest  
3315 | #000000 | Southern Appalachian Oak Forest  
3316 | #000000 | Southern Piedmont Mesic Forest  
3317 | #000000 | Allegheny-Cumberland Dry Oak Forest and Woodland  
3318 | #000000 | Southern and Central Appalachian Cove Forest  
3319 | #000000 | Central Interior and Appalachian Riparian Shrubland  
3320 | #000000 | Central and Southern Appalachian Montane Oak Forest  
3321 | #000000 | South-Central Interior Mesophytic Forest  
3322 | #000000 | Crowley's Ridge Mesic Loess Slope Forest  
3323 | #000100 | West Gulf Coastal Plain Mesic Hardwood Forest  
3324 | #000000 | Northern Atlantic Coastal Plain Hardwood Forest  
3325 | #000100 | East Gulf Coastal Plain Northern Mesic Hardwood Slope Forest  
3326 | #000000 | South-Central Interior/Upper Coastal Plain Flatwoods  
3327 | #000000 | East Gulf Coastal Plain Northern Loess Bluff Forest  
3328 | #000000 | Southern Coastal Plain Limestone Forest  
3329 | #000000 | East Gulf Coastal Plain Southern Loess Bluff Forest  
3330 | #000100 | Southern Coastal Plain Dry Upland Hardwood Forest  
3331 | #000100 | Eastern Great Plains Tallgrass Aspen Forest and Woodland  
3332 | #000100 | Gulf and Atlantic Coastal Plain Floodplain Herbaceous  
3333 | #000000 | South Florida Hardwood Hammock  
3334 | #000000 | Ozark-Ouachita Mesic Hardwood Forest  
3335 | #000100 | Southern Atlantic Coastal Plain Dry and Dry-Mesic Oak Forest  
3336 | #000000 | Southwest Florida Coastal Strand and Maritime Hammock  
3337 | #000000 | Southeast Florida Coastal Strand and Maritime Hammock  
3338 | #000100 | Central and South Texas Coastal Fringe Forest and Woodland  
3339 | #000100 | West Gulf Coastal Plain Chenier and Upper Texas Coastal Fringe Forest and Woodland  
3340 | #000000 | Appalachian Shale Barrens  
3342 | #000000 | Piedmont Hardpan Woodland and Forest  
3343 | #000100 | Southern Atlantic Coastal Plain Mesic Hardwood Forest  
3344 | #000000 | Boreal Jack Pine-Black Spruce Forest  
3346 | #000000 | Atlantic Coastal Plain Fall-line Sandhills Longleaf Pine Woodland  
3347 | #000000 | Atlantic Coastal Plain Upland Longleaf Pine Woodland  
3348 | #000000 | West Gulf Coastal Plain Upland Longleaf Pine Forest and Woodland  
3349 | #000000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
3350 | #000100 | Central and Southern Appalachian Spruce-Fir Forest  
3351 | #000000 | Southeastern Interior Longleaf Pine Woodland  
3352 | #000000 | Southern Appalachian Montane Pine Forest and Woodland  
3353 | #000000 | Southern Appalachian Low-Elevation Pine Forest  
3354 | #000000 | Northeastern Interior Pine Barrens  
3355 | #000000 | Northern Atlantic Coastal Plain Pitch Pine Barrens  
3356 | #000000 | Florida Longleaf Pine Sandhill  
3357 | #000100 | Southern Coastal Plain Mesic Slope Forest  
3358 | #000000 | East-Central Texas Plains Pine Forest and Woodland  
3359 | #000100 | Gulf and Atlantic Coastal Plain Floodplain Shrubland  
3361 | #000000 | Central Atlantic Coastal Plain Maritime Forest  
3362 | #000000 | Laurentian-Acadian Northern Pine Forest  
3363 | #010000 | Central Interior Highlands Dry Acidic Glade and Barrens  
3364 | #000000 | Ozark-Ouachita Dry Oak Woodland  
3365 | #000000 | Boreal White Spruce-Fir Forest  
3366 | #000000 | Laurentian-Acadian Pine-Hemlock Forest  
3367 | #000000 | Ozark-Ouachita Shortleaf Pine Forest and Woodland  
3368 | #000100 | Southern Piedmont Dry Pine Forest  
3369 | #000000 | Central Appalachian Dry Pine Forest  
3370 | #000000 | Appalachian Hemlock Forest  
3371 | #000100 | West Gulf Coastal Plain Pine Forest  
3372 | #000000 | East Gulf Coastal Plain Interior Shortleaf Pine Forest  
3373 | #000000 | Acadian Low-Elevation Spruce-Fir Forest  
3374 | #000000 | Acadian-Appalachian Montane Spruce-Fir Forest  
3375 | #000000 | Eastern Serpentine Woodland  
3376 | #000000 | Southern Ridge and Valley/Cumberland Dry Calcareous Forest  
3377 | #000000 | Central Appalachian Rocky Pine Woodland  
3378 | #000000 | West Gulf Coastal Plain Sandhill Shortleaf Pine Forest and Woodland  
3379 | #000100 | Northern Atlantic Coastal Plain Maritime Forest  
3380 | #000000 | East Gulf Coastal Plain Maritime Forest  
3381 | #000000 | Lower Mississippi River Dune Woodland and Forest  
3382 | #000000 | Southern Atlantic Coastal Plain Maritime Forest  
3383 | #000000 | Edwards Plateau Limestone Woodland  
3384 | #000100 | Mississippi Delta Maritime Forest  
3385 | #000000 | Western Great Plains Wooded Draw and Ravine  
3386 | #000000 | Acadian-Appalachian Alpine Tundra  
3387 | #000100 | Florida Peninsula Inland Scrub Shrubland  
3389 | #000000 | Acadian-Appalachian Subalpine Woodland  
3390 | #000000 | Tamaulipan Mixed Deciduous Thornscrub  
3391 | #000000 | Tamaulipan Mesquite Upland Tree  
3392 | #000000 | Tamaulipan Calcareous Thornscrub  
3393 | #000000 | Edwards Plateau Limestone Shrubland  
3394 | #000000 | North-Central Interior Oak Savanna  
3395 | #000000 | North-Central Oak Barrens Woodland  
3396 | #010000 | Gulf and Atlantic Coastal Plain Tidal Marsh Herbaceous  
3397 | #000000 | Nashville Basin Limestone Glade and Woodland  
3398 | #000000 | Cumberland Sandstone Glade and Barrens  
3399 | #000000 | Northern Atlantic Coastal Plain Grassland  
3400 | #000000 | Central Appalachian Alkaline Glade and Woodland  
3401 | #010000 | Central Interior Highlands Calcareous Glade and Barrens Woodland  
3402 | #000000 | Laurentian-Acadian Swamp Shrubland  
3403 | #000000 | West Gulf Coastal Plain Catahoula Barrens  
3405 | #010000 | West Gulf Coastal Plain Nepheline Syenite Glade  
3406 | #000100 | Southern Piedmont Dry Oak Forest  
3407 | #000000 | Laurentian Pine Barrens  
3408 | #000000 | Alabama Ketona Glade and Woodland  
3409 | #000000 | Great Lakes Alvar Shrubland  
3410 | #000000 | Llano Uplift Acidic Forest and Woodland  
3411 | #010000 | Great Lakes Wet-Mesic Lakeplain Prairie  
3412 | #010000 | North-Central Interior Sand and Gravel Tallgrass Prairie  
3413 | #000000 | Bluegrass Savanna and Woodland  
3414 | #000000 | Southern Appalachian Shrub Bald  
3415 | #010000 | Arkansas Valley Prairie and Woodland  
3416 | #000000 | Western Highland Rim Prairie and Barrens  
3417 | #000000 | Eastern Highland Rim Prairie and Barrens  
3418 | #000000 | Pennyroyal Karst Plain Prairie and Barrens  
3419 | #000000 | Southern Ridge and Valley Patch Prairie  
3420 | #010000 | Northern Tallgrass Prairie  
3421 | #010000 | Central Tallgrass Prairie  
3422 | #010000 | Texas Blackland Tallgrass Prairie  
3423 | #010000 | Southeastern Great Plains Tallgrass Prairie  
3425 | #000000 | Florida Dry Prairie Grassland  
3426 | #010000 | Southern Atlantic Coastal Plain Dune and Maritime Grassland  
3428 | #010000 | West Gulf Coastal Plain Northern Calcareous Prairie  
3429 | #010000 | West Gulf Coastal Plain Southern Calcareous Prairie  
3430 | #000000 | Southern Coastal Plain Blackland Prairie  
3433 | #010000 | East Gulf Coastal Plain Jackson Prairie  
3434 | #010000 | Texas-Louisiana Coastal Prairie  
3435 | #010000 | East Gulf Coastal Plain Dune and Coastal Grassland  
3436 | #010000 | Northern Atlantic Coastal Plain Dune and Swale Shrubland  
3437 | #010000 | Central and Upper Texas Coast Dune and Coastal Grassland  
3438 | #000000 | Tamaulipan Savanna Grassland  
3439 | #010000 | South Texas Lomas  
3440 | #010000 | Tamaulipan Clay Grassland  
3442 | #010000 | South Texas Sand Sheet Grassland  
3443 | #010000 | South Texas Dune and Coastal Grassland  
3444 | #000000 | Eastern Boreal Floodplain Woodland  
3446 | #000000 | South Florida Pine Flatwoods  
3447 | #000000 | South Florida Cypress Dome  
3448 | #000100 | Southern Piedmont Dry Oak-Pine Forest  
3449 | #000000 | Central Atlantic Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
3450 | #000000 | Southern Atlantic Coastal Plain Wet Pine Savanna and Flatwoods  
3451 | #000000 | West Gulf Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
3452 | #000000 | Atlantic Coastal Plain Peatland Pocosin and Canebrake Woodland  
3453 | #000000 | Central Florida Pine Flatwoods  
3454 | #000000 | East Gulf Coastal Plain Near-Coast Pine Flatwoods  
3455 | #000000 | East Gulf Coastal Plain Southern Loblolly Flatwoods  
3456 | #000000 | Northern Atlantic Coastal Plain Pitch Pine Lowland  
3457 | #000100 | South-Central Interior/Upper Coastal Plain Wet Flatwoods  
3458 | #000100 | West Gulf Coastal Plain Pine Flatwoods  
3459 | #000000 | Atlantic Coastal Plain Clay-Based Carolina Bay Wetland  
3460 | #000000 | Southern Coastal Plain Nonriverine Cypress Dome Woodland  
3461 | #000000 | Southern Coastal Plain Seepage Swamp and Baygall Woodland  
3462 | #000000 | West Gulf Coastal Plain Seepage Swamp and Baygall  
3463 | #000000 | Central Appalachian Dry Oak Forest  
3464 | #000000 | Acadian Near-Boreal Spruce Barrens  
3466 | #000000 | Great Lakes Wooded Dune and Swale  
3467 | #000000 | Tamaulipan Floodplain Forest  
3468 | #000000 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
3469 | #000000 | Eastern Great Plains Floodplain Woodland  
3470 | #000000 | Caribbean Coastal Wetland Systems  
3471 | #000000 | Central Interior and Appalachian Floodplain Forest  
3472 | #000000 | Central Interior and Appalachian Riparian Forest  
3473 | #000100 | Gulf and Atlantic Coastal Plain Floodplain Forest  
3474 | #000100 | Gulf and Atlantic Coastal Plain Small Stream Riparian Woodland  
3475 | #000000 | Laurentian-Acadian Floodplain Forest  
3476 | #000000 | Tamaulipan Riparian Woodland  
3477 | #000000 | Boreal Acidic Peatland Forest  
3478 | #000000 | Caribbean Forested Swamp  
3479 | #000000 | Central Interior and Appalachian Swamp Forest  
3480 | #000000 | Gulf and Atlantic Coastal Plain Swamp Systems  
3481 | #000000 | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp Forest  
3482 | #000000 | Great Plains Prairie Pothole  
3483 | #010000 | South Florida Everglades Sawgrass Marsh  
3485 | #010000 | East Gulf Coastal Plain Savanna and Wet Prairie  
3486 | #010000 | Texas Saline Coastal Prairie  
3488 | #000000 | Eastern Great Plains Wet Meadow-Prairie-Marsh  
3489 | #010000 | Floridian Highlands Freshwater Marsh Herbaceous  
3490 | #010000 | Gulf and Atlantic Coastal Plain Tidal Marsh Shrubland  
3491 | #010000 | Acadian Salt Marsh and Estuary Systems  
3492 | #010000 | Great Lakes Coastal Marsh Herbaceous  
3493 | #000000 | Central Interior and Appalachian Herbaceous Wetlands  
3494 | #010000 | Laurentian-Acadian Forested Wetlands  
3495 | #010000 | Western Great Plains Depressional Wetland Systems  
3497 | #000000 | Central Interior and Appalachian Sparsely Vegetated Systems  
3498 | #000000 | Gulf and Atlantic Coastal Plain Sparsely Vegetated Systems  
3499 | #000000 | Laurentian-Acadian Sparsely Vegetated Systems  
3501 | #000000 | Southern Atlantic Coastal Plain Nonriverine Swamp and Wet Hardwood Forest  
3502 | #000000 | Central Appalachian Dry Oak-Pine Forest  
3503 | #010000 | Chihuahuan Loamy Plains Desert Grassland  
3504 | #010000 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland  
3506 | #000100 | West Gulf Coastal Plain Nonriverine Wet Hardwood Flatwoods  
3507 | #000000 | Ozark-Ouachita Shortleaf Pine-Bluestem Woodland  
3509 | #000000 | Mississippi River Alluvial Plain Dry-Mesic Loess Slope Forest  
3510 | #000000 | Crowley's Ridge Sand Forest  
3511 | #000000 | Appalachian Northern Hardwood Forest  
3512 | #000000 | Appalachian Hemlock-Northern Hardwood Forest  
3513 | #000100 | Lower Mississippi River Flatwoods  
3517 | #000000 | Paleozoic Plateau Bluff and Talus Woodland  
3518 | #000100 | North-Central Interior Wet Flatwoods  
3519 | #000000 | East-Central Texas Plains Post Oak Savanna and Woodland  
3522 | #000000 | Northern Atlantic Coastal Plain Heathland  
3523 | #000000 | Edwards Plateau Dry-Mesic Slope Forest and Woodland  
3524 | #000000 | Edwards Plateau Mesic Canyon  
3525 | #000000 | Edwards Plateau Riparian Woodland  
3526 | #000000 | Laurentian-Acadian Swamp Woodland  
3527 | #000000 | East Gulf Coastal Plain Interior Oak Forest  
3528 | #010000 | Ruderal Upland Shrubland  
3529 | #010000 | Ruderal Upland Herbaceous  
3531 | #010000 | Ruderal Upland Forest  
3532 | #010000 | Ruderal Forest-Northern and Central Hardwood and Conifer  
3533 | #010000 | Ruderal Forest-Southeast Hardwood and Conifer  
3534 | #000000 | Managed Tree Plantation-Northern and Central Hardwood and Conifer Plantation Group  
3535 | #000000 | Managed Tree Plantation-Southeast Conifer and Hardwood Plantation Group  
3536 | #000000 | Introduced Wetland Vegetation-Tree  
3538 | #000000 | Introduced Wetland Vegetation-Herbaceous  
3539 | #010000 | Modified/Managed Northern Tallgrass Grassland  
3540 | #010000 | Modified/Managed Southern Tallgrass Grassland  
3546 | #000000 | East Gulf Coastal Plain Interior Shortleaf Pine-Oak Forest  
3550 | #000100 | Pinus taeda Forest Alliance  
3551 | #000000 | Pinus elliottii Saturated Temperate Woodland Alliance  
3552 | #000000 | Pinus palustris-Pinus elliottii Forest Alliance  
3553 | #000000 | Mixed Loblolly-Slash Pine  
3554 | #000000 | Acadian Low-Elevation Hardwood Forest  
3555 | #000000 | Acadian Low-Elevation Spruce-Fir-Hardwood Forest  
3556 | #000000 | Central Appalachian Rocky Oak Woodland  
3557 | #000000 | Central Appalachian Rocky Pine-Oak Woodland  
3558 | #000000 | Edwards Plateau Limestone Grassland  
3559 | #000000 | Edwards Plateau Limestone Shrubland  
3560 | #000000 | Tamaulipan Mesquite Upland Shrub  
3561 | #000000 | Llano Uplift Acidic Herbaceous Glade  
3562 | #000000 | Tamaulipan Riparian Shrubland  
3563 | #000000 | Edwards Plateau Riparian Shrubland  
3564 | #010000 | Modified/Managed Southern Tallgrass Shrubland  
3565 | #000100 | Florida Peninsula Inland Scrub Woodland  
3566 | #000000 | Florida Dry Prairie Shruband  
3567 | #000000 | Southern Coastal Plain Blackland Prairie Woodland  
3568 | #010000 | East Gulf Coastal Plain Jackson Prairie Woodland  
3569 | #000000 | Central Atlantic Coastal Plain Wet Longleaf Pine Savanna and Shrubland  
3570 | #000000 | Southern Coastal Plain Nonriverine Cypress Dome Herbaceous  
3571 | #000000 | Southern Coastal Plain Seepage Swamp and Baygall Shrubland  
3572 | #000000 | South Florida Cypress Dome Herbaceous  
3573 | #000100 | Gulf and Atlantic Coastal Plain Small Stream Riparian Herbaceous  
3574 | #000100 | Gulf and Atlantic Coastal Plain Small Stream Riparian Shrubland  
3575 | #000000 | Caribbean Herbaceous Swamp  
3576 | #010000 | South Florida Everglades Forest  
3577 | #010000 | East Gulf Coastal Plain Wet Prairie Grassland  
3578 | #010000 | East Gulf Coastal Plain Wet Prairie Shrubland  
3579 | #010000 | Floridian Highlands Freshwater Marsh Shrubland  
3580 | #010000 | Floridian Highlands Freshwater Marsh Woodland  
3581 | #010000 | South Florida Everglades Shrubland  
3582 | #000000 | Ozark-Ouachita Oak Forest and Woodland  
3583 | #000000 | Ozark-Ouachita Shortleaf Pine-Oak Forest and Woodland  
3584 | #000100 | West Gulf Coastal Plain Hardwood Forest  
3585 | #000100 | West Gulf Coastal Plain Pine-Hardwood Forest  
3586 | #000000 | West Gulf Coastal Plain Sandhill Oak Forest and Woodland  
3587 | #000000 | West Gulf Coastal Plain Sandhill Oak and Shortleaf Pine Forest and Woodland  
3588 | #000000 | East Gulf Coastal Plain Southern Hardwood Flatwoods  
3589 | #000000 | East Gulf Coastal Plain Southern Loblolly-Hardwood Flatwoods  
3590 | #000100 | West Gulf Coastal Plain Hardwood Flatwoods  
3591 | #000100 | West Gulf Coastal Plain Pine-Hardwood Flatwoods  
3600 | #000000 | Western North American Boreal White Spruce Forest  
3601 | #000000 | Western North American Boreal Treeline White Spruce Woodland  
3602 | #000000 | Western North American Boreal Spruce-Lichen Woodland  
3603 | #000000 | Alaska Boreal White Spruce Forest  
3604 | #000000 | Western North American Boreal Mesic Black Spruce Forest  
3605 | #000000 | Western North American Boreal Mesic Birch-Aspen Forest  
3606 | #000100 | Western North American Boreal Dry Aspen-Steppe Bluff  
3607 | #000000 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
3608 | #000000 | Alaska Sub-boreal Avalanche Slope Shrubland  
3609 | #000000 | Alaska Sub-boreal Mesic Subalpine Alder Shrubland  
3610 | #000000 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland  
3611 | #010000 | Western North American Sub-boreal Mesic Bluejoint Meadow  
3612 | #010000 | Western North American Boreal Dry Grassland  
3631 | #000000 | Western North American Boreal Alpine Dwarf-Shrub Summit  
3633 | #010000 | Western North American Boreal Alpine Mesic Herbaceous Meadow  
3634 | #010000 | Western North American Boreal Alpine Dryas Dwarf-Shrubland  
3635 | #000000 | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland  
3636 | #000000 | Western North American Boreal Alpine Dwarf-Shrub-Lichen Shrubland  
3638 | #000000 | Alaska Arctic Mesic Alder Shrubland  
3639 | #000000 | Alaska Arctic Mesic-Wet Willow Shrubland  
3640 | #000000 | Aleutian Mesic-Wet Willow Shrubland  
3641 | #000000 | North Pacific Maritime Mesic Subalpine Parkland  
3642 | #000000 | Aleutian Kenai Birch-Cottonwood-Poplar Forest  
3643 | #000000 | Alaskan Pacific Maritime Alpine Dwarf-Shrubland  
3644 | #000000 | Alaskan Pacific Maritime Sitka Spruce Forest  
3645 | #010000 | Alaska Sub-boreal and Maritime Alpine Mesic Herbaceous Meadow  
3646 | #000000 | Alaskan Pacific Maritime Western Hemlock Forest  
3648 | #000000 | Alaskan Pacific Maritime Mountain Hemlock Forest  
3649 | #000000 | Alaskan Pacific Maritime Subalpine Mountain Hemlock Woodland  
3650 | #000000 | Alaskan Pacific Maritime Periglacial Woodland  
3651 | #010000 | Aleutian Mesic Herbaceous Meadow  
3652 | #000000 | Alaskan Pacific Maritime Subalpine Alder-Salmonberry Shrubland  
3653 | #010000 | Alaskan Pacific Maritime Mesic Herbaceous Meadow  
3654 | #000000 | Alaskan Pacific Maritime Sitka Spruce Beach Ridge  
3671 | #010000 | Aleutian American Dunegrass Grassland  
3672 | #000000 | Alaskan Pacific Maritime Subalpine Copperbush Shrubland  
3674 | #000000 | Alaskan Pacific Maritime Alpine Sparse Shrub and Fell-field  
3675 | #000000 | North Pacific Mesic Western Hemlock-Yellow-cedar Forest  
3677 | #000000 | Alaska Sub-boreal White-Lutz Spruce Forest and Woodland  
3678 | #000000 | Alaska Sub-boreal Mountain Hemlock-White Spruce Forest  
3679 | #000100 | Alaska Sub-boreal White Spruce Forest  
3680 | #000000 | Alaskan Pacific Maritime Avalanche Slope Shrubland  
3682 | #000000 | Alaska Arctic Scrub Birch-Ericaceous Shrubland  
3683 | #000000 | Alaska Arctic Mesic Sedge-Willow Tundra  
3684 | #000000 | Alaska Arctic Mesic Sedge-Dryas Tundra  
3685 | #010000 | Alaska Arctic Acidic Sparse Tundra  
3686 | #010000 | Alaska Arctic Non-Acidic Sparse Tundra  
3687 | #010000 | Alaska Arctic Lichen Tundra  
3688 | #010000 | Alaska Arctic Acidic Dryas Dwarf-Shrubland  
3689 | #010000 | Alaska Arctic Non-Acidic Dryas Dwarf-Shrubland  
3690 | #010000 | Alaska Arctic Dwarf-Shrubland  
3691 | #010000 | Alaska Arctic Acidic Dwarf-Shrub Lichen Tundra  
3692 | #010000 | Alaska Arctic Non-Acidic Dwarf-Shrub Lichen Tundra  
3699 | #010000 | Alaska Arctic Mesic Herbaceous Meadow  
3709 | #010000 | Alaska Arctic Marine Beach and Beach Meadow  
3718 | #000000 | Aleutian Mesic Alder-Salmonberry Shrubland  
3719 | #000000 | Aleutian Crowberry-Herbaceous Heath  
3720 | #000000 | Aleutian Mixed Dwarf-Shrub-Herbaceous Shrubland  
3725 | #010000 | Aleutian Marine Beach and Beach Meadow  
3730 | #000000 | Aleutian Sparse Heath and Fell-Field  
3731 | #000000 | Aleutian Oval-leaf Blueberry Shrubland  
3736 | #000000 | Barren  
3737 | #000000 | Snow-Ice  
3738 | #000001 | Open Water  
3739 | #000000 | North Pacific Hypermaritime Western Red-cedar-Western Hemlock Forest  
3740 | #010000 | Boreal Aquatic Beds  
3741 | #010000 | Polar Tidal Marshes and Aquatic Beds  
3742 | #010000 | Temperate Pacific Tidal Marshes, Aquatic Beds, and Intertidal Flats  
3743 | #010000 | Aleutian Herbaceous Wetlands  
3744 | #010000 | Arctic Herbaceous Wetlands  
3745 | #010000 | Boreal Herbaceous Wetlands  
3746 | #010000 | Pacific Maritime Herbaceous Wetlands  
3747 | #010000 | Arctic Sedge Meadows  
3748 | #010000 | Aleutian Shrub-Herbaceous Wetlands  
3749 | #010000 | Pacific Maritime Coastal Meadows and Slough-Levee  
3750 | #000100 | Alaska Sub-boreal Hardwood Forest  
3751 | #000000 | Boreal Coniferous Woody Wetland  
3752 | #000000 | Pacific Maritime Coniferous Woody Wetland  
3753 | #000000 | Boreal Coniferous-Deciduous Woody Wetland  
3754 | #010100 | Agriculture-Pasture and Hay  
3755 | #010100 | Agriculture-Cultivated Crops and Irrigated Agriculture  
3756 | #010000 | Arctic Dwarf Shrub Wetland  
3757 | #000000 | Boreal Dwarf Shrub Wetland  
3758 | #000000 | Pacific Maritime Dwarf Shrub Wetland  
3759 | #010000 | Recently Burned - Herb Cover  
3760 | #010000 | Recently Burned - Shrub Cover  
3761 | #010000 | Aleutian Shrub Floodplains  
3762 | #000000 | Arctic Floodplains  
3763 | #000000 | Boreal Forested Floodplains  
3764 | #000000 | Pacific Maritime Forested Floodplains  
3765 | #000000 | Boreal Black Spruce-Tussock Woodland  
3766 | #000000 | Alaskan Pacific Maritime Periglacial Shrubland  
3767 | #000000 | Developed-Open Space  
3768 | #010000 | Developed-Low Intensity  
3769 | #000000 | Developed-Medium Intensity  
3770 | #000000 | Developed-High Intensity  
3771 | #000000 | Aleutian Shrub Peatlands  
3772 | #000000 | Arctic Shrub Peatlands  
3773 | #000000 | Boreal Peatlands  
3774 | #000000 | Pacific Maritime Forested Peatlands  
3775 | #010000 | Aleutian Forested Floodplains  
3776 | #000000 | Boreal Riparian Stringer Forest and Shrubland  
3777 | #000000 | Boreal Shrub Swamp  
3778 | #000000 | Pacific Maritime Shrub Swamp  
3779 | #000100 | Alaska Boreal Hardwood Forest  
3780 | #000100 | Alaska Boreal White Spruce-Hardwood Forest  
3781 | #010000 | Arctic Shrub Sedge-Tussock-Lichen Tundra  
3782 | #010000 | Boreal Tussock Tundra  
3783 | #010000 | Arctic Shrub Tussock Tundra  
3784 | #010000 | Arctic Shrub-Tussock Tundra  
3785 | #000000 | Arctic Shrub Tundra  
3786 | #000000 | Boreal Shrub-Tussock Tundra  
3787 | #000000 | Boreal Herbaceous Floodplains  
3788 | #000000 | Boreal Shrub Floodplains  
3789 | #000100 | Alaska Sub-boreal White Spruce-Hardwood Forest  
3790 | #000000 | Pacific Maritime Shrub Floodplains  
3791 | #000000 | Aleutian Sparsely Vegetated  
3792 | #000000 | Arctic Sparsely Vegetated  
3793 | #000000 | Boreal Sparsely Vegetated  
3794 | #000000 | Pacific Maritime Sparsely Vegetated  
3795 | #000000 | Aleutian Herbaceous Peatlands  
3796 | #000000 | Arctic Herbaceous Peatlands  
3797 | #000000 | Pacific Maritime Shrub Peatlands  
3798 | #010000 | Arctic Herbaceous Sedge-Tussock-Lichen Tundra  
3799 | #010000 | Arctic Herbaceous Tussock Tundra  
3800 | #000000 | Developed-Open Space  
3801 | #010000 | Developed-Low Intensity  
3802 | #000000 | Developed-Medium Intensity  
3803 | #000000 | Developed-High Intensity  
3804 | #010100 | Agriculture  
3805 | #000001 | Water  
3806 | #010000 | Hawai'i Bog  
3807 | #010000 | Hawai'i Islands Introduced Wetland Vegetation-Tree  
3808 | #000100 | Hawai'i Lowland Rainforest  
3809 | #000100 | Hawai'i Montane Cloud Forest  
3810 | #000100 | Hawai'i Montane Rainforest  
3811 | #000000 | Hawai'i Wet Cliff and Ridge Crest Shrubland  
3812 | #010000 | Hawai'i Introduced Wetland Vegetation-Shrub  
3813 | #000000 | Hawai'i Lowland Dry Forest  
3814 | #000000 | Hawai'i Lowland Mesic Forest  
3815 | #000000 | Hawai'i Montane-Subalpine Dry Forest and Woodland  
3816 | #000000 | Hawai'i Montane-Subalpine Mesic Forest  
3817 | #000000 | Hawai'i Lowland Dry Shrubland  
3818 | #000000 | Hawai'i Lowland Mesic Shrubland  
3819 | #000000 | Hawai'i Lowland Dry Grassland  
3820 | #010000 | Hawai'i Lowland Mesic Grassland  
3821 | #000000 | Hawai'i Montane-Subalpine Dry Shrubland  
3822 | #000000 | Hawai'i Montane-Subalpine Dry Grassland  
3823 | #010000 | Hawai'i Montane-Subalpine Mesic Grassland  
3824 | #000000 | Hawai'i Alpine Dwarf-Shrubland  
3825 | #000000 | Hawai'i Dry Cliff  
3826 | #000000 | Hawai'i Dry Coastal Strand  
3827 | #000000 | Hawai'i Wet-Mesic Coastal Strand  
3828 | #010000 | Hawai'i Subalpine Mesic Shrubland  
3830 | #000000 | Barren  
3832 | #000000 | Barren  
3833 | #000100 | Pacific Islands Limestone Forest  
3834 | #000100 | Pacific Islands Littoral/Strand Vegetation  
3835 | #000000 | Pacific Islands Lowland Forest  
3836 | #000000 | Pacific Islands Mangrove Forest  
3837 | #000100 | Pacific Islands Palm Forest  
3838 | #010000 | Hawai'i Introduced Wetland Vegetation-Herbaceous  
3839 | #000000 | Pacific Islands Ravine Forest  
3840 | #000000 | Pacific Islands Savannah  
3841 | #000000 | Pacific Islands Scrub Forest/Shrub  
3842 | #000000 | Pacific Islands Swamp/Marsh  
3843 | #000000 | Pacific Islands Upland Forest  
3845 | #010000 | Hawai'i Introduced Dry Forest  
3846 | #010000 | Hawai'i Introduced Wet-Mesic Forest  
3847 | #010000 | Hawai'i Introduced Deciduous Shrubland  
3848 | #010000 | Hawai'i Introduced Perennial Grassland  
3849 | #010000 | Hawai'i Introduced Evergreen Shrubland  
3850 | #000000 | Pacific Islands Introduced Forest  
3852 | #010000 | Hawai'i Introduced Coastal Wetland Vegetation - Tree  
3853 | #010000 | Hawai'i Introduced Coastal Wetland Vegetation - Shrub  
3854 | #010000 | Hawai'i Introduced Coastal Wetland Vegetation - Herbaceous  
3855 | #000000 | Hawai'i Managed Tree Plantation  
3856 | #000000 | Pacific Islands Plantation Forest  
3857 | #000000 | Urban  
3858 | #010000 | Agriculture  
3859 | #000001 | Water  
3860 | #000000 | Caribbean High-medium density urban  
3861 | #000000 | Caribbean Low-medium density urban  
3862 | #010000 | Caribbean Herbaceous agriculture - cultivated lands  
3863 | #000100 | Caribbean Active sun coffee and mixed woody agriculture  
3864 | #010000 | Caribbean Pasture, hay or inactive agriculture  
3865 | #010000 | Caribbean Pasture, hay or other grassy areas  
3866 | #000000 | Caribbean Drought deciduous open woodland  
3867 | #000000 | Caribbean Drought deciduous dense woodland  
3868 | #000100 | Caribbean Deciduous, evergreen coastal and mixed forest or shrubland with succulents  
3869 | #000100 | Caribbean Semi-deciduous and drought deciduous forest on alluvium and non-carbonate substrates  
3870 | #000000 | Caribbean Semi-deciduous and drought deciduous forest on karst (includes semi-evergreen forest)  
3871 | #000000 | Caribbean Drought deciduous, semi-deciduous and seasonal evergreen forest on serpentine  
3872 | #000100 | Caribbean Seasonal evergreen and semi-deciduous forest on karst  
3873 | #000000 | Caribbean Seasonal evergreen and evergreen forest  
3874 | #000100 | Caribbean Seasonal evergreen forest with coconut palm  
3875 | #000000 | Caribbean Evergreen and seasonal evergreen forest on karst  
3876 | #000000 | Caribbean Evergreen forest on serpentine  
3877 | #000000 | Caribbean Elfin, sierra palm, transitional and tall cloud forest  
3878 | #010000 | Caribbean Emergent wetlands including seasonnally flooded pasture  
3879 | #000000 | Caribbean Salt or mud flats  
3880 | #000000 | Caribbean Mangrove  
3881 | #000000 | Caribbean Seasonally flooded savannahs and woodlands  
3882 | #010000 | Caribbean Pterocarpus swamp  
3883 | #000000 | Caribbean Tidally flooded evergreen dwarf-shrubland and forb vegetation  
3884 | #000000 | Quarries  
3885 | #000000 | Coastal sand and rock  
3886 | #000000 | Bare soil  
3887 | #000001 | Water  
3900 | #000000 | Western Cool Temperate Urban Deciduous Forest  
3901 | #000000 | Western Cool Temperate Urban Evergreen Forest  
3902 | #000000 | Western Cool Temperate Urban Mixed Forest  
3903 | #000000 | Western Cool Temperate Urban Herbaceous  
3904 | #000000 | Western Cool Temperate Urban Shrubland  
3905 | #000000 | Eastern Cool Temperate Urban Deciduous Forest  
3906 | #000000 | Eastern Cool Temperate Urban Evergreen Forest  
3907 | #000000 | Eastern Cool Temperate Urban Mixed Forest  
3908 | #000000 | Eastern Cool Temperate Urban Herbaceous  
3909 | #000000 | Eastern Cool Temperate Urban Shrubland  
3910 | #000000 | Western Warm Temperate Urban Deciduous Forest  
3911 | #000000 | Western Warm Temperate Urban Evergreen Forest  
3912 | #000000 | Western Warm Temperate Urban Mixed Forest  
3913 | #000000 | Western Warm Temperate Urban Herbaceous  
3914 | #000000 | Western Warm Temperate Urban Shrubland  
3915 | #000000 | Eastern Warm Temperate Urban Urban Deciduous Forest  
3916 | #000000 | Eastern Warm Temperate Urban Urban Evergreen Forest  
3917 | #000000 | Eastern Warm Temperate Urban Urban Mixed Forest  
3918 | #000000 | Eastern Warm Temperate Urban Urban Herbaceous  
3919 | #000000 | Eastern Warm Temperate Urban Urban Shrubland  
3920 | #000000 | Western Cool Temperate Developed Ruderal Deciduous Forest  
3921 | #000000 | Western Cool Temperate Developed Ruderal Evergreen Forest  
3922 | #000000 | Western Cool Temperate Developed Ruderal Mixed Forest  
3923 | #000000 | Western Cool Temperate Developed Ruderal Shrubland  
3924 | #000000 | Western Cool Temperate Developed Ruderal Grassland  
3925 | #000000 | Western Warm Temperate Developed Ruderal Deciduous Forest  
3926 | #000000 | Western Warm Temperate Developed Ruderal Evergreen Forest  
3927 | #000000 | Western Warm Temperate Developed Ruderal Mixed Forest  
3928 | #000000 | Western Warm Temperate Developed Ruderal Shrubland  
3929 | #000000 | Western Warm Temperate Developed Ruderal Grassland  
3930 | #000000 | Eastern Cool Temperate Developed Ruderal Deciduous Forest  
3931 | #000000 | Eastern Cool Temperate Developed Ruderal Evergreen Forest  
3932 | #000000 | Eastern Cool Temperate Developed Ruderal Mixed Forest  
3933 | #000000 | Eastern Cool Temperate Developed Ruderal Shrubland  
3934 | #000000 | Eastern Cool Temperate Developed Ruderal Grassland  
3935 | #000000 | Eastern Warm Temperate Developed Ruderal Deciduous Forest  
3936 | #000000 | Eastern Warm Temperate Developed Ruderal Evergreen Forest  
3937 | #000000 | Eastern Warm Temperate Developed Ruderal Mixed Forest  
3938 | #000000 | Eastern Warm Temperate Developed Ruderal Shrubland  
3939 | #000000 | Eastern Warm Temperate Developed Ruderal Grassland  
3940 | #010000 | Western Cool Temperate Undeveloped Ruderal Deciduous Forest  
3941 | #010000 | Western Cool Temperate Undeveloped Ruderal Evergreen Forest  
3942 | #010000 | Western Cool Temperate Undeveloped Ruderal Mixed Forest  
3943 | #000000 | Western Cool Temperate Undeveloped Ruderal Shrubland  
3944 | #000000 | Western Cool Temperate Undeveloped Ruderal Grassland  
3945 | #010000 | Western Warm Temperate Undeveloped Ruderal Deciduous Forest  
3946 | #010000 | Western Warm Temperate Undeveloped Ruderal Evergreen Forest  
3947 | #010000 | Western Warm Temperate Undeveloped Ruderal Mixed Forest  
3948 | #000000 | Western Warm Temperate Undeveloped Ruderal Shrubland  
3949 | #000000 | Western Warm Temperate Undeveloped Ruderal Grassland  
3950 | #010000 | Eastern Cool Temperate Undeveloped Ruderal Deciduous Forest  
3951 | #010000 | Eastern Cool Temperate Undeveloped Ruderal Evergreen Forest  
3952 | #010000 | Eastern Cool Temperate Undeveloped Ruderal Mixed Forest  
3953 | #000000 | Eastern Cool Temperate Undeveloped Ruderal Shrubland  
3954 | #000000 | Eastern Cool Temperate Undeveloped Ruderal Grassland  
3955 | #010000 | Eastern Warm Temperate Undeveloped Ruderal Deciduous Forest  
3956 | #010000 | Eastern Warm Temperate Undeveloped Ruderal Evergreen Forest  
3957 | #010000 | Eastern Warm Temperate Undeveloped Ruderal Mixed Forest  
3958 | #000000 | Eastern Warm Temperate Undeveloped Ruderal Shrubland  
3959 | #000000 | Eastern Warm Temperate Undeveloped Ruderal Grassland  
3960 | #000000 | Western Cool Temperate Orchard  
3961 | #000000 | Western Cool Temperate Vineyard  
3962 | #000000 | Western Cool Temperate Bush fruit and berries  
3963 | #010000 | Western Cool Temperate Row Crop - Close Grown Crop  
3964 | #000100 | Western Cool Temperate Row Crop  
3965 | #010000 | Western Cool Temperate Close Grown Crop  
3966 | #010100 | Western Cool Temperate Fallow/Idle Cropland  
3967 | #000000 | Western Cool Temperate Pasture and Hayland  
3968 | #000000 | Western Cool Temperate Wheat  
3969 | #000100 | Western Cool Temperate Aquaculture  
3970 | #000000 | Eastern Cool Temperate Orchard  
3971 | #000000 | Eastern Cool Temperate Vineyard  
3972 | #000000 | Eastern Cool Temperate Bush fruit and berries  
3973 | #010000 | Eastern Cool Temperate Row Crop - Close Grown Crop  
3974 | #000100 | Eastern Cool Temperate Row Crop  
3975 | #010000 | Eastern Cool Temperate Close Grown Crop  
3976 | #010100 | Eastern Cool Temperate Fallow/Idle Cropland  
3977 | #000000 | Eastern Cool Temperate Pasture and Hayland  
3978 | #000000 | Eastern Cool Temperate Wheat  
3979 | #000100 | Eastern Cool Temperate Aquaculture  
3980 | #000000 | Western Warm Temperate Orchard  
3981 | #000000 | Western Warm Temperate Vineyard  
3982 | #000000 | Western Warm Temperate Bush fruit and berries  
3983 | #010000 | Western Warm Temperate Row Crop - Close Grown Crop  
3984 | #000100 | Western Warm Temperate Row Crop  
3985 | #010000 | Western Warm Temperate Close Grown Crop  
3986 | #010100 | Western Warm Temperate Fallow/Idle Cropland  
3987 | #000000 | Western Warm Temperate Pasture and Hayland  
3988 | #000000 | Western Warm Temperate Wheat  
3989 | #000100 | Western Warm Temperate Aquaculture  
3990 | #000000 | Eastern Warm Temperate Orchard  
3991 | #000000 | Eastern Warm Temperate Vineyard  
3992 | #000000 | Eastern Warm Temperate Bush fruit and berries  
3993 | #010000 | Eastern Warm Temperate Row Crop - Close Grown Crop  
3994 | #000100 | Eastern Warm Temperate Row Crop  
3995 | #010000 | Eastern Warm Temperate Close Grown Crop  
3996 | #010100 | Eastern Warm Temperate Fallow/Idle Cropland  
3997 | #000000 | Eastern Warm Temperate Pasture and Hayland  
3998 | #000000 | Eastern Warm Temperate Wheat  
3999 | #000100 | Eastern Warm Temperate Aquaculture  
**Image Properties**
Name | Type | Description  
---|---|---  
EVT_classes | DOUBLE | Class values of the Existing Vegetation Type.  
EVT_names | STRING | Descriptive names of the Existing Vegetation Type.  
**Terms of Use**
LANDFIRE data are public domain data with no use restrictions, though if modifications or derivatives of the product(s) are created, then please add some descriptive modifier to the data set to avoid confusion.
Citations:
  * The suggested way to cite LANDFIRE products is specific to each product, so the model for citation is provided, with an example for a particular product. Producer. Year released. Product xxxxx:
    * Individual model name.
    * BpS Models and Descriptions, Online. LANDFIRE. Washington, DC. U.S. Department of Agriculture, Forest Service
    * U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA
    * The Nature Conservancy (Producers). Available- URL. Access date.
Example Citation: LANDFIRE Biophysical Settings. 2018. Biophysical setting 14420: South Texas sand sheet grassland. In: LANDFIRE Biophysical Setting Model: Map zone 36, [Online]. In: BpS Models and Descriptions. In: LANDFIRE. Washington, DC: U.S. Department of Agriculture, Forest Service; U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA: The Nature Conservancy (Producers). Available: <https://www.landfire.gov/bps-models.php> [2018, June 27]. Additional guidance on citation of LANDFIRE products can be found [here](https://landfire.gov/data/citation)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDFIRE/Vegetation/EVT/v1_4_0');
varvisualization={
bands:['EVT'],
};
Map.setCenter(-121.671,40.699,5);
Map.addLayer(dataset,visualization,'EVT');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Vegetation_EVT_v1_4_0)
[ LANDFIRE EVT (Existing Vegetation Type) v1.4.0 ](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0)
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy. LANDFIRE (LF) layers are created using predictive landscape models based on extensive …
LANDFIRE/Vegetation/EVT/v1_4_0, doi,fire,forest-biomass,landfire,nature-conservancy,usda,usgs,vegetation,wildfire 
2014-09-01T00:00:00Z/2014-09-01T00:00:00Z
17.52 -175.1 71.48 -63.66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://landfire.gov/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_EVT_v1_4_0)


