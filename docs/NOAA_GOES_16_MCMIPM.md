 
#  GOES-16 MCMIPM Series ABI Level 2 Cloud and Moisture Imagery Mesoscale 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NOAA/GOES/16/MCMIPM](https://developers.google.com/earth-engine/datasets/images/NOAA/NOAA_GOES_16_MCMIPM_sample.png) 

Dataset Availability
    2017-07-10T00:00:00Z–2025-04-07T18:32:55.300000Z 

Dataset Provider
     [ NOAA ](https://data.noaa.gov/onestop/collections/details/385d4d38-267e-40c1-859d-b5d8a079c5df) 

Earth Engine Snippet
     `    ee.ImageCollection("NOAA/GOES/16/MCMIPM")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_GOES_16_MCMIPM) 

Cadence
    10 Minutes 

Tags
     [abi](https://developers.google.com/earth-engine/datasets/tags/abi) [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [goes](https://developers.google.com/earth-engine/datasets/tags/goes) [goes-16](https://developers.google.com/earth-engine/datasets/tags/goes-16) [goes-east](https://developers.google.com/earth-engine/datasets/tags/goes-east) [goes-r](https://developers.google.com/earth-engine/datasets/tags/goes-r) [mcmip](https://developers.google.com/earth-engine/datasets/tags/mcmip) [nesdis](https://developers.google.com/earth-engine/datasets/tags/nesdis) [noaa](https://developers.google.com/earth-engine/datasets/tags/noaa) [ospo](https://developers.google.com/earth-engine/datasets/tags/ospo) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [weather](https://developers.google.com/earth-engine/datasets/tags/weather)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#dois) More
The Cloud and Moisture Imagery products are all at 2km resolution. Bands 1-6 are reflective. The dimensionless "reflectance factor" quantity is normalized by the solar zenith angle. These bands support the characterization of clouds, vegetation, snow/ice, and aerosols. Bands 7-16 are emissive. The brightness temperature at the Top-Of-Atmosphere (TOA) is measured in Kelvin. These bands support the characterization of the surface, clouds, water vapor, ozone, volcanic ash, and dust based on emissive properties.
The locations of domains 1 and 2 change over time.
[README](https://www.ncei.noaa.gov/products/satellite/goes-r-series)
NOAA's Office of Satellite and Product Operations has a [General Satellite Messages](https://www.ospo.noaa.gov/Operations/messages.html) channel with status updates.
**Pixel Size** 2000 meters 
**Bands**
Name | Units | Min | Max | Wavelength | Description  
---|---|---|---|---|---  
`CMI_C01` | Reflectance factor |  0  |  1.3  | 0.45-0.49µm | Visible - Blue Daytime aerosol over land, coastal water mapping.  
`DQF_C01` |  0  |  4  | Data quality flags  
`CMI_C02` | Reflectance factor |  0  |  1.3  | 0.59-0.69µm | Visible - Red Daytime clouds, fog, insolation, winds  
`DQF_C02` |  0  |  4  | Data quality flags  
`CMI_C03` | Reflectance factor |  0  |  1.3  | 0.846-0.885µm | Near-IR - Veggie Daytime vegetation, burn scar, aerosol over water, winds  
`DQF_C03` |  0  |  4  | Data quality flags  
`CMI_C04` | Reflectance factor |  0  |  1.3  | 1.371-1.386µm | Near-IR - Cirrus Daytime cirrus cloud  
`DQF_C04` |  0  |  4  | Data quality flags  
`CMI_C05` | Reflectance factor |  0  |  1.3  | 1.58-1.64µm | Near-IR - Snow/Ice Daytime cloud-top phase and particle size, snow  
`DQF_C05` |  0  |  4  | Data quality flags  
`CMI_C06` | Reflectance factor |  0  |  1.3  | 2.225-2.275µm | Near IR - Cloud Particle Size Daytime land, cloud properties, particle size, vegetation, snow  
`DQF_C06` |  0  |  4  | Data quality flags  
`CMI_C07` | K |  197.31  |  411.86  | 3.80-4.00µm | Infrared - Shortwave Window Brightness  
`DQF_C07` |  0  |  4  | Data quality flags  
`CMI_C08` | K |  138.05  |  311.06  | 5.77-6.6µm | Infrared - Upper-level water vapor High-level atmospheric water vapor, winds, rainfall Brightness  
`DQF_C08` |  0  |  4  | Data quality flags  
`CMI_C09` | K |  137.7  |  311.08  | 6.75-7.15µm | Infrared - Mid-level water vapor Mid-level atmospheric water vapor, winds, rainfall Brightness  
`DQF_C09` |  0  |  4  | Data quality flags  
`CMI_C10` | K |  126.91  |  331.2  | 7.24-7.44µm | Infrared - Lower-level water vapor Lower-level water vapor, winds, and sulfur dioxide Brightness  
`DQF_C10` |  0  |  4  | Data quality flags  
`CMI_C11` | K |  127.69  |  341.3  | 8.3-8.7µm | Infrared - Cloud-top phase Total water for stability, cloud phase, dust, sulfur dioxide, rainfall Brightness  
`DQF_C11` |  0  |  4  | Data quality flags  
`CMI_C12` | K |  117.49  |  311.06  | 9.42-9.8µm | Infrared - Ozone Total ozone, turbulence, winds  
`DQF_C12` |  0  |  4  | Data quality flags  
`CMI_C13` | K |  89.62  |  341.27  | 10.1-10.6µm | Infrared - "Clean" longwave window Surface and clouds Brightness  
`DQF_C13` |  0  |  4  | Data quality flags  
`CMI_C14` | K |  96.19  |  341.28  | 10.8-11.6µm | Infrared - Longwave window Imagery, sea surface temperature, clouds, rainfall Brightness  
`DQF_C14` |  0  |  4  | Data quality flags  
`CMI_C15` | K |  97.38  |  341.28  | 11.8-12.8µm | Infrared "Dirty" longwave Total water, volcanic ash, sea surface temperature Brightness  
`DQF_C15` |  0  |  4  | Data quality flags  
`CMI_C16` | K |  92.7  |  318.26  | 13.0-13.6µm | Infrared - CO_2 longwave Air temperature, cloud heights Brightness  
`DQF_C16` |  0  |  4  | Data quality flags  
**DQF_C01 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C02 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C03 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C04 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C05 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C06 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C07 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C08 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C09 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C10 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C11 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C12 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C13 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C14 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C15 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**DQF_C16 Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Good pixels  
1 | #ff00ff | Conditionally usable pixels  
2 | #0000ff | Out of range pixels  
3 | #00ffff | No value pixels  
4 | #ffff00 | Focal plane temperature threshold exceeded  
**Image Properties**
Name | Type | Description  
---|---|---  
CMI_C01_offset | DOUBLE | Offset to add to scaled CMI_C01 values  
CMI_C01_scale | DOUBLE | Scale to multiply with raw CMI_C01 values  
CMI_C02_offset | DOUBLE | Offset to add to scaled CMI_C02 values  
CMI_C02_scale | DOUBLE | Scale to multiply with raw CMI_C02 values  
CMI_C03_offset | DOUBLE | Offset to add to scaled CMI_C03 values  
CMI_C03_scale | DOUBLE | Scale to multiply with raw CMI_C03 values  
CMI_C04_offset | DOUBLE | Offset to add to scaled CMI_C04 values  
CMI_C04_scale | DOUBLE | Scale to multiply with raw CMI_C04 values  
CMI_C05_offset | DOUBLE | Offset to add to scaled CMI_C05 values  
CMI_C05_scale | DOUBLE | Scale to multiply with raw CMI_C05 values  
CMI_C06_offset | DOUBLE | Offset to add to scaled CMI_C06 values  
CMI_C06_scale | DOUBLE | Scale to multiply with raw CMI_C06 values  
CMI_C07_offset | DOUBLE | Offset to add to scaled CMI_C07 values  
CMI_C07_scale | DOUBLE | Scale to multiply with raw CMI_C07 values  
CMI_C08_offset | DOUBLE | Offset to add to scaled CMI_C08 values  
CMI_C08_scale | DOUBLE | Scale to multiply with raw CMI_C08 values  
CMI_C09_offset | DOUBLE | Offset to add to scaled CMI_C09 values  
CMI_C09_scale | DOUBLE | Scale to multiply with raw CMI_C09 values  
CMI_C10_offset | DOUBLE | Offset to add to scaled CMI_C10 values  
CMI_C10_scale | DOUBLE | Scale to multiply with raw CMI_C10 values  
CMI_C11_offset | DOUBLE | Offset to add to scaled CMI_C11 values  
CMI_C11_scale | DOUBLE | Scale to multiply with raw CMI_C11 values  
CMI_C12_offset | DOUBLE | Offset to add to scaled CMI_C12 values  
CMI_C12_scale | DOUBLE | Scale to multiply with raw CMI_C12 values  
CMI_C13_offset | DOUBLE | Offset to add to scaled CMI_C13 values  
CMI_C13_scale | DOUBLE | Scale to multiply with raw CMI_C13 values  
CMI_C14_offset | DOUBLE | Offset to add to scaled CMI_C14 values  
CMI_C14_scale | DOUBLE | Scale to multiply with raw CMI_C14 values  
CMI_C15_offset | DOUBLE | Offset to add to scaled CMI_C15 values  
CMI_C15_scale | DOUBLE | Scale to multiply with raw CMI_C15 values  
CMI_C16_offset | DOUBLE | Offset to add to scaled CMI_C16 values  
CMI_C16_scale | DOUBLE | Scale to multiply with raw CMI_C16 values  
**Terms of Use**
NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use.
Citations:
  * Bah, Gunshor, Schmit, Generation of GOES-16 True Color Imagery without a Green Band, 2018. [doi:10.1029/2018EA000379](https://doi.org/10.1029/2018EA000379)
  * Product User Guide (PUG) Volume 5, [L2+ Products](https://www.goes-r.gov/products/docs/PUG-L2+-vol5.pdf).
  * Schmit, T., Griffith, P., et al, (2016), A closer look at the ABI on the GOES-R series, Bull. Amer. Meteor. Soc., 98(4), 681-698. [doi:10.1175/BAMS-D-15-00230.1](https://doi.org/10.1175/BAMS-D-15-00230.1)


  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/10.1175/BAMS-D-15-00230.1)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM#code-editor-javascript-sample) More
```
// Demonstrates displaying GOES-16 Mesoscale images.
// Band names.
varBLUE='CMI_C01';
varRED='CMI_C02';
varVEGGIE='CMI_C03';
varGREEN='GREEN';
/**
 * Properly scales an MCMIPM image.
 *
 * @param {ee.Image} image An unaltered MCMIPM image.
 * @return {ee.Image}
 */
varapplyScaleAndOffset=function(image){
varnames=image.select('CMI_C..').bandNames();
// Scale the radiance bands using the image's metadata.
varscales=names.map(function(name){
returnimage.getNumber(ee.String(name).cat('_scale'));
});
varoffsets=names.map(function(name){
returnimage.getNumber(ee.String(name).cat('_offset'));
});
varscaled=image.select('CMI_C..')
.multiply(ee.Image.constant(scales))
.add(ee.Image.constant(offsets));
returnimage.addBands({srcImg:scaled,overwrite:true});
};
/**
 * Computes and adds a green radiance band to a MCMIPM image.
 *
 * The image must already have been properly scaled via applyScaleAndOffset.
 *
 * For more information on computing the green band, see:
 *  https://doi.org/10.1029/2018EA000379
 *
 * @param {ee.Image} image An image to add a green radiance band to. It
 *   must be the result of the applyScaleAndOffset function.
 * @return {ee.Image}
 */
varaddGreenBand=function(image){
functiontoBandExpression(bandName){return'b(\''+bandName+'\')';}
varB_BLUE=toBandExpression(BLUE);
varB_RED=toBandExpression(RED);
varB_VEGGIE=toBandExpression(VEGGIE);
// Green = 0.45 * Red + 0.10 * NIR + 0.45 * Blue
varGREEN_EXPR=GREEN+' = 0.45 * '+B_RED+' + 0.10 * '+B_VEGGIE+
' + 0.45 * '+B_BLUE;
vargreen=image.expression(GREEN_EXPR).select(GREEN);
returnimage.addBands(green);
};

varCOLLECTION='NOAA/GOES/16/MCMIPM';
// Select a subset of the collection, correct the values, and add a green band.
varSTART=ee.Date('2020-09-02T20:40:00');
varEND=START.advance(10,'minutes');
varcollection=ee.ImageCollection(COLLECTION)
.filterDate(START,END)
.map(applyScaleAndOffset)
.map(addGreenBand);
// Separates the two domains.
vardomain1_col=collection.filter('domain == 1');
vardomain2_col=collection.filter('domain == 2');
// Note that there are 20 assets, 10 in each domain.
varsize=ee.String('sizes: collection = ').cat(collection.size());
varsize1=ee.String('domain1 = ').cat(domain1_col.size());
varsize2=ee.String('domain2 = ').cat(domain2_col.size());
print(size.cat(' → ').cat(size1).cat(' and ').cat(size2));
// Visualization parameters.
vargoesRgbViz={bands:[RED,GREEN,BLUE],min:0.0,max:0.38,gamma:1.3};
// Displays a sample image from domain 1 and 2.
Map.addLayer(domain1_col.first(),goesRgbViz,'Domain 1');
Map.addLayer(domain2_col.first(),goesRgbViz,'Domain 2');
Map.setCenter(-86,39,5);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NOAA/NOAA_GOES_16_MCMIPM)
[ GOES-16 MCMIPM Series ABI Level 2 Cloud and Moisture Imagery Mesoscale ](https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM)
The Cloud and Moisture Imagery products are all at 2km resolution. Bands 1-6 are reflective. The dimensionless "reflectance factor" quantity is normalized by the solar zenith angle. These bands support the characterization of clouds, vegetation, snow/ice, and aerosols. Bands 7-16 are emissive. The brightness temperature at the Top-Of-Atmosphere (TOA) is …
NOAA/GOES/16/MCMIPM, abi,atmosphere,goes,goes-16,goes-east,goes-r,mcmip,nesdis,noaa,ospo,satellite-imagery,weather 
2017-07-10T00:00:00Z/2025-04-07T18:32:55.300000Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/https://data.noaa.gov/onestop/collections/details/385d4d38-267e-40c1-859d-b5d8a079c5df)
  * [ https://doi.org/10.1175/BAMS-D-15-00230.1 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NOAA_GOES_16_MCMIPM)


