 
#  EO-1 Hyperion Hyperspectral Imager 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![EO1/HYPERION](https://developers.google.com/earth-engine/datasets/images/EO1/EO1_HYPERION_sample.png) 

Dataset Availability
    2001-05-01T00:00:00Z–2017-03-13T00:00:00Z 

Dataset Provider
     [ USGS ](https://eo1.usgs.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("EO1/HYPERION")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EO1/EO1_HYPERION) 

Revisit Interval
    200 Days 

Tags
     [hyperspectral](https://developers.google.com/earth-engine/datasets/tags/hyperspectral) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
eo-1
hyperion
[Description](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#citations) More
Hyperion is a high resolution hyperspectral imager producing 220 unique spectral channels ranging from 0.357 to 2.576 micrometers with a 10-nm bandwidth. The instrument operates in a pushbroom fashion, with a spatial resolution of 30 meters for all bands and a standard scene width of 7.7 kilometers.
This dataset contains level 1A radiance images, radiometrically calibrated and orthorectified. The SWIR bands have a scaling factor of 80 and the VNIR bands have a scaling factor of 40 applied.
  * VNIR bands (B008-B057, 426.82nm - 925.41nm): L = Digital Number / 40
  * SWIR bands (B077-B224, 912.45nm - 2395.50nm): L = Digital Number / 80


Note that bands B001-B007, B058-B076, and B225-242 are not calibrated, have no valid values and are not included into EE assets. See the [detailed spectral coverage information](https://doi.org/10.5066/P9JXHMO2).
This is a preview dataset; only a portion of the data from the original source have been downloaded.
**Pixel Size** 30 meters 
**Bands**
Name | Units | Wavelength | Description  
---|---|---|---  
`B008` | W/m^2 SRμm | 426.8200nm, FWHM: 11.3871nm | VNIR band B8  
`B009` | W/m^2 SRμm | 436.9900nm, FWHM: 11.3871nm | VNIR band B9  
`B010` | W/m^2 SRμm | 447.1700nm, FWHM: 11.3871nm | VNIR band B10  
`B011` | W/m^2 SRμm | 457.3400nm, FWHM: 11.3871nm | VNIR band B11  
`B012` | W/m^2 SRμm | 467.5200nm, FWHM: 11.3871nm | VNIR band B12  
`B013` | W/m^2 SRμm | 477.6900nm, FWHM: 11.3871nm | VNIR band B13  
`B014` | W/m^2 SRμm | 487.8700nm, FWHM: 11.3784nm | VNIR band B14  
`B015` | W/m^2 SRμm | 498.0400nm, FWHM: 11.3538nm | VNIR band B15  
`B016` | W/m^2 SRμm | 508.2200nm, FWHM: 11.3133nm | VNIR band B16  
`B017` | W/m^2 SRμm | 518.3900nm, FWHM: 11.2580nm | VNIR band B17  
`B018` | W/m^2 SRμm | 528.5700nm, FWHM: 11.1907nm | VNIR band B18  
`B019` | W/m^2 SRμm | 538.7400nm, FWHM: 11.1119nm | VNIR band B19  
`B020` | W/m^2 SRμm | 548.9200nm, FWHM: 11.0245nm | VNIR band B20  
`B021` | W/m^2 SRμm | 559.0900nm, FWHM: 10.9321nm | VNIR band B21  
`B022` | W/m^2 SRμm | 569.2700nm, FWHM: 10.8368nm | VNIR band B22  
`B023` | W/m^2 SRμm | 579.4500nm, FWHM: 10.7407nm | VNIR band B23  
`B024` | W/m^2 SRμm | 589.6200nm, FWHM: 10.6482nm | VNIR band B24  
`B025` | W/m^2 SRμm | 599.8000nm, FWHM: 10.5607nm | VNIR band B25  
`B026` | W/m^2 SRμm | 609.9700nm, FWHM: 10.4823nm | VNIR band B26  
`B027` | W/m^2 SRμm | 620.1500nm, FWHM: 10.4147nm | VNIR band B27  
`B028` | W/m^2 SRμm | 630.3200nm, FWHM: 10.3595nm | VNIR band B28  
`B029` | W/m^2 SRμm | 640.5000nm, FWHM: 10.3188nm | VNIR band B29  
`B030` | W/m^2 SRμm | 650.6700nm, FWHM: 10.2942nm | VNIR band B30  
`B031` | W/m^2 SRμm | 660.8500nm, FWHM: 10.2856nm | VNIR band B31  
`B032` | W/m^2 SRμm | 671.0200nm, FWHM: 10.2980nm | VNIR band B32  
`B033` | W/m^2 SRμm | 681.2000nm, FWHM: 10.3349nm | VNIR band B33  
`B034` | W/m^2 SRμm | 691.3700nm, FWHM: 10.3909nm | VNIR band B34  
`B035` | W/m^2 SRμm | 701.5500nm, FWHM: 10.4592nm | VNIR band B35  
`B036` | W/m^2 SRμm | 711.7200nm, FWHM: 10.5322nm | VNIR band B36  
`B037` | W/m^2 SRμm | 721.9000nm, FWHM: 10.6004nm | VNIR band B37  
`B038` | W/m^2 SRμm | 732.0700nm, FWHM: 10.6562nm | VNIR band B38  
`B039` | W/m^2 SRμm | 742.2500nm, FWHM: 10.6933nm | VNIR band B39  
`B040` | W/m^2 SRμm | 752.4300nm, FWHM: 10.7058nm | VNIR band B40  
`B041` | W/m^2 SRμm | 762.6000nm, FWHM: 10.7276nm | VNIR band B41  
`B042` | W/m^2 SRμm | 772.7800nm, FWHM: 10.7907nm | VNIR band B42  
`B043` | W/m^2 SRμm | 782.9500nm, FWHM: 10.8833nm | VNIR band B43  
`B044` | W/m^2 SRμm | 793.1300nm, FWHM: 10.9938nm | VNIR band B44  
`B045` | W/m^2 SRμm | 803.3000nm, FWHM: 11.1044nm | VNIR band B45  
`B046` | W/m^2 SRμm | 813.4800nm, FWHM: 11.1980nm | VNIR band B46  
`B047` | W/m^2 SRμm | 823.6500nm, FWHM: 11.2600nm | VNIR band B47  
`B048` | W/m^2 SRμm | 833.8300nm, FWHM: 11.2824nm | VNIR band B48  
`B049` | W/m^2 SRμm | 844.0000nm, FWHM: 11.2822nm | VNIR band B49  
`B050` | W/m^2 SRμm | 854.1800nm, FWHM: 11.2816nm | VNIR band B50  
`B051` | W/m^2 SRμm | 864.3500nm, FWHM: 11.2809nm | VNIR band B51  
`B052` | W/m^2 SRμm | 874.5300nm, FWHM: 11.2797nm | VNIR band B52  
`B053` | W/m^2 SRμm | 884.7000nm, FWHM: 11.2782nm | VNIR band B53  
`B054` | W/m^2 SRμm | 894.8800nm, FWHM: 11.2771nm | VNIR band B54  
`B055` | W/m^2 SRμm | 905.0500nm, FWHM: 11.2765nm | VNIR band B55  
`B056` | W/m^2 SRμm | 915.2300nm, FWHM: 11.2756nm | VNIR band B56  
`B057` | W/m^2 SRμm | 925.4100nm, FWHM: 11.2754nm | VNIR band B57  
`B077` | W/m^2 SRμm | 912.4500nm, FWHM: 11.0457nm | SWIR band B77  
`B078` | W/m^2 SRμm | 922.5400nm, FWHM: 11.0457nm | SWIR band B78  
`B079` | W/m^2 SRμm | 932.6400nm, FWHM: 11.0457nm | SWIR band B79  
`B080` | W/m^2 SRμm | 942.7300nm, FWHM: 11.0457nm | SWIR band B80  
`B081` | W/m^2 SRμm | 952.8200nm, FWHM: 11.0457nm | SWIR band B81  
`B082` | W/m^2 SRμm | 962.9100nm, FWHM: 11.0457nm | SWIR band B82  
`B083` | W/m^2 SRμm | 972.9900nm, FWHM: 11.0457nm | SWIR band B83  
`B084` | W/m^2 SRμm | 983.0800nm, FWHM: 11.0457nm | SWIR band B84  
`B085` | W/m^2 SRμm | 993.1700nm, FWHM: 11.0457nm | SWIR band B85  
`B086` | W/m^2 SRμm | 1003.3000nm, FWHM: 11.0457nm | SWIR band B86  
`B087` | W/m^2 SRμm | 1013.3000nm, FWHM: 11.0457nm | SWIR band B87  
`B088` | W/m^2 SRμm | 1023.4000nm, FWHM: 11.0451nm | SWIR band B88  
`B089` | W/m^2 SRμm | 1033.4900nm, FWHM: 11.0423nm | SWIR band B89  
`B090` | W/m^2 SRμm | 1043.5900nm, FWHM: 11.0372nm | SWIR band B90  
`B091` | W/m^2 SRμm | 1053.6900nm, FWHM: 11.0302nm | SWIR band B91  
`B092` | W/m^2 SRμm | 1063.7900nm, FWHM: 11.0218nm | SWIR band B92  
`B093` | W/m^2 SRμm | 1073.8900nm, FWHM: 11.0122nm | SWIR band B93  
`B094` | W/m^2 SRμm | 1083.9900nm, FWHM: 11.0013nm | SWIR band B94  
`B095` | W/m^2 SRμm | 1094.0900nm, FWHM: 10.9871nm | SWIR band B95  
`B096` | W/m^2 SRμm | 1104.1900nm, FWHM: 10.9732nm | SWIR band B96  
`B097` | W/m^2 SRμm | 1114.1900nm, FWHM: 10.9572nm | SWIR band B97  
`B098` | W/m^2 SRμm | 1124.2800nm, FWHM: 10.9418nm | SWIR band B98  
`B099` | W/m^2 SRμm | 1134.3800nm, FWHM: 10.9248nm | SWIR band B99  
`B100` | W/m^2 SRμm | 1144.4800nm, FWHM: 10.9065nm | SWIR band B100  
`B101` | W/m^2 SRμm | 1154.5800nm, FWHM: 10.8884nm | SWIR band B101  
`B102` | W/m^2 SRμm | 1164.6800nm, FWHM: 10.8696nm | SWIR band B102  
`B103` | W/m^2 SRμm | 1174.7700nm, FWHM: 10.8513nm | SWIR band B103  
`B104` | W/m^2 SRμm | 1184.8700nm, FWHM: 10.8335nm | SWIR band B104  
`B105` | W/m^2 SRμm | 1194.9700nm, FWHM: 10.8154nm | SWIR band B105  
`B106` | W/m^2 SRμm | 1205.0700nm, FWHM: 10.7979nm | SWIR band B106  
`B107` | W/m^2 SRμm | 1215.1700nm, FWHM: 10.7822nm | SWIR band B107  
`B108` | W/m^2 SRμm | 1225.1700nm, FWHM: 10.7663nm | SWIR band B108  
`B109` | W/m^2 SRμm | 1235.2700nm, FWHM: 10.7520nm | SWIR band B109  
`B110` | W/m^2 SRμm | 1245.3600nm, FWHM: 10.7385nm | SWIR band B110  
`B111` | W/m^2 SRμm | 1255.4600nm, FWHM: 10.7270nm | SWIR band B111  
`B112` | W/m^2 SRμm | 1265.5600nm, FWHM: 10.7174nm | SWIR band B112  
`B113` | W/m^2 SRμm | 1275.6600nm, FWHM: 10.7091nm | SWIR band B113  
`B114` | W/m^2 SRμm | 1285.7600nm, FWHM: 10.7022nm | SWIR band B114  
`B115` | W/m^2 SRμm | 1295.8600nm, FWHM: 10.6970nm | SWIR band B115  
`B116` | W/m^2 SRμm | 1305.9600nm, FWHM: 10.6946nm | SWIR band B116  
`B117` | W/m^2 SRμm | 1316.0500nm, FWHM: 10.6937nm | SWIR band B117  
`B118` | W/m^2 SRμm | 1326.0500nm, FWHM: 10.6949nm | SWIR band B118  
`B119` | W/m^2 SRμm | 1336.1500nm, FWHM: 10.6996nm | SWIR band B119  
`B120` | W/m^2 SRμm | 1346.2500nm, FWHM: 10.7058nm | SWIR band B120  
`B121` | W/m^2 SRμm | 1356.3500nm, FWHM: 10.7163nm | SWIR band B121  
`B122` | W/m^2 SRμm | 1366.4500nm, FWHM: 10.7283nm | SWIR band B122  
`B123` | W/m^2 SRμm | 1376.5500nm, FWHM: 10.7437nm | SWIR band B123  
`B124` | W/m^2 SRμm | 1386.6500nm, FWHM: 10.7612nm | SWIR band B124  
`B125` | W/m^2 SRμm | 1396.7400nm, FWHM:10.7807nm | SWIR band B125  
`B126` | W/m^2 SRμm | 1406.8400nm, FWHM: 10.8034nm | SWIR band B126  
`B127` | W/m^2 SRμm | 1416.9400nm, FWHM: 10.8267nm | SWIR band B127  
`B128` | W/m^2 SRμm | 1426.9400nm, FWHM: 10.8534nm | SWIR band B128  
`B129` | W/m^2 SRμm | 1437.0400nm, FWHM: 10.8818nm | SWIR band B129  
`B130` | W/m^2 SRμm | 1447.1400nm, FWHM: 10.9110nm | SWIR band B130  
`B131` | W/m^2 SRμm | 1457.2300nm, FWHM: 10.9422nm | SWIR band B131  
`B132` | W/m^2 SRμm | 1467.3300nm, FWHM: 10.9743nm | SWIR band B132  
`B133` | W/m^2 SRμm | 1477.4300nm, FWHM: 11.0074nm | SWIR band B133  
`B134` | W/m^2 SRμm | 1487.5300nm, FWHM: 11.0414nm | SWIR band B134  
`B135` | W/m^2 SRμm | 1497.6300nm, FWHM: 11.0759nm | SWIR band B135  
`B136` | W/m^2 SRμm | 1507.7300nm, FWHM: 11.1108nm | SWIR band B136  
`B137` | W/m^2 SRμm | 1517.8300nm, FWHM: 11.1461nm | SWIR band B137  
`B138` | W/m^2 SRμm | 1527.9200nm, FWHM: 11.1811nm | SWIR band B138  
`B139` | W/m^2 SRμm | 1537.9200nm, FWHM: 11.2156nm | SWIR band B139  
`B140` | W/m^2 SRμm | 1548.0200nm, FWHM: 11.2496nm | SWIR band B140  
`B141` | W/m^2 SRμm | 1558.1200nm, FWHM: 11.2826nm | SWIR band B141  
`B142` | W/m^2 SRμm | 1568.2200nm, FWHM: 11.3146nm | SWIR band B142  
`B143` | W/m^2 SRμm | 1578.3200nm, FWHM: 11.3460nm | SWIR band B143  
`B144` | W/m^2 SRμm | 1588.4200nm, FWHM: 11.3753nm | SWIR band B144  
`B145` | W/m^2 SRμm | 1598.5100nm, FWHM: 11.4037nm | SWIR band B145  
`B146` | W/m^2 SRμm | 1608.6100nm, FWHM: 11.4302nm | SWIR band B146  
`B147` | W/m^2 SRμm | 1618.7100nm, FWHM: 11.4538nm | SWIR band B147  
`B148` | W/m^2 SRμm | 1628.8100nm, FWHM: 11.4760nm | SWIR band B148  
`B149` | W/m^2 SRμm | 1638.8100nm, FWHM: 11.4958nm | SWIR band B149  
`B150` | W/m^2 SRμm | 1648.9000nm, FWHM: 11.5133nm | SWIR band B150  
`B151` | W/m^2 SRμm | 1659.0000nm, FWHM: 11.5286nm | SWIR band B151  
`B152` | W/m^2 SRμm | 1669.1000nm, FWHM: 11.5404nm | SWIR band B152  
`B153` | W/m^2 SRμm | 1679.2000nm, FWHM: 11.5505nm | SWIR band B153  
`B154` | W/m^2 SRμm | 1689.3000nm, FWHM: 11.5580nm | SWIR band B154  
`B155` | W/m^2 SRμm | 1699.4000nm, FWHM: 11.5621nm | SWIR band B155  
`B156` | W/m^2 SRμm | 1709.5000nm, FWHM: 11.5634nm | SWIR band B156  
`B157` | W/m^2 SRμm | 1719.6000nm, FWHM: 11.5617nm | SWIR band B157  
`B158` | W/m^2 SRμm | 1729.7000nm, FWHM: 11.5563nm | SWIR band B158  
`B159` | W/m^2 SRμm | 1739.7000nm, FWHM: 11.5477nm | SWIR band B159  
`B160` | W/m^2 SRμm | 1749.7900nm, FWHM: 11.5346nm | SWIR band B160  
`B161` | W/m^2 SRμm | 1759.8900nm, FWHM: 11.5193nm | SWIR band B161  
`B162` | W/m^2 SRμm | 1769.9900nm, FWHM: 11.5002nm | SWIR band B162  
`B163` | W/m^2 SRμm | 1780.0900nm, FWHM: 11.4789nm | SWIR band B163  
`B164` | W/m^2 SRμm | 1790.1900nm, FWHM: 11.4548nm | SWIR band B164  
`B165` | W/m^2 SRμm | 1800.2900nm, FWHM: 11.4279nm | SWIR band B165  
`B166` | W/m^2 SRμm | 1810.3800nm, FWHM: 11.3994nm | SWIR band B166  
`B167` | W/m^2 SRμm | 1820.4800nm, FWHM: 11.3688nm | SWIR band B167  
`B168` | W/m^2 SRμm | 1830.5800nm, FWHM: 11.3366nm | SWIR band B168  
`B169` | W/m^2 SRμm | 1840.5800nm, FWHM: 11.3036nm | SWIR band B169  
`B170` | W/m^2 SRμm | 1850.6800nm, FWHM: 11.2696nm | SWIR band B170  
`B171` | W/m^2 SRμm | 1860.7800nm, FWHM: 11.2363nm | SWIR band B171  
`B172` | W/m^2 SRμm | 1870.8700nm, FWHM: 11.2007nm | SWIR band B172  
`B173` | W/m^2 SRμm | 1880.9800nm, FWHM: 11.1666nm | SWIR band B173  
`B174` | W/m^2 SRμm | 1891.0700nm, FWHM: 11.1333nm | SWIR band B174  
`B175` | W/m^2 SRμm | 1901.1700nm, FWHM: 11.1018nm | SWIR band B175  
`B176` | W/m^2 SRμm | 1911.2700nm, FWHM: 11.0714nm | SWIR band B176  
`B177` | W/m^2 SRμm | 1921.3700nm, FWHM: 11.0424nm | SWIR band B177  
`B178` | W/m^2 SRμm | 1931.4700nm, FWHM: 11.0155nm | SWIR band B178  
`B179` | W/m^2 SRμm | 1941.5700nm, FWHM: 10.9912nm | SWIR band B179  
`B180` | W/m^2 SRμm | 1951.5700nm, FWHM: 10.9698nm | SWIR band B180  
`B181` | W/m^2 SRμm | 1961.6600nm, FWHM: 10.9508nm | SWIR band B181  
`B182` | W/m^2 SRμm | 1971.7600nm, FWHM: 10.9355nm | SWIR band B182  
`B183` | W/m^2 SRμm | 1981.8600nm, FWHM: 10.9230nm | SWIR band B183  
`B184` | W/m^2 SRμm | 1991.9600nm, FWHM: 10.9139nm | SWIR band B184  
`B185` | W/m^2 SRμm | 2002.0600nm, FWHM: 10.9083nm | SWIR band B185  
`B186` | W/m^2 SRμm | 2012.1500nm, FWHM: 10.9069nm | SWIR band B186  
`B187` | W/m^2 SRμm | 2022.2500nm, FWHM: 10.9057nm | SWIR band B187  
`B188` | W/m^2 SRμm | 2032.3500nm, FWHM: 10.9013nm | SWIR band B188  
`B189` | W/m^2 SRμm | 2042.4500nm, FWHM: 10.8951nm | SWIR band B189  
`B190` | W/m^2 SRμm | 2052.4500nm, FWHM: 10.8854nm | SWIR band B190  
`B191` | W/m^2 SRμm | 2062.5500nm, FWHM: 10.8740nm | SWIR band B191  
`B192` | W/m^2 SRμm | 2072.6500nm, FWHM: 10.8591nm | SWIR band B192  
`B193` | W/m^2 SRμm | 2082.7500nm, FWHM: 10.8429nm | SWIR band B193  
`B194` | W/m^2 SRμm | 2092.8400nm, FWHM: 10.8242nm | SWIR band B194  
`B195` | W/m^2 SRμm | 2102.9400nm, FWHM: 10.8039nm | SWIR band B195  
`B196` | W/m^2 SRμm | 2113.0400nm, FWHM: 10.7820nm | SWIR band B196  
`B197` | W/m^2 SRμm | 2123.1400nm, FWHM: 10.7592nm | SWIR band B197  
`B198` | W/m^2 SRμm | 2133.2400nm, FWHM: 10.7342nm | SWIR band B198  
`B199` | W/m^2 SRμm | 2143.3400nm, FWHM: 10.7092nm | SWIR band B199  
`B200` | W/m^2 SRμm | 2153.3400nm, FWHM: 10.6834nm | SWIR band B200  
`B201` | W/m^2 SRμm | 2163.4300nm, FWHM: 10.6572nm | SWIR band B201  
`B202` | W/m^2 SRμm | 2173.5300nm, FWHM: 10.6312nm | SWIR band B202  
`B203` | W/m^2 SRμm | 2183.6300nm, FWHM: 10.6052nm | SWIR band B203  
`B204` | W/m^2 SRμm | 2193.7300nm, FWHM: 10.5803nm | SWIR band B204  
`B205` | W/m^2 SRμm | 2203.8300nm, FWHM: 10.5560nm | SWIR band B205  
`B206` | W/m^2 SRμm | 2213.9300nm, FWHM: 10.5328nm | SWIR band B206  
`B207` | W/m^2 SRμm | 2224.0300nm, FWHM: 10.5101nm | SWIR band B207  
`B208` | W/m^2 SRμm | 2234.1200nm, FWHM: 10.4904nm | SWIR band B208  
`B209` | W/m^2 SRμm | 2244.2200nm, FWHM: 10.4722nm | SWIR band B209  
`B210` | W/m^2 SRμm | 2254.2200nm, FWHM: 10.4552nm | SWIR band B210  
`B211` | W/m^2 SRμm | 2264.3200nm, FWHM: 10.4408nm | SWIR band B211  
`B212` | W/m^2 SRμm | 2274.4200nm, FWHM: 10.4285nm | SWIR band B212  
`B213` | W/m^2 SRμm | 2284.5200nm, FWHM: 10.4197nm | SWIR band B213  
`B214` | W/m^2 SRμm | 2294.6100nm, FWHM: 10.4129nm | SWIR band B214  
`B215` | W/m^2 SRμm | 2304.7100nm, FWHM: 10.4088nm | SWIR band B215  
`B216` | W/m^2 SRμm | 2314.8100nm, FWHM: 10.4077nm | SWIR band B216  
`B217` | W/m^2 SRμm | 2324.9100nm, FWHM: 10.4077nm | SWIR band B217  
`B218` | W/m^2 SRμm | 2335.0100nm, FWHM: 10.4077nm | SWIR band B218  
`B219` | W/m^2 SRμm | 2345.1100nm, FWHM: 10.4077nm | SWIR band B219  
`B220` | W/m^2 SRμm | 2355.2100nm, FWHM: 10.4077nm | SWIR band B220  
`B221` | W/m^2 SRμm | 2365.2000nm, FWHM: 10.4077nm | SWIR band B221  
`B222` | W/m^2 SRμm | 2375.3000nm, FWHM: 10.4077nm | SWIR band B222  
`B223` | W/m^2 SRμm | 2385.4000nm, FWHM: 10.4077nm | SWIR band B223  
`B224` | W/m^2 SRμm | 2395.5000nm, FWHM: 10.4077nm | SWIR band B224  
**Image Properties**
Name | Type | Description  
---|---|---  
ABNORMAL_PIXELS | STRING | Indicator of whether image was corrected for abnormal pixels: 'Y' or 'N'  
CORRECTION_METHOD_BIAS | STRING | Correction method used by L1G in creating image: 'CPF' (for CPF bias) or 'NONE' (for no bias used)  
CORRECTION_METHOD_GAIN | STRING | Correction method used by L1G in creating the image: 'CPF' (for CPF bias) or 'NONE' (for no bias used)  
CPF_FILE_NAME | STRING | Archive-generated external element file name for Calibration Parameter File  
DATEHOUR_CONTACT_PERIOD | DOUBLE | Date and hour of contact period start  
DPS_VERSION_NUMBER | STRING | DPS processing version number  
ELEVATION_SOURCE | STRING | Indicates the primary source (if any) of Digital Elevation Model (DEM) used in the correction process: 'N' (no correction applied), 'SRTM-2', 'SRTM-1', 'NED', 'DTED', or 'GTOPO30'  
EO1_XBAND | STRING | EO-1 X-band used to downlink data to LGS  
EPHEMERIS_TYPE | STRING | Identifier to inform user of orbital ephemeris type used: 'ACS', 'DEFINITIVE', 'GPS', or 'PREDICTIVE'  
GROUND_STATION | STRING | Ground station that received data  
INOPERABLE_DETECTORS | STRING | Indicator of whether image was corrected for inoperable or out of spec detectors: 'Y' or 'N'  
PROCESSING_SOFTWARE | STRING | L1G processing system and software version  
PRODUCT_CREATION_TIME | DOUBLE | L1G system date and time when metadata file for L1G product set was created.  
PRODUCT_TYPE | STRING | Identifier to inform user of product type: 'L1GS' or 'L1GST'  
RESAMPLING_OPTION | STRING | Resampling option used in creating image: 'NN' or 'CC'  
SCALING_FACTOR_SWIR | DOUBLE | Scaling factor used to convert calibrated DN to radiance units for bands 77-224  
SCALING_FACTOR_VNIR | DOUBLE | Scaling factor used to convert calibrated DN to radiance units for bands 8-57  
SENSOR_LOOK_ANGLE | DOUBLE | The look angle is the angle between nadir and the center of the collected image. It is zero when the collected data are centered at the nadir point. The angle when descending is positive when the sensor is pointing east, negative when the sensor is pointing west of nadir. -90 - 90  
STRIPING | STRING | Indicator of whether image was corrected for striping: 'Y' or 'N'  
SUN_AZIMUTH | DOUBLE | Sun azimuth angle in degrees for image center location at image center acquisition time. -180 through 180 where a positive value indicates angles to the east or clockwise from north and a negative value indicates angles to the west or counterclockwise from north.  
SUN_ELEVATION | DOUBLE | Sun elevation angle in degrees for image center location at image center acquisition time. -90 through 90 where a positive value indicates a daytime scene and a negative value indicates a nighttime scene.  
**Terms of Use**
Hyperion data are in the public domain. Once a scene has been downloaded from the USGS, it can be redistributed as desired.
Citations:
  * Data available from the U.S. Geological Survey.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('EO1/HYPERION')
.filter(ee.Filter.date('2016-01-01','2017-03-01'));
varrgb=dataset.select(['B050','B023','B015']);
varrgbVis={
min:1000.0,
max:14000.0,
gamma:2.5,
};
Map.setCenter(162.0044,-77.3463,9);
Map.addLayer(rgb.median(),rgbVis,'RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/EO1/EO1_HYPERION)
[ EO-1 Hyperion Hyperspectral Imager ](https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION)
Hyperion is a high resolution hyperspectral imager producing 220 unique spectral channels ranging from 0.357 to 2.576 micrometers with a 10-nm bandwidth. The instrument operates in a pushbroom fashion, with a spatial resolution of 30 meters for all bands and a standard scene width of 7.7 kilometers. This dataset contains …
EO1/HYPERION, hyperspectral,satellite-imagery,usgs 
2001-05-01T00:00:00Z/2017-03-13T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://eo1.usgs.gov/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/EO1_HYPERION)


