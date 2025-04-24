 
#  EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/EMIT/L2A/RFL](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_EMIT_L2A_RFL_sample.png) 

Dataset Availability
    2022-08-09T00:00:00Z–2025-04-20T10:48:03Z 

Dataset Provider
     [ NASA Jet Propulsion Laboratory ](https://earth.jpl.nasa.gov/emit/data/data-products/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/EMIT/L2A/RFL")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_EMIT_L2A_RFL) 

Cadence
    1 Day 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [emit](https://developers.google.com/earth-engine/datasets/tags/emit) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#dois) More
The EMIT Project is part of the Earth Venture-Instrument (EV-I) Program directed by the Program Director of the NASA Earth Science Division (ESD). EMIT is comprised of a VSWIR Infrared Dyson imaging spectrometer adapted for installation on the International Space Station (ISS). EMIT measures radiance between 380 and 2500 nanometers, with an approximate 7 nm bandpass. Data are collected in a swath that is approximately 75 km wide at the equator, with an approximate ground sampling distance of 60 m. See the provider's [NASA EMIT Overview](https://lpdaac.usgs.gov/documents/1695/EMIT_L2B_GHG_User_Guide_V1.pdf) for more details.
EMIT was a particularly useful tool for mapping out greenhouse gases, including methane, carbon dioxide, and water vapor. This is consistent with previous findings from airborne data, but global nature, revisit frequency and wide swath of EMIT provided an unprecedented opportunity to investigate greenhouse gas retrievals.
The Level 2A data product contains estimated surface reflectance, uncertainty, and mask data. In addition, the geolocation of all pixel centers is included as well as the calculation of observation geometry and illumination angles on a pixel-by-pixel basis.
**Pixel Size** 60 meters 
**Bands**
Name | Units | Description  
---|---|---  
`reflectance_0` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 0  
`reflectance_1` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 1  
`reflectance_2` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 2  
`reflectance_3` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 3  
`reflectance_4` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 4  
`reflectance_5` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 5  
`reflectance_6` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 6  
`reflectance_7` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 7  
`reflectance_8` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 8  
`reflectance_9` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 9  
`reflectance_10` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 10  
`reflectance_11` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 11  
`reflectance_12` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 12  
`reflectance_13` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 13  
`reflectance_14` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 14  
`reflectance_15` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 15  
`reflectance_16` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 16  
`reflectance_17` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 17  
`reflectance_18` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 18  
`reflectance_19` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 19  
`reflectance_20` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 20  
`reflectance_21` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 21  
`reflectance_22` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 22  
`reflectance_23` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 23  
`reflectance_24` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 24  
`reflectance_25` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 25  
`reflectance_26` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 26  
`reflectance_27` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 27  
`reflectance_28` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 28  
`reflectance_29` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 29  
`reflectance_30` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 30  
`reflectance_31` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 31  
`reflectance_32` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 32  
`reflectance_33` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 33  
`reflectance_34` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 34  
`reflectance_35` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 35  
`reflectance_36` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 36  
`reflectance_37` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 37  
`reflectance_38` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 38  
`reflectance_39` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 39  
`reflectance_40` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 40  
`reflectance_41` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 41  
`reflectance_42` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 42  
`reflectance_43` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 43  
`reflectance_44` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 44  
`reflectance_45` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 45  
`reflectance_46` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 46  
`reflectance_47` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 47  
`reflectance_48` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 48  
`reflectance_49` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 49  
`reflectance_50` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 50  
`reflectance_51` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 51  
`reflectance_52` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 52  
`reflectance_53` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 53  
`reflectance_54` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 54  
`reflectance_55` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 55  
`reflectance_56` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 56  
`reflectance_57` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 57  
`reflectance_58` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 58  
`reflectance_59` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 59  
`reflectance_60` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 60  
`reflectance_61` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 61  
`reflectance_62` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 62  
`reflectance_63` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 63  
`reflectance_64` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 64  
`reflectance_65` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 65  
`reflectance_66` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 66  
`reflectance_67` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 67  
`reflectance_68` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 68  
`reflectance_69` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 69  
`reflectance_70` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 70  
`reflectance_71` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 71  
`reflectance_72` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 72  
`reflectance_73` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 73  
`reflectance_74` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 74  
`reflectance_75` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 75  
`reflectance_76` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 76  
`reflectance_77` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 77  
`reflectance_78` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 78  
`reflectance_79` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 79  
`reflectance_80` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 80  
`reflectance_81` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 81  
`reflectance_82` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 82  
`reflectance_83` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 83  
`reflectance_84` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 84  
`reflectance_85` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 85  
`reflectance_86` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 86  
`reflectance_87` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 87  
`reflectance_88` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 88  
`reflectance_89` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 89  
`reflectance_90` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 90  
`reflectance_91` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 91  
`reflectance_92` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 92  
`reflectance_93` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 93  
`reflectance_94` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 94  
`reflectance_95` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 95  
`reflectance_96` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 96  
`reflectance_97` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 97  
`reflectance_98` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 98  
`reflectance_99` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 99  
`reflectance_100` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 100  
`reflectance_101` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 101  
`reflectance_102` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 102  
`reflectance_103` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 103  
`reflectance_104` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 104  
`reflectance_105` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 105  
`reflectance_106` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 106  
`reflectance_107` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 107  
`reflectance_108` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 108  
`reflectance_109` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 109  
`reflectance_110` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 110  
`reflectance_111` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 111  
`reflectance_112` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 112  
`reflectance_113` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 113  
`reflectance_114` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 114  
`reflectance_115` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 115  
`reflectance_116` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 116  
`reflectance_117` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 117  
`reflectance_118` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 118  
`reflectance_119` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 119  
`reflectance_120` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 120  
`reflectance_121` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 121  
`reflectance_122` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 122  
`reflectance_123` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 123  
`reflectance_124` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 124  
`reflectance_125` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 125  
`reflectance_126` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 126  
`reflectance_127` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 127  
`reflectance_128` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 128  
`reflectance_129` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 129  
`reflectance_130` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 130  
`reflectance_131` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 131  
`reflectance_132` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 132  
`reflectance_133` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 133  
`reflectance_134` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 134  
`reflectance_135` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 135  
`reflectance_136` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 136  
`reflectance_137` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 137  
`reflectance_138` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 138  
`reflectance_139` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 139  
`reflectance_140` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 140  
`reflectance_141` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 141  
`reflectance_142` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 142  
`reflectance_143` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 143  
`reflectance_144` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 144  
`reflectance_145` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 145  
`reflectance_146` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 146  
`reflectance_147` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 147  
`reflectance_148` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 148  
`reflectance_149` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 149  
`reflectance_150` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 150  
`reflectance_151` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 151  
`reflectance_152` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 152  
`reflectance_153` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 153  
`reflectance_154` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 154  
`reflectance_155` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 155  
`reflectance_156` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 156  
`reflectance_157` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 157  
`reflectance_158` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 158  
`reflectance_159` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 159  
`reflectance_160` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 160  
`reflectance_161` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 161  
`reflectance_162` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 162  
`reflectance_163` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 163  
`reflectance_164` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 164  
`reflectance_165` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 165  
`reflectance_166` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 166  
`reflectance_167` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 167  
`reflectance_168` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 168  
`reflectance_169` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 169  
`reflectance_170` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 170  
`reflectance_171` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 171  
`reflectance_172` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 172  
`reflectance_173` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 173  
`reflectance_174` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 174  
`reflectance_175` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 175  
`reflectance_176` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 176  
`reflectance_177` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 177  
`reflectance_178` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 178  
`reflectance_179` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 179  
`reflectance_180` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 180  
`reflectance_181` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 181  
`reflectance_182` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 182  
`reflectance_183` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 183  
`reflectance_184` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 184  
`reflectance_185` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 185  
`reflectance_186` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 186  
`reflectance_187` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 187  
`reflectance_188` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 188  
`reflectance_189` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 189  
`reflectance_190` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 190  
`reflectance_191` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 191  
`reflectance_192` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 192  
`reflectance_193` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 193  
`reflectance_194` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 194  
`reflectance_195` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 195  
`reflectance_196` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 196  
`reflectance_197` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 197  
`reflectance_198` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 198  
`reflectance_199` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 199  
`reflectance_200` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 200  
`reflectance_201` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 201  
`reflectance_202` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 202  
`reflectance_203` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 203  
`reflectance_204` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 204  
`reflectance_205` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 205  
`reflectance_206` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 206  
`reflectance_207` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 207  
`reflectance_208` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 208  
`reflectance_209` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 209  
`reflectance_210` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 210  
`reflectance_211` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 211  
`reflectance_212` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 212  
`reflectance_213` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 213  
`reflectance_214` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 214  
`reflectance_215` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 215  
`reflectance_216` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 216  
`reflectance_217` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 217  
`reflectance_218` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 218  
`reflectance_219` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 219  
`reflectance_220` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 220  
`reflectance_221` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 221  
`reflectance_222` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 222  
`reflectance_223` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 223  
`reflectance_224` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 224  
`reflectance_225` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 225  
`reflectance_226` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 226  
`reflectance_227` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 227  
`reflectance_228` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 228  
`reflectance_229` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 229  
`reflectance_230` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 230  
`reflectance_231` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 231  
`reflectance_232` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 232  
`reflectance_233` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 233  
`reflectance_234` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 234  
`reflectance_235` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 235  
`reflectance_236` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 236  
`reflectance_237` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 237  
`reflectance_238` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 238  
`reflectance_239` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 239  
`reflectance_240` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 240  
`reflectance_241` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 241  
`reflectance_242` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 242  
`reflectance_243` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 243  
`reflectance_244` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 244  
`reflectance_245` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 245  
`reflectance_246` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 246  
`reflectance_247` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 247  
`reflectance_248` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 248  
`reflectance_249` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 249  
`reflectance_250` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 250  
`reflectance_251` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 251  
`reflectance_252` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 252  
`reflectance_253` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 253  
`reflectance_254` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 254  
`reflectance_255` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 255  
`reflectance_256` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 256  
`reflectance_257` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 257  
`reflectance_258` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 258  
`reflectance_259` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 259  
`reflectance_260` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 260  
`reflectance_261` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 261  
`reflectance_262` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 262  
`reflectance_263` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 263  
`reflectance_264` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 264  
`reflectance_265` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 265  
`reflectance_266` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 266  
`reflectance_267` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 267  
`reflectance_268` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 268  
`reflectance_269` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 269  
`reflectance_270` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 270  
`reflectance_271` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 271  
`reflectance_272` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 272  
`reflectance_273` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 273  
`reflectance_274` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 274  
`reflectance_275` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 275  
`reflectance_276` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 276  
`reflectance_277` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 277  
`reflectance_278` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 278  
`reflectance_279` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 279  
`reflectance_280` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 280  
`reflectance_281` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 281  
`reflectance_282` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 282  
`reflectance_283` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 283  
`reflectance_284` | Spectral reflectance | Reflectance observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 284  
`reflectance_uncertainity_0` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 0  
`reflectance_uncertainity_1` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 1  
`reflectance_uncertainity_2` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 2  
`reflectance_uncertainity_3` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 3  
`reflectance_uncertainity_4` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 4  
`reflectance_uncertainity_5` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 5  
`reflectance_uncertainity_6` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 6  
`reflectance_uncertainity_7` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 7  
`reflectance_uncertainity_8` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 8  
`reflectance_uncertainity_9` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 9  
`reflectance_uncertainity_10` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 10  
`reflectance_uncertainity_11` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 11  
`reflectance_uncertainity_12` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 12  
`reflectance_uncertainity_13` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 13  
`reflectance_uncertainity_14` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 14  
`reflectance_uncertainity_15` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 15  
`reflectance_uncertainity_16` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 16  
`reflectance_uncertainity_17` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 17  
`reflectance_uncertainity_18` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 18  
`reflectance_uncertainity_19` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 19  
`reflectance_uncertainity_20` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 20  
`reflectance_uncertainity_21` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 21  
`reflectance_uncertainity_22` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 22  
`reflectance_uncertainity_23` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 23  
`reflectance_uncertainity_24` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 24  
`reflectance_uncertainity_25` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 25  
`reflectance_uncertainity_26` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 26  
`reflectance_uncertainity_27` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 27  
`reflectance_uncertainity_28` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 28  
`reflectance_uncertainity_29` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 29  
`reflectance_uncertainity_30` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 30  
`reflectance_uncertainity_31` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 31  
`reflectance_uncertainity_32` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 32  
`reflectance_uncertainity_33` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 33  
`reflectance_uncertainity_34` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 34  
`reflectance_uncertainity_35` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 35  
`reflectance_uncertainity_36` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 36  
`reflectance_uncertainity_37` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 37  
`reflectance_uncertainity_38` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 38  
`reflectance_uncertainity_39` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 39  
`reflectance_uncertainity_40` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 40  
`reflectance_uncertainity_41` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 41  
`reflectance_uncertainity_42` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 42  
`reflectance_uncertainity_43` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 43  
`reflectance_uncertainity_44` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 44  
`reflectance_uncertainity_45` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 45  
`reflectance_uncertainity_46` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 46  
`reflectance_uncertainity_47` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 47  
`reflectance_uncertainity_48` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 48  
`reflectance_uncertainity_49` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 49  
`reflectance_uncertainity_50` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 50  
`reflectance_uncertainity_51` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 51  
`reflectance_uncertainity_52` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 52  
`reflectance_uncertainity_53` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 53  
`reflectance_uncertainity_54` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 54  
`reflectance_uncertainity_55` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 55  
`reflectance_uncertainity_56` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 56  
`reflectance_uncertainity_57` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 57  
`reflectance_uncertainity_58` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 58  
`reflectance_uncertainity_59` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 59  
`reflectance_uncertainity_60` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 60  
`reflectance_uncertainity_61` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 61  
`reflectance_uncertainity_62` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 62  
`reflectance_uncertainity_63` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 63  
`reflectance_uncertainity_64` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 64  
`reflectance_uncertainity_65` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 65  
`reflectance_uncertainity_66` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 66  
`reflectance_uncertainity_67` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 67  
`reflectance_uncertainity_68` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 68  
`reflectance_uncertainity_69` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 69  
`reflectance_uncertainity_70` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 70  
`reflectance_uncertainity_71` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 71  
`reflectance_uncertainity_72` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 72  
`reflectance_uncertainity_73` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 73  
`reflectance_uncertainity_74` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 74  
`reflectance_uncertainity_75` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 75  
`reflectance_uncertainity_76` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 76  
`reflectance_uncertainity_77` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 77  
`reflectance_uncertainity_78` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 78  
`reflectance_uncertainity_79` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 79  
`reflectance_uncertainity_80` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 80  
`reflectance_uncertainity_81` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 81  
`reflectance_uncertainity_82` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 82  
`reflectance_uncertainity_83` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 83  
`reflectance_uncertainity_84` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 84  
`reflectance_uncertainity_85` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 85  
`reflectance_uncertainity_86` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 86  
`reflectance_uncertainity_87` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 87  
`reflectance_uncertainity_88` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 88  
`reflectance_uncertainity_89` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 89  
`reflectance_uncertainity_90` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 90  
`reflectance_uncertainity_91` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 91  
`reflectance_uncertainity_92` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 92  
`reflectance_uncertainity_93` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 93  
`reflectance_uncertainity_94` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 94  
`reflectance_uncertainity_95` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 95  
`reflectance_uncertainity_96` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 96  
`reflectance_uncertainity_97` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 97  
`reflectance_uncertainity_98` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 98  
`reflectance_uncertainity_99` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 99  
`reflectance_uncertainity_100` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 100  
`reflectance_uncertainity_101` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 101  
`reflectance_uncertainity_102` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 102  
`reflectance_uncertainity_103` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 103  
`reflectance_uncertainity_104` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 104  
`reflectance_uncertainity_105` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 105  
`reflectance_uncertainity_106` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 106  
`reflectance_uncertainity_107` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 107  
`reflectance_uncertainity_108` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 108  
`reflectance_uncertainity_109` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 109  
`reflectance_uncertainity_110` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 110  
`reflectance_uncertainity_111` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 111  
`reflectance_uncertainity_112` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 112  
`reflectance_uncertainity_113` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 113  
`reflectance_uncertainity_114` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 114  
`reflectance_uncertainity_115` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 115  
`reflectance_uncertainity_116` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 116  
`reflectance_uncertainity_117` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 117  
`reflectance_uncertainity_118` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 118  
`reflectance_uncertainity_119` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 119  
`reflectance_uncertainity_120` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 120  
`reflectance_uncertainity_121` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 121  
`reflectance_uncertainity_122` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 122  
`reflectance_uncertainity_123` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 123  
`reflectance_uncertainity_124` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 124  
`reflectance_uncertainity_125` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 125  
`reflectance_uncertainity_126` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 126  
`reflectance_uncertainity_127` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 127  
`reflectance_uncertainity_128` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 128  
`reflectance_uncertainity_129` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 129  
`reflectance_uncertainity_130` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 130  
`reflectance_uncertainity_131` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 131  
`reflectance_uncertainity_132` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 132  
`reflectance_uncertainity_133` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 133  
`reflectance_uncertainity_134` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 134  
`reflectance_uncertainity_135` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 135  
`reflectance_uncertainity_136` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 136  
`reflectance_uncertainity_137` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 137  
`reflectance_uncertainity_138` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 138  
`reflectance_uncertainity_139` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 139  
`reflectance_uncertainity_140` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 140  
`reflectance_uncertainity_141` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 141  
`reflectance_uncertainity_142` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 142  
`reflectance_uncertainity_143` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 143  
`reflectance_uncertainity_144` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 144  
`reflectance_uncertainity_145` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 145  
`reflectance_uncertainity_146` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 146  
`reflectance_uncertainity_147` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 147  
`reflectance_uncertainity_148` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 148  
`reflectance_uncertainity_149` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 149  
`reflectance_uncertainity_150` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 150  
`reflectance_uncertainity_151` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 151  
`reflectance_uncertainity_152` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 152  
`reflectance_uncertainity_153` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 153  
`reflectance_uncertainity_154` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 154  
`reflectance_uncertainity_155` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 155  
`reflectance_uncertainity_156` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 156  
`reflectance_uncertainity_157` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 157  
`reflectance_uncertainity_158` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 158  
`reflectance_uncertainity_159` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 159  
`reflectance_uncertainity_160` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 160  
`reflectance_uncertainity_161` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 161  
`reflectance_uncertainity_162` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 162  
`reflectance_uncertainity_163` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 163  
`reflectance_uncertainity_164` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 164  
`reflectance_uncertainity_165` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 165  
`reflectance_uncertainity_166` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 166  
`reflectance_uncertainity_167` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 167  
`reflectance_uncertainity_168` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 168  
`reflectance_uncertainity_169` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 169  
`reflectance_uncertainity_170` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 170  
`reflectance_uncertainity_171` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 171  
`reflectance_uncertainity_172` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 172  
`reflectance_uncertainity_173` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 173  
`reflectance_uncertainity_174` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 174  
`reflectance_uncertainity_175` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 175  
`reflectance_uncertainity_176` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 176  
`reflectance_uncertainity_177` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 177  
`reflectance_uncertainity_178` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 178  
`reflectance_uncertainity_179` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 179  
`reflectance_uncertainity_180` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 180  
`reflectance_uncertainity_181` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 181  
`reflectance_uncertainity_182` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 182  
`reflectance_uncertainity_183` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 183  
`reflectance_uncertainity_184` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 184  
`reflectance_uncertainity_185` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 185  
`reflectance_uncertainity_186` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 186  
`reflectance_uncertainity_187` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 187  
`reflectance_uncertainity_188` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 188  
`reflectance_uncertainity_189` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 189  
`reflectance_uncertainity_190` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 190  
`reflectance_uncertainity_191` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 191  
`reflectance_uncertainity_192` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 192  
`reflectance_uncertainity_193` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 193  
`reflectance_uncertainity_194` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 194  
`reflectance_uncertainity_195` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 195  
`reflectance_uncertainity_196` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 196  
`reflectance_uncertainity_197` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 197  
`reflectance_uncertainity_198` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 198  
`reflectance_uncertainity_199` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 199  
`reflectance_uncertainity_200` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 200  
`reflectance_uncertainity_201` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 201  
`reflectance_uncertainity_202` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 202  
`reflectance_uncertainity_203` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 203  
`reflectance_uncertainity_204` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 204  
`reflectance_uncertainity_205` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 205  
`reflectance_uncertainity_206` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 206  
`reflectance_uncertainity_207` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 207  
`reflectance_uncertainity_208` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 208  
`reflectance_uncertainity_209` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 209  
`reflectance_uncertainity_210` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 210  
`reflectance_uncertainity_211` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 211  
`reflectance_uncertainity_212` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 212  
`reflectance_uncertainity_213` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 213  
`reflectance_uncertainity_214` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 214  
`reflectance_uncertainity_215` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 215  
`reflectance_uncertainity_216` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 216  
`reflectance_uncertainity_217` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 217  
`reflectance_uncertainity_218` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 218  
`reflectance_uncertainity_219` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 219  
`reflectance_uncertainity_220` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 220  
`reflectance_uncertainity_221` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 221  
`reflectance_uncertainity_222` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 222  
`reflectance_uncertainity_223` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 223  
`reflectance_uncertainity_224` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 224  
`reflectance_uncertainity_225` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 225  
`reflectance_uncertainity_226` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 226  
`reflectance_uncertainity_227` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 227  
`reflectance_uncertainity_228` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 228  
`reflectance_uncertainity_229` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 229  
`reflectance_uncertainity_230` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 230  
`reflectance_uncertainity_231` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 231  
`reflectance_uncertainity_232` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 232  
`reflectance_uncertainity_233` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 233  
`reflectance_uncertainity_234` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 234  
`reflectance_uncertainity_235` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 235  
`reflectance_uncertainity_236` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 236  
`reflectance_uncertainity_237` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 237  
`reflectance_uncertainity_238` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 238  
`reflectance_uncertainity_239` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 239  
`reflectance_uncertainity_240` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 240  
`reflectance_uncertainity_241` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 241  
`reflectance_uncertainity_242` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 242  
`reflectance_uncertainity_243` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 243  
`reflectance_uncertainity_244` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 244  
`reflectance_uncertainity_245` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 245  
`reflectance_uncertainity_246` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 246  
`reflectance_uncertainity_247` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 247  
`reflectance_uncertainity_248` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 248  
`reflectance_uncertainity_249` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 249  
`reflectance_uncertainity_250` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 250  
`reflectance_uncertainity_251` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 251  
`reflectance_uncertainity_252` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 252  
`reflectance_uncertainity_253` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 253  
`reflectance_uncertainity_254` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 254  
`reflectance_uncertainity_255` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 255  
`reflectance_uncertainity_256` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 256  
`reflectance_uncertainity_257` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 257  
`reflectance_uncertainity_258` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 258  
`reflectance_uncertainity_259` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 259  
`reflectance_uncertainity_260` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 260  
`reflectance_uncertainity_261` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 261  
`reflectance_uncertainity_262` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 262  
`reflectance_uncertainity_263` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 263  
`reflectance_uncertainity_264` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 264  
`reflectance_uncertainity_265` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 265  
`reflectance_uncertainity_266` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 266  
`reflectance_uncertainity_267` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 267  
`reflectance_uncertainity_268` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 268  
`reflectance_uncertainity_269` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 269  
`reflectance_uncertainity_270` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 270  
`reflectance_uncertainity_271` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 271  
`reflectance_uncertainity_272` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 272  
`reflectance_uncertainity_273` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 273  
`reflectance_uncertainity_274` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 274  
`reflectance_uncertainity_275` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 275  
`reflectance_uncertainity_276` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 276  
`reflectance_uncertainity_277` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 277  
`reflectance_uncertainity_278` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 278  
`reflectance_uncertainity_279` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 279  
`reflectance_uncertainity_280` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 280  
`reflectance_uncertainity_281` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 281  
`reflectance_uncertainity_282` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 282  
`reflectance_uncertainity_283` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 283  
`reflectance_uncertainity_284` | Standard deviation | Reflectance uncertainty observed for the corresponding reflectance_fwhm and reflectance_wavelengths settings at index 284  
`elev` | m | Total elevation  
`cloud_flag` | Cloud Coverage  
`cirrus_flag` | Dense Cirrus clouds  
`water_flag` | Water bodies  
`spacecraft_flag` | Spacecraft or space station components that intersect the EMIT field of view  
`dilated_cloud_flag` | Cloud coverage + buffer  
`AOD550` | Aerosol Optical Depth at 550nm estimates  
`H2O` | g/cm^2 | Water Vapor estimates  
`aggregate_flag` | Aggregated binary flag of bands, included flags are cloud, cirrus, water, spacecraft, and dilated cloud  
**Image Properties**
Name | Type | Description  
---|---|---  
ORBIT | STRING | Unique Orbit Identification Number  
ORBIT_SEGMENT | STRING | Orbit Segment  
SCENE | STRING | Unique scene identification number  
SOLAR_AZIMUTH | STRING | Solar Azimuth  
SOLAR_ZENITH | STRING | Solar Zenith  
reflectance_fwhm | DOUBLE_LIST | An array of length 285, where the value at index i is the full width at half maximum setting for reflectance band i.  
reflectance_wavelengths | DOUBLE_LIST | An array of length 285, where the value at index i is the wavelength center setting for reflectance band i.  
**Terms of Use**
NASA EMIT data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Green, R. (2022). EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001 [Data set]. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2024-06-14 from <https://doi.org/10.5067/EMIT/EMITL2ARFL.001>


  * [ https://doi.org/10.5067/EMIT/EMITL2ARFL.001 ](https://doi.org/10.5067/EMIT/EMITL2ARFL.001)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/EMIT/L2A/RFL')
.filter(ee.Filter.date('2022-01-01','2023-12-01'));
varemitRadVis={
min:0,
max:0.1,
};
Map.setCenter(-121.4612,38.334,10);
Map.addLayer(
dataset,emitRadVis,
'Emit Reflectance');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_EMIT_L2A_RFL)
[ EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m ](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL)
The EMIT Project is part of the Earth Venture-Instrument (EV-I) Program directed by the Program Director of the NASA Earth Science Division (ESD). EMIT is comprised of a VSWIR Infrared Dyson imaging spectrometer adapted for installation on the International Space Station (ISS). EMIT measures radiance between 380 and 2500 nanometers, …
NASA/EMIT/L2A/RFL, daily,emit,nasa,reflectance,satellite-imagery 
2022-08-09T00:00:00Z/2025-04-20T10:48:03Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/EMIT/EMITL2ARFL.001 ](https://doi.org/https://earth.jpl.nasa.gov/emit/data/data-products/)
  * [ https://doi.org/10.5067/EMIT/EMITL2ARFL.001 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L2A_RFL)


