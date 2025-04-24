 
#  VNP09GA: VIIRS Surface Reflectance Daily 500m and 1km 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/VIIRS/002/VNP09GA](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_VIIRS_002_VNP09GA_sample.png) 

Dataset Availability
    2012-01-19T00:00:00Z–2025-04-18T00:00:00Z 

Dataset Provider
     [ NASA Land SIPS ](https://doi.org/10.5067/VIIRS/VNP09GA.002) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/VIIRS/002/VNP09GA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_VIIRS_002_VNP09GA) 

Cadence
    1 Day 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [npp](https://developers.google.com/earth-engine/datasets/tags/npp) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [viirs](https://developers.google.com/earth-engine/datasets/tags/viirs)
vnp09ga
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#dois) More
The Visible Infrared Imaging Radiometer Suite (VIIRS) daily surface reflectance (VNP09GA) product provides an estimate of land surface reflectance from the Suomi National Polar-Orbiting Partnership (S-NPP) VIIRS sensor. Data are provided for three imagery bands (I1, I2, I3) at nominal 500 meter resolution (~463 meter) and nine moderate-resolution bands (M1, M2, M3, M4, M5, M7, M8, M10, M11) at nominal 1 kilometer (~926 meter) resolution. The 500 meter and 1 kilometer datasets are derived through resampling the native 375 meter and 750 meter VIIRS resolutions, respectively, in the L2 input product. These bands are corrected for atmospheric conditions to provide an estimate of the surface spectral reflectance as it would be measured at ground level.
The data is temporally aggregated over each of the 16 possible passes per day. When multiple observations are present for each day, only the first of the highest-quality observations is included.
The band scale factors are already applied.
For additional information, visit the VIIRS [Land Product Quality Assessment website](https://landweb.modaps.eosdis.nasa.gov/browse?sensor=VIIRS&sat=SNPP)
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/1657/VNP09_User_Guide_V2.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf)


**Bands**
Name | Units | Min | Max | Pixel Size | Wavelength | Description  
---|---|---|---|---|---|---  
`M1` |  -0.01  |  1.6  |  1000 meters  | 0.402 - 0.422µm | 1km surface reflectance band M1  
`M2` |  -0.01  |  1.6  |  1000 meters  | 0.436 - 0.454µm | 1km surface reflectance Band M2  
`M3` |  -0.01  |  1.6  |  1000 meters  | 0.478 - 0.488µm | 1km surface reflectance band M3  
`M4` |  -0.01  |  1.6  |  1000 meters  | 0.545 - 0.565µm | 1km surface reflectance band M4  
`M5` |  -0.01  |  1.6  |  1000 meters  | 0.662 - 0.682µm | 1km surface reflectance band M5  
`M7` |  -0.01  |  1.6  |  1000 meters  | 0.846 - 0.885µm | 1km surface reflectance band M7  
`M8` |  -0.01  |  1.6  |  1000 meters  | 1.230 - 1.250µm | 1km surface reflectance band M8  
`M10` |  -0.01  |  1.6  |  1000 meters  | 1.580 - 1.640µm | 1km surface reflectance band M10  
`M11` |  -0.01  |  1.6  |  1000 meters  | 2.230 - 2.280µm | 1km surface reflectance band M11  
`I1` |  -0.01  |  1.6  |  500 meters  | 0.600 - 0.680µm | 500m surface reflectance band I1  
`I2` |  -0.01  |  1.6  |  500 meters  | 0.850 - 0.880µm | 500m surface reflectance band I2  
`I3` |  -0.01  |  1.6  |  500 meters  | 1.580 - 1.640µm | 500m surface reflectance band I3  
`SensorAzimuth` | deg |  -180  |  180  |  1000 meters  | Sensor azimuth angle  
`SensorZenith` | deg |  0  |  180  |  1000 meters  | Sensor zenith angle  
`SolarAzimuth` | deg |  -180  |  180  |  1000 meters  | Solar azimuth angle  
`SolarZenith` | deg |  0  |  180  |  1000 meters  | Solar zenith angle  
`iobs_res` |  0  |  254  |  500 meters  | Observation number  
`num_observations_1km` |  0  |  127  |  1000 meters  | Number of observations 1km  
`num_observations_500m` |  0  |  127  |  500 meters  | Number of observations 500m  
`obscov_1km` | % |  0  |  100  |  1000 meters  | Observations coverage 1km  
`obscov_500m` | % |  0  |  100  |  500 meters  | Observations coverage 500km  
`orbit_pnt` |  0  |  15  |  1000 meters  | Orbit pointer  
`QF1` |  1000 meters  | Quality flags 1  
Bitmask for QF1
  * Bits 0-1: Cloud mask quality 
    * 0: Poor
    * 1: Low
    * 2: Medium
    * 3: High
  * Bits 2-3: Cloud detection & confidence 
    * 0: Confident clear
    * 1: Probably clear
    * 2: Probably cloudy
    * 3: Confident cloudy
  * Bit 4: Day/night 
    * 0: Day
    * 1: Night
  * Bit 5: Low sun mask 
    * 0: High
    * 1: Low
  * Bits 6-7: Sun glint 
    * 0: None
    * 1: Geometry based
    * 2: Wind speed based
    * 3: Geometry and wind speed based

  
`QF2` |  1000 meters  | Quality flags 2  
Bitmask for QF2
  * Bits 0-2: Land/water background 
    * 0: Land & desert
    * 1: Land no desert
    * 2: Inland water
    * 3: Sea water
    * 4: 
    * 5: Coastal
  * Bit 3: Shadow mask 
    * 0: No cloud shadow
    * 1: Shadow
  * Bit 4: Heavy aerosol mask 
    * 0: No heavy aerosol
    * 1: Heavy aerosol
  * Bit 5: Snow/ice 
    * 0: No snow/ice
    * 1: Snow or ice
  * Bit 6: Thin cirrus reflective 
    * 0: No cloud
    * 1: Cloud
  * Bit 7: This cirrus emissive 
    * 0: No cloud
    * 1: Cloud

  
`QF3` |  1000 meters  | Quality flags 3  
Bitmask for QF3
  * Bit 0: Bad M1 SDR data 
    * 0: No
    * 1: Yes
  * Bit 1: Bad M2 SDR data 
    * 0: No
    * 1: Yes
  * Bit 2: Bad M3 SDR data 
    * 0: No
    * 1: Yes
  * Bit 3: Bad M4 SDR data 
    * 0: No
    * 1: Yes
  * Bit 4: Bad M5 SDR data 
    * 0: No
    * 1: Yes
  * Bit 5: Bad M7 SDR data 
    * 0: No
    * 1: Yes
  * Bit 6: Bad M8 SDR data 
    * 0: No
    * 1: Yes
  * Bit 7: Bad M10 SDR data 
    * 0: No
    * 1: Yes

  
`QF4` |  1000 meters  | Quality flags 4  
Bitmask for QF4
  * Bit 0: Bad M11 SDR data 
    * 0: No
    * 1: Yes
  * Bit 1: Bad I1 SDR data 
    * 0: No
    * 1: Yes
  * Bit 2: Bad I2 SDR data 
    * 0: No
    * 1: Yes
  * Bit 3: Bad I3 SDR data 
    * 0: No
    * 1: Yes
  * Bit 4: Overall quality of AOT 
    * 0: Good
    * 1: Bad
  * Bit 5: Missing AOT input data 
    * 0: No
    * 1: Yes
  * Bit 6: Invalid land AM input data 
    * 0: Valid
    * 1: Invalid AM input over land or over ocean
  * Bit 7: Missing PW input data 
    * 0: No
    * 1: Yes

  
`QF5` |  1000 meters  | Quality flags 5  
Bitmask for QF5
  * Bit 0: Missing ozone input data 
    * 0: No
    * 1: Yes
  * Bit 1: Missing surface pressure input data 
    * 0: No
    * 1: Yes
  * Bit 2: Overall quality M1 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 3: Overall quality M2 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 4: Overall quality M3 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 5: Overall quality M4 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 6: Overall quality M5 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 7: Overall quality M7 surface reflection data 
    * 0: Good
    * 1: Bad

  
`QF6` |  1000 meters  | Quality flags 6  
Bitmask for QF6
  * Bit 0: Overall quality M8 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 1: Overall quality M10 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 2: Overall quality M11 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 3: Overall quality I1 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 4: Overall quality I2 surface reflection data 
    * 0: Good
    * 1: Bad
  * Bit 5: Overall quality I3 surface reflection data 
    * 0: Good
    * 1: Bad

  
`QF7` |  1000 meters  | Quality flags 7  
Bitmask for QF7
  * Bit 0: Snow present 
    * 0: No
    * 1: Yes
  * Bit 1: Adjacent to cloud 
    * 0: No
    * 1: Yes
  * Bits 2-3: Aerosol quantity 
    * 0: Climatology
    * 1: Low
    * 2: Average
    * 3: High
  * Bit 4: Thin cirrus flag 
    * 0: No
    * 1: Yes

  
`land_water_mask` |  0  |  7  |  1000 meters  | Land/water mask.  
**land_water_mask Class Table**
Value | Color | Description  
---|---|---  
0 | #0000ff | Shallow_Ocean  
1 | #008000 | Land  
2 | #ffff00 | Coastline  
3 | #808000 | Shallow_Inland  
4 | #00ffff | Ephemeral  
5 | #800000 | Deep_Inland  
6 | #ff0000 | Continental  
7 | #000080 | Deep_Ocean  
**Terms of Use**
LP DAAC NASA data are freely accessible; however, when an author publishes these data or works based on the data, it is requested that the author cite the datasets within the text of the publication and include a reference to them in the reference list.
Citations:
  * Vermote, E., Franch, B., Claverie, M. (2023). VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V002 [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center.


  * [ https://doi.org/10.5067/VIIRS/VNP09GA.002 ](https://doi.org/10.5067/VIIRS/VNP09GA.002)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/VIIRS/002/VNP09GA')
.filter(ee.Filter.date('2014-05-01','2014-05-31'));
varrgb=dataset.select(['M5','M4','M3']);
varrgbVis={
min:0.0,
max:0.3
};
Map.setCenter(17.93,7.71,2);
Map.addLayer(rgb,rgbVis,'RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_VIIRS_002_VNP09GA)
[ VNP09GA: VIIRS Surface Reflectance Daily 500m and 1km ](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA)
The Visible Infrared Imaging Radiometer Suite (VIIRS) daily surface reflectance (VNP09GA) product provides an estimate of land surface reflectance from the Suomi National Polar-Orbiting Partnership (S-NPP) VIIRS sensor. Data are provided for three imagery bands (I1, I2, I3) at nominal 500 meter resolution (~463 meter) and nine moderate-resolution bands (M1, …
NASA/VIIRS/002/VNP09GA, daily,nasa,noaa,npp,reflectance,satellite-imagery,sr,viirs 
2012-01-19T00:00:00Z/2025-04-18T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/VIIRS/VNP09GA.002 ](https://doi.org/https://doi.org/10.5067/VIIRS/VNP09GA.002)
  * [ https://doi.org/10.5067/VIIRS/VNP09GA.002 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP09GA)


