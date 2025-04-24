 
#  SLGA: Soil and Landscape Grid of Australia (Soil Attributes) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CSIRO/SLGA](https://developers.google.com/earth-engine/datasets/images/CSIRO/CSIRO_SLGA_sample.png) 

Dataset Availability
    1950-01-01T00:00:00Z–2013-12-31T00:00:00Z 

Dataset Provider
     [ CSIRO/SLGA ](https://www.clw.csiro.au/aclep/soilandlandscapegrid/) 

Earth Engine Snippet
     `    ee.ImageCollection("CSIRO/SLGA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSIRO/CSIRO_SLGA) 

Tags
     [australia](https://developers.google.com/earth-engine/datasets/tags/australia) [csiro](https://developers.google.com/earth-engine/datasets/tags/csiro) [soil](https://developers.google.com/earth-engine/datasets/tags/soil) [tern](https://developers.google.com/earth-engine/datasets/tags/tern)
digital-soil-mapping
globalsoilmap
slga
soil-depth
[Description](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#dois) More
The Soil and Landscape Grid of Australia (SLGA) is a comprehensive dataset of soil attributes across Australia at 3 arc-second resolution (~90m pixels). The surfaces are the outcomes from modelling that describe the spatial distribution of the soil attributes using existing soil data and environmental covariates. See [Viscarra Rossel et al (2015)](https://www.publish.csiro.au/sr/SR14366) for further details. The SLGA can be used in studies of vadose zone processes, including solute transport, groundwater and nutrient fluxes beyond the root zone, as well as a wide spectrum of ecological, hydrological, and broader environmental applications.
Each product contains six digital soil attribute maps and their upper and lower confidence limits, representing the soil attribute at six depths: 0-5cm, 5-15cm, 15-30cm, 30-60cm, 60-100cm, and 100-200cm. These depths and soil attributes are consistent with the specifications of [GlobalSoilMap](https://www.isric.org/projects/globalsoilmapnet).
This collection has 12 images. Ten of them contain data for GSM primary soil attributes; the other two contain regolith depth and soil depth GSM attributes.
Attribute | Description | Code | # of Bands  
---|---|---|---  
Bulk Density (whole earth) | Bulk density of the whole soil (including coarse fragments) in mass per unit volume by a method equivalent to the core method | BDW | 18  
Organic Carbon | Mass fraction of carbon by weight in the < 2mm soil material as determined by dry combustion at 900 Celsius | SOC | 18  
Clay | < 2µm mass fraction of the <2mm soil material determined using the pipette method | CLY | 18  
Silt | 2-20µm mass fraction of the < 2mm soil material determined using the pipette method | SLT | 18  
Sand | 20µm - 2mm mass fraction of the < 2mm soil material determined using the pipette method | SND | 18  
pH (CaCl2) | pH of 1:5 soil/0.01M calcium chloride extract | pHc | 18  
Available Water Capacity | Available water capacity computed for each of the specified depth increments | AWC | 18  
Total Nitrogen | Mass fraction of total nitrogen in the soil by weight | NTO | 18  
Total Phosphorus | Mass fraction of total phosphorus in the soil by weight | PTO | 18  
Effective Cation Exchange Capacity | Cations extracted using barium chloride (BaCl2) plus exchangeable H + Al | ECE | 18  
Depth of Regolith | Depth to hard rock. Depth is inclusive of all regolith. | DER | 3  
Depth of Soil | Depth of soil profile (A & B horizons) | DES | 3  
**Pixel Size** 92.77 meters 
**Bands**
Name | Units | Description  
---|---|---  
`AWC_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`AWC_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`AWC_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`AWC_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`AWC_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`AWC_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`AWC_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`AWC_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`AWC_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`AWC_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`AWC_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`AWC_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`AWC_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`AWC_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`AWC_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`AWC_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`AWC_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`AWC_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`BDW_000_005_EV` | g/cm^3 | The soil attribute's estimated value at depth 0-5cm  
`BDW_000_005_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`BDW_000_005_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`BDW_005_015_EV` | g/cm^3 | The soil attribute's estimated value at depth 5-15cm  
`BDW_005_015_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`BDW_005_015_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`BDW_015_030_EV` | g/cm^3 | The soil attribute's estimated value at depth 15-30cm  
`BDW_015_030_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`BDW_015_030_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`BDW_030_060_EV` | g/cm^3 | The soil attribute's estimated value at depth 30-60cm  
`BDW_030_060_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`BDW_030_060_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`BDW_060_100_EV` | g/cm^3 | The soil attribute's estimated value at depth 60-100cm  
`BDW_060_100_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`BDW_060_100_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`BDW_100_200_EV` | g/cm^3 | The soil attribute's estimated value at depth 100-200cm  
`BDW_100_200_05` | g/cm^3 | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`BDW_100_200_95` | g/cm^3 | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`CLY_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`CLY_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`CLY_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`CLY_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`CLY_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`CLY_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`CLY_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`CLY_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`CLY_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`CLY_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`CLY_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`CLY_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`CLY_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`CLY_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`CLY_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`CLY_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`CLY_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`CLY_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`DER_000_200_EV` | m | The estimated value for the regolith depth  
`DER_000_200_05` | m | The 5th percentile confidence limit for the regolith depth  
`DER_000_200_95` | m | The 95th percentile confidence limit for the regolith depth  
`DES_000_200_EV` | m | The estimated value for the soil depth  
`DES_000_200_05` | m | The 5th percentile confidence limit for the soil depth  
`DES_000_200_95` | m | The 5th percentile confidence limit for the soil depth  
`ECE_000_005_EV` | meq/100g | The soil attribute's estimated value at depth 0-5cm  
`ECE_000_005_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`ECE_000_005_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`ECE_005_015_EV` | meq/100g | The soil attribute's estimated value at depth 5-15cm  
`ECE_005_015_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`ECE_005_015_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`ECE_015_030_EV` | meq/100g | The soil attribute's estimated value at depth 15-30cm  
`ECE_015_030_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`ECE_015_030_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`ECE_030_060_EV` | meq/100g | The soil attribute's estimated value at depth 30-60cm  
`ECE_030_060_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`ECE_030_060_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`ECE_060_100_EV` | meq/100g | The soil attribute's estimated value at depth 60-100cm  
`ECE_060_100_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`ECE_060_100_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`ECE_100_200_EV` | meq/100g | The soil attribute's estimated value at depth 100-200cm  
`ECE_100_200_05` | meq/100g | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`ECE_100_200_95` | meq/100g | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`NTO_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`NTO_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`NTO_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`NTO_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`NTO_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`NTO_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`NTO_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`NTO_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`NTO_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`NTO_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`NTO_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`NTO_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`NTO_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`NTO_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`NTO_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`NTO_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`NTO_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`NTO_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`pHc_000_005_EV` | The soil attribute's estimated value at depth 0-5cm  
`pHc_000_005_05` | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`pHc_000_005_95` | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`pHc_005_015_EV` | The soil attribute's estimated value at depth 5-15cm  
`pHc_005_015_05` | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`pHc_005_015_95` | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`pHc_015_030_EV` | The soil attribute's estimated value at depth 15-30cm  
`pHc_015_030_05` | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`pHc_015_030_95` | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`pHc_030_060_EV` | The soil attribute's estimated value at depth 30-60cm  
`pHc_030_060_05` | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`pHc_030_060_95` | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`pHc_060_100_EV` | The soil attribute's estimated value at depth 60-100cm  
`pHc_060_100_05` | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`pHc_060_100_95` | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`pHc_100_200_EV` | The soil attribute's estimated value at depth 100-200cm  
`pHc_100_200_05` | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`pHc_100_200_95` | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`PTO_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`PTO_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`PTO_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`PTO_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`PTO_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`PTO_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`PTO_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`PTO_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`PTO_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`PTO_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`PTO_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`PTO_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`PTO_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`PTO_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`PTO_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`PTO_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`PTO_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`PTO_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`SLT_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`SLT_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`SLT_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`SLT_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`SLT_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`SLT_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`SLT_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`SLT_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`SLT_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`SLT_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`SLT_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`SLT_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`SLT_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`SLT_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`SLT_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`SLT_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`SLT_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`SLT_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`SND_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`SND_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`SND_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`SND_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`SND_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`SND_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`SND_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`SND_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`SND_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`SND_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`SND_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`SND_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`SND_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`SND_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`SND_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`SND_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`SND_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`SND_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
`SOC_000_005_EV` | % | The soil attribute's estimated value at depth 0-5cm  
`SOC_000_005_05` | % | The soil attribute's 5th percentile confidence limit at depth 0-5cm  
`SOC_000_005_95` | % | The soil attribute's 95th percentile confidence limit at depth 0-5cm  
`SOC_005_015_EV` | % | The soil attribute's estimated value at depth 5-15cm  
`SOC_005_015_05` | % | The soil attribute's 5th percentile confidence limit at depth 5-15cm  
`SOC_005_015_95` | % | The soil attribute's 95th percentile confidence limit at depth 5-15cm  
`SOC_015_030_EV` | % | The soil attribute's estimated value at depth 15-30cm  
`SOC_015_030_05` | % | The soil attribute's 5th percentile confidence limit at depth 15-30cm  
`SOC_015_030_95` | % | The soil attribute's 95th percentile confidence limit at depth 15-30cm  
`SOC_030_060_EV` | % | The soil attribute's estimated value at depth 30-60cm  
`SOC_030_060_05` | % | The soil attribute's 5th percentile confidence limit at depth 30-60cm  
`SOC_030_060_95` | % | The soil attribute's 95th percentile confidence limit at depth 30-60cm  
`SOC_060_100_EV` | % | The soil attribute's estimated value at depth 60-100cm  
`SOC_060_100_05` | % | The soil attribute's 5th percentile confidence limit at depth 60-100cm  
`SOC_060_100_95` | % | The soil attribute's 95th percentile confidence limit at depth 60-100cm  
`SOC_100_200_EV` | % | The soil attribute's estimated value at depth 100-200cm  
`SOC_100_200_05` | % | The soil attribute's 5th percentile confidence limit at depth 100-200cm  
`SOC_100_200_95` | % | The soil attribute's 95th percentile confidence limit at depth 100-200cm  
**Image Properties**
Name | Type | Description  
---|---|---  
anzlic_topic_category | STRING | Topic category according to Australia's and New Zealand's Spatial Information Council  
contact | STRING | General contact  
contact_gee_ingestion | STRING | Who to contact for issues related to Earth Engine ingestion  
contact_lead_researcher | STRING | Lead Researcher  
contact_project_director | STRING | Project Director  
contact_project_leader | STRING | Project Leader  
country | STRING | Country this asset covers  
country_code | STRING | ISO country code  
credit | STRING | Credit  
datatype | STRING | 'Numeric Value' or 'Categorical Value'  
datatype_code | STRING | 'N' or 'C'  
date_created | DOUBLE | Date of publication  
estimate_spatial_support | STRING | GSM v2.3 tier 1 or 2, 'P' or 'B'  
estimate_spatial_support_code | STRING | 'Point estimate' or 'Block estimate'  
field_of_research | STRING | 'Soil sciences not elsewhere classified'  
gsm_type | STRING | GlobalSoilMap attribute type  
product_type | STRING | 'Data mining-kriging methods', 'Composite models. Various modelling combined with variance weighted averaging', or 'Polygon disaggregation methods'  
product_type_code | STRING | 'N', 'C', or 'D'  
project | STRING | ' National Soil Attribute Maps - Composite product', 'Australia-wide 3D Soil Attribute Maps', 'Western Australia Polygon Dissaggregation (DAFW)', 'South Australia Polygon Dissaggregation (DEWNR)', or 'Tasmania (DPIWE) Soil Attribute Mapping'  
project_code | STRING | 'NAT', 'TRN', 'WAT', 'SAT', or 'TAS'  
provider_url | STRING | Provider URL  
rights_statement | STRING | Rights statement  
**Terms of Use**
All products developed by the Soil and Landscape Grid of Australia are available at no cost under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/) (CC BY) and users should read the [Disclaimer](https://www.clw.csiro.au/aclep/soilandlandscapegrid/About-Disclaimer.html).
Citations:
  * Viscarra Rossel, Raphael; Chen, Charlie; Grundy, Mike; Searle, Ross; Clifford, David; Odgers, Nathan; Holmes, Karen; Griffin, Ted; Liddicoat, Craig; Kidd, Darren (2014): Soil and Landscape Grid National Soil Attribute Maps - SOIL ATTRIBUTE Release 1. v2. CSIRO. Data Collection [doi:10.1071/SR14366](https://doi.org/10.1071/SR14366).
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Bulk Density - Whole Earth (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., Kidd, D., & Clifford, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Clay (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Effective Cation Exchange Capacity (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - pH - CaCl2 (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., Kidd, D., & Clifford, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Sand (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., Kidd, D., & Clifford, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Silt (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Soil Depth (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Total Nitrogen (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Total Phosphorus (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Viscarra Rossel, R., Chen, C., Grundy, M., Searle, R., Clifford, D., Odgers, N., Holmes, K., Griffin, T., Liddicoat, C., & Kidd, D. (2014). _Soil and Landscape Grid National Soil Attribute Maps - Organic Carbon (3" resolution) - Release 1_ [Data set]. CSIRO.
  * Wilford, J., Searle, R., Thomas, M., & Grundy, M. (2015). _Soil and Landscape Grid National Soil Attribute Maps - Depth of Regolith (3" resolution) - Release 2_ [Data set]. CSIRO.


  * [ https://doi.org/10.4225/08/546ED604ADD8A ](https://doi.org/10.4225/08/546ED604ADD8A)
  * [ https://doi.org/10.4225/08/546EE212B0048 ](https://doi.org/10.4225/08/546EE212B0048)
  * [ https://doi.org/10.4225/08/546EEE35164BF ](https://doi.org/10.4225/08/546EEE35164BF)
  * [ https://doi.org/10.4225/08/546F091C11777 ](https://doi.org/10.4225/08/546F091C11777)
  * [ https://doi.org/10.4225/08/546F17EC6AB6E ](https://doi.org/10.4225/08/546F17EC6AB6E)
  * [ https://doi.org/10.4225/08/546F29646877E ](https://doi.org/10.4225/08/546F29646877E)
  * [ https://doi.org/10.4225/08/546F48D6A6D48 ](https://doi.org/10.4225/08/546F48D6A6D48)
  * [ https://doi.org/10.4225/08/546F540FE10AA ](https://doi.org/10.4225/08/546F540FE10AA)
  * [ https://doi.org/10.4225/08/546F564AE11F9 ](https://doi.org/10.4225/08/546F564AE11F9)
  * [ https://doi.org/10.4225/08/546F617719CAF ](https://doi.org/10.4225/08/546F617719CAF)
  * [ https://doi.org/10.4225/08/547523BB0801A ](https://doi.org/10.4225/08/547523BB0801A)
  * [ https://doi.org/10.4225/08/55C9472F05295 ](https://doi.org/10.4225/08/55C9472F05295)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('CSIRO/SLGA')
.filter(ee.Filter.eq('attribute_code','DES'));
varsoilDepth=dataset.select('DES_000_200_EV');
varsoilDepthVis={
min:0.1,
max:1.84,
palette:['8d6738','252525'],
};
Map.setCenter(132.495,-21.984,5);
Map.addLayer(soilDepth,soilDepthVis,'Soil Depth');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSIRO/CSIRO_SLGA)
[ SLGA: Soil and Landscape Grid of Australia (Soil Attributes) ](https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA)
The Soil and Landscape Grid of Australia (SLGA) is a comprehensive dataset of soil attributes across Australia at 3 arc-second resolution (~90m pixels). The surfaces are the outcomes from modelling that describe the spatial distribution of the soil attributes using existing soil data and environmental covariates. See Viscarra Rossel et …
CSIRO/SLGA, australia,csiro,soil,tern 
1950-01-01T00:00:00Z/2013-12-31T00:00:00Z
-44.15 113 -9.97 154 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.4225/08/55C9472F05295 ](https://doi.org/https://www.clw.csiro.au/aclep/soilandlandscapegrid/)
  * [ https://doi.org/10.4225/08/55C9472F05295 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CSIRO_SLGA)


