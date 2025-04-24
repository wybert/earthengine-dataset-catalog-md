 
#  EMIT L1B At-Sensor Calibrated Radiance and Geolocation Data 60 m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/EMIT/L1B/RAD](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_EMIT_L1B_RAD_sample.png) 

Dataset Availability
    2022-08-09T00:00:00Z–2025-04-20T10:48:03Z 

Dataset Provider
     [ NASA Jet Propulsion Laboratory ](https://earth.jpl.nasa.gov/emit/data/data-products/) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/EMIT/L1B/RAD")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_EMIT_L1B_RAD) 

Cadence
    1 Day 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [emit](https://developers.google.com/earth-engine/datasets/tags/emit) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#dois) More
The EMIT Project is part of the Earth Venture-Instrument (EV-I) Program directed by the Program Director of the NASA Earth Science Division (ESD). EMIT is comprised of a VSWIR Infrared Dyson imaging spectrometer adapted for installation on the International Space Station (ISS). EMIT measures radiance between 380 and 2500 nanometers, with an approximate 7 nm bandpass. Data are collected in a swath that is approximately 75 km wide at the equator, with an approximate ground sampling distance of 60 m. See the provider's [NASA EMIT Overview](https://lpdaac.usgs.gov/documents/1695/EMIT_L2B_GHG_User_Guide_V1.pdf) for more details.
EMIT was a particularly useful tool for mapping out greenhouse gases, including methane, carbon dioxide, and water vapor. This is consistent with previous findings from airborne data, but global nature, revisit frequency and wide swath of EMIT provided an unprecedented opportunity to investigate greenhouse gas retrievals.
The EMIT Level 1B At-Sensor Calibrated Radiance and Geolocation (EMITL1BRAD) Version 1 data product provides at-sensor calibrated radiance values along with observation data in a spatially raw, non-orthocorrected format.
**Pixel Size** 60 meters 
**Bands**
Name | Units | Description  
---|---|---  
`radiance_0` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 0  
`radiance_1` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 1  
`radiance_2` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 2  
`radiance_3` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 3  
`radiance_4` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 4  
`radiance_5` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 5  
`radiance_6` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 6  
`radiance_7` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 7  
`radiance_8` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 8  
`radiance_9` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 9  
`radiance_10` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 10  
`radiance_11` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 11  
`radiance_12` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 12  
`radiance_13` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 13  
`radiance_14` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 14  
`radiance_15` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 15  
`radiance_16` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 16  
`radiance_17` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 17  
`radiance_18` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 18  
`radiance_19` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 19  
`radiance_20` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 20  
`radiance_21` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 21  
`radiance_22` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 22  
`radiance_23` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 23  
`radiance_24` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 24  
`radiance_25` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 25  
`radiance_26` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 26  
`radiance_27` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 27  
`radiance_28` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 28  
`radiance_29` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 29  
`radiance_30` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 30  
`radiance_31` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 31  
`radiance_32` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 32  
`radiance_33` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 33  
`radiance_34` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 34  
`radiance_35` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 35  
`radiance_36` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 36  
`radiance_37` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 37  
`radiance_38` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 38  
`radiance_39` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 39  
`radiance_40` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 40  
`radiance_41` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 41  
`radiance_42` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 42  
`radiance_43` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 43  
`radiance_44` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 44  
`radiance_45` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 45  
`radiance_46` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 46  
`radiance_47` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 47  
`radiance_48` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 48  
`radiance_49` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 49  
`radiance_50` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 50  
`radiance_51` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 51  
`radiance_52` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 52  
`radiance_53` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 53  
`radiance_54` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 54  
`radiance_55` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 55  
`radiance_56` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 56  
`radiance_57` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 57  
`radiance_58` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 58  
`radiance_59` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 59  
`radiance_60` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 60  
`radiance_61` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 61  
`radiance_62` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 62  
`radiance_63` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 63  
`radiance_64` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 64  
`radiance_65` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 65  
`radiance_66` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 66  
`radiance_67` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 67  
`radiance_68` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 68  
`radiance_69` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 69  
`radiance_70` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 70  
`radiance_71` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 71  
`radiance_72` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 72  
`radiance_73` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 73  
`radiance_74` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 74  
`radiance_75` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 75  
`radiance_76` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 76  
`radiance_77` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 77  
`radiance_78` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 78  
`radiance_79` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 79  
`radiance_80` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 80  
`radiance_81` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 81  
`radiance_82` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 82  
`radiance_83` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 83  
`radiance_84` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 84  
`radiance_85` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 85  
`radiance_86` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 86  
`radiance_87` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 87  
`radiance_88` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 88  
`radiance_89` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 89  
`radiance_90` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 90  
`radiance_91` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 91  
`radiance_92` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 92  
`radiance_93` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 93  
`radiance_94` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 94  
`radiance_95` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 95  
`radiance_96` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 96  
`radiance_97` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 97  
`radiance_98` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 98  
`radiance_99` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 99  
`radiance_100` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 100  
`radiance_101` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 101  
`radiance_102` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 102  
`radiance_103` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 103  
`radiance_104` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 104  
`radiance_105` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 105  
`radiance_106` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 106  
`radiance_107` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 107  
`radiance_108` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 108  
`radiance_109` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 109  
`radiance_110` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 110  
`radiance_111` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 111  
`radiance_112` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 112  
`radiance_113` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 113  
`radiance_114` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 114  
`radiance_115` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 115  
`radiance_116` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 116  
`radiance_117` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 117  
`radiance_118` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 118  
`radiance_119` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 119  
`radiance_120` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 120  
`radiance_121` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 121  
`radiance_122` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 122  
`radiance_123` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 123  
`radiance_124` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 124  
`radiance_125` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 125  
`radiance_126` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 126  
`radiance_127` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 127  
`radiance_128` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 128  
`radiance_129` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 129  
`radiance_130` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 130  
`radiance_131` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 131  
`radiance_132` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 132  
`radiance_133` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 133  
`radiance_134` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 134  
`radiance_135` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 135  
`radiance_136` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 136  
`radiance_137` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 137  
`radiance_138` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 138  
`radiance_139` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 139  
`radiance_140` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 140  
`radiance_141` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 141  
`radiance_142` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 142  
`radiance_143` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 143  
`radiance_144` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 144  
`radiance_145` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 145  
`radiance_146` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 146  
`radiance_147` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 147  
`radiance_148` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 148  
`radiance_149` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 149  
`radiance_150` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 150  
`radiance_151` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 151  
`radiance_152` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 152  
`radiance_153` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 153  
`radiance_154` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 154  
`radiance_155` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 155  
`radiance_156` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 156  
`radiance_157` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 157  
`radiance_158` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 158  
`radiance_159` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 159  
`radiance_160` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 160  
`radiance_161` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 161  
`radiance_162` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 162  
`radiance_163` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 163  
`radiance_164` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 164  
`radiance_165` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 165  
`radiance_166` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 166  
`radiance_167` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 167  
`radiance_168` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 168  
`radiance_169` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 169  
`radiance_170` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 170  
`radiance_171` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 171  
`radiance_172` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 172  
`radiance_173` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 173  
`radiance_174` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 174  
`radiance_175` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 175  
`radiance_176` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 176  
`radiance_177` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 177  
`radiance_178` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 178  
`radiance_179` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 179  
`radiance_180` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 180  
`radiance_181` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 181  
`radiance_182` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 182  
`radiance_183` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 183  
`radiance_184` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 184  
`radiance_185` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 185  
`radiance_186` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 186  
`radiance_187` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 187  
`radiance_188` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 188  
`radiance_189` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 189  
`radiance_190` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 190  
`radiance_191` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 191  
`radiance_192` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 192  
`radiance_193` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 193  
`radiance_194` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 194  
`radiance_195` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 195  
`radiance_196` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 196  
`radiance_197` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 197  
`radiance_198` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 198  
`radiance_199` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 199  
`radiance_200` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 200  
`radiance_201` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 201  
`radiance_202` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 202  
`radiance_203` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 203  
`radiance_204` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 204  
`radiance_205` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 205  
`radiance_206` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 206  
`radiance_207` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 207  
`radiance_208` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 208  
`radiance_209` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 209  
`radiance_210` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 210  
`radiance_211` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 211  
`radiance_212` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 212  
`radiance_213` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 213  
`radiance_214` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 214  
`radiance_215` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 215  
`radiance_216` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 216  
`radiance_217` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 217  
`radiance_218` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 218  
`radiance_219` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 219  
`radiance_220` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 220  
`radiance_221` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 221  
`radiance_222` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 222  
`radiance_223` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 223  
`radiance_224` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 224  
`radiance_225` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 225  
`radiance_226` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 226  
`radiance_227` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 227  
`radiance_228` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 228  
`radiance_229` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 229  
`radiance_230` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 230  
`radiance_231` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 231  
`radiance_232` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 232  
`radiance_233` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 233  
`radiance_234` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 234  
`radiance_235` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 235  
`radiance_236` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 236  
`radiance_237` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 237  
`radiance_238` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 238  
`radiance_239` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 239  
`radiance_240` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 240  
`radiance_241` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 241  
`radiance_242` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 242  
`radiance_243` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 243  
`radiance_244` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 244  
`radiance_245` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 245  
`radiance_246` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 246  
`radiance_247` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 247  
`radiance_248` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 248  
`radiance_249` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 249  
`radiance_250` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 250  
`radiance_251` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 251  
`radiance_252` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 252  
`radiance_253` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 253  
`radiance_254` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 254  
`radiance_255` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 255  
`radiance_256` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 256  
`radiance_257` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 257  
`radiance_258` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 258  
`radiance_259` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 259  
`radiance_260` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 260  
`radiance_261` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 261  
`radiance_262` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 262  
`radiance_263` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 263  
`radiance_264` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 264  
`radiance_265` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 265  
`radiance_266` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 266  
`radiance_267` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 267  
`radiance_268` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 268  
`radiance_269` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 269  
`radiance_270` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 270  
`radiance_271` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 271  
`radiance_272` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 272  
`radiance_273` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 273  
`radiance_274` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 274  
`radiance_275` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 275  
`radiance_276` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 276  
`radiance_277` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 277  
`radiance_278` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 278  
`radiance_279` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 279  
`radiance_280` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 280  
`radiance_281` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 281  
`radiance_282` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 282  
`radiance_283` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 283  
`radiance_284` | nanoWatts/sr/cm^2/nm | Radiance observed for the corresponding radiance_fwhm and radiance_wavelengths settings at index 284  
`elev` | m | Total elevation  
`path_length` | m | Distance between sensor and ground  
`to_sensor_azimuth` | deg | 0 to 360 degrees clockwise from N  
`to_sensor_zenith` | deg | 0 to 90 degrees from zenith  
`to_sun_azimuth` | deg | 0 to 360 degrees clockwise from N  
`to_sun_zenith` | deg | 0 to 90 degrees from zenith  
`solar_phase` | deg | Degrees between to-sensor and to-sun vectors in principal plane  
`slope` | deg | Local surface slope as derived from Digital Elevation Model (DEM) in degrees  
`aspect` | deg | Local surface aspect 0 to 360 degrees clockwise from N  
`cosine_i` | Apparent local illumination factor based on DEM slope and aspect and to sun vector, 0 to 1  
`utc_time` | h | Fractional hours since UTC midnight  
`earth_sun_distance` | AU | Distance between the Earth and the Sun  
**Image Properties**
Name | Type | Description  
---|---|---  
ORBIT | STRING | Unique Orbit Identification Number  
ORBIT_SEGMENT | STRING | Orbit Segment  
SCENE | STRING | Unique scene identification number  
SOLAR_AZIMUTH | STRING | Solar Azimuth  
SOLAR_ZENITH | STRING | Solar Zenith  
radiance_fwhm | DOUBLE_LIST | An array of length 285, where the value at index i is the full width at half maximum setting for radiance band i.  
radiance_wavelengths | DOUBLE_LIST | An array of length 285, where the value at index i is the wavelength center setting for radiance band i.  
**Terms of Use**
NASA EMIT data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Green, R. (2022). EMIT L1B At-Sensor Calibrated Radiance and Geolocation Data 60 m V001 dataset. NASA EOSDIS Land Processes Distributed Active Archive Center. Accessed 2024-05-20 from <https://doi.org/10.5067/EMIT/EMITL1BRAD.001>


  * [ https://doi.org/10.5067/EMIT/EMITL1BRAD.001 ](https://doi.org/10.5067/EMIT/EMITL1BRAD.001)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/EMIT/L1B/RAD');
varemitRadVis={
min:0,
max:10.0,
};
Map.setCenter(-122.59,38.34,10);
Map.addLayer(
dataset,emitRadVis,
'Emit Radiance');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_EMIT_L1B_RAD)
[ EMIT L1B At-Sensor Calibrated Radiance and Geolocation Data 60 m ](https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD)
The EMIT Project is part of the Earth Venture-Instrument (EV-I) Program directed by the Program Director of the NASA Earth Science Division (ESD). EMIT is comprised of a VSWIR Infrared Dyson imaging spectrometer adapted for installation on the International Space Station (ISS). EMIT measures radiance between 380 and 2500 nanometers, …
NASA/EMIT/L1B/RAD, daily,emit,nasa,radiance,satellite-imagery 
2022-08-09T00:00:00Z/2025-04-20T10:48:03Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/EMIT/EMITL1BRAD.001 ](https://doi.org/https://earth.jpl.nasa.gov/emit/data/data-products/)
  * [ https://doi.org/10.5067/EMIT/EMITL1BRAD.001 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_EMIT_L1B_RAD)


