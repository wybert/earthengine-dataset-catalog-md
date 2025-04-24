 
#  MethaneSAT L4 Area Sources Public Preview V1.0.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![projects/edf-methanesat-ee/assets/public-preview/L4area](https://developers.google.com/earth-engine/datasets/images/edf-methanesat-ee/projects_edf-methanesat-ee_assets_public-preview_L4area_sample.png)
info
This dataset is part of a Publisher Catalog, and not managed by Google Earth Engine. Contact [EDF-MethaneSAT](https://www.methanesat.org/contact) for bugs or [view more datasets](https://developers.google.com/earth-engine/datasets/publisher/edf-methanesat-ee) from the Environmental Defense Fund - MethaneSAT Catalog. [Learn more about Publisher datasets](https://developers.google.com/earth-engine/datasets/publisher). 
[ ![Catalog Owner Logo](https://developers.google.com/static/earth-engine/datasets/logos/edf-methanesat-ee_logo.png) ](https://www.methanesat.org/data) 

Catalog Owner
    Environmental Defense Fund - MethaneSAT 

Dataset Availability
    2006-01-24T00:00:00Z–2025-01-17T00:00:00Z 

Dataset Provider
     [ Environmental Defense Fund - MethaneSAT ](https://methanesat.org) 

Contact
    [EDF-MethaneSAT](https://www.methanesat.org/contact) 

Earth Engine Snippet
     `    ee.ImageCollection("projects/edf-methanesat-ee/assets/public-preview/L4area")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/edf-methanesat-ee/projects_edf-methanesat-ee_assets_public-preview_L4area) 

Cadence
    7 Days 

Tags
     [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [edf](https://developers.google.com/earth-engine/datasets/tags/edf) [edf-methanesat-ee](https://developers.google.com/earth-engine/datasets/tags/edf-methanesat-ee) [emissions](https://developers.google.com/earth-engine/datasets/tags/emissions) [ghg](https://developers.google.com/earth-engine/datasets/tags/ghg) [methane](https://developers.google.com/earth-engine/datasets/tags/methane) [methanesat](https://developers.google.com/earth-engine/datasets/tags/methanesat) [publisher-dataset](https://developers.google.com/earth-engine/datasets/tags/publisher-dataset)
[Description](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#citations) More
_The dispersed area emissions model is still in development and not representative of a final product._
This early "Public Preview" dataset provides high precision data for methane emissions over wide areas from the oil and gas sector. This includes total emissions that come from discrete point sources and dispersed area sources. These emissions data come from the Appalachian, Permian, and Uinta basins in the United States; the Amu Darya and South Caspian basins in Turkmenistan; and the Maturin basin in Venezuela. These novel measurements demonstrate the importance of quantifying total methane emissions with high resolution to meet global methane mitigation goals.
Dispersed area emissions are estimated from methane concentration observations in the form of column-averaged dry-air mole fractions of methane (XCH4) using an inverse model. An atmospheric transport model - the Stochastic Time-Inverted Lagrangian Transport (STILT) model; [Lin et al. (2003)](https://doi.org/10.1029/2002JD003161), [Fasoli et al. (2018)](https://doi.org/10.5194/gmd-11-2813-2018); driven by meteorological data from the National Centers for Environmental Prediction ([NCEP](https://www.weather.gov/ncep/)) Global Forecast System ([GFS](https://www.emc.ncep.noaa.gov/emc/pages/numerical_forecast_systems/gfs.php)) - is used to link variations in observed XCH4 to potential upwind sources.
The sources of variation in observed XCH4 include 1) dispersed area emissions, 2) discrete point sources, 3) inflow across the domain boundary, and 4) the background concentration. Discrete point source emissions are determined individually using a divergence integral approach described by [Chulakadaba et al. (2023)](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-822/) and prescribed to the inverse model. XCH4 inflow across the domain boundary and dispersed area emissions are then estimated simultaneously using an inverse model with an enforced non-negative solution. Total emissions are the sum of dispersed area and point source emissions.
This set of initial observations made by MethaneSAT are consistent with independent empirical data where available from other sources. Contact the data provider for more information about the project at this link: <https://www.methanesat.org/contact/>.
**Bands**
Name | Units | Min | Max | Pixel Size | Description  
---|---|---|---|---|---  
`flux` | kg/h |  0*  |  625*  |  5000 meters  | Methane emissions traceable to a 5km^2 area.  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
area_source_total_kg_hr | INT | Total value of area emissions for this collection in kg/hr. Missing values are indicated by -1.  
collection_id | STRING | satellite observation number.  
processing_id | STRING | (internal) Processing run identifier that represents the calculations that led to the features. It is not an attribute describing the flight, but the processing pipeline.  
target_id | INT | Satellite Target ID.  
time_coverage_end | STRING | Data collection end time in YYYY-MM-DDThh:mm:ssZ format STRING (ISO 8601).  
time_coverage_start | STRING | Data collection start time in YYYY-MM-DDThh:mm:ssZ format STRING (ISO 8601).  
**Terms of Use**
Use of this data is subject to [MethaneSAT's Content License Terms of Use](https://www.methanesat.org/sites/default/files/2025-02/MethaneSAT%20-%20Content%20License%20Terms%20of%20Use%20%28Revised%202-12-2025%29%5B25%5D.pdf).
YOUR LICENSE TO ACCESS THE DATA
  * We hereby grant you a limited, nonexclusive, nonassignable, nontransferable, revocable license to use, reproduce, publish, make derivative works, display and perform publicly any Data first made available through the Platform pursuant to the terms set forth herein, subject to your agreement to, compliance with and satisfaction of these Terms of Use (the “License”)
  * You agree to and acknowledge the following restrictions relating to the License:
    * (1) To access the Data, you must complete this [Request Form](https://docs.google.com/forms/d/e/1FAIpQLSdzJDwpTs99tMT5bGk0gep10_UEHi64kGtJWat1FrP8ZjwQcA/viewform), which will ask for your contact information, intended use cases, target customers, and other details that will assist MethaneSAT’s understanding of how the Data is being used by you, and, upon submission of such form, MethaneSAT may (in its sole discretion) grant you access to the Data;
    * (2) With respect to certain aspects of the Data as described herein, you may use methane concentrations, in parts per billion or any other unit of concentration (“Level 3 Data” or “L3 Data”) and methane emission fluxes, in kilograms per hour (“Level 4 Data” or “L4 Data”) for:
      * (i) internal business evaluation and testing,
      * (ii) commercial applications, such as developing and selling derivative products and services that incorporate or are informed by the L3 Data or L4 Data,
      * (iii) distribution of the Data made available herein to wholly controlled affiliates of which you will be responsible and liable on their behalf for adherence to these Terms of Use, or
      * (iv) methane mitigation activities, including both commercial and non-commercial initiatives;
    * (3) You are strictly prohibited from using L3 Data to calculate or derive L4 Data or any similar outputs, except and exclusively for internal use purposes and not to distribute to any third party;
    * (4) You may not distribute, publish, sublicense, sell, or otherwise provide L3 Data or L4 Data in its raw form to any third parties, provided, however, that you may develop, commercialize, and sell derivative products and services based on your review of the L3 Data and L4 Data, provided, further (and for the avoidance of doubt), that the underlying L3 Data and L4 Data (in its raw form) shall not be shared nor made directly accessible to end users/third parties; and
    * (5) That you are not permitted to distribute the Data on any other platform that would make the Data available to third parties, other than to you and your wholly controlled affiliates.
  * As a condition of accessing the Data, you further agree and acknowledge that:
    * (1) MethaneSAT seeks information about how the Data will be used and, as such, you shall use best efforts, upon request by MethaneSAT, that you will
      * (i) provide feedback on the quality of the Data and any proposed improvements thereto, and
      * (ii) share anonymized insights on target customers and market applications;
    * (2) MethaneSAT may use aggregated or anonymized insights to refine its Data offerings.


ATTRIBUTION
If you share or use the Data in any manner with any third parties, you must:
  * Explicitly state to these third parties that they are agreeing to be bound by the Terms of Use;
  * Display a citation that states: “Data from MethaneSAT” and “Download the most current dataset at Google Earth Engine and/or Google Cloud”; and
  * Explicitly state to these third parties that, if such third party creates a further project containing the Data, any such users of that project must also agree to be bound by these Terms of Use.


Citations:
  * Chulakadabba, A., Sargent, M., Lauvaux, T., Benmergui, J. S., Franklin, J. E., Chan Miller, C., Wilzewski, J. S., Roche, S., Conway, E., Souri, A. H., Sun, K., Luo, B., Hawthrone, J., Samra, J., Daube, B. C., Liu, X., Chance, K., Li, Y., Gautam, R., Omara, M., Rutherford, J. S., Sherwin, E. D., Brandt, A., and Wofsy, S. C. 2023. Methane point source quantification using MethaneAIR: a new airborne imaging spectrometer, Atmos. Meas. Tech., 16, 5771-5785. [doi:10.5194/amt-16-5771-2023](https://doi.org/10.5194/amt-16-5771-2023),


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area#code-editor-javascript-sample) More
```
// Request access to this data by filling out the form at: https://forms.gle/jqw4Mvr63dsV1fUF8
vardataset=ee.ImageCollection("projects/edf-methanesat-ee/assets/public-preview/L4area")
.filterDate('2024-06-01','2025-01-31');
varcolorRange=[
"#F9ED3B","#F7E33A","#F5D838","#F1C335","#EEB934","#ECAE32","#EB9E2F",
"#EA8D2C","#EC8129","#F16823","#D85627","#BF442C","#983623","#70281A"
];
varfluxVisParams={
min:0,
max:625,
palette:colorRange,
};
Map.setCenter(-98.72,36.49,4);
Map.addLayer(dataset,fluxVisParams,'Methane area sources flux');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/edf-methanesat-ee/projects_edf-methanesat-ee_assets_public-preview_L4area)
[ MethaneSAT L4 Area Sources Public Preview V1.0.0 ](https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area)
The dispersed area emissions model is still in development and not representative of a final product. This early "Public Preview" dataset provides high precision data for methane emissions over wide areas from the oil and gas sector. This includes total emissions that come from discrete point sources and dispersed area …
projects/edf-methanesat-ee/assets/public-preview/L4area, atmosphere,climate,edf,edf-methanesat-ee,emissions,ghg,methane,methanesat,publisher-dataset 
2006-01-24T00:00:00Z/2025-01-17T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://methanesat.org)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_edf-methanesat-ee_assets_public-preview_L4area)


