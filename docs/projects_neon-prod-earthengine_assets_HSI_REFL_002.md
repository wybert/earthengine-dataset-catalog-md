 
#  NEON Surface Bidirectional Reflectance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![projects/neon-prod-earthengine/assets/HSI_REFL/002](https://developers.google.com/earth-engine/datasets/images/neon-prod-earthengine/projects_neon-prod-earthengine_assets_HSI_REFL_002_sample.png)
info
This dataset is part of a Publisher Catalog, and not managed by Google Earth Engine. Contact listaopgee@battelleecology.org for bugs or [view more datasets](https://developers.google.com/earth-engine/datasets/publisher/neon-prod-earthengine) from the National Ecological Observatory Network Catalog. [Learn more about Publisher datasets](https://developers.google.com/earth-engine/datasets/publisher). 
[ ![Catalog Owner Logo](https://developers.google.com/static/earth-engine/datasets/logos/neon-prod-earthengine_logo.png) ](https://www.neonscience.org/data-collection/airborne-remote-sensing) 

Catalog Owner
    National Ecological Observatory Network 

Dataset Availability
    2013-01-01T00:00:00Z–2024-09-08T16:03:42Z 

Dataset Provider
     [ NEON ](https://data.neonscience.org/data-products/DP3.30006.002) 

Earth Engine Snippet
     `    ee.ImageCollection("projects/neon-prod-earthengine/assets/HSI_REFL/002")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/neon-prod-earthengine/projects_neon-prod-earthengine_assets_HSI_REFL_002) 

Tags
     [airborne](https://developers.google.com/earth-engine/datasets/tags/airborne) [forest](https://developers.google.com/earth-engine/datasets/tags/forest) [hyperspectral](https://developers.google.com/earth-engine/datasets/tags/hyperspectral) [neon](https://developers.google.com/earth-engine/datasets/tags/neon) [neon-prod-earthengine](https://developers.google.com/earth-engine/datasets/tags/neon-prod-earthengine) [publisher-dataset](https://developers.google.com/earth-engine/datasets/tags/publisher-dataset) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation)
[Description](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#citations) More
The NEON AOP Surface Bidirectional Reflectance is a hyperspectral VSWIR (visible to shortwave infrared) data product, containing 426 bands spanning wavelengths from ~380 nm to 2510 nm. Reflectance is scaled by a factor of 10000. Wavelengths between 1340-1445 nm and 1790-1955 nm are set to -100; these are water vapor absorption bands without valid values. The dataset also contains QA raster bands. Major processing steps include orthorectification, plus atmospheric, topographic, and Bidirecitonal Reflectance Distribution Function (BRDF) corrections. Data are collected by one of three [NEON Imaging Spectrometer (NIS)](https://www.neonscience.org/data-collection/imaging-spectrometer) sensors, AVIRIS-NG spectrometers built by NASA's Jet Propulsion Lab (JPL). Reflectance is converted to a mosaic using the nadir-most pixels from the flight lines acquired with the least cloud cover. Spatial resolution is 1 m and spectral resolution is ~5 nm. The center wavelength and full width half max (FWHM) for each band are provided in the Image Properties. Availability in GEE may not represent full availability in the NEON Data Portal (linked below). Additional sites and years can be added to GEE upon request by emailing listaopgee@battelleecology.org.
See [NEON Data Product DP3.30006.002](https://data.neonscience.org/data-products/DP3.30006.002) for more details.
Get started by exploring the [Intro to AOP Data in Google Earth Engine Tutorial Series](https://www.neonscience.org/resources/learning-hub/tutorials/intro-aop-data-google-earth-engine-tutorial-series)
Browse and interact with AOP data in the [NEON AOP GEE Data Viewer App](https://neon-prod-earthengine.projects.earthengine.app/view/neon-aop-gee-data-viewer---desktop)
**Pixel Size** 1 meter 
**Bands**
Name | Units | Wavelength | Description  
---|---|---|---  
`B001` | 382.2587nm, FWHM: 5.6785nm | VNIR Band B001  
`B002` | 387.2674nm, FWHM: 5.6774nm | VNIR Band B002  
`B003` | 392.2761nm, FWHM: 5.6762nm | VNIR Band B003  
`B004` | 397.2848nm, FWHM: 5.6751nm | VNIR Band B004  
`B005` | 402.2935nm, FWHM: 5.674nm | VNIR Band B005  
`B006` | 407.3022nm, FWHM: 5.6729nm | VNIR Band B006  
`B007` | 412.3109nm, FWHM: 5.6719nm | VNIR Band B007  
`B008` | 417.3195nm, FWHM: 5.6708nm | VNIR Band B008  
`B009` | 422.3282nm, FWHM: 5.6697nm | VNIR Band B009  
`B010` | 427.3369nm, FWHM: 5.6687nm | VNIR Band B010  
`B011` | 432.3455nm, FWHM: 5.6677nm | VNIR Band B011  
`B012` | 437.3542nm, FWHM: 5.6667nm | VNIR Band B012  
`B013` | 442.363nm, FWHM: 5.6657nm | VNIR Band B013  
`B014` | 447.3716nm, FWHM: 5.6647nm | VNIR Band B014  
`B015` | 452.3804nm, FWHM: 5.6638nm | VNIR Band B015  
`B016` | 457.389nm, FWHM: 5.6628nm | VNIR Band B016  
`B017` | 462.3978nm, FWHM: 5.6619nm | VNIR Band B017  
`B018` | 467.4064nm, FWHM: 5.661nm | VNIR Band B018  
`B019` | 472.415nm, FWHM: 5.6601nm | VNIR Band B019  
`B020` | 477.4238nm, FWHM: 5.6592nm | VNIR Band B020  
`B021` | 482.4324nm, FWHM: 5.6583nm | VNIR Band B021  
`B022` | 487.4412nm, FWHM: 5.6575nm | VNIR Band B022  
`B023` | 492.4498nm, FWHM: 5.6566nm | VNIR Band B023  
`B024` | 497.4585nm, FWHM: 5.6558nm | VNIR Band B024  
`B025` | 502.4672nm, FWHM: 5.655nm | VNIR Band B025  
`B026` | 507.4759nm, FWHM: 5.6542nm | VNIR Band B026  
`B027` | 512.4846nm, FWHM: 5.6534nm | VNIR Band B027  
`B028` | 517.4932nm, FWHM: 5.6526nm | VNIR Band B028  
`B029` | 522.502nm, FWHM: 5.6519nm | VNIR Band B029  
`B030` | 527.5106nm, FWHM: 5.6511nm | VNIR Band B030  
`B031` | 532.5194nm, FWHM: 5.6504nm | VNIR Band B031  
`B032` | 537.528nm, FWHM: 5.6497nm | VNIR Band B032  
`B033` | 542.5367nm, FWHM: 5.649nm | VNIR Band B033  
`B034` | 547.5454nm, FWHM: 5.6483nm | VNIR Band B034  
`B035` | 552.5542nm, FWHM: 5.6476nm | VNIR Band B035  
`B036` | 557.5628nm, FWHM: 5.647nm | VNIR Band B036  
`B037` | 562.5714nm, FWHM: 5.6463nm | VNIR Band B037  
`B038` | 567.5802nm, FWHM: 5.6457nm | VNIR Band B038  
`B039` | 572.5888nm, FWHM: 5.6451nm | VNIR Band B039  
`B040` | 577.5974nm, FWHM: 5.6445nm | VNIR Band B040  
`B041` | 582.6062nm, FWHM: 5.6439nm | VNIR Band B041  
`B042` | 587.6148nm, FWHM: 5.6433nm | VNIR Band B042  
`B043` | 592.6236nm, FWHM: 5.6428nm | VNIR Band B043  
`B044` | 597.6322nm, FWHM: 5.6422nm | VNIR Band B044  
`B045` | 602.641nm, FWHM: 5.6417nm | VNIR Band B045  
`B046` | 607.6496nm, FWHM: 5.6412nm | VNIR Band B046  
`B047` | 612.6584nm, FWHM: 5.6407nm | VNIR Band B047  
`B048` | 617.667nm, FWHM: 5.6402nm | VNIR Band B048  
`B049` | 622.6757nm, FWHM: 5.6397nm | VNIR Band B049  
`B050` | 627.6844nm, FWHM: 5.6393nm | VNIR Band B050  
`B051` | 632.693nm, FWHM: 5.6388nm | VNIR Band B051  
`B052` | 637.7017nm, FWHM: 5.6384nm | VNIR Band B052  
`B053` | 642.7104nm, FWHM: 5.638nm | VNIR Band B053  
`B054` | 647.7191nm, FWHM: 5.6376nm | VNIR Band B054  
`B055` | 652.7278nm, FWHM: 5.6372nm | VNIR Band B055  
`B056` | 657.7365nm, FWHM: 5.6368nm | VNIR Band B056  
`B057` | 662.7452nm, FWHM: 5.6365nm | VNIR Band B057  
`B058` | 667.7538nm, FWHM: 5.6361nm | VNIR Band B058  
`B059` | 672.7626nm, FWHM: 5.6358nm | VNIR Band B059  
`B060` | 677.7712nm, FWHM: 5.6355nm | VNIR Band B060  
`B061` | 682.78nm, FWHM: 5.6352nm | VNIR Band B061  
`B062` | 687.7886nm, FWHM: 5.6349nm | VNIR Band B062  
`B063` | 692.7974nm, FWHM: 5.6347nm | VNIR Band B063  
`B064` | 697.806nm, FWHM: 5.6344nm | VNIR Band B064  
`B065` | 702.8148nm, FWHM: 5.6342nm | VNIR Band B065  
`B066` | 707.8233nm, FWHM: 5.6339nm | VNIR Band B066  
`B067` | 712.832nm, FWHM: 5.6337nm | VNIR Band B067  
`B068` | 717.8408nm, FWHM: 5.6335nm | VNIR Band B068  
`B069` | 722.8495nm, FWHM: 5.6334nm | VNIR Band B069  
`B070` | 727.858nm, FWHM: 5.6332nm | VNIR Band B070  
`B071` | 732.8668nm, FWHM: 5.633nm | VNIR Band B071  
`B072` | 737.8754nm, FWHM: 5.6329nm | VNIR Band B072  
`B073` | 742.8842nm, FWHM: 5.6328nm | VNIR Band B073  
`B074` | 747.8928nm, FWHM: 5.6327nm | VNIR Band B074  
`B075` | 752.9016nm, FWHM: 5.6326nm | VNIR Band B075  
`B076` | 757.9102nm, FWHM: 5.6325nm | VNIR Band B076  
`B077` | 762.9189nm, FWHM: 5.6324nm | VNIR Band B077  
`B078` | 767.9276nm, FWHM: 5.6324nm | VNIR Band B078  
`B079` | 772.9364nm, FWHM: 5.6323nm | VNIR Band B079  
`B080` | 777.945nm, FWHM: 5.6323nm | VNIR Band B080  
`B081` | 782.9538nm, FWHM: 5.6323nm | VNIR Band B081  
`B082` | 787.9624nm, FWHM: 5.6323nm | VNIR Band B082  
`B083` | 792.9712nm, FWHM: 5.6323nm | VNIR Band B083  
`B084` | 797.9798nm, FWHM: 5.6324nm | VNIR Band B084  
`B085` | 802.9884nm, FWHM: 5.6324nm | VNIR Band B085  
`B086` | 807.997nm, FWHM: 5.6325nm | VNIR Band B086  
`B087` | 813.0058nm, FWHM: 5.6326nm | VNIR Band B087  
`B088` | 818.0144nm, FWHM: 5.6326nm | VNIR Band B088  
`B089` | 823.023nm, FWHM: 5.6328nm | VNIR Band B089  
`B090` | 828.0318nm, FWHM: 5.6329nm | VNIR Band B090  
`B091` | 833.0404nm, FWHM: 5.633nm | VNIR Band B091  
`B092` | 838.0492nm, FWHM: 5.6332nm | VNIR Band B092  
`B093` | 843.0579nm, FWHM: 5.6333nm | VNIR Band B093  
`B094` | 848.0665nm, FWHM: 5.6335nm | VNIR Band B094  
`B095` | 853.0753nm, FWHM: 5.6337nm | VNIR Band B095  
`B096` | 858.084nm, FWHM: 5.6339nm | VNIR Band B096  
`B097` | 863.0927nm, FWHM: 5.6341nm | VNIR Band B097  
`B098` | 868.1014nm, FWHM: 5.6344nm | VNIR Band B098  
`B099` | 873.11nm, FWHM: 5.6346nm | VNIR Band B099  
`B100` | 878.1187nm, FWHM: 5.6349nm | VNIR Band B100  
`B101` | 883.1274nm, FWHM: 5.6352nm | VNIR Band B101  
`B102` | 888.1361nm, FWHM: 5.6354nm | VNIR Band B102  
`B103` | 893.1447nm, FWHM: 5.6358nm | VNIR Band B103  
`B104` | 898.1534nm, FWHM: 5.6361nm | VNIR Band B104  
`B105` | 903.1621nm, FWHM: 5.6364nm | VNIR Band B105  
`B106` | 908.1708nm, FWHM: 5.6368nm | VNIR Band B106  
`B107` | 913.1795nm, FWHM: 5.6371nm | VNIR Band B107  
`B108` | 918.1882nm, FWHM: 5.6375nm | VNIR Band B108  
`B109` | 923.1968nm, FWHM: 5.6379nm | VNIR Band B109  
`B110` | 928.2056nm, FWHM: 5.6383nm | VNIR Band B110  
`B111` | 933.2143nm, FWHM: 5.6387nm | VNIR Band B111  
`B112` | 938.223nm, FWHM: 5.6392nm | VNIR Band B112  
`B113` | 943.2316nm, FWHM: 5.6396nm | VNIR Band B113  
`B114` | 948.2403nm, FWHM: 5.6401nm | VNIR Band B114  
`B115` | 953.249nm, FWHM: 5.6406nm | VNIR Band B115  
`B116` | 958.2578nm, FWHM: 5.641nm | VNIR Band B116  
`B117` | 963.2663nm, FWHM: 5.6416nm | VNIR Band B117  
`B118` | 968.275nm, FWHM: 5.6421nm | VNIR Band B118  
`B119` | 973.2838nm, FWHM: 5.6426nm | VNIR Band B119  
`B120` | 978.2924nm, FWHM: 5.6432nm | VNIR Band B120  
`B121` | 983.301nm, FWHM: 5.6437nm | VNIR Band B121  
`B122` | 988.3098nm, FWHM: 5.6443nm | VNIR Band B122  
`B123` | 993.3184nm, FWHM: 5.6449nm | VNIR Band B123  
`B124` | 998.3272nm, FWHM: 5.6455nm | VNIR Band B124  
`B125` | 1003.3359nm, FWHM: 5.6461nm | VNIR Band B125  
`B126` | 1008.3444nm, FWHM: 5.6468nm | VNIR Band B126  
`B127` | 1013.3532nm, FWHM: 5.6474nm | VNIR Band B127  
`B128` | 1018.3619nm, FWHM: 5.6481nm | VNIR Band B128  
`B129` | 1023.3706nm, FWHM: 5.6487nm | VNIR Band B129  
`B130` | 1028.3793nm, FWHM: 5.6494nm | VNIR Band B130  
`B131` | 1033.388nm, FWHM: 5.6501nm | VNIR Band B131  
`B132` | 1038.3966nm, FWHM: 5.6508nm | VNIR Band B132  
`B133` | 1043.4054nm, FWHM: 5.6516nm | VNIR Band B133  
`B134` | 1048.414nm, FWHM: 5.6523nm | VNIR Band B134  
`B135` | 1053.4227nm, FWHM: 5.6531nm | VNIR Band B135  
`B136` | 1058.4314nm, FWHM: 5.6539nm | VNIR Band B136  
`B137` | 1063.4401nm, FWHM: 5.6547nm | VNIR Band B137  
`B138` | 1068.4487nm, FWHM: 5.6555nm | VNIR Band B138  
`B139` | 1073.4574nm, FWHM: 5.6563nm | VNIR Band B139  
`B140` | 1078.4661nm, FWHM: 5.6571nm | VNIR Band B140  
`B141` | 1083.4749nm, FWHM: 5.6579nm | VNIR Band B141  
`B142` | 1088.4836nm, FWHM: 5.6588nm | VNIR Band B142  
`B143` | 1093.4922nm, FWHM: 5.6597nm | VNIR Band B143  
`B144` | 1098.5009nm, FWHM: 5.6606nm | VNIR Band B144  
`B145` | 1103.5095nm, FWHM: 5.6615nm | VNIR Band B145  
`B146` | 1108.5182nm, FWHM: 5.6624nm | VNIR Band B146  
`B147` | 1113.527nm, FWHM: 5.6633nm | VNIR Band B147  
`B148` | 1118.5356nm, FWHM: 5.6642nm | VNIR Band B148  
`B149` | 1123.5443nm, FWHM: 5.6652nm | VNIR Band B149  
`B150` | 1128.553nm, FWHM: 5.6662nm | VNIR Band B150  
`B151` | 1133.5616nm, FWHM: 5.6672nm | VNIR Band B151  
`B152` | 1138.5704nm, FWHM: 5.6682nm | VNIR Band B152  
`B153` | 1143.5791nm, FWHM: 5.6692nm | VNIR Band B153  
`B154` | 1148.5878nm, FWHM: 5.6702nm | VNIR Band B154  
`B155` | 1153.5964nm, FWHM: 5.6712nm | VNIR Band B155  
`B156` | 1158.6051nm, FWHM: 5.6723nm | VNIR Band B156  
`B157` | 1163.6138nm, FWHM: 5.6733nm | VNIR Band B157  
`B158` | 1168.6224nm, FWHM: 5.6744nm | VNIR Band B158  
`B159` | 1173.6312nm, FWHM: 5.6755nm | VNIR Band B159  
`B160` | 1178.6398nm, FWHM: 5.6766nm | VNIR Band B160  
`B161` | 1183.6484nm, FWHM: 5.6778nm | VNIR Band B161  
`B162` | 1188.6571nm, FWHM: 5.6789nm | VNIR Band B162  
`B163` | 1193.6658nm, FWHM: 5.68nm | VNIR Band B163  
`B164` | 1198.6746nm, FWHM: 5.6812nm | VNIR Band B164  
`B165` | 1203.6833nm, FWHM: 5.6824nm | VNIR Band B165  
`B166` | 1208.692nm, FWHM: 5.6836nm | VNIR Band B166  
`B167` | 1213.7006nm, FWHM: 5.6848nm | VNIR Band B167  
`B168` | 1218.7092nm, FWHM: 5.686nm | VNIR Band B168  
`B169` | 1223.718nm, FWHM: 5.6872nm | VNIR Band B169  
`B170` | 1228.7267nm, FWHM: 5.6885nm | VNIR Band B170  
`B171` | 1233.7355nm, FWHM: 5.6897nm | VNIR Band B171  
`B172` | 1238.7441nm, FWHM: 5.691nm | VNIR Band B172  
`B173` | 1243.7528nm, FWHM: 5.6923nm | VNIR Band B173  
`B174` | 1248.7616nm, FWHM: 5.6936nm | VNIR Band B174  
`B175` | 1253.7703nm, FWHM: 5.6949nm | VNIR Band B175  
`B176` | 1258.7789nm, FWHM: 5.6962nm | VNIR Band B176  
`B177` | 1263.7875nm, FWHM: 5.6976nm | VNIR Band B177  
`B178` | 1268.7963nm, FWHM: 5.6989nm | VNIR Band B178  
`B179` | 1273.8049nm, FWHM: 5.7003nm | VNIR Band B179  
`B180` | 1278.8136nm, FWHM: 5.7017nm | VNIR Band B180  
`B181` | 1283.8223nm, FWHM: 5.7031nm | VNIR Band B181  
`B182` | 1288.831nm, FWHM: 5.7045nm | VNIR Band B182  
`B183` | 1293.8397nm, FWHM: 5.7059nm | VNIR Band B183  
`B184` | 1298.8485nm, FWHM: 5.7073nm | VNIR Band B184  
`B185` | 1303.857nm, FWHM: 5.7088nm | VNIR Band B185  
`B186` | 1308.8656nm, FWHM: 5.7102nm | VNIR Band B186  
`B187` | 1313.8743nm, FWHM: 5.7117nm | VNIR Band B187  
`B188` | 1318.8829nm, FWHM: 5.7132nm | VNIR Band B188  
`B189` | 1323.8917nm, FWHM: 5.7147nm | VNIR Band B189  
`B190` | 1328.9004nm, FWHM: 5.7162nm | VNIR Band B190  
`B191` | 1333.909nm, FWHM: 5.7177nm | VNIR Band B191  
`B192` | 1338.9178nm, FWHM: 5.7193nm | VNIR Band B192  
`B193` | 1343.9265nm, FWHM: 5.7208nm | VNIR Band B193  
`B194` | 1348.9352nm, FWHM: 5.7224nm | VNIR Band B194  
`B195` | 1353.9437nm, FWHM: 5.724nm | VNIR Band B195  
`B196` | 1358.9528nm, FWHM: 5.7256nm | VNIR Band B196  
`B197` | 1363.9613nm, FWHM: 5.7272nm | VNIR Band B197  
`B198` | 1368.97nm, FWHM: 5.7288nm | VNIR Band B198  
`B199` | 1373.9788nm, FWHM: 5.7305nm | VNIR Band B199  
`B200` | 1378.9873nm, FWHM: 5.7321nm | VNIR Band B200  
`B201` | 1383.9961nm, FWHM: 5.7338nm | VNIR Band B201  
`B202` | 1389.0048nm, FWHM: 5.7355nm | VNIR Band B202  
`B203` | 1394.0135nm, FWHM: 5.7371nm | VNIR Band B203  
`B204` | 1399.0221nm, FWHM: 5.7388nm | VNIR Band B204  
`B205` | 1404.0309nm, FWHM: 5.7406nm | SWIR Band B205  
`B206` | 1409.0394nm, FWHM: 5.7423nm | SWIR Band B206  
`B207` | 1414.0481nm, FWHM: 5.744nm | SWIR Band B207  
`B208` | 1419.0569nm, FWHM: 5.7458nm | SWIR Band B208  
`B209` | 1424.0656nm, FWHM: 5.7476nm | SWIR Band B209  
`B210` | 1429.0742nm, FWHM: 5.7493nm | SWIR Band B210  
`B211` | 1434.083nm, FWHM: 5.7511nm | SWIR Band B211  
`B212` | 1439.0917nm, FWHM: 5.7529nm | SWIR Band B212  
`B213` | 1444.1003nm, FWHM: 5.7548nm | SWIR Band B213  
`B214` | 1449.1088nm, FWHM: 5.7566nm | SWIR Band B214  
`B215` | 1454.1174nm, FWHM: 5.7584nm | SWIR Band B215  
`B216` | 1459.1263nm, FWHM: 5.7603nm | SWIR Band B216  
`B217` | 1464.135nm, FWHM: 5.7622nm | SWIR Band B217  
`B218` | 1469.1436nm, FWHM: 5.7641nm | SWIR Band B218  
`B219` | 1474.1522nm, FWHM: 5.766nm | SWIR Band B219  
`B220` | 1479.161nm, FWHM: 5.7679nm | SWIR Band B220  
`B221` | 1484.1697nm, FWHM: 5.7698nm | SWIR Band B221  
`B222` | 1489.1785nm, FWHM: 5.7717nm | SWIR Band B222  
`B223` | 1494.1871nm, FWHM: 5.7737nm | SWIR Band B223  
`B224` | 1499.1959nm, FWHM: 5.7757nm | SWIR Band B224  
`B225` | 1504.2045nm, FWHM: 5.7776nm | SWIR Band B225  
`B226` | 1509.2135nm, FWHM: 5.7796nm | SWIR Band B226  
`B227` | 1514.2219nm, FWHM: 5.7816nm | SWIR Band B227  
`B228` | 1519.2306nm, FWHM: 5.7837nm | SWIR Band B228  
`B229` | 1524.2394nm, FWHM: 5.7857nm | SWIR Band B229  
`B230` | 1529.2479nm, FWHM: 5.7877nm | SWIR Band B230  
`B231` | 1534.2566nm, FWHM: 5.7898nm | SWIR Band B231  
`B232` | 1539.2654nm, FWHM: 5.7919nm | SWIR Band B232  
`B233` | 1544.2742nm, FWHM: 5.7939nm | SWIR Band B233  
`B234` | 1549.2828nm, FWHM: 5.796nm | SWIR Band B234  
`B235` | 1554.2914nm, FWHM: 5.7981nm | SWIR Band B235  
`B236` | 1559.3nm, FWHM: 5.8003nm | SWIR Band B236  
`B237` | 1564.3088nm, FWHM: 5.8024nm | SWIR Band B237  
`B238` | 1569.3175nm, FWHM: 5.8045nm | SWIR Band B238  
`B239` | 1574.326nm, FWHM: 5.8067nm | SWIR Band B239  
`B240` | 1579.3348nm, FWHM: 5.8089nm | SWIR Band B240  
`B241` | 1584.3436nm, FWHM: 5.8111nm | SWIR Band B241  
`B242` | 1589.3522nm, FWHM: 5.8133nm | SWIR Band B242  
`B243` | 1594.361nm, FWHM: 5.8155nm | SWIR Band B243  
`B244` | 1599.3695nm, FWHM: 5.8177nm | SWIR Band B244  
`B245` | 1604.3783nm, FWHM: 5.8199nm | SWIR Band B245  
`B246` | 1609.387nm, FWHM: 5.8222nm | SWIR Band B246  
`B247` | 1614.3956nm, FWHM: 5.8244nm | SWIR Band B247  
`B248` | 1619.4043nm, FWHM: 5.8267nm | SWIR Band B248  
`B249` | 1624.413nm, FWHM: 5.829nm | SWIR Band B249  
`B250` | 1629.4215nm, FWHM: 5.8313nm | SWIR Band B250  
`B251` | 1634.4303nm, FWHM: 5.8336nm | SWIR Band B251  
`B252` | 1639.4388nm, FWHM: 5.8359nm | SWIR Band B252  
`B253` | 1644.4475nm, FWHM: 5.8383nm | SWIR Band B253  
`B254` | 1649.4563nm, FWHM: 5.8406nm | SWIR Band B254  
`B255` | 1654.465nm, FWHM: 5.843nm | SWIR Band B255  
`B256` | 1659.4736nm, FWHM: 5.8454nm | SWIR Band B256  
`B257` | 1664.4824nm, FWHM: 5.8478nm | SWIR Band B257  
`B258` | 1669.4911nm, FWHM: 5.8502nm | SWIR Band B258  
`B259` | 1674.5nm, FWHM: 5.8526nm | SWIR Band B259  
`B260` | 1679.5085nm, FWHM: 5.855nm | SWIR Band B260  
`B261` | 1684.5175nm, FWHM: 5.8574nm | SWIR Band B261  
`B262` | 1689.526nm, FWHM: 5.8599nm | SWIR Band B262  
`B263` | 1694.5345nm, FWHM: 5.8623nm | SWIR Band B263  
`B264` | 1699.5432nm, FWHM: 5.8648nm | SWIR Band B264  
`B265` | 1704.5518nm, FWHM: 5.8673nm | SWIR Band B265  
`B266` | 1709.5605nm, FWHM: 5.8698nm | SWIR Band B266  
`B267` | 1714.5692nm, FWHM: 5.8723nm | SWIR Band B267  
`B268` | 1719.578nm, FWHM: 5.8749nm | SWIR Band B268  
`B269` | 1724.5868nm, FWHM: 5.8774nm | SWIR Band B269  
`B270` | 1729.5955nm, FWHM: 5.88nm | SWIR Band B270  
`B271` | 1734.6042nm, FWHM: 5.8825nm | SWIR Band B271  
`B272` | 1739.613nm, FWHM: 5.8851nm | SWIR Band B272  
`B273` | 1744.6215nm, FWHM: 5.8877nm | SWIR Band B273  
`B274` | 1749.6302nm, FWHM: 5.8903nm | SWIR Band B274  
`B275` | 1754.6388nm, FWHM: 5.8929nm | SWIR Band B275  
`B276` | 1759.6476nm, FWHM: 5.8955nm | SWIR Band B276  
`B277` | 1764.6562nm, FWHM: 5.8982nm | SWIR Band B277  
`B278` | 1769.665nm, FWHM: 5.9008nm | SWIR Band B278  
`B279` | 1774.6738nm, FWHM: 5.9035nm | SWIR Band B279  
`B280` | 1779.6824nm, FWHM: 5.9062nm | SWIR Band B280  
`B281` | 1784.691nm, FWHM: 5.9089nm | SWIR Band B281  
`B282` | 1789.6996nm, FWHM: 5.9116nm | SWIR Band B282  
`B283` | 1794.7083nm, FWHM: 5.9143nm | SWIR Band B283  
`B284` | 1799.717nm, FWHM: 5.917nm | SWIR Band B284  
`B285` | 1804.7256nm, FWHM: 5.9197nm | SWIR Band B285  
`B286` | 1809.7343nm, FWHM: 5.9225nm | SWIR Band B286  
`B287` | 1814.7432nm, FWHM: 5.9253nm | SWIR Band B287  
`B288` | 1819.752nm, FWHM: 5.928nm | SWIR Band B288  
`B289` | 1824.7604nm, FWHM: 5.9308nm | SWIR Band B289  
`B290` | 1829.7692nm, FWHM: 5.9336nm | SWIR Band B290  
`B291` | 1834.778nm, FWHM: 5.9364nm | SWIR Band B291  
`B292` | 1839.7864nm, FWHM: 5.9393nm | SWIR Band B292  
`B293` | 1844.7952nm, FWHM: 5.9421nm | SWIR Band B293  
`B294` | 1849.8038nm, FWHM: 5.945nm | SWIR Band B294  
`B295` | 1854.8124nm, FWHM: 5.9478nm | SWIR Band B295  
`B296` | 1859.8214nm, FWHM: 5.9507nm | SWIR Band B296  
`B297` | 1864.83nm, FWHM: 5.9536nm | SWIR Band B297  
`B298` | 1869.8387nm, FWHM: 5.9565nm | SWIR Band B298  
`B299` | 1874.8474nm, FWHM: 5.9594nm | SWIR Band B299  
`B300` | 1879.8562nm, FWHM: 5.9623nm | SWIR Band B300  
`B301` | 1884.8646nm, FWHM: 5.9653nm | SWIR Band B301  
`B302` | 1889.8734nm, FWHM: 5.9682nm | SWIR Band B302  
`B303` | 1894.882nm, FWHM: 5.9712nm | SWIR Band B303  
`B304` | 1899.8907nm, FWHM: 5.9741nm | SWIR Band B304  
`B305` | 1904.8997nm, FWHM: 5.9771nm | SWIR Band B305  
`B306` | 1909.9082nm, FWHM: 5.9801nm | SWIR Band B306  
`B307` | 1914.9167nm, FWHM: 5.9831nm | SWIR Band B307  
`B308` | 1919.9257nm, FWHM: 5.9862nm | SWIR Band B308  
`B309` | 1924.9344nm, FWHM: 5.9892nm | SWIR Band B309  
`B310` | 1929.9427nm, FWHM: 5.9923nm | SWIR Band B310  
`B311` | 1934.9517nm, FWHM: 5.9953nm | SWIR Band B311  
`B312` | 1939.9604nm, FWHM: 5.9984nm | SWIR Band B312  
`B313` | 1944.9688nm, FWHM: 6.0015nm | SWIR Band B313  
`B314` | 1949.9775nm, FWHM: 6.0046nm | SWIR Band B314  
`B315` | 1954.9865nm, FWHM: 6.0077nm | SWIR Band B315  
`B316` | 1959.995nm, FWHM: 6.0108nm | SWIR Band B316  
`B317` | 1965.0035nm, FWHM: 6.0139nm | SWIR Band B317  
`B318` | 1970.0125nm, FWHM: 6.0171nm | SWIR Band B318  
`B319` | 1975.0208nm, FWHM: 6.0202nm | SWIR Band B319  
`B320` | 1980.0295nm, FWHM: 6.0234nm | SWIR Band B320  
`B321` | 1985.0385nm, FWHM: 6.0266nm | SWIR Band B321  
`B322` | 1990.047nm, FWHM: 6.0298nm | SWIR Band B322  
`B323` | 1995.0558nm, FWHM: 6.033nm | SWIR Band B323  
`B324` | 2000.0645nm, FWHM: 6.0362nm | SWIR Band B324  
`B325` | 2005.0732nm, FWHM: 6.0394nm | SWIR Band B325  
`B326` | 2010.082nm, FWHM: 6.0427nm | SWIR Band B326  
`B327` | 2015.0906nm, FWHM: 6.0459nm | SWIR Band B327  
`B328` | 2020.0992nm, FWHM: 6.0492nm | SWIR Band B328  
`B329` | 2025.1078nm, FWHM: 6.0525nm | SWIR Band B329  
`B330` | 2030.1165nm, FWHM: 6.0558nm | SWIR Band B330  
`B331` | 2035.1252nm, FWHM: 6.0591nm | SWIR Band B331  
`B332` | 2040.134nm, FWHM: 6.0624nm | SWIR Band B332  
`B333` | 2045.1428nm, FWHM: 6.0657nm | SWIR Band B333  
`B334` | 2050.1516nm, FWHM: 6.0691nm | SWIR Band B334  
`B335` | 2055.16nm, FWHM: 6.0724nm | SWIR Band B335  
`B336` | 2060.1687nm, FWHM: 6.0758nm | SWIR Band B336  
`B337` | 2065.1772nm, FWHM: 6.0792nm | SWIR Band B337  
`B338` | 2070.186nm, FWHM: 6.0826nm | SWIR Band B338  
`B339` | 2075.1948nm, FWHM: 6.086nm | SWIR Band B339  
`B340` | 2080.2034nm, FWHM: 6.0894nm | SWIR Band B340  
`B341` | 2085.2122nm, FWHM: 6.0928nm | SWIR Band B341  
`B342` | 2090.221nm, FWHM: 6.0962nm | SWIR Band B342  
`B343` | 2095.2295nm, FWHM: 6.0997nm | SWIR Band B343  
`B344` | 2100.2383nm, FWHM: 6.1032nm | SWIR Band B344  
`B345` | 2105.2466nm, FWHM: 6.1066nm | SWIR Band B345  
`B346` | 2110.2556nm, FWHM: 6.1101nm | SWIR Band B346  
`B347` | 2115.2642nm, FWHM: 6.1136nm | SWIR Band B347  
`B348` | 2120.273nm, FWHM: 6.1171nm | SWIR Band B348  
`B349` | 2125.2817nm, FWHM: 6.1207nm | SWIR Band B349  
`B350` | 2130.2903nm, FWHM: 6.1242nm | SWIR Band B350  
`B351` | 2135.299nm, FWHM: 6.1277nm | SWIR Band B351  
`B352` | 2140.3079nm, FWHM: 6.1313nm | SWIR Band B352  
`B353` | 2145.3164nm, FWHM: 6.1349nm | SWIR Band B353  
`B354` | 2150.325nm, FWHM: 6.1385nm | SWIR Band B354  
`B355` | 2155.3337nm, FWHM: 6.1421nm | SWIR Band B355  
`B356` | 2160.3423nm, FWHM: 6.1457nm | SWIR Band B356  
`B357` | 2165.351nm, FWHM: 6.1493nm | SWIR Band B357  
`B358` | 2170.3599nm, FWHM: 6.1529nm | SWIR Band B358  
`B359` | 2175.3684nm, FWHM: 6.1566nm | SWIR Band B359  
`B360` | 2180.3774nm, FWHM: 6.1602nm | SWIR Band B360  
`B361` | 2185.386nm, FWHM: 6.1639nm | SWIR Band B361  
`B362` | 2190.3948nm, FWHM: 6.1676nm | SWIR Band B362  
`B363` | 2195.4033nm, FWHM: 6.1713nm | SWIR Band B363  
`B364` | 2200.4119nm, FWHM: 6.175nm | SWIR Band B364  
`B365` | 2205.4207nm, FWHM: 6.1787nm | SWIR Band B365  
`B366` | 2210.4292nm, FWHM: 6.1824nm | SWIR Band B366  
`B367` | 2215.4377nm, FWHM: 6.1862nm | SWIR Band B367  
`B368` | 2220.4468nm, FWHM: 6.1899nm | SWIR Band B368  
`B369` | 2225.4556nm, FWHM: 6.1937nm | SWIR Band B369  
`B370` | 2230.464nm, FWHM: 6.1975nm | SWIR Band B370  
`B371` | 2235.473nm, FWHM: 6.2013nm | SWIR Band B371  
`B372` | 2240.4817nm, FWHM: 6.2051nm | SWIR Band B372  
`B373` | 2245.49nm, FWHM: 6.2089nm | SWIR Band B373  
`B374` | 2250.4988nm, FWHM: 6.2127nm | SWIR Band B374  
`B375` | 2255.5073nm, FWHM: 6.2166nm | SWIR Band B375  
`B376` | 2260.516nm, FWHM: 6.2204nm | SWIR Band B376  
`B377` | 2265.5247nm, FWHM: 6.2243nm | SWIR Band B377  
`B378` | 2270.5334nm, FWHM: 6.2282nm | SWIR Band B378  
`B379` | 2275.5422nm, FWHM: 6.2321nm | SWIR Band B379  
`B380` | 2280.551nm, FWHM: 6.236nm | SWIR Band B380  
`B381` | 2285.5598nm, FWHM: 6.2399nm | SWIR Band B381  
`B382` | 2290.5684nm, FWHM: 6.2438nm | SWIR Band B382  
`B383` | 2295.577nm, FWHM: 6.2478nm | SWIR Band B383  
`B384` | 2300.5857nm, FWHM: 6.2517nm | SWIR Band B384  
`B385` | 2305.5942nm, FWHM: 6.2557nm | SWIR Band B385  
`B386` | 2310.603nm, FWHM: 6.2597nm | SWIR Band B386  
`B387` | 2315.6116nm, FWHM: 6.2637nm | SWIR Band B387  
`B388` | 2320.6204nm, FWHM: 6.2677nm | SWIR Band B388  
`B389` | 2325.6292nm, FWHM: 6.2717nm | SWIR Band B389  
`B390` | 2330.638nm, FWHM: 6.2757nm | SWIR Band B390  
`B391` | 2335.6465nm, FWHM: 6.2797nm | SWIR Band B391  
`B392` | 2340.655nm, FWHM: 6.2838nm | SWIR Band B392  
`B393` | 2345.6638nm, FWHM: 6.2879nm | SWIR Band B393  
`B394` | 2350.6724nm, FWHM: 6.2919nm | SWIR Band B394  
`B395` | 2355.6812nm, FWHM: 6.296nm | SWIR Band B395  
`B396` | 2360.69nm, FWHM: 6.3001nm | SWIR Band B396  
`B397` | 2365.6985nm, FWHM: 6.3042nm | SWIR Band B397  
`B398` | 2370.7073nm, FWHM: 6.3084nm | SWIR Band B398  
`B399` | 2375.716nm, FWHM: 6.3125nm | SWIR Band B399  
`B400` | 2380.7246nm, FWHM: 6.3167nm | SWIR Band B400  
`B401` | 2385.7332nm, FWHM: 6.3208nm | SWIR Band B401  
`B402` | 2390.7422nm, FWHM: 6.325nm | SWIR Band B402  
`B403` | 2395.7507nm, FWHM: 6.3292nm | SWIR Band B403  
`B404` | 2400.7593nm, FWHM: 6.3334nm | SWIR Band B404  
`B405` | 2405.7678nm, FWHM: 6.3376nm | SWIR Band B405  
`B406` | 2410.7769nm, FWHM: 6.3418nm | SWIR Band B406  
`B407` | 2415.7854nm, FWHM: 6.3461nm | SWIR Band B407  
`B408` | 2420.7942nm, FWHM: 6.3503nm | SWIR Band B408  
`B409` | 2425.803nm, FWHM: 6.3546nm | SWIR Band B409  
`B410` | 2430.8113nm, FWHM: 6.3589nm | SWIR Band B410  
`B411` | 2435.82nm, FWHM: 6.3632nm | SWIR Band B411  
`B412` | 2440.8286nm, FWHM: 6.3675nm | SWIR Band B412  
`B413` | 2445.8374nm, FWHM: 6.3718nm | SWIR Band B413  
`B414` | 2450.846nm, FWHM: 6.3761nm | SWIR Band B414  
`B415` | 2455.855nm, FWHM: 6.3805nm | SWIR Band B415  
`B416` | 2460.8635nm, FWHM: 6.3848nm | SWIR Band B416  
`B417` | 2465.8723nm, FWHM: 6.3892nm | SWIR Band B417  
`B418` | 2470.881nm, FWHM: 6.3936nm | SWIR Band B418  
`B419` | 2475.89nm, FWHM: 6.398nm | SWIR Band B419  
`B420` | 2480.8987nm, FWHM: 6.4024nm | SWIR Band B420  
`B421` | 2485.907nm, FWHM: 6.4068nm | SWIR Band B421  
`B422` | 2490.9158nm, FWHM: 6.4112nm | SWIR Band B422  
`B423` | 2495.9243nm, FWHM: 6.4157nm | SWIR Band B423  
`B424` | 2500.933nm, FWHM: 6.4201nm | SWIR Band B424  
`B425` | 2505.9417nm, FWHM: 6.4246nm | SWIR Band B425  
`B426` | 2510.9507nm, FWHM: 6.4291nm | SWIR Band B426  
`Aerosol_Optical_Depth` | deg | Aerosol Optical Depth  
`Aspect` | deg | Aspect used as input to ATCOR  
`Cast_Shadow` | Cast Shadow mask used as input to ATCOR  
`Dark_Dense_Vegetation_Classification` | Dark Dense Vegetation (DDV) Classification  
`Haze_Cloud_Water_Map` | Haze Cloud Water Map generated by ATCOR  
`Illumination_Factor` | deg | Illumination Factor used as input to ATCOR  
`Path_Length` | m | Path length between sensor and surface  
`Sky_View_Factor` | % | Sky View Factor used as input to ATCOR  
`Slope` | deg | Slope used as input to ATCOR  
`Smooth_Surface_Elevation` | m | Smooth Surface Elevation used as input to ATCOR  
`Visibility_Index_Map` | km | Visibility Index Map - sea level values of visibility index / total optical thickeness  
`Water_Vapor_Column` | cm | Water Vapor Column - (cm)*1000 ground-to-space used in ATCOR  
`to-sensor_Azimuth_Angle` | deg | to-sensor Azimuth Angle  
`to-sensor_Zenith_Angle` | deg | to-sensor Zenith Angle  
`Weather_Quality_Indicator` | Weather Quality Indicator - estimated percentage of overhead cloud cover during acquisition  
`Acquisition_Date` | Acquisition Date, YYYYMMDD  
**Cast_Shadow Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | no shadow  
1 | #a9a9a9 | shadow  
**Dark_Dense_Vegetation_Classification Class Table**
Value | Color | Description  
---|---|---  
0 | #5c265f | geocoded background  
1 | #135e9c | water  
2 | #2e6f40 | DDV reference  
3 | #e1e3e1 | non-reference  
4 | #383734 | topographic shadow  
**Haze_Cloud_Water_Map Class Table**
Value | Color | Description  
---|---|---  
0 | #5c265f | geocoded background  
1 | #474747 | shadow  
2 | #9db8d1 | thin cirrus (water)  
3 | #5a6978 | medium cirrus (water)  
4 | #3d4a57 | thick cirrus (water)  
5 | #9a7b4f | land (clear)  
6 | #454d42 | saturated  
7 | #f7f7f7 | snow/ice  
8 | #d5e3d3 | thin cirrus (land)  
9 | #9da89b | medium cirrus (land)  
10 | #5a6359 | thick cirrus (land)  
11 | #ced4cd | thin haze (land)  
12 | #8c918c | medium haze (land)  
13 | #ceddde | thin haze/glint (water)  
14 | #849596 | med. haze/glint (water)  
15 | #98a39b | cloud (land)  
16 | #9899a3 | cloud (water)  
17 | #135e9c | water  
18 | #e1e8ed | cirrus cloud  
19 | #9ea7ad | cirrus cloud (thick)  
20 | #00ffff | bright  
21 | #383734 | topographic shadow  
22 | #4f4f4e | cloud (building) shadow  
**Weather_Quality_Indicator Class Table**
Value | Color | Description  
---|---|---  
0 | #239e2f | mostly clear: <10% cloud cover  
1 | #f5ee1d | partly cloudy: 10-50% cloud cover  
2 | #c40a0a | mostly cloudy: >50% cloud cover  
**Image Properties**
Name | Type | Description  
---|---|---  
AOP_VISIT_NUMBER | INT | Unique visit number to the NEON site.  
CITATION | STRING | Data citation. See [NEON Data Policies and Citation Guidelines](https://www.neonscience.org/data-samples/data-policies-citation).  
DOI | STRING | Digital Object Identifier. NEON data that have been released are assigned a DOI.  
FLIGHT_YEAR | INT | Year the data were collected.  
NEON_DOMAIN | STRING | NEON eco-climatic domain code, "D01" to "D20". See [NEON Field Sites and Domains](https://www.neonscience.org/field-sites/about-field-sites).  
NEON_SITE | STRING | NEON four-digit site code. See [NEON Field Sites](https://www.neonscience.org/field-sites/).  
NEON_SITE_NAME | STRING | Full name of the NEON site. See [NEON Field Sites](https://www.neonscience.org/field-sites/).  
NEON_DATA_PROD_URL | STRING | NEON data product url. Always set to: <https://data.neonscience.org/data-products/DP3.30006.002>.  
PROVISIONAL_RELEASED | STRING | Whether the data are Provisional or Released. See <https://www.neonscience.org/data-samples/data-management/data-revisions-releases>.  
RELEASE_YEAR | INT | If data are released, the year of the NEON Release Tag.  
SCALE_FACTOR | DOUBLE | Reflectance scale factor.  
SENSOR_ID | STRING | ID of NEON Imaging Spectrometer (NIS), or Global Airborne Observatory (GAO): "NIS1", "NIS2", "NIS3", "GAO".  
**Terms of Use**
[proprietary](https://developers.google.com/earth-engine/datasets/catalog/Use%20a%20custom%20URL%20for%20the%20non-standard%20license)
All data collected by NEON and provided as data products, with the exception of data related to rare, threatened, or endangered (RTE) species, are released to the public domain under [Creative Commons CC0 1.0 "No Rights Reserved"](https://creativecommons.org/publicdomain/zero/1.0/). No copyright has been applied to NEON data; any person may copy, modify, or distribute the data, for commercial or non-commercial purposes, without asking for permission. NEON data may still be subject to other laws or rights such as for privacy, and NEON makes no warranties about the data and disclaims all liability. When using or citing NEON data, no implication should be made about endorsement by NEON. In most countries, data and facts are not copyrightable. By putting NEON data into the public domain, we encourage broad use, particularly in scientific analyses and data aggregations. However, please be aware of the following scholarly norms: NEON data should be used in a way that is mindful of the limitations of the data, using the documentation associated with the data packages as a guide. Please refer to [NEON Data Guidelines and Policies](https://www.neonscience.org/data-samples/guidelines-policies) for detailed information on how to properly use and cite NEON data, as well as best practices for publishing research that uses NEON data.
Citations:
  * See [NEON citation guidelines](https://www.neonscience.org/data-samples/guidelines-policies/citing)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002#code-editor-javascript-sample) More
```
// Read in the NEON AOP Bidirectional Reflectance Image Collection
varrefl002=ee.ImageCollection(
"projects/neon-prod-earthengine/assets/HSI_REFL/002");
// Display available images in the HSI_REFL/002 Image Collection
print('NEON Bidirectional Reflectance Images',refl002.aggregate_array('system:index'))
// Specify the start and end dates and filter by date range
varstartDate=ee.Date('2022-01-01');
varendDate=startDate.advance(1,'year');
varrefl002_2022=refl002.filterDate(startDate,endDate);
// Filter by NEON site name (see https://www.neonscience.org/field-sites/explore-field-sites)
varreflLIRO_2022=refl002_2022.filter('NEON_SITE == "LIRO"').mosaic();
// Define the visualization parameters, display the red, green, and blue bands for a true-color image
varrgbVis={min:340,max:2150,bands:['B053','B035','B019'],gamma:2}
// Add the reflectance layer to the Map and center on the site
Map.addLayer(reflLIRO_2022,rgbVis,'LIRO 2022 Bidirectional Reflectance');
Map.setCenter(-89.70,46.01,14);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/neon-prod-earthengine/projects_neon-prod-earthengine_assets_HSI_REFL_002)
[ NEON Surface Bidirectional Reflectance ](https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002)
The NEON AOP Surface Bidirectional Reflectance is a hyperspectral VSWIR (visible to shortwave infrared) data product, containing 426 bands spanning wavelengths from ~380 nm to 2510 nm. Reflectance is scaled by a factor of 10000. Wavelengths between 1340-1445 nm and 1790-1955 nm are set to -100; these are water vapor …
projects/neon-prod-earthengine/assets/HSI_REFL/002, airborne,forest,hyperspectral,neon,neon-prod-earthengine,publisher-dataset,satellite-imagery,surface-reflectance,vegetation 
2013-01-01T00:00:00Z/2024-09-08T16:03:42Z
16 -170 73 -66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://data.neonscience.org/data-products/DP3.30006.002)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_neon-prod-earthengine_assets_HSI_REFL_002)


