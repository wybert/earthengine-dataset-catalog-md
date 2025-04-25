 
#  IPCC AR6 Sea Level Projections Regional (Medium Confidence) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![IPCC/AR6/SLP](https://developers.google.com/earth-engine/datasets/images/IPCC/IPCC_AR6_SLP_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2120-01-01T00:00:00Z 

Dataset Provider
     [ IPCC ](https://zenodo.org/records/6382554) 

Earth Engine Snippet
     `    ee.ImageCollection("IPCC/AR6/SLP")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/IPCC/IPCC_AR6_SLP) 

Cadence
    10 Years 

Tags
     [ipcc](https://developers.google.com/earth-engine/datasets/tags/ipcc) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [oceans](https://developers.google.com/earth-engine/datasets/tags/oceans)
sea-level-changes
[Description](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#dois) More
The dataset provided by the IPCC features comprehensive global and regional sea level projections from the IPCC 6th Assessment Report (AR6). This collection contains assets for the medium confidence sea level rise projections. The dataset spans from 2020 to 2150 and includes projections for various future scenarios outlined in the AR6. It offers a detailed breakdown of individual processes contributing to sea level changes, alongside globally averaged projections, regional projections on a regular global grid. These projections align with those in the IPCC AR6 report, ensuring consistency and reliability. (Local projections at specific tide gauge locations are not included because they are not on a regular grid.)
The following are summaries of the future scenarios included in the dataset:
  * SSP1-1.9 holds warming to approximately 1.5°C above 1850-1900 in 2100 after slight overshoot (median) and implies net zero CO2 emissions around the middle of the century.
  * SSP1-2.6 stays below 2.0°C warming relative to 1850-1900 (median) with implied net zero emissions in the second half of the century.
  * SSP2-4.5 is approximately in line with the upper end of aggregate Nationally Determined Contribution emission levels by 2030. SR1.5 assessed temperature projections for NDCs to be between 2.7 and 3.4°C by 2100, corresponding to the upper half of projected warming under SSP2-4.5.
  * SSP3-7.0 is a medium to high reference scenario resulting from no additional climate policy under the SSP3 socioeconomic development narrative. SSP3-7.0 has particularly high non-CO2 emissions, including high aerosols emissions.
  * SSP5-8.5 is a high reference scenario with no additional climate policy. Emission levels as high as SSP5-8.5 are not obtained by Integrated Assessment Models (IAMs) under any of the SSPs other than the fossil fueled SSP5 socioeconomic development pathway.


Each component of the sea level projection scenarios is provided as a separate band, as detailed in the table below.
Component | Description  
---|---  
Total | Total integrated over all components  
AIS | Antarctic Ice Sheet  
GIS | Greenland Ice Sheet  
glaciers | Glaciers  
landwaterstorage | Land Water Storage  
oceandynamics | Ocean Dynamics (includes Thermal Expansion)  
verticallandmotion | Vertical Land Motion (non-climatic processes)  
**Pixel Size** 111.32 meters 
**Bands**
Name | Units | Description  
---|---|---  
`total_rates_quantile_0` | mm/y | Total rates for the quantile 0  
`total_rates_quantile_0_001` | mm/y | Total rates for the quantile 0.001  
`total_rates_quantile_0_005` | mm/y | Total rates for the quantile 0.005  
`total_rates_quantile_0_01` | mm/y | Total rates for the quantile 0.01  
`total_rates_quantile_0_02` | mm/y | Total rates for the quantile 0.02  
`total_rates_quantile_0_03` | mm/y | Total rates for the quantile 0.03  
`total_rates_quantile_0_04` | mm/y | Total rates for the quantile 0.04  
`total_rates_quantile_0_05` | mm/y | Total rates for the quantile 0.05  
`total_rates_quantile_0_06` | mm/y | Total rates for the quantile 0.06  
`total_rates_quantile_0_07` | mm/y | Total rates for the quantile 0.07  
`total_rates_quantile_0_08` | mm/y | Total rates for the quantile 0.08  
`total_rates_quantile_0_09` | mm/y | Total rates for the quantile 0.09  
`total_rates_quantile_0_1` | mm/y | Total rates for the quantile 0.1  
`total_rates_quantile_0_11` | mm/y | Total rates for the quantile 0.11  
`total_rates_quantile_0_12` | mm/y | Total rates for the quantile 0.12  
`total_rates_quantile_0_13` | mm/y | Total rates for the quantile 0.13  
`total_rates_quantile_0_14` | mm/y | Total rates for the quantile 0.14  
`total_rates_quantile_0_15` | mm/y | Total rates for the quantile 0.15  
`total_rates_quantile_0_16` | mm/y | Total rates for the quantile 0.16  
`total_rates_quantile_0_167` | mm/y | Total rates for the quantile 0.167  
`total_rates_quantile_0_17` | mm/y | Total rates for the quantile 0.17  
`total_rates_quantile_0_18` | mm/y | Total rates for the quantile 0.18  
`total_rates_quantile_0_19` | mm/y | Total rates for the quantile 0.19  
`total_rates_quantile_0_2` | mm/y | Total rates for the quantile 0.2  
`total_rates_quantile_0_21` | mm/y | Total rates for the quantile 0.21  
`total_rates_quantile_0_22` | mm/y | Total rates for the quantile 0.22  
`total_rates_quantile_0_23` | mm/y | Total rates for the quantile 0.23  
`total_rates_quantile_0_24` | mm/y | Total rates for the quantile 0.24  
`total_rates_quantile_0_25` | mm/y | Total rates for the quantile 0.25  
`total_rates_quantile_0_26` | mm/y | Total rates for the quantile 0.26  
`total_rates_quantile_0_27` | mm/y | Total rates for the quantile 0.27  
`total_rates_quantile_0_28` | mm/y | Total rates for the quantile 0.28  
`total_rates_quantile_0_29` | mm/y | Total rates for the quantile 0.29  
`total_rates_quantile_0_3` | mm/y | Total rates for the quantile 0.3  
`total_rates_quantile_0_31` | mm/y | Total rates for the quantile 0.31  
`total_rates_quantile_0_32` | mm/y | Total rates for the quantile 0.32  
`total_rates_quantile_0_33` | mm/y | Total rates for the quantile 0.33  
`total_rates_quantile_0_34` | mm/y | Total rates for the quantile 0.34  
`total_rates_quantile_0_35` | mm/y | Total rates for the quantile 0.35  
`total_rates_quantile_0_36` | mm/y | Total rates for the quantile 0.36  
`total_rates_quantile_0_37` | mm/y | Total rates for the quantile 0.37  
`total_rates_quantile_0_38` | mm/y | Total rates for the quantile 0.38  
`total_rates_quantile_0_39` | mm/y | Total rates for the quantile 0.39  
`total_rates_quantile_0_4` | mm/y | Total rates for the quantile 0.4  
`total_rates_quantile_0_41` | mm/y | Total rates for the quantile 0.41  
`total_rates_quantile_0_42` | mm/y | Total rates for the quantile 0.42  
`total_rates_quantile_0_43` | mm/y | Total rates for the quantile 0.43  
`total_rates_quantile_0_44` | mm/y | Total rates for the quantile 0.44  
`total_rates_quantile_0_45` | mm/y | Total rates for the quantile 0.45  
`total_rates_quantile_0_46` | mm/y | Total rates for the quantile 0.46  
`total_rates_quantile_0_47` | mm/y | Total rates for the quantile 0.47  
`total_rates_quantile_0_48` | mm/y | Total rates for the quantile 0.48  
`total_rates_quantile_0_49` | mm/y | Total rates for the quantile 0.49  
`total_rates_quantile_0_5` | mm/y | Total rates for the quantile 0.5  
`total_rates_quantile_0_51` | mm/y | Total rates for the quantile 0.51  
`total_rates_quantile_0_52` | mm/y | Total rates for the quantile 0.52  
`total_rates_quantile_0_53` | mm/y | Total rates for the quantile 0.53  
`total_rates_quantile_0_54` | mm/y | Total rates for the quantile 0.54  
`total_rates_quantile_0_55` | mm/y | Total rates for the quantile 0.55  
`total_rates_quantile_0_56` | mm/y | Total rates for the quantile 0.56  
`total_rates_quantile_0_57` | mm/y | Total rates for the quantile 0.57  
`total_rates_quantile_0_58` | mm/y | Total rates for the quantile 0.58  
`total_rates_quantile_0_59` | mm/y | Total rates for the quantile 0.59  
`total_rates_quantile_0_6` | mm/y | Total rates for the quantile 0.6  
`total_rates_quantile_0_61` | mm/y | Total rates for the quantile 0.61  
`total_rates_quantile_0_62` | mm/y | Total rates for the quantile 0.62  
`total_rates_quantile_0_63` | mm/y | Total rates for the quantile 0.63  
`total_rates_quantile_0_64` | mm/y | Total rates for the quantile 0.64  
`total_rates_quantile_0_65` | mm/y | Total rates for the quantile 0.65  
`total_rates_quantile_0_66` | mm/y | Total rates for the quantile 0.66  
`total_rates_quantile_0_67` | mm/y | Total rates for the quantile 0.67  
`total_rates_quantile_0_68` | mm/y | Total rates for the quantile 0.68  
`total_rates_quantile_0_69` | mm/y | Total rates for the quantile 0.69  
`total_rates_quantile_0_7` | mm/y | Total rates for the quantile 0.7  
`total_rates_quantile_0_71` | mm/y | Total rates for the quantile 0.71  
`total_rates_quantile_0_72` | mm/y | Total rates for the quantile 0.72  
`total_rates_quantile_0_73` | mm/y | Total rates for the quantile 0.73  
`total_rates_quantile_0_74` | mm/y | Total rates for the quantile 0.74  
`total_rates_quantile_0_75` | mm/y | Total rates for the quantile 0.75  
`total_rates_quantile_0_76` | mm/y | Total rates for the quantile 0.76  
`total_rates_quantile_0_77` | mm/y | Total rates for the quantile 0.77  
`total_rates_quantile_0_78` | mm/y | Total rates for the quantile 0.78  
`total_rates_quantile_0_79` | mm/y | Total rates for the quantile 0.79  
`total_rates_quantile_0_8` | mm/y | Total rates for the quantile 0.8  
`total_rates_quantile_0_81` | mm/y | Total rates for the quantile 0.81  
`total_rates_quantile_0_82` | mm/y | Total rates for the quantile 0.82  
`total_rates_quantile_0_83` | mm/y | Total rates for the quantile 0.83  
`total_rates_quantile_0_833` | mm/y | Total rates for the quantile 0.833  
`total_rates_quantile_0_84` | mm/y | Total rates for the quantile 0.84  
`total_rates_quantile_0_85` | mm/y | Total rates for the quantile 0.85  
`total_rates_quantile_0_86` | mm/y | Total rates for the quantile 0.86  
`total_rates_quantile_0_87` | mm/y | Total rates for the quantile 0.87  
`total_rates_quantile_0_88` | mm/y | Total rates for the quantile 0.88  
`total_rates_quantile_0_89` | mm/y | Total rates for the quantile 0.89  
`total_rates_quantile_0_9` | mm/y | Total rates for the quantile 0.9  
`total_rates_quantile_0_91` | mm/y | Total rates for the quantile 0.91  
`total_rates_quantile_0_92` | mm/y | Total rates for the quantile 0.92  
`total_rates_quantile_0_93` | mm/y | Total rates for the quantile 0.93  
`total_rates_quantile_0_94` | mm/y | Total rates for the quantile 0.94  
`total_rates_quantile_0_95` | mm/y | Total rates for the quantile 0.95  
`total_rates_quantile_0_96` | mm/y | Total rates for the quantile 0.96  
`total_rates_quantile_0_97` | mm/y | Total rates for the quantile 0.97  
`total_rates_quantile_0_98` | mm/y | Total rates for the quantile 0.98  
`total_rates_quantile_0_99` | mm/y | Total rates for the quantile 0.99  
`total_rates_quantile_0_995` | mm/y | Total rates for the quantile 0.995  
`total_rates_quantile_0_999` | mm/y | Total rates for the quantile 0.999  
`total_rates_quantile_1` | mm/y | Total rates for the quantile 1  
`total_values_quantile_0` | mm | Total values for the quantile 0  
`total_values_quantile_0_001` | mm | Total values for the quantile 0.001  
`total_values_quantile_0_005` | mm | Total values for the quantile 0.005  
`total_values_quantile_0_01` | mm | Total values for the quantile 0.01  
`total_values_quantile_0_02` | mm | Total values for the quantile 0.02  
`total_values_quantile_0_03` | mm | Total values for the quantile 0.03  
`total_values_quantile_0_04` | mm | Total values for the quantile 0.04  
`total_values_quantile_0_05` | mm | Total values for the quantile 0.05  
`total_values_quantile_0_06` | mm | Total values for the quantile 0.06  
`total_values_quantile_0_07` | mm | Total values for the quantile 0.07  
`total_values_quantile_0_08` | mm | Total values for the quantile 0.08  
`total_values_quantile_0_09` | mm | Total values for the quantile 0.09  
`total_values_quantile_0_1` | mm | Total values for the quantile 0.1  
`total_values_quantile_0_11` | mm | Total values for the quantile 0.11  
`total_values_quantile_0_12` | mm | Total values for the quantile 0.12  
`total_values_quantile_0_13` | mm | Total values for the quantile 0.13  
`total_values_quantile_0_14` | mm | Total values for the quantile 0.14  
`total_values_quantile_0_15` | mm | Total values for the quantile 0.15  
`total_values_quantile_0_16` | mm | Total values for the quantile 0.16  
`total_values_quantile_0_167` | mm | Total values for the quantile 0.167  
`total_values_quantile_0_17` | mm | Total values for the quantile 0.17  
`total_values_quantile_0_18` | mm | Total values for the quantile 0.18  
`total_values_quantile_0_19` | mm | Total values for the quantile 0.19  
`total_values_quantile_0_2` | mm | Total values for the quantile 0.2  
`total_values_quantile_0_21` | mm | Total values for the quantile 0.21  
`total_values_quantile_0_22` | mm | Total values for the quantile 0.22  
`total_values_quantile_0_23` | mm | Total values for the quantile 0.23  
`total_values_quantile_0_24` | mm | Total values for the quantile 0.24  
`total_values_quantile_0_25` | mm | Total values for the quantile 0.25  
`total_values_quantile_0_26` | mm | Total values for the quantile 0.26  
`total_values_quantile_0_27` | mm | Total values for the quantile 0.27  
`total_values_quantile_0_28` | mm | Total values for the quantile 0.28  
`total_values_quantile_0_29` | mm | Total values for the quantile 0.29  
`total_values_quantile_0_3` | mm | Total values for the quantile 0.3  
`total_values_quantile_0_31` | mm | Total values for the quantile 0.31  
`total_values_quantile_0_32` | mm | Total values for the quantile 0.32  
`total_values_quantile_0_33` | mm | Total values for the quantile 0.33  
`total_values_quantile_0_34` | mm | Total values for the quantile 0.34  
`total_values_quantile_0_35` | mm | Total values for the quantile 0.35  
`total_values_quantile_0_36` | mm | Total values for the quantile 0.36  
`total_values_quantile_0_37` | mm | Total values for the quantile 0.37  
`total_values_quantile_0_38` | mm | Total values for the quantile 0.38  
`total_values_quantile_0_39` | mm | Total values for the quantile 0.39  
`total_values_quantile_0_4` | mm | Total values for the quantile 0.4  
`total_values_quantile_0_41` | mm | Total values for the quantile 0.41  
`total_values_quantile_0_42` | mm | Total values for the quantile 0.42  
`total_values_quantile_0_43` | mm | Total values for the quantile 0.43  
`total_values_quantile_0_44` | mm | Total values for the quantile 0.44  
`total_values_quantile_0_45` | mm | Total values for the quantile 0.45  
`total_values_quantile_0_46` | mm | Total values for the quantile 0.46  
`total_values_quantile_0_47` | mm | Total values for the quantile 0.47  
`total_values_quantile_0_48` | mm | Total values for the quantile 0.48  
`total_values_quantile_0_49` | mm | Total values for the quantile 0.49  
`total_values_quantile_0_5` | mm | Total values for the quantile 0.5  
`total_values_quantile_0_51` | mm | Total values for the quantile 0.51  
`total_values_quantile_0_52` | mm | Total values for the quantile 0.52  
`total_values_quantile_0_53` | mm | Total values for the quantile 0.53  
`total_values_quantile_0_54` | mm | Total values for the quantile 0.54  
`total_values_quantile_0_55` | mm | Total values for the quantile 0.55  
`total_values_quantile_0_56` | mm | Total values for the quantile 0.56  
`total_values_quantile_0_57` | mm | Total values for the quantile 0.57  
`total_values_quantile_0_58` | mm | Total values for the quantile 0.58  
`total_values_quantile_0_59` | mm | Total values for the quantile 0.59  
`total_values_quantile_0_6` | mm | Total values for the quantile 0.6  
`total_values_quantile_0_61` | mm | Total values for the quantile 0.61  
`total_values_quantile_0_62` | mm | Total values for the quantile 0.62  
`total_values_quantile_0_63` | mm | Total values for the quantile 0.63  
`total_values_quantile_0_64` | mm | Total values for the quantile 0.64  
`total_values_quantile_0_65` | mm | Total values for the quantile 0.65  
`total_values_quantile_0_66` | mm | Total values for the quantile 0.66  
`total_values_quantile_0_67` | mm | Total values for the quantile 0.67  
`total_values_quantile_0_68` | mm | Total values for the quantile 0.68  
`total_values_quantile_0_69` | mm | Total values for the quantile 0.69  
`total_values_quantile_0_7` | mm | Total values for the quantile 0.7  
`total_values_quantile_0_71` | mm | Total values for the quantile 0.71  
`total_values_quantile_0_72` | mm | Total values for the quantile 0.72  
`total_values_quantile_0_73` | mm | Total values for the quantile 0.73  
`total_values_quantile_0_74` | mm | Total values for the quantile 0.74  
`total_values_quantile_0_75` | mm | Total values for the quantile 0.75  
`total_values_quantile_0_76` | mm | Total values for the quantile 0.76  
`total_values_quantile_0_77` | mm | Total values for the quantile 0.77  
`total_values_quantile_0_78` | mm | Total values for the quantile 0.78  
`total_values_quantile_0_79` | mm | Total values for the quantile 0.79  
`total_values_quantile_0_8` | mm | Total values for the quantile 0.8  
`total_values_quantile_0_81` | mm | Total values for the quantile 0.81  
`total_values_quantile_0_82` | mm | Total values for the quantile 0.82  
`total_values_quantile_0_83` | mm | Total values for the quantile 0.83  
`total_values_quantile_0_833` | mm | Total values for the quantile 0.833  
`total_values_quantile_0_84` | mm | Total values for the quantile 0.84  
`total_values_quantile_0_85` | mm | Total values for the quantile 0.85  
`total_values_quantile_0_86` | mm | Total values for the quantile 0.86  
`total_values_quantile_0_87` | mm | Total values for the quantile 0.87  
`total_values_quantile_0_88` | mm | Total values for the quantile 0.88  
`total_values_quantile_0_89` | mm | Total values for the quantile 0.89  
`total_values_quantile_0_9` | mm | Total values for the quantile 0.9  
`total_values_quantile_0_91` | mm | Total values for the quantile 0.91  
`total_values_quantile_0_92` | mm | Total values for the quantile 0.92  
`total_values_quantile_0_93` | mm | Total values for the quantile 0.93  
`total_values_quantile_0_94` | mm | Total values for the quantile 0.94  
`total_values_quantile_0_95` | mm | Total values for the quantile 0.95  
`total_values_quantile_0_96` | mm | Total values for the quantile 0.96  
`total_values_quantile_0_97` | mm | Total values for the quantile 0.97  
`total_values_quantile_0_98` | mm | Total values for the quantile 0.98  
`total_values_quantile_0_99` | mm | Total values for the quantile 0.99  
`total_values_quantile_0_995` | mm | Total values for the quantile 0.995  
`total_values_quantile_0_999` | mm | Total values for the quantile 0.999  
`total_values_quantile_1` | mm | Total values for the quantile 1  
`AIS_rates_quantile_0` | mm/y | AIS rates for the quantile 0  
`AIS_rates_quantile_0_001` | mm/y | AIS rates for the quantile 0.001  
`AIS_rates_quantile_0_005` | mm/y | AIS rates for the quantile 0.005  
`AIS_rates_quantile_0_01` | mm/y | AIS rates for the quantile 0.01  
`AIS_rates_quantile_0_02` | mm/y | AIS rates for the quantile 0.02  
`AIS_rates_quantile_0_03` | mm/y | AIS rates for the quantile 0.03  
`AIS_rates_quantile_0_04` | mm/y | AIS rates for the quantile 0.04  
`AIS_rates_quantile_0_05` | mm/y | AIS rates for the quantile 0.05  
`AIS_rates_quantile_0_06` | mm/y | AIS rates for the quantile 0.06  
`AIS_rates_quantile_0_07` | mm/y | AIS rates for the quantile 0.07  
`AIS_rates_quantile_0_08` | mm/y | AIS rates for the quantile 0.08  
`AIS_rates_quantile_0_09` | mm/y | AIS rates for the quantile 0.09  
`AIS_rates_quantile_0_1` | mm/y | AIS rates for the quantile 0.1  
`AIS_rates_quantile_0_11` | mm/y | AIS rates for the quantile 0.11  
`AIS_rates_quantile_0_12` | mm/y | AIS rates for the quantile 0.12  
`AIS_rates_quantile_0_13` | mm/y | AIS rates for the quantile 0.13  
`AIS_rates_quantile_0_14` | mm/y | AIS rates for the quantile 0.14  
`AIS_rates_quantile_0_15` | mm/y | AIS rates for the quantile 0.15  
`AIS_rates_quantile_0_16` | mm/y | AIS rates for the quantile 0.16  
`AIS_rates_quantile_0_167` | mm/y | AIS rates for the quantile 0.167  
`AIS_rates_quantile_0_17` | mm/y | AIS rates for the quantile 0.17  
`AIS_rates_quantile_0_18` | mm/y | AIS rates for the quantile 0.18  
`AIS_rates_quantile_0_19` | mm/y | AIS rates for the quantile 0.19  
`AIS_rates_quantile_0_2` | mm/y | AIS rates for the quantile 0.2  
`AIS_rates_quantile_0_21` | mm/y | AIS rates for the quantile 0.21  
`AIS_rates_quantile_0_22` | mm/y | AIS rates for the quantile 0.22  
`AIS_rates_quantile_0_23` | mm/y | AIS rates for the quantile 0.23  
`AIS_rates_quantile_0_24` | mm/y | AIS rates for the quantile 0.24  
`AIS_rates_quantile_0_25` | mm/y | AIS rates for the quantile 0.25  
`AIS_rates_quantile_0_26` | mm/y | AIS rates for the quantile 0.26  
`AIS_rates_quantile_0_27` | mm/y | AIS rates for the quantile 0.27  
`AIS_rates_quantile_0_28` | mm/y | AIS rates for the quantile 0.28  
`AIS_rates_quantile_0_29` | mm/y | AIS rates for the quantile 0.29  
`AIS_rates_quantile_0_3` | mm/y | AIS rates for the quantile 0.3  
`AIS_rates_quantile_0_31` | mm/y | AIS rates for the quantile 0.31  
`AIS_rates_quantile_0_32` | mm/y | AIS rates for the quantile 0.32  
`AIS_rates_quantile_0_33` | mm/y | AIS rates for the quantile 0.33  
`AIS_rates_quantile_0_34` | mm/y | AIS rates for the quantile 0.34  
`AIS_rates_quantile_0_35` | mm/y | AIS rates for the quantile 0.35  
`AIS_rates_quantile_0_36` | mm/y | AIS rates for the quantile 0.36  
`AIS_rates_quantile_0_37` | mm/y | AIS rates for the quantile 0.37  
`AIS_rates_quantile_0_38` | mm/y | AIS rates for the quantile 0.38  
`AIS_rates_quantile_0_39` | mm/y | AIS rates for the quantile 0.39  
`AIS_rates_quantile_0_4` | mm/y | AIS rates for the quantile 0.4  
`AIS_rates_quantile_0_41` | mm/y | AIS rates for the quantile 0.41  
`AIS_rates_quantile_0_42` | mm/y | AIS rates for the quantile 0.42  
`AIS_rates_quantile_0_43` | mm/y | AIS rates for the quantile 0.43  
`AIS_rates_quantile_0_44` | mm/y | AIS rates for the quantile 0.44  
`AIS_rates_quantile_0_45` | mm/y | AIS rates for the quantile 0.45  
`AIS_rates_quantile_0_46` | mm/y | AIS rates for the quantile 0.46  
`AIS_rates_quantile_0_47` | mm/y | AIS rates for the quantile 0.47  
`AIS_rates_quantile_0_48` | mm/y | AIS rates for the quantile 0.48  
`AIS_rates_quantile_0_49` | mm/y | AIS rates for the quantile 0.49  
`AIS_rates_quantile_0_5` | mm/y | AIS rates for the quantile 0.5  
`AIS_rates_quantile_0_51` | mm/y | AIS rates for the quantile 0.51  
`AIS_rates_quantile_0_52` | mm/y | AIS rates for the quantile 0.52  
`AIS_rates_quantile_0_53` | mm/y | AIS rates for the quantile 0.53  
`AIS_rates_quantile_0_54` | mm/y | AIS rates for the quantile 0.54  
`AIS_rates_quantile_0_55` | mm/y | AIS rates for the quantile 0.55  
`AIS_rates_quantile_0_56` | mm/y | AIS rates for the quantile 0.56  
`AIS_rates_quantile_0_57` | mm/y | AIS rates for the quantile 0.57  
`AIS_rates_quantile_0_58` | mm/y | AIS rates for the quantile 0.58  
`AIS_rates_quantile_0_59` | mm/y | AIS rates for the quantile 0.59  
`AIS_rates_quantile_0_6` | mm/y | AIS rates for the quantile 0.6  
`AIS_rates_quantile_0_61` | mm/y | AIS rates for the quantile 0.61  
`AIS_rates_quantile_0_62` | mm/y | AIS rates for the quantile 0.62  
`AIS_rates_quantile_0_63` | mm/y | AIS rates for the quantile 0.63  
`AIS_rates_quantile_0_64` | mm/y | AIS rates for the quantile 0.64  
`AIS_rates_quantile_0_65` | mm/y | AIS rates for the quantile 0.65  
`AIS_rates_quantile_0_66` | mm/y | AIS rates for the quantile 0.66  
`AIS_rates_quantile_0_67` | mm/y | AIS rates for the quantile 0.67  
`AIS_rates_quantile_0_68` | mm/y | AIS rates for the quantile 0.68  
`AIS_rates_quantile_0_69` | mm/y | AIS rates for the quantile 0.69  
`AIS_rates_quantile_0_7` | mm/y | AIS rates for the quantile 0.7  
`AIS_rates_quantile_0_71` | mm/y | AIS rates for the quantile 0.71  
`AIS_rates_quantile_0_72` | mm/y | AIS rates for the quantile 0.72  
`AIS_rates_quantile_0_73` | mm/y | AIS rates for the quantile 0.73  
`AIS_rates_quantile_0_74` | mm/y | AIS rates for the quantile 0.74  
`AIS_rates_quantile_0_75` | mm/y | AIS rates for the quantile 0.75  
`AIS_rates_quantile_0_76` | mm/y | AIS rates for the quantile 0.76  
`AIS_rates_quantile_0_77` | mm/y | AIS rates for the quantile 0.77  
`AIS_rates_quantile_0_78` | mm/y | AIS rates for the quantile 0.78  
`AIS_rates_quantile_0_79` | mm/y | AIS rates for the quantile 0.79  
`AIS_rates_quantile_0_8` | mm/y | AIS rates for the quantile 0.8  
`AIS_rates_quantile_0_81` | mm/y | AIS rates for the quantile 0.81  
`AIS_rates_quantile_0_82` | mm/y | AIS rates for the quantile 0.82  
`AIS_rates_quantile_0_83` | mm/y | AIS rates for the quantile 0.83  
`AIS_rates_quantile_0_833` | mm/y | AIS rates for the quantile 0.833  
`AIS_rates_quantile_0_84` | mm/y | AIS rates for the quantile 0.84  
`AIS_rates_quantile_0_85` | mm/y | AIS rates for the quantile 0.85  
`AIS_rates_quantile_0_86` | mm/y | AIS rates for the quantile 0.86  
`AIS_rates_quantile_0_87` | mm/y | AIS rates for the quantile 0.87  
`AIS_rates_quantile_0_88` | mm/y | AIS rates for the quantile 0.88  
`AIS_rates_quantile_0_89` | mm/y | AIS rates for the quantile 0.89  
`AIS_rates_quantile_0_9` | mm/y | AIS rates for the quantile 0.9  
`AIS_rates_quantile_0_91` | mm/y | AIS rates for the quantile 0.91  
`AIS_rates_quantile_0_92` | mm/y | AIS rates for the quantile 0.92  
`AIS_rates_quantile_0_93` | mm/y | AIS rates for the quantile 0.93  
`AIS_rates_quantile_0_94` | mm/y | AIS rates for the quantile 0.94  
`AIS_rates_quantile_0_95` | mm/y | AIS rates for the quantile 0.95  
`AIS_rates_quantile_0_96` | mm/y | AIS rates for the quantile 0.96  
`AIS_rates_quantile_0_97` | mm/y | AIS rates for the quantile 0.97  
`AIS_rates_quantile_0_98` | mm/y | AIS rates for the quantile 0.98  
`AIS_rates_quantile_0_99` | mm/y | AIS rates for the quantile 0.99  
`AIS_rates_quantile_0_995` | mm/y | AIS rates for the quantile 0.995  
`AIS_rates_quantile_0_999` | mm/y | AIS rates for the quantile 0.999  
`AIS_rates_quantile_1` | mm/y | AIS rates for the quantile 1  
`AIS_values_quantile_0` | mm | AIS values for the quantile 0  
`AIS_values_quantile_0_001` | mm | AIS values for the quantile 0.001  
`AIS_values_quantile_0_005` | mm | AIS values for the quantile 0.005  
`AIS_values_quantile_0_01` | mm | AIS values for the quantile 0.01  
`AIS_values_quantile_0_02` | mm | AIS values for the quantile 0.02  
`AIS_values_quantile_0_03` | mm | AIS values for the quantile 0.03  
`AIS_values_quantile_0_04` | mm | AIS values for the quantile 0.04  
`AIS_values_quantile_0_05` | mm | AIS values for the quantile 0.05  
`AIS_values_quantile_0_06` | mm | AIS values for the quantile 0.06  
`AIS_values_quantile_0_07` | mm | AIS values for the quantile 0.07  
`AIS_values_quantile_0_08` | mm | AIS values for the quantile 0.08  
`AIS_values_quantile_0_09` | mm | AIS values for the quantile 0.09  
`AIS_values_quantile_0_1` | mm | AIS values for the quantile 0.1  
`AIS_values_quantile_0_11` | mm | AIS values for the quantile 0.11  
`AIS_values_quantile_0_12` | mm | AIS values for the quantile 0.12  
`AIS_values_quantile_0_13` | mm | AIS values for the quantile 0.13  
`AIS_values_quantile_0_14` | mm | AIS values for the quantile 0.14  
`AIS_values_quantile_0_15` | mm | AIS values for the quantile 0.15  
`AIS_values_quantile_0_16` | mm | AIS values for the quantile 0.16  
`AIS_values_quantile_0_167` | mm | AIS values for the quantile 0.167  
`AIS_values_quantile_0_17` | mm | AIS values for the quantile 0.17  
`AIS_values_quantile_0_18` | mm | AIS values for the quantile 0.18  
`AIS_values_quantile_0_19` | mm | AIS values for the quantile 0.19  
`AIS_values_quantile_0_2` | mm | AIS values for the quantile 0.2  
`AIS_values_quantile_0_21` | mm | AIS values for the quantile 0.21  
`AIS_values_quantile_0_22` | mm | AIS values for the quantile 0.22  
`AIS_values_quantile_0_23` | mm | AIS values for the quantile 0.23  
`AIS_values_quantile_0_24` | mm | AIS values for the quantile 0.24  
`AIS_values_quantile_0_25` | mm | AIS values for the quantile 0.25  
`AIS_values_quantile_0_26` | mm | AIS values for the quantile 0.26  
`AIS_values_quantile_0_27` | mm | AIS values for the quantile 0.27  
`AIS_values_quantile_0_28` | mm | AIS values for the quantile 0.28  
`AIS_values_quantile_0_29` | mm | AIS values for the quantile 0.29  
`AIS_values_quantile_0_3` | mm | AIS values for the quantile 0.3  
`AIS_values_quantile_0_31` | mm | AIS values for the quantile 0.31  
`AIS_values_quantile_0_32` | mm | AIS values for the quantile 0.32  
`AIS_values_quantile_0_33` | mm | AIS values for the quantile 0.33  
`AIS_values_quantile_0_34` | mm | AIS values for the quantile 0.34  
`AIS_values_quantile_0_35` | mm | AIS values for the quantile 0.35  
`AIS_values_quantile_0_36` | mm | AIS values for the quantile 0.36  
`AIS_values_quantile_0_37` | mm | AIS values for the quantile 0.37  
`AIS_values_quantile_0_38` | mm | AIS values for the quantile 0.38  
`AIS_values_quantile_0_39` | mm | AIS values for the quantile 0.39  
`AIS_values_quantile_0_4` | mm | AIS values for the quantile 0.4  
`AIS_values_quantile_0_41` | mm | AIS values for the quantile 0.41  
`AIS_values_quantile_0_42` | mm | AIS values for the quantile 0.42  
`AIS_values_quantile_0_43` | mm | AIS values for the quantile 0.43  
`AIS_values_quantile_0_44` | mm | AIS values for the quantile 0.44  
`AIS_values_quantile_0_45` | mm | AIS values for the quantile 0.45  
`AIS_values_quantile_0_46` | mm | AIS values for the quantile 0.46  
`AIS_values_quantile_0_47` | mm | AIS values for the quantile 0.47  
`AIS_values_quantile_0_48` | mm | AIS values for the quantile 0.48  
`AIS_values_quantile_0_49` | mm | AIS values for the quantile 0.49  
`AIS_values_quantile_0_5` | mm | AIS values for the quantile 0.5  
`AIS_values_quantile_0_51` | mm | AIS values for the quantile 0.51  
`AIS_values_quantile_0_52` | mm | AIS values for the quantile 0.52  
`AIS_values_quantile_0_53` | mm | AIS values for the quantile 0.53  
`AIS_values_quantile_0_54` | mm | AIS values for the quantile 0.54  
`AIS_values_quantile_0_55` | mm | AIS values for the quantile 0.55  
`AIS_values_quantile_0_56` | mm | AIS values for the quantile 0.56  
`AIS_values_quantile_0_57` | mm | AIS values for the quantile 0.57  
`AIS_values_quantile_0_58` | mm | AIS values for the quantile 0.58  
`AIS_values_quantile_0_59` | mm | AIS values for the quantile 0.59  
`AIS_values_quantile_0_6` | mm | AIS values for the quantile 0.6  
`AIS_values_quantile_0_61` | mm | AIS values for the quantile 0.61  
`AIS_values_quantile_0_62` | mm | AIS values for the quantile 0.62  
`AIS_values_quantile_0_63` | mm | AIS values for the quantile 0.63  
`AIS_values_quantile_0_64` | mm | AIS values for the quantile 0.64  
`AIS_values_quantile_0_65` | mm | AIS values for the quantile 0.65  
`AIS_values_quantile_0_66` | mm | AIS values for the quantile 0.66  
`AIS_values_quantile_0_67` | mm | AIS values for the quantile 0.67  
`AIS_values_quantile_0_68` | mm | AIS values for the quantile 0.68  
`AIS_values_quantile_0_69` | mm | AIS values for the quantile 0.69  
`AIS_values_quantile_0_7` | mm | AIS values for the quantile 0.7  
`AIS_values_quantile_0_71` | mm | AIS values for the quantile 0.71  
`AIS_values_quantile_0_72` | mm | AIS values for the quantile 0.72  
`AIS_values_quantile_0_73` | mm | AIS values for the quantile 0.73  
`AIS_values_quantile_0_74` | mm | AIS values for the quantile 0.74  
`AIS_values_quantile_0_75` | mm | AIS values for the quantile 0.75  
`AIS_values_quantile_0_76` | mm | AIS values for the quantile 0.76  
`AIS_values_quantile_0_77` | mm | AIS values for the quantile 0.77  
`AIS_values_quantile_0_78` | mm | AIS values for the quantile 0.78  
`AIS_values_quantile_0_79` | mm | AIS values for the quantile 0.79  
`AIS_values_quantile_0_8` | mm | AIS values for the quantile 0.8  
`AIS_values_quantile_0_81` | mm | AIS values for the quantile 0.81  
`AIS_values_quantile_0_82` | mm | AIS values for the quantile 0.82  
`AIS_values_quantile_0_83` | mm | AIS values for the quantile 0.83  
`AIS_values_quantile_0_833` | mm | AIS values for the quantile 0.833  
`AIS_values_quantile_0_84` | mm | AIS values for the quantile 0.84  
`AIS_values_quantile_0_85` | mm | AIS values for the quantile 0.85  
`AIS_values_quantile_0_86` | mm | AIS values for the quantile 0.86  
`AIS_values_quantile_0_87` | mm | AIS values for the quantile 0.87  
`AIS_values_quantile_0_88` | mm | AIS values for the quantile 0.88  
`AIS_values_quantile_0_89` | mm | AIS values for the quantile 0.89  
`AIS_values_quantile_0_9` | mm | AIS values for the quantile 0.9  
`AIS_values_quantile_0_91` | mm | AIS values for the quantile 0.91  
`AIS_values_quantile_0_92` | mm | AIS values for the quantile 0.92  
`AIS_values_quantile_0_93` | mm | AIS values for the quantile 0.93  
`AIS_values_quantile_0_94` | mm | AIS values for the quantile 0.94  
`AIS_values_quantile_0_95` | mm | AIS values for the quantile 0.95  
`AIS_values_quantile_0_96` | mm | AIS values for the quantile 0.96  
`AIS_values_quantile_0_97` | mm | AIS values for the quantile 0.97  
`AIS_values_quantile_0_98` | mm | AIS values for the quantile 0.98  
`AIS_values_quantile_0_99` | mm | AIS values for the quantile 0.99  
`AIS_values_quantile_0_995` | mm | AIS values for the quantile 0.995  
`AIS_values_quantile_0_999` | mm | AIS values for the quantile 0.999  
`AIS_values_quantile_1` | mm | AIS values for the quantile 1  
`GIS_rates_quantile_0` | mm/y | GIS rates for the quantile 0  
`GIS_rates_quantile_0_001` | mm/y | GIS rates for the quantile 0.001  
`GIS_rates_quantile_0_005` | mm/y | GIS rates for the quantile 0.005  
`GIS_rates_quantile_0_01` | mm/y | GIS rates for the quantile 0.01  
`GIS_rates_quantile_0_02` | mm/y | GIS rates for the quantile 0.02  
`GIS_rates_quantile_0_03` | mm/y | GIS rates for the quantile 0.03  
`GIS_rates_quantile_0_04` | mm/y | GIS rates for the quantile 0.04  
`GIS_rates_quantile_0_05` | mm/y | GIS rates for the quantile 0.05  
`GIS_rates_quantile_0_06` | mm/y | GIS rates for the quantile 0.06  
`GIS_rates_quantile_0_07` | mm/y | GIS rates for the quantile 0.07  
`GIS_rates_quantile_0_08` | mm/y | GIS rates for the quantile 0.08  
`GIS_rates_quantile_0_09` | mm/y | GIS rates for the quantile 0.09  
`GIS_rates_quantile_0_1` | mm/y | GIS rates for the quantile 0.1  
`GIS_rates_quantile_0_11` | mm/y | GIS rates for the quantile 0.11  
`GIS_rates_quantile_0_12` | mm/y | GIS rates for the quantile 0.12  
`GIS_rates_quantile_0_13` | mm/y | GIS rates for the quantile 0.13  
`GIS_rates_quantile_0_14` | mm/y | GIS rates for the quantile 0.14  
`GIS_rates_quantile_0_15` | mm/y | GIS rates for the quantile 0.15  
`GIS_rates_quantile_0_16` | mm/y | GIS rates for the quantile 0.16  
`GIS_rates_quantile_0_167` | mm/y | GIS rates for the quantile 0.167  
`GIS_rates_quantile_0_17` | mm/y | GIS rates for the quantile 0.17  
`GIS_rates_quantile_0_18` | mm/y | GIS rates for the quantile 0.18  
`GIS_rates_quantile_0_19` | mm/y | GIS rates for the quantile 0.19  
`GIS_rates_quantile_0_2` | mm/y | GIS rates for the quantile 0.2  
`GIS_rates_quantile_0_21` | mm/y | GIS rates for the quantile 0.21  
`GIS_rates_quantile_0_22` | mm/y | GIS rates for the quantile 0.22  
`GIS_rates_quantile_0_23` | mm/y | GIS rates for the quantile 0.23  
`GIS_rates_quantile_0_24` | mm/y | GIS rates for the quantile 0.24  
`GIS_rates_quantile_0_25` | mm/y | GIS rates for the quantile 0.25  
`GIS_rates_quantile_0_26` | mm/y | GIS rates for the quantile 0.26  
`GIS_rates_quantile_0_27` | mm/y | GIS rates for the quantile 0.27  
`GIS_rates_quantile_0_28` | mm/y | GIS rates for the quantile 0.28  
`GIS_rates_quantile_0_29` | mm/y | GIS rates for the quantile 0.29  
`GIS_rates_quantile_0_3` | mm/y | GIS rates for the quantile 0.3  
`GIS_rates_quantile_0_31` | mm/y | GIS rates for the quantile 0.31  
`GIS_rates_quantile_0_32` | mm/y | GIS rates for the quantile 0.32  
`GIS_rates_quantile_0_33` | mm/y | GIS rates for the quantile 0.33  
`GIS_rates_quantile_0_34` | mm/y | GIS rates for the quantile 0.34  
`GIS_rates_quantile_0_35` | mm/y | GIS rates for the quantile 0.35  
`GIS_rates_quantile_0_36` | mm/y | GIS rates for the quantile 0.36  
`GIS_rates_quantile_0_37` | mm/y | GIS rates for the quantile 0.37  
`GIS_rates_quantile_0_38` | mm/y | GIS rates for the quantile 0.38  
`GIS_rates_quantile_0_39` | mm/y | GIS rates for the quantile 0.39  
`GIS_rates_quantile_0_4` | mm/y | GIS rates for the quantile 0.4  
`GIS_rates_quantile_0_41` | mm/y | GIS rates for the quantile 0.41  
`GIS_rates_quantile_0_42` | mm/y | GIS rates for the quantile 0.42  
`GIS_rates_quantile_0_43` | mm/y | GIS rates for the quantile 0.43  
`GIS_rates_quantile_0_44` | mm/y | GIS rates for the quantile 0.44  
`GIS_rates_quantile_0_45` | mm/y | GIS rates for the quantile 0.45  
`GIS_rates_quantile_0_46` | mm/y | GIS rates for the quantile 0.46  
`GIS_rates_quantile_0_47` | mm/y | GIS rates for the quantile 0.47  
`GIS_rates_quantile_0_48` | mm/y | GIS rates for the quantile 0.48  
`GIS_rates_quantile_0_49` | mm/y | GIS rates for the quantile 0.49  
`GIS_rates_quantile_0_5` | mm/y | GIS rates for the quantile 0.5  
`GIS_rates_quantile_0_51` | mm/y | GIS rates for the quantile 0.51  
`GIS_rates_quantile_0_52` | mm/y | GIS rates for the quantile 0.52  
`GIS_rates_quantile_0_53` | mm/y | GIS rates for the quantile 0.53  
`GIS_rates_quantile_0_54` | mm/y | GIS rates for the quantile 0.54  
`GIS_rates_quantile_0_55` | mm/y | GIS rates for the quantile 0.55  
`GIS_rates_quantile_0_56` | mm/y | GIS rates for the quantile 0.56  
`GIS_rates_quantile_0_57` | mm/y | GIS rates for the quantile 0.57  
`GIS_rates_quantile_0_58` | mm/y | GIS rates for the quantile 0.58  
`GIS_rates_quantile_0_59` | mm/y | GIS rates for the quantile 0.59  
`GIS_rates_quantile_0_6` | mm/y | GIS rates for the quantile 0.6  
`GIS_rates_quantile_0_61` | mm/y | GIS rates for the quantile 0.61  
`GIS_rates_quantile_0_62` | mm/y | GIS rates for the quantile 0.62  
`GIS_rates_quantile_0_63` | mm/y | GIS rates for the quantile 0.63  
`GIS_rates_quantile_0_64` | mm/y | GIS rates for the quantile 0.64  
`GIS_rates_quantile_0_65` | mm/y | GIS rates for the quantile 0.65  
`GIS_rates_quantile_0_66` | mm/y | GIS rates for the quantile 0.66  
`GIS_rates_quantile_0_67` | mm/y | GIS rates for the quantile 0.67  
`GIS_rates_quantile_0_68` | mm/y | GIS rates for the quantile 0.68  
`GIS_rates_quantile_0_69` | mm/y | GIS rates for the quantile 0.69  
`GIS_rates_quantile_0_7` | mm/y | GIS rates for the quantile 0.7  
`GIS_rates_quantile_0_71` | mm/y | GIS rates for the quantile 0.71  
`GIS_rates_quantile_0_72` | mm/y | GIS rates for the quantile 0.72  
`GIS_rates_quantile_0_73` | mm/y | GIS rates for the quantile 0.73  
`GIS_rates_quantile_0_74` | mm/y | GIS rates for the quantile 0.74  
`GIS_rates_quantile_0_75` | mm/y | GIS rates for the quantile 0.75  
`GIS_rates_quantile_0_76` | mm/y | GIS rates for the quantile 0.76  
`GIS_rates_quantile_0_77` | mm/y | GIS rates for the quantile 0.77  
`GIS_rates_quantile_0_78` | mm/y | GIS rates for the quantile 0.78  
`GIS_rates_quantile_0_79` | mm/y | GIS rates for the quantile 0.79  
`GIS_rates_quantile_0_8` | mm/y | GIS rates for the quantile 0.8  
`GIS_rates_quantile_0_81` | mm/y | GIS rates for the quantile 0.81  
`GIS_rates_quantile_0_82` | mm/y | GIS rates for the quantile 0.82  
`GIS_rates_quantile_0_83` | mm/y | GIS rates for the quantile 0.83  
`GIS_rates_quantile_0_833` | mm/y | GIS rates for the quantile 0.833  
`GIS_rates_quantile_0_84` | mm/y | GIS rates for the quantile 0.84  
`GIS_rates_quantile_0_85` | mm/y | GIS rates for the quantile 0.85  
`GIS_rates_quantile_0_86` | mm/y | GIS rates for the quantile 0.86  
`GIS_rates_quantile_0_87` | mm/y | GIS rates for the quantile 0.87  
`GIS_rates_quantile_0_88` | mm/y | GIS rates for the quantile 0.88  
`GIS_rates_quantile_0_89` | mm/y | GIS rates for the quantile 0.89  
`GIS_rates_quantile_0_9` | mm/y | GIS rates for the quantile 0.9  
`GIS_rates_quantile_0_91` | mm/y | GIS rates for the quantile 0.91  
`GIS_rates_quantile_0_92` | mm/y | GIS rates for the quantile 0.92  
`GIS_rates_quantile_0_93` | mm/y | GIS rates for the quantile 0.93  
`GIS_rates_quantile_0_94` | mm/y | GIS rates for the quantile 0.94  
`GIS_rates_quantile_0_95` | mm/y | GIS rates for the quantile 0.95  
`GIS_rates_quantile_0_96` | mm/y | GIS rates for the quantile 0.96  
`GIS_rates_quantile_0_97` | mm/y | GIS rates for the quantile 0.97  
`GIS_rates_quantile_0_98` | mm/y | GIS rates for the quantile 0.98  
`GIS_rates_quantile_0_99` | mm/y | GIS rates for the quantile 0.99  
`GIS_rates_quantile_0_995` | mm/y | GIS rates for the quantile 0.995  
`GIS_rates_quantile_0_999` | mm/y | GIS rates for the quantile 0.999  
`GIS_rates_quantile_1` | mm/y | GIS rates for the quantile 1  
`GIS_values_quantile_0` | mm | GIS values for the quantile 0  
`GIS_values_quantile_0_001` | mm | GIS values for the quantile 0.001  
`GIS_values_quantile_0_005` | mm | GIS values for the quantile 0.005  
`GIS_values_quantile_0_01` | mm | GIS values for the quantile 0.01  
`GIS_values_quantile_0_02` | mm | GIS values for the quantile 0.02  
`GIS_values_quantile_0_03` | mm | GIS values for the quantile 0.03  
`GIS_values_quantile_0_04` | mm | GIS values for the quantile 0.04  
`GIS_values_quantile_0_05` | mm | GIS values for the quantile 0.05  
`GIS_values_quantile_0_06` | mm | GIS values for the quantile 0.06  
`GIS_values_quantile_0_07` | mm | GIS values for the quantile 0.07  
`GIS_values_quantile_0_08` | mm | GIS values for the quantile 0.08  
`GIS_values_quantile_0_09` | mm | GIS values for the quantile 0.09  
`GIS_values_quantile_0_1` | mm | GIS values for the quantile 0.1  
`GIS_values_quantile_0_11` | mm | GIS values for the quantile 0.11  
`GIS_values_quantile_0_12` | mm | GIS values for the quantile 0.12  
`GIS_values_quantile_0_13` | mm | GIS values for the quantile 0.13  
`GIS_values_quantile_0_14` | mm | GIS values for the quantile 0.14  
`GIS_values_quantile_0_15` | mm | GIS values for the quantile 0.15  
`GIS_values_quantile_0_16` | mm | GIS values for the quantile 0.16  
`GIS_values_quantile_0_167` | mm | GIS values for the quantile 0.167  
`GIS_values_quantile_0_17` | mm | GIS values for the quantile 0.17  
`GIS_values_quantile_0_18` | mm | GIS values for the quantile 0.18  
`GIS_values_quantile_0_19` | mm | GIS values for the quantile 0.19  
`GIS_values_quantile_0_2` | mm | GIS values for the quantile 0.2  
`GIS_values_quantile_0_21` | mm | GIS values for the quantile 0.21  
`GIS_values_quantile_0_22` | mm | GIS values for the quantile 0.22  
`GIS_values_quantile_0_23` | mm | GIS values for the quantile 0.23  
`GIS_values_quantile_0_24` | mm | GIS values for the quantile 0.24  
`GIS_values_quantile_0_25` | mm | GIS values for the quantile 0.25  
`GIS_values_quantile_0_26` | mm | GIS values for the quantile 0.26  
`GIS_values_quantile_0_27` | mm | GIS values for the quantile 0.27  
`GIS_values_quantile_0_28` | mm | GIS values for the quantile 0.28  
`GIS_values_quantile_0_29` | mm | GIS values for the quantile 0.29  
`GIS_values_quantile_0_3` | mm | GIS values for the quantile 0.3  
`GIS_values_quantile_0_31` | mm | GIS values for the quantile 0.31  
`GIS_values_quantile_0_32` | mm | GIS values for the quantile 0.32  
`GIS_values_quantile_0_33` | mm | GIS values for the quantile 0.33  
`GIS_values_quantile_0_34` | mm | GIS values for the quantile 0.34  
`GIS_values_quantile_0_35` | mm | GIS values for the quantile 0.35  
`GIS_values_quantile_0_36` | mm | GIS values for the quantile 0.36  
`GIS_values_quantile_0_37` | mm | GIS values for the quantile 0.37  
`GIS_values_quantile_0_38` | mm | GIS values for the quantile 0.38  
`GIS_values_quantile_0_39` | mm | GIS values for the quantile 0.39  
`GIS_values_quantile_0_4` | mm | GIS values for the quantile 0.4  
`GIS_values_quantile_0_41` | mm | GIS values for the quantile 0.41  
`GIS_values_quantile_0_42` | mm | GIS values for the quantile 0.42  
`GIS_values_quantile_0_43` | mm | GIS values for the quantile 0.43  
`GIS_values_quantile_0_44` | mm | GIS values for the quantile 0.44  
`GIS_values_quantile_0_45` | mm | GIS values for the quantile 0.45  
`GIS_values_quantile_0_46` | mm | GIS values for the quantile 0.46  
`GIS_values_quantile_0_47` | mm | GIS values for the quantile 0.47  
`GIS_values_quantile_0_48` | mm | GIS values for the quantile 0.48  
`GIS_values_quantile_0_49` | mm | GIS values for the quantile 0.49  
`GIS_values_quantile_0_5` | mm | GIS values for the quantile 0.5  
`GIS_values_quantile_0_51` | mm | GIS values for the quantile 0.51  
`GIS_values_quantile_0_52` | mm | GIS values for the quantile 0.52  
`GIS_values_quantile_0_53` | mm | GIS values for the quantile 0.53  
`GIS_values_quantile_0_54` | mm | GIS values for the quantile 0.54  
`GIS_values_quantile_0_55` | mm | GIS values for the quantile 0.55  
`GIS_values_quantile_0_56` | mm | GIS values for the quantile 0.56  
`GIS_values_quantile_0_57` | mm | GIS values for the quantile 0.57  
`GIS_values_quantile_0_58` | mm | GIS values for the quantile 0.58  
`GIS_values_quantile_0_59` | mm | GIS values for the quantile 0.59  
`GIS_values_quantile_0_6` | mm | GIS values for the quantile 0.6  
`GIS_values_quantile_0_61` | mm | GIS values for the quantile 0.61  
`GIS_values_quantile_0_62` | mm | GIS values for the quantile 0.62  
`GIS_values_quantile_0_63` | mm | GIS values for the quantile 0.63  
`GIS_values_quantile_0_64` | mm | GIS values for the quantile 0.64  
`GIS_values_quantile_0_65` | mm | GIS values for the quantile 0.65  
`GIS_values_quantile_0_66` | mm | GIS values for the quantile 0.66  
`GIS_values_quantile_0_67` | mm | GIS values for the quantile 0.67  
`GIS_values_quantile_0_68` | mm | GIS values for the quantile 0.68  
`GIS_values_quantile_0_69` | mm | GIS values for the quantile 0.69  
`GIS_values_quantile_0_7` | mm | GIS values for the quantile 0.7  
`GIS_values_quantile_0_71` | mm | GIS values for the quantile 0.71  
`GIS_values_quantile_0_72` | mm | GIS values for the quantile 0.72  
`GIS_values_quantile_0_73` | mm | GIS values for the quantile 0.73  
`GIS_values_quantile_0_74` | mm | GIS values for the quantile 0.74  
`GIS_values_quantile_0_75` | mm | GIS values for the quantile 0.75  
`GIS_values_quantile_0_76` | mm | GIS values for the quantile 0.76  
`GIS_values_quantile_0_77` | mm | GIS values for the quantile 0.77  
`GIS_values_quantile_0_78` | mm | GIS values for the quantile 0.78  
`GIS_values_quantile_0_79` | mm | GIS values for the quantile 0.79  
`GIS_values_quantile_0_8` | mm | GIS values for the quantile 0.8  
`GIS_values_quantile_0_81` | mm | GIS values for the quantile 0.81  
`GIS_values_quantile_0_82` | mm | GIS values for the quantile 0.82  
`GIS_values_quantile_0_83` | mm | GIS values for the quantile 0.83  
`GIS_values_quantile_0_833` | mm | GIS values for the quantile 0.833  
`GIS_values_quantile_0_84` | mm | GIS values for the quantile 0.84  
`GIS_values_quantile_0_85` | mm | GIS values for the quantile 0.85  
`GIS_values_quantile_0_86` | mm | GIS values for the quantile 0.86  
`GIS_values_quantile_0_87` | mm | GIS values for the quantile 0.87  
`GIS_values_quantile_0_88` | mm | GIS values for the quantile 0.88  
`GIS_values_quantile_0_89` | mm | GIS values for the quantile 0.89  
`GIS_values_quantile_0_9` | mm | GIS values for the quantile 0.9  
`GIS_values_quantile_0_91` | mm | GIS values for the quantile 0.91  
`GIS_values_quantile_0_92` | mm | GIS values for the quantile 0.92  
`GIS_values_quantile_0_93` | mm | GIS values for the quantile 0.93  
`GIS_values_quantile_0_94` | mm | GIS values for the quantile 0.94  
`GIS_values_quantile_0_95` | mm | GIS values for the quantile 0.95  
`GIS_values_quantile_0_96` | mm | GIS values for the quantile 0.96  
`GIS_values_quantile_0_97` | mm | GIS values for the quantile 0.97  
`GIS_values_quantile_0_98` | mm | GIS values for the quantile 0.98  
`GIS_values_quantile_0_99` | mm | GIS values for the quantile 0.99  
`GIS_values_quantile_0_995` | mm | GIS values for the quantile 0.995  
`GIS_values_quantile_0_999` | mm | GIS values for the quantile 0.999  
`GIS_values_quantile_1` | mm | GIS values for the quantile 1  
`glaciers_rates_quantile_0` | mm/y | Glaciers rates for the quantile 0  
`glaciers_rates_quantile_0_001` | mm/y | Glaciers rates for the quantile 0.001  
`glaciers_rates_quantile_0_005` | mm/y | Glaciers rates for the quantile 0.005  
`glaciers_rates_quantile_0_01` | mm/y | Glaciers rates for the quantile 0.01  
`glaciers_rates_quantile_0_02` | mm/y | Glaciers rates for the quantile 0.02  
`glaciers_rates_quantile_0_03` | mm/y | Glaciers rates for the quantile 0.03  
`glaciers_rates_quantile_0_04` | mm/y | Glaciers rates for the quantile 0.04  
`glaciers_rates_quantile_0_05` | mm/y | Glaciers rates for the quantile 0.05  
`glaciers_rates_quantile_0_06` | mm/y | Glaciers rates for the quantile 0.06  
`glaciers_rates_quantile_0_07` | mm/y | Glaciers rates for the quantile 0.07  
`glaciers_rates_quantile_0_08` | mm/y | Glaciers rates for the quantile 0.08  
`glaciers_rates_quantile_0_09` | mm/y | Glaciers rates for the quantile 0.09  
`glaciers_rates_quantile_0_1` | mm/y | Glaciers rates for the quantile 0.1  
`glaciers_rates_quantile_0_11` | mm/y | Glaciers rates for the quantile 0.11  
`glaciers_rates_quantile_0_12` | mm/y | Glaciers rates for the quantile 0.12  
`glaciers_rates_quantile_0_13` | mm/y | Glaciers rates for the quantile 0.13  
`glaciers_rates_quantile_0_14` | mm/y | Glaciers rates for the quantile 0.14  
`glaciers_rates_quantile_0_15` | mm/y | Glaciers rates for the quantile 0.15  
`glaciers_rates_quantile_0_16` | mm/y | Glaciers rates for the quantile 0.16  
`glaciers_rates_quantile_0_167` | mm/y | Glaciers rates for the quantile 0.167  
`glaciers_rates_quantile_0_17` | mm/y | Glaciers rates for the quantile 0.17  
`glaciers_rates_quantile_0_18` | mm/y | Glaciers rates for the quantile 0.18  
`glaciers_rates_quantile_0_19` | mm/y | Glaciers rates for the quantile 0.19  
`glaciers_rates_quantile_0_2` | mm/y | Glaciers rates for the quantile 0.2  
`glaciers_rates_quantile_0_21` | mm/y | Glaciers rates for the quantile 0.21  
`glaciers_rates_quantile_0_22` | mm/y | Glaciers rates for the quantile 0.22  
`glaciers_rates_quantile_0_23` | mm/y | Glaciers rates for the quantile 0.23  
`glaciers_rates_quantile_0_24` | mm/y | Glaciers rates for the quantile 0.24  
`glaciers_rates_quantile_0_25` | mm/y | Glaciers rates for the quantile 0.25  
`glaciers_rates_quantile_0_26` | mm/y | Glaciers rates for the quantile 0.26  
`glaciers_rates_quantile_0_27` | mm/y | Glaciers rates for the quantile 0.27  
`glaciers_rates_quantile_0_28` | mm/y | Glaciers rates for the quantile 0.28  
`glaciers_rates_quantile_0_29` | mm/y | Glaciers rates for the quantile 0.29  
`glaciers_rates_quantile_0_3` | mm/y | Glaciers rates for the quantile 0.3  
`glaciers_rates_quantile_0_31` | mm/y | Glaciers rates for the quantile 0.31  
`glaciers_rates_quantile_0_32` | mm/y | Glaciers rates for the quantile 0.32  
`glaciers_rates_quantile_0_33` | mm/y | Glaciers rates for the quantile 0.33  
`glaciers_rates_quantile_0_34` | mm/y | Glaciers rates for the quantile 0.34  
`glaciers_rates_quantile_0_35` | mm/y | Glaciers rates for the quantile 0.35  
`glaciers_rates_quantile_0_36` | mm/y | Glaciers rates for the quantile 0.36  
`glaciers_rates_quantile_0_37` | mm/y | Glaciers rates for the quantile 0.37  
`glaciers_rates_quantile_0_38` | mm/y | Glaciers rates for the quantile 0.38  
`glaciers_rates_quantile_0_39` | mm/y | Glaciers rates for the quantile 0.39  
`glaciers_rates_quantile_0_4` | mm/y | Glaciers rates for the quantile 0.4  
`glaciers_rates_quantile_0_41` | mm/y | Glaciers rates for the quantile 0.41  
`glaciers_rates_quantile_0_42` | mm/y | Glaciers rates for the quantile 0.42  
`glaciers_rates_quantile_0_43` | mm/y | Glaciers rates for the quantile 0.43  
`glaciers_rates_quantile_0_44` | mm/y | Glaciers rates for the quantile 0.44  
`glaciers_rates_quantile_0_45` | mm/y | Glaciers rates for the quantile 0.45  
`glaciers_rates_quantile_0_46` | mm/y | Glaciers rates for the quantile 0.46  
`glaciers_rates_quantile_0_47` | mm/y | Glaciers rates for the quantile 0.47  
`glaciers_rates_quantile_0_48` | mm/y | Glaciers rates for the quantile 0.48  
`glaciers_rates_quantile_0_49` | mm/y | Glaciers rates for the quantile 0.49  
`glaciers_rates_quantile_0_5` | mm/y | Glaciers rates for the quantile 0.5  
`glaciers_rates_quantile_0_51` | mm/y | Glaciers rates for the quantile 0.51  
`glaciers_rates_quantile_0_52` | mm/y | Glaciers rates for the quantile 0.52  
`glaciers_rates_quantile_0_53` | mm/y | Glaciers rates for the quantile 0.53  
`glaciers_rates_quantile_0_54` | mm/y | Glaciers rates for the quantile 0.54  
`glaciers_rates_quantile_0_55` | mm/y | Glaciers rates for the quantile 0.55  
`glaciers_rates_quantile_0_56` | mm/y | Glaciers rates for the quantile 0.56  
`glaciers_rates_quantile_0_57` | mm/y | Glaciers rates for the quantile 0.57  
`glaciers_rates_quantile_0_58` | mm/y | Glaciers rates for the quantile 0.58  
`glaciers_rates_quantile_0_59` | mm/y | Glaciers rates for the quantile 0.59  
`glaciers_rates_quantile_0_6` | mm/y | Glaciers rates for the quantile 0.6  
`glaciers_rates_quantile_0_61` | mm/y | Glaciers rates for the quantile 0.61  
`glaciers_rates_quantile_0_62` | mm/y | Glaciers rates for the quantile 0.62  
`glaciers_rates_quantile_0_63` | mm/y | Glaciers rates for the quantile 0.63  
`glaciers_rates_quantile_0_64` | mm/y | Glaciers rates for the quantile 0.64  
`glaciers_rates_quantile_0_65` | mm/y | Glaciers rates for the quantile 0.65  
`glaciers_rates_quantile_0_66` | mm/y | Glaciers rates for the quantile 0.66  
`glaciers_rates_quantile_0_67` | mm/y | Glaciers rates for the quantile 0.67  
`glaciers_rates_quantile_0_68` | mm/y | Glaciers rates for the quantile 0.68  
`glaciers_rates_quantile_0_69` | mm/y | Glaciers rates for the quantile 0.69  
`glaciers_rates_quantile_0_7` | mm/y | Glaciers rates for the quantile 0.7  
`glaciers_rates_quantile_0_71` | mm/y | Glaciers rates for the quantile 0.71  
`glaciers_rates_quantile_0_72` | mm/y | Glaciers rates for the quantile 0.72  
`glaciers_rates_quantile_0_73` | mm/y | Glaciers rates for the quantile 0.73  
`glaciers_rates_quantile_0_74` | mm/y | Glaciers rates for the quantile 0.74  
`glaciers_rates_quantile_0_75` | mm/y | Glaciers rates for the quantile 0.75  
`glaciers_rates_quantile_0_76` | mm/y | Glaciers rates for the quantile 0.76  
`glaciers_rates_quantile_0_77` | mm/y | Glaciers rates for the quantile 0.77  
`glaciers_rates_quantile_0_78` | mm/y | Glaciers rates for the quantile 0.78  
`glaciers_rates_quantile_0_79` | mm/y | Glaciers rates for the quantile 0.79  
`glaciers_rates_quantile_0_8` | mm/y | Glaciers rates for the quantile 0.8  
`glaciers_rates_quantile_0_81` | mm/y | Glaciers rates for the quantile 0.81  
`glaciers_rates_quantile_0_82` | mm/y | Glaciers rates for the quantile 0.82  
`glaciers_rates_quantile_0_83` | mm/y | Glaciers rates for the quantile 0.83  
`glaciers_rates_quantile_0_833` | mm/y | Glaciers rates for the quantile 0.833  
`glaciers_rates_quantile_0_84` | mm/y | Glaciers rates for the quantile 0.84  
`glaciers_rates_quantile_0_85` | mm/y | Glaciers rates for the quantile 0.85  
`glaciers_rates_quantile_0_86` | mm/y | Glaciers rates for the quantile 0.86  
`glaciers_rates_quantile_0_87` | mm/y | Glaciers rates for the quantile 0.87  
`glaciers_rates_quantile_0_88` | mm/y | Glaciers rates for the quantile 0.88  
`glaciers_rates_quantile_0_89` | mm/y | Glaciers rates for the quantile 0.89  
`glaciers_rates_quantile_0_9` | mm/y | Glaciers rates for the quantile 0.9  
`glaciers_rates_quantile_0_91` | mm/y | Glaciers rates for the quantile 0.91  
`glaciers_rates_quantile_0_92` | mm/y | Glaciers rates for the quantile 0.92  
`glaciers_rates_quantile_0_93` | mm/y | Glaciers rates for the quantile 0.93  
`glaciers_rates_quantile_0_94` | mm/y | Glaciers rates for the quantile 0.94  
`glaciers_rates_quantile_0_95` | mm/y | Glaciers rates for the quantile 0.95  
`glaciers_rates_quantile_0_96` | mm/y | Glaciers rates for the quantile 0.96  
`glaciers_rates_quantile_0_97` | mm/y | Glaciers rates for the quantile 0.97  
`glaciers_rates_quantile_0_98` | mm/y | Glaciers rates for the quantile 0.98  
`glaciers_rates_quantile_0_99` | mm/y | Glaciers rates for the quantile 0.99  
`glaciers_rates_quantile_0_995` | mm/y | Glaciers rates for the quantile 0.995  
`glaciers_rates_quantile_0_999` | mm/y | Glaciers rates for the quantile 0.999  
`glaciers_rates_quantile_1` | mm/y | Glaciers rates for the quantile 1  
`glaciers_values_quantile_0` | mm | Glaciers values for the quantile 0  
`glaciers_values_quantile_0_001` | mm | Glaciers values for the quantile 0.001  
`glaciers_values_quantile_0_005` | mm | Glaciers values for the quantile 0.005  
`glaciers_values_quantile_0_01` | mm | Glaciers values for the quantile 0.01  
`glaciers_values_quantile_0_02` | mm | Glaciers values for the quantile 0.02  
`glaciers_values_quantile_0_03` | mm | Glaciers values for the quantile 0.03  
`glaciers_values_quantile_0_04` | mm | Glaciers values for the quantile 0.04  
`glaciers_values_quantile_0_05` | mm | Glaciers values for the quantile 0.05  
`glaciers_values_quantile_0_06` | mm | Glaciers values for the quantile 0.06  
`glaciers_values_quantile_0_07` | mm | Glaciers values for the quantile 0.07  
`glaciers_values_quantile_0_08` | mm | Glaciers values for the quantile 0.08  
`glaciers_values_quantile_0_09` | mm | Glaciers values for the quantile 0.09  
`glaciers_values_quantile_0_1` | mm | Glaciers values for the quantile 0.1  
`glaciers_values_quantile_0_11` | mm | Glaciers values for the quantile 0.11  
`glaciers_values_quantile_0_12` | mm | Glaciers values for the quantile 0.12  
`glaciers_values_quantile_0_13` | mm | Glaciers values for the quantile 0.13  
`glaciers_values_quantile_0_14` | mm | Glaciers values for the quantile 0.14  
`glaciers_values_quantile_0_15` | mm | Glaciers values for the quantile 0.15  
`glaciers_values_quantile_0_16` | mm | Glaciers values for the quantile 0.16  
`glaciers_values_quantile_0_167` | mm | Glaciers values for the quantile 0.167  
`glaciers_values_quantile_0_17` | mm | Glaciers values for the quantile 0.17  
`glaciers_values_quantile_0_18` | mm | Glaciers values for the quantile 0.18  
`glaciers_values_quantile_0_19` | mm | Glaciers values for the quantile 0.19  
`glaciers_values_quantile_0_2` | mm | Glaciers values for the quantile 0.2  
`glaciers_values_quantile_0_21` | mm | Glaciers values for the quantile 0.21  
`glaciers_values_quantile_0_22` | mm | Glaciers values for the quantile 0.22  
`glaciers_values_quantile_0_23` | mm | Glaciers values for the quantile 0.23  
`glaciers_values_quantile_0_24` | mm | Glaciers values for the quantile 0.24  
`glaciers_values_quantile_0_25` | mm | Glaciers values for the quantile 0.25  
`glaciers_values_quantile_0_26` | mm | Glaciers values for the quantile 0.26  
`glaciers_values_quantile_0_27` | mm | Glaciers values for the quantile 0.27  
`glaciers_values_quantile_0_28` | mm | Glaciers values for the quantile 0.28  
`glaciers_values_quantile_0_29` | mm | Glaciers values for the quantile 0.29  
`glaciers_values_quantile_0_3` | mm | Glaciers values for the quantile 0.3  
`glaciers_values_quantile_0_31` | mm | Glaciers values for the quantile 0.31  
`glaciers_values_quantile_0_32` | mm | Glaciers values for the quantile 0.32  
`glaciers_values_quantile_0_33` | mm | Glaciers values for the quantile 0.33  
`glaciers_values_quantile_0_34` | mm | Glaciers values for the quantile 0.34  
`glaciers_values_quantile_0_35` | mm | Glaciers values for the quantile 0.35  
`glaciers_values_quantile_0_36` | mm | Glaciers values for the quantile 0.36  
`glaciers_values_quantile_0_37` | mm | Glaciers values for the quantile 0.37  
`glaciers_values_quantile_0_38` | mm | Glaciers values for the quantile 0.38  
`glaciers_values_quantile_0_39` | mm | Glaciers values for the quantile 0.39  
`glaciers_values_quantile_0_4` | mm | Glaciers values for the quantile 0.4  
`glaciers_values_quantile_0_41` | mm | Glaciers values for the quantile 0.41  
`glaciers_values_quantile_0_42` | mm | Glaciers values for the quantile 0.42  
`glaciers_values_quantile_0_43` | mm | Glaciers values for the quantile 0.43  
`glaciers_values_quantile_0_44` | mm | Glaciers values for the quantile 0.44  
`glaciers_values_quantile_0_45` | mm | Glaciers values for the quantile 0.45  
`glaciers_values_quantile_0_46` | mm | Glaciers values for the quantile 0.46  
`glaciers_values_quantile_0_47` | mm | Glaciers values for the quantile 0.47  
`glaciers_values_quantile_0_48` | mm | Glaciers values for the quantile 0.48  
`glaciers_values_quantile_0_49` | mm | Glaciers values for the quantile 0.49  
`glaciers_values_quantile_0_5` | mm | Glaciers values for the quantile 0.5  
`glaciers_values_quantile_0_51` | mm | Glaciers values for the quantile 0.51  
`glaciers_values_quantile_0_52` | mm | Glaciers values for the quantile 0.52  
`glaciers_values_quantile_0_53` | mm | Glaciers values for the quantile 0.53  
`glaciers_values_quantile_0_54` | mm | Glaciers values for the quantile 0.54  
`glaciers_values_quantile_0_55` | mm | Glaciers values for the quantile 0.55  
`glaciers_values_quantile_0_56` | mm | Glaciers values for the quantile 0.56  
`glaciers_values_quantile_0_57` | mm | Glaciers values for the quantile 0.57  
`glaciers_values_quantile_0_58` | mm | Glaciers values for the quantile 0.58  
`glaciers_values_quantile_0_59` | mm | Glaciers values for the quantile 0.59  
`glaciers_values_quantile_0_6` | mm | Glaciers values for the quantile 0.6  
`glaciers_values_quantile_0_61` | mm | Glaciers values for the quantile 0.61  
`glaciers_values_quantile_0_62` | mm | Glaciers values for the quantile 0.62  
`glaciers_values_quantile_0_63` | mm | Glaciers values for the quantile 0.63  
`glaciers_values_quantile_0_64` | mm | Glaciers values for the quantile 0.64  
`glaciers_values_quantile_0_65` | mm | Glaciers values for the quantile 0.65  
`glaciers_values_quantile_0_66` | mm | Glaciers values for the quantile 0.66  
`glaciers_values_quantile_0_67` | mm | Glaciers values for the quantile 0.67  
`glaciers_values_quantile_0_68` | mm | Glaciers values for the quantile 0.68  
`glaciers_values_quantile_0_69` | mm | Glaciers values for the quantile 0.69  
`glaciers_values_quantile_0_7` | mm | Glaciers values for the quantile 0.7  
`glaciers_values_quantile_0_71` | mm | Glaciers values for the quantile 0.71  
`glaciers_values_quantile_0_72` | mm | Glaciers values for the quantile 0.72  
`glaciers_values_quantile_0_73` | mm | Glaciers values for the quantile 0.73  
`glaciers_values_quantile_0_74` | mm | Glaciers values for the quantile 0.74  
`glaciers_values_quantile_0_75` | mm | Glaciers values for the quantile 0.75  
`glaciers_values_quantile_0_76` | mm | Glaciers values for the quantile 0.76  
`glaciers_values_quantile_0_77` | mm | Glaciers values for the quantile 0.77  
`glaciers_values_quantile_0_78` | mm | Glaciers values for the quantile 0.78  
`glaciers_values_quantile_0_79` | mm | Glaciers values for the quantile 0.79  
`glaciers_values_quantile_0_8` | mm | Glaciers values for the quantile 0.8  
`glaciers_values_quantile_0_81` | mm | Glaciers values for the quantile 0.81  
`glaciers_values_quantile_0_82` | mm | Glaciers values for the quantile 0.82  
`glaciers_values_quantile_0_83` | mm | Glaciers values for the quantile 0.83  
`glaciers_values_quantile_0_833` | mm | Glaciers values for the quantile 0.833  
`glaciers_values_quantile_0_84` | mm | Glaciers values for the quantile 0.84  
`glaciers_values_quantile_0_85` | mm | Glaciers values for the quantile 0.85  
`glaciers_values_quantile_0_86` | mm | Glaciers values for the quantile 0.86  
`glaciers_values_quantile_0_87` | mm | Glaciers values for the quantile 0.87  
`glaciers_values_quantile_0_88` | mm | Glaciers values for the quantile 0.88  
`glaciers_values_quantile_0_89` | mm | Glaciers values for the quantile 0.89  
`glaciers_values_quantile_0_9` | mm | Glaciers values for the quantile 0.9  
`glaciers_values_quantile_0_91` | mm | Glaciers values for the quantile 0.91  
`glaciers_values_quantile_0_92` | mm | Glaciers values for the quantile 0.92  
`glaciers_values_quantile_0_93` | mm | Glaciers values for the quantile 0.93  
`glaciers_values_quantile_0_94` | mm | Glaciers values for the quantile 0.94  
`glaciers_values_quantile_0_95` | mm | Glaciers values for the quantile 0.95  
`glaciers_values_quantile_0_96` | mm | Glaciers values for the quantile 0.96  
`glaciers_values_quantile_0_97` | mm | Glaciers values for the quantile 0.97  
`glaciers_values_quantile_0_98` | mm | Glaciers values for the quantile 0.98  
`glaciers_values_quantile_0_99` | mm | Glaciers values for the quantile 0.99  
`glaciers_values_quantile_0_995` | mm | Glaciers values for the quantile 0.995  
`glaciers_values_quantile_0_999` | mm | Glaciers values for the quantile 0.999  
`glaciers_values_quantile_1` | mm | Glaciers values for the quantile 1  
`landwaterstorage_rates_quantile_0` | mm/y | Land water storage rates for the quantile 0  
`landwaterstorage_rates_quantile_0_001` | mm/y | Land water storage rates for the quantile 0.001  
`landwaterstorage_rates_quantile_0_005` | mm/y | Land water storage rates for the quantile 0.005  
`landwaterstorage_rates_quantile_0_01` | mm/y | Land water storage rates for the quantile 0.01  
`landwaterstorage_rates_quantile_0_02` | mm/y | Land water storage rates for the quantile 0.02  
`landwaterstorage_rates_quantile_0_03` | mm/y | Land water storage rates for the quantile 0.03  
`landwaterstorage_rates_quantile_0_04` | mm/y | Land water storage rates for the quantile 0.04  
`landwaterstorage_rates_quantile_0_05` | mm/y | Land water storage rates for the quantile 0.05  
`landwaterstorage_rates_quantile_0_06` | mm/y | Land water storage rates for the quantile 0.06  
`landwaterstorage_rates_quantile_0_07` | mm/y | Land water storage rates for the quantile 0.07  
`landwaterstorage_rates_quantile_0_08` | mm/y | Land water storage rates for the quantile 0.08  
`landwaterstorage_rates_quantile_0_09` | mm/y | Land water storage rates for the quantile 0.09  
`landwaterstorage_rates_quantile_0_1` | mm/y | Land water storage rates for the quantile 0.1  
`landwaterstorage_rates_quantile_0_11` | mm/y | Land water storage rates for the quantile 0.11  
`landwaterstorage_rates_quantile_0_12` | mm/y | Land water storage rates for the quantile 0.12  
`landwaterstorage_rates_quantile_0_13` | mm/y | Land water storage rates for the quantile 0.13  
`landwaterstorage_rates_quantile_0_14` | mm/y | Land water storage rates for the quantile 0.14  
`landwaterstorage_rates_quantile_0_15` | mm/y | Land water storage rates for the quantile 0.15  
`landwaterstorage_rates_quantile_0_16` | mm/y | Land water storage rates for the quantile 0.16  
`landwaterstorage_rates_quantile_0_167` | mm/y | Land water storage rates for the quantile 0.167  
`landwaterstorage_rates_quantile_0_17` | mm/y | Land water storage rates for the quantile 0.17  
`landwaterstorage_rates_quantile_0_18` | mm/y | Land water storage rates for the quantile 0.18  
`landwaterstorage_rates_quantile_0_19` | mm/y | Land water storage rates for the quantile 0.19  
`landwaterstorage_rates_quantile_0_2` | mm/y | Land water storage rates for the quantile 0.2  
`landwaterstorage_rates_quantile_0_21` | mm/y | Land water storage rates for the quantile 0.21  
`landwaterstorage_rates_quantile_0_22` | mm/y | Land water storage rates for the quantile 0.22  
`landwaterstorage_rates_quantile_0_23` | mm/y | Land water storage rates for the quantile 0.23  
`landwaterstorage_rates_quantile_0_24` | mm/y | Land water storage rates for the quantile 0.24  
`landwaterstorage_rates_quantile_0_25` | mm/y | Land water storage rates for the quantile 0.25  
`landwaterstorage_rates_quantile_0_26` | mm/y | Land water storage rates for the quantile 0.26  
`landwaterstorage_rates_quantile_0_27` | mm/y | Land water storage rates for the quantile 0.27  
`landwaterstorage_rates_quantile_0_28` | mm/y | Land water storage rates for the quantile 0.28  
`landwaterstorage_rates_quantile_0_29` | mm/y | Land water storage rates for the quantile 0.29  
`landwaterstorage_rates_quantile_0_3` | mm/y | Land water storage rates for the quantile 0.3  
`landwaterstorage_rates_quantile_0_31` | mm/y | Land water storage rates for the quantile 0.31  
`landwaterstorage_rates_quantile_0_32` | mm/y | Land water storage rates for the quantile 0.32  
`landwaterstorage_rates_quantile_0_33` | mm/y | Land water storage rates for the quantile 0.33  
`landwaterstorage_rates_quantile_0_34` | mm/y | Land water storage rates for the quantile 0.34  
`landwaterstorage_rates_quantile_0_35` | mm/y | Land water storage rates for the quantile 0.35  
`landwaterstorage_rates_quantile_0_36` | mm/y | Land water storage rates for the quantile 0.36  
`landwaterstorage_rates_quantile_0_37` | mm/y | Land water storage rates for the quantile 0.37  
`landwaterstorage_rates_quantile_0_38` | mm/y | Land water storage rates for the quantile 0.38  
`landwaterstorage_rates_quantile_0_39` | mm/y | Land water storage rates for the quantile 0.39  
`landwaterstorage_rates_quantile_0_4` | mm/y | Land water storage rates for the quantile 0.4  
`landwaterstorage_rates_quantile_0_41` | mm/y | Land water storage rates for the quantile 0.41  
`landwaterstorage_rates_quantile_0_42` | mm/y | Land water storage rates for the quantile 0.42  
`landwaterstorage_rates_quantile_0_43` | mm/y | Land water storage rates for the quantile 0.43  
`landwaterstorage_rates_quantile_0_44` | mm/y | Land water storage rates for the quantile 0.44  
`landwaterstorage_rates_quantile_0_45` | mm/y | Land water storage rates for the quantile 0.45  
`landwaterstorage_rates_quantile_0_46` | mm/y | Land water storage rates for the quantile 0.46  
`landwaterstorage_rates_quantile_0_47` | mm/y | Land water storage rates for the quantile 0.47  
`landwaterstorage_rates_quantile_0_48` | mm/y | Land water storage rates for the quantile 0.48  
`landwaterstorage_rates_quantile_0_49` | mm/y | Land water storage rates for the quantile 0.49  
`landwaterstorage_rates_quantile_0_5` | mm/y | Land water storage rates for the quantile 0.5  
`landwaterstorage_rates_quantile_0_51` | mm/y | Land water storage rates for the quantile 0.51  
`landwaterstorage_rates_quantile_0_52` | mm/y | Land water storage rates for the quantile 0.52  
`landwaterstorage_rates_quantile_0_53` | mm/y | Land water storage rates for the quantile 0.53  
`landwaterstorage_rates_quantile_0_54` | mm/y | Land water storage rates for the quantile 0.54  
`landwaterstorage_rates_quantile_0_55` | mm/y | Land water storage rates for the quantile 0.55  
`landwaterstorage_rates_quantile_0_56` | mm/y | Land water storage rates for the quantile 0.56  
`landwaterstorage_rates_quantile_0_57` | mm/y | Land water storage rates for the quantile 0.57  
`landwaterstorage_rates_quantile_0_58` | mm/y | Land water storage rates for the quantile 0.58  
`landwaterstorage_rates_quantile_0_59` | mm/y | Land water storage rates for the quantile 0.59  
`landwaterstorage_rates_quantile_0_6` | mm/y | Land water storage rates for the quantile 0.6  
`landwaterstorage_rates_quantile_0_61` | mm/y | Land water storage rates for the quantile 0.61  
`landwaterstorage_rates_quantile_0_62` | mm/y | Land water storage rates for the quantile 0.62  
`landwaterstorage_rates_quantile_0_63` | mm/y | Land water storage rates for the quantile 0.63  
`landwaterstorage_rates_quantile_0_64` | mm/y | Land water storage rates for the quantile 0.64  
`landwaterstorage_rates_quantile_0_65` | mm/y | Land water storage rates for the quantile 0.65  
`landwaterstorage_rates_quantile_0_66` | mm/y | Land water storage rates for the quantile 0.66  
`landwaterstorage_rates_quantile_0_67` | mm/y | Land water storage rates for the quantile 0.67  
`landwaterstorage_rates_quantile_0_68` | mm/y | Land water storage rates for the quantile 0.68  
`landwaterstorage_rates_quantile_0_69` | mm/y | Land water storage rates for the quantile 0.69  
`landwaterstorage_rates_quantile_0_7` | mm/y | Land water storage rates for the quantile 0.7  
`landwaterstorage_rates_quantile_0_71` | mm/y | Land water storage rates for the quantile 0.71  
`landwaterstorage_rates_quantile_0_72` | mm/y | Land water storage rates for the quantile 0.72  
`landwaterstorage_rates_quantile_0_73` | mm/y | Land water storage rates for the quantile 0.73  
`landwaterstorage_rates_quantile_0_74` | mm/y | Land water storage rates for the quantile 0.74  
`landwaterstorage_rates_quantile_0_75` | mm/y | Land water storage rates for the quantile 0.75  
`landwaterstorage_rates_quantile_0_76` | mm/y | Land water storage rates for the quantile 0.76  
`landwaterstorage_rates_quantile_0_77` | mm/y | Land water storage rates for the quantile 0.77  
`landwaterstorage_rates_quantile_0_78` | mm/y | Land water storage rates for the quantile 0.78  
`landwaterstorage_rates_quantile_0_79` | mm/y | Land water storage rates for the quantile 0.79  
`landwaterstorage_rates_quantile_0_8` | mm/y | Land water storage rates for the quantile 0.8  
`landwaterstorage_rates_quantile_0_81` | mm/y | Land water storage rates for the quantile 0.81  
`landwaterstorage_rates_quantile_0_82` | mm/y | Land water storage rates for the quantile 0.82  
`landwaterstorage_rates_quantile_0_83` | mm/y | Land water storage rates for the quantile 0.83  
`landwaterstorage_rates_quantile_0_833` | mm/y | Land water storage rates for the quantile 0.833  
`landwaterstorage_rates_quantile_0_84` | mm/y | Land water storage rates for the quantile 0.84  
`landwaterstorage_rates_quantile_0_85` | mm/y | Land water storage rates for the quantile 0.85  
`landwaterstorage_rates_quantile_0_86` | mm/y | Land water storage rates for the quantile 0.86  
`landwaterstorage_rates_quantile_0_87` | mm/y | Land water storage rates for the quantile 0.87  
`landwaterstorage_rates_quantile_0_88` | mm/y | Land water storage rates for the quantile 0.88  
`landwaterstorage_rates_quantile_0_89` | mm/y | Land water storage rates for the quantile 0.89  
`landwaterstorage_rates_quantile_0_9` | mm/y | Land water storage rates for the quantile 0.9  
`landwaterstorage_rates_quantile_0_91` | mm/y | Land water storage rates for the quantile 0.91  
`landwaterstorage_rates_quantile_0_92` | mm/y | Land water storage rates for the quantile 0.92  
`landwaterstorage_rates_quantile_0_93` | mm/y | Land water storage rates for the quantile 0.93  
`landwaterstorage_rates_quantile_0_94` | mm/y | Land water storage rates for the quantile 0.94  
`landwaterstorage_rates_quantile_0_95` | mm/y | Land water storage rates for the quantile 0.95  
`landwaterstorage_rates_quantile_0_96` | mm/y | Land water storage rates for the quantile 0.96  
`landwaterstorage_rates_quantile_0_97` | mm/y | Land water storage rates for the quantile 0.97  
`landwaterstorage_rates_quantile_0_98` | mm/y | Land water storage rates for the quantile 0.98  
`landwaterstorage_rates_quantile_0_99` | mm/y | Land water storage rates for the quantile 0.99  
`landwaterstorage_rates_quantile_0_995` | mm/y | Land water storage rates for the quantile 0.995  
`landwaterstorage_rates_quantile_0_999` | mm/y | Land water storage rates for the quantile 0.999  
`landwaterstorage_rates_quantile_1` | mm/y | Land water storage rates for the quantile 1  
`landwaterstorage_values_quantile_0` | mm | Land water storage values for the quantile 0  
`landwaterstorage_values_quantile_0_001` | mm | Land water storage values for the quantile 0.001  
`landwaterstorage_values_quantile_0_005` | mm | Land water storage values for the quantile 0.005  
`landwaterstorage_values_quantile_0_01` | mm | Land water storage values for the quantile 0.01  
`landwaterstorage_values_quantile_0_02` | mm | Land water storage values for the quantile 0.02  
`landwaterstorage_values_quantile_0_03` | mm | Land water storage values for the quantile 0.03  
`landwaterstorage_values_quantile_0_04` | mm | Land water storage values for the quantile 0.04  
`landwaterstorage_values_quantile_0_05` | mm | Land water storage values for the quantile 0.05  
`landwaterstorage_values_quantile_0_06` | mm | Land water storage values for the quantile 0.06  
`landwaterstorage_values_quantile_0_07` | mm | Land water storage values for the quantile 0.07  
`landwaterstorage_values_quantile_0_08` | mm | Land water storage values for the quantile 0.08  
`landwaterstorage_values_quantile_0_09` | mm | Land water storage values for the quantile 0.09  
`landwaterstorage_values_quantile_0_1` | mm | Land water storage values for the quantile 0.1  
`landwaterstorage_values_quantile_0_11` | mm | Land water storage values for the quantile 0.11  
`landwaterstorage_values_quantile_0_12` | mm | Land water storage values for the quantile 0.12  
`landwaterstorage_values_quantile_0_13` | mm | Land water storage values for the quantile 0.13  
`landwaterstorage_values_quantile_0_14` | mm | Land water storage values for the quantile 0.14  
`landwaterstorage_values_quantile_0_15` | mm | Land water storage values for the quantile 0.15  
`landwaterstorage_values_quantile_0_16` | mm | Land water storage values for the quantile 0.16  
`landwaterstorage_values_quantile_0_167` | mm | Land water storage values for the quantile 0.167  
`landwaterstorage_values_quantile_0_17` | mm | Land water storage values for the quantile 0.17  
`landwaterstorage_values_quantile_0_18` | mm | Land water storage values for the quantile 0.18  
`landwaterstorage_values_quantile_0_19` | mm | Land water storage values for the quantile 0.19  
`landwaterstorage_values_quantile_0_2` | mm | Land water storage values for the quantile 0.2  
`landwaterstorage_values_quantile_0_21` | mm | Land water storage values for the quantile 0.21  
`landwaterstorage_values_quantile_0_22` | mm | Land water storage values for the quantile 0.22  
`landwaterstorage_values_quantile_0_23` | mm | Land water storage values for the quantile 0.23  
`landwaterstorage_values_quantile_0_24` | mm | Land water storage values for the quantile 0.24  
`landwaterstorage_values_quantile_0_25` | mm | Land water storage values for the quantile 0.25  
`landwaterstorage_values_quantile_0_26` | mm | Land water storage values for the quantile 0.26  
`landwaterstorage_values_quantile_0_27` | mm | Land water storage values for the quantile 0.27  
`landwaterstorage_values_quantile_0_28` | mm | Land water storage values for the quantile 0.28  
`landwaterstorage_values_quantile_0_29` | mm | Land water storage values for the quantile 0.29  
`landwaterstorage_values_quantile_0_3` | mm | Land water storage values for the quantile 0.3  
`landwaterstorage_values_quantile_0_31` | mm | Land water storage values for the quantile 0.31  
`landwaterstorage_values_quantile_0_32` | mm | Land water storage values for the quantile 0.32  
`landwaterstorage_values_quantile_0_33` | mm | Land water storage values for the quantile 0.33  
`landwaterstorage_values_quantile_0_34` | mm | Land water storage values for the quantile 0.34  
`landwaterstorage_values_quantile_0_35` | mm | Land water storage values for the quantile 0.35  
`landwaterstorage_values_quantile_0_36` | mm | Land water storage values for the quantile 0.36  
`landwaterstorage_values_quantile_0_37` | mm | Land water storage values for the quantile 0.37  
`landwaterstorage_values_quantile_0_38` | mm | Land water storage values for the quantile 0.38  
`landwaterstorage_values_quantile_0_39` | mm | Land water storage values for the quantile 0.39  
`landwaterstorage_values_quantile_0_4` | mm | Land water storage values for the quantile 0.4  
`landwaterstorage_values_quantile_0_41` | mm | Land water storage values for the quantile 0.41  
`landwaterstorage_values_quantile_0_42` | mm | Land water storage values for the quantile 0.42  
`landwaterstorage_values_quantile_0_43` | mm | Land water storage values for the quantile 0.43  
`landwaterstorage_values_quantile_0_44` | mm | Land water storage values for the quantile 0.44  
`landwaterstorage_values_quantile_0_45` | mm | Land water storage values for the quantile 0.45  
`landwaterstorage_values_quantile_0_46` | mm | Land water storage values for the quantile 0.46  
`landwaterstorage_values_quantile_0_47` | mm | Land water storage values for the quantile 0.47  
`landwaterstorage_values_quantile_0_48` | mm | Land water storage values for the quantile 0.48  
`landwaterstorage_values_quantile_0_49` | mm | Land water storage values for the quantile 0.49  
`landwaterstorage_values_quantile_0_5` | mm | Land water storage values for the quantile 0.5  
`landwaterstorage_values_quantile_0_51` | mm | Land water storage values for the quantile 0.51  
`landwaterstorage_values_quantile_0_52` | mm | Land water storage values for the quantile 0.52  
`landwaterstorage_values_quantile_0_53` | mm | Land water storage values for the quantile 0.53  
`landwaterstorage_values_quantile_0_54` | mm | Land water storage values for the quantile 0.54  
`landwaterstorage_values_quantile_0_55` | mm | Land water storage values for the quantile 0.55  
`landwaterstorage_values_quantile_0_56` | mm | Land water storage values for the quantile 0.56  
`landwaterstorage_values_quantile_0_57` | mm | Land water storage values for the quantile 0.57  
`landwaterstorage_values_quantile_0_58` | mm | Land water storage values for the quantile 0.58  
`landwaterstorage_values_quantile_0_59` | mm | Land water storage values for the quantile 0.59  
`landwaterstorage_values_quantile_0_6` | mm | Land water storage values for the quantile 0.6  
`landwaterstorage_values_quantile_0_61` | mm | Land water storage values for the quantile 0.61  
`landwaterstorage_values_quantile_0_62` | mm | Land water storage values for the quantile 0.62  
`landwaterstorage_values_quantile_0_63` | mm | Land water storage values for the quantile 0.63  
`landwaterstorage_values_quantile_0_64` | mm | Land water storage values for the quantile 0.64  
`landwaterstorage_values_quantile_0_65` | mm | Land water storage values for the quantile 0.65  
`landwaterstorage_values_quantile_0_66` | mm | Land water storage values for the quantile 0.66  
`landwaterstorage_values_quantile_0_67` | mm | Land water storage values for the quantile 0.67  
`landwaterstorage_values_quantile_0_68` | mm | Land water storage values for the quantile 0.68  
`landwaterstorage_values_quantile_0_69` | mm | Land water storage values for the quantile 0.69  
`landwaterstorage_values_quantile_0_7` | mm | Land water storage values for the quantile 0.7  
`landwaterstorage_values_quantile_0_71` | mm | Land water storage values for the quantile 0.71  
`landwaterstorage_values_quantile_0_72` | mm | Land water storage values for the quantile 0.72  
`landwaterstorage_values_quantile_0_73` | mm | Land water storage values for the quantile 0.73  
`landwaterstorage_values_quantile_0_74` | mm | Land water storage values for the quantile 0.74  
`landwaterstorage_values_quantile_0_75` | mm | Land water storage values for the quantile 0.75  
`landwaterstorage_values_quantile_0_76` | mm | Land water storage values for the quantile 0.76  
`landwaterstorage_values_quantile_0_77` | mm | Land water storage values for the quantile 0.77  
`landwaterstorage_values_quantile_0_78` | mm | Land water storage values for the quantile 0.78  
`landwaterstorage_values_quantile_0_79` | mm | Land water storage values for the quantile 0.79  
`landwaterstorage_values_quantile_0_8` | mm | Land water storage values for the quantile 0.8  
`landwaterstorage_values_quantile_0_81` | mm | Land water storage values for the quantile 0.81  
`landwaterstorage_values_quantile_0_82` | mm | Land water storage values for the quantile 0.82  
`landwaterstorage_values_quantile_0_83` | mm | Land water storage values for the quantile 0.83  
`landwaterstorage_values_quantile_0_833` | mm | Land water storage values for the quantile 0.833  
`landwaterstorage_values_quantile_0_84` | mm | Land water storage values for the quantile 0.84  
`landwaterstorage_values_quantile_0_85` | mm | Land water storage values for the quantile 0.85  
`landwaterstorage_values_quantile_0_86` | mm | Land water storage values for the quantile 0.86  
`landwaterstorage_values_quantile_0_87` | mm | Land water storage values for the quantile 0.87  
`landwaterstorage_values_quantile_0_88` | mm | Land water storage values for the quantile 0.88  
`landwaterstorage_values_quantile_0_89` | mm | Land water storage values for the quantile 0.89  
`landwaterstorage_values_quantile_0_9` | mm | Land water storage values for the quantile 0.9  
`landwaterstorage_values_quantile_0_91` | mm | Land water storage values for the quantile 0.91  
`landwaterstorage_values_quantile_0_92` | mm | Land water storage values for the quantile 0.92  
`landwaterstorage_values_quantile_0_93` | mm | Land water storage values for the quantile 0.93  
`landwaterstorage_values_quantile_0_94` | mm | Land water storage values for the quantile 0.94  
`landwaterstorage_values_quantile_0_95` | mm | Land water storage values for the quantile 0.95  
`landwaterstorage_values_quantile_0_96` | mm | Land water storage values for the quantile 0.96  
`landwaterstorage_values_quantile_0_97` | mm | Land water storage values for the quantile 0.97  
`landwaterstorage_values_quantile_0_98` | mm | Land water storage values for the quantile 0.98  
`landwaterstorage_values_quantile_0_99` | mm | Land water storage values for the quantile 0.99  
`landwaterstorage_values_quantile_0_995` | mm | Land water storage values for the quantile 0.995  
`landwaterstorage_values_quantile_0_999` | mm | Land water storage values for the quantile 0.999  
`landwaterstorage_values_quantile_1` | mm | Land water storage values for the quantile 1  
`oceandynamics_rates_quantile_0` | mm/y | Ocean dynamics rates for the quantile 0  
`oceandynamics_rates_quantile_0_001` | mm/y | Ocean dynamics rates for the quantile 0.001  
`oceandynamics_rates_quantile_0_005` | mm/y | Ocean dynamics rates for the quantile 0.005  
`oceandynamics_rates_quantile_0_01` | mm/y | Ocean dynamics rates for the quantile 0.01  
`oceandynamics_rates_quantile_0_02` | mm/y | Ocean dynamics rates for the quantile 0.02  
`oceandynamics_rates_quantile_0_03` | mm/y | Ocean dynamics rates for the quantile 0.03  
`oceandynamics_rates_quantile_0_04` | mm/y | Ocean dynamics rates for the quantile 0.04  
`oceandynamics_rates_quantile_0_05` | mm/y | Ocean dynamics rates for the quantile 0.05  
`oceandynamics_rates_quantile_0_06` | mm/y | Ocean dynamics rates for the quantile 0.06  
`oceandynamics_rates_quantile_0_07` | mm/y | Ocean dynamics rates for the quantile 0.07  
`oceandynamics_rates_quantile_0_08` | mm/y | Ocean dynamics rates for the quantile 0.08  
`oceandynamics_rates_quantile_0_09` | mm/y | Ocean dynamics rates for the quantile 0.09  
`oceandynamics_rates_quantile_0_1` | mm/y | Ocean dynamics rates for the quantile 0.1  
`oceandynamics_rates_quantile_0_11` | mm/y | Ocean dynamics rates for the quantile 0.11  
`oceandynamics_rates_quantile_0_12` | mm/y | Ocean dynamics rates for the quantile 0.12  
`oceandynamics_rates_quantile_0_13` | mm/y | Ocean dynamics rates for the quantile 0.13  
`oceandynamics_rates_quantile_0_14` | mm/y | Ocean dynamics rates for the quantile 0.14  
`oceandynamics_rates_quantile_0_15` | mm/y | Ocean dynamics rates for the quantile 0.15  
`oceandynamics_rates_quantile_0_16` | mm/y | Ocean dynamics rates for the quantile 0.16  
`oceandynamics_rates_quantile_0_167` | mm/y | Ocean dynamics rates for the quantile 0.167  
`oceandynamics_rates_quantile_0_17` | mm/y | Ocean dynamics rates for the quantile 0.17  
`oceandynamics_rates_quantile_0_18` | mm/y | Ocean dynamics rates for the quantile 0.18  
`oceandynamics_rates_quantile_0_19` | mm/y | Ocean dynamics rates for the quantile 0.19  
`oceandynamics_rates_quantile_0_2` | mm/y | Ocean dynamics rates for the quantile 0.2  
`oceandynamics_rates_quantile_0_21` | mm/y | Ocean dynamics rates for the quantile 0.21  
`oceandynamics_rates_quantile_0_22` | mm/y | Ocean dynamics rates for the quantile 0.22  
`oceandynamics_rates_quantile_0_23` | mm/y | Ocean dynamics rates for the quantile 0.23  
`oceandynamics_rates_quantile_0_24` | mm/y | Ocean dynamics rates for the quantile 0.24  
`oceandynamics_rates_quantile_0_25` | mm/y | Ocean dynamics rates for the quantile 0.25  
`oceandynamics_rates_quantile_0_26` | mm/y | Ocean dynamics rates for the quantile 0.26  
`oceandynamics_rates_quantile_0_27` | mm/y | Ocean dynamics rates for the quantile 0.27  
`oceandynamics_rates_quantile_0_28` | mm/y | Ocean dynamics rates for the quantile 0.28  
`oceandynamics_rates_quantile_0_29` | mm/y | Ocean dynamics rates for the quantile 0.29  
`oceandynamics_rates_quantile_0_3` | mm/y | Ocean dynamics rates for the quantile 0.3  
`oceandynamics_rates_quantile_0_31` | mm/y | Ocean dynamics rates for the quantile 0.31  
`oceandynamics_rates_quantile_0_32` | mm/y | Ocean dynamics rates for the quantile 0.32  
`oceandynamics_rates_quantile_0_33` | mm/y | Ocean dynamics rates for the quantile 0.33  
`oceandynamics_rates_quantile_0_34` | mm/y | Ocean dynamics rates for the quantile 0.34  
`oceandynamics_rates_quantile_0_35` | mm/y | Ocean dynamics rates for the quantile 0.35  
`oceandynamics_rates_quantile_0_36` | mm/y | Ocean dynamics rates for the quantile 0.36  
`oceandynamics_rates_quantile_0_37` | mm/y | Ocean dynamics rates for the quantile 0.37  
`oceandynamics_rates_quantile_0_38` | mm/y | Ocean dynamics rates for the quantile 0.38  
`oceandynamics_rates_quantile_0_39` | mm/y | Ocean dynamics rates for the quantile 0.39  
`oceandynamics_rates_quantile_0_4` | mm/y | Ocean dynamics rates for the quantile 0.4  
`oceandynamics_rates_quantile_0_41` | mm/y | Ocean dynamics rates for the quantile 0.41  
`oceandynamics_rates_quantile_0_42` | mm/y | Ocean dynamics rates for the quantile 0.42  
`oceandynamics_rates_quantile_0_43` | mm/y | Ocean dynamics rates for the quantile 0.43  
`oceandynamics_rates_quantile_0_44` | mm/y | Ocean dynamics rates for the quantile 0.44  
`oceandynamics_rates_quantile_0_45` | mm/y | Ocean dynamics rates for the quantile 0.45  
`oceandynamics_rates_quantile_0_46` | mm/y | Ocean dynamics rates for the quantile 0.46  
`oceandynamics_rates_quantile_0_47` | mm/y | Ocean dynamics rates for the quantile 0.47  
`oceandynamics_rates_quantile_0_48` | mm/y | Ocean dynamics rates for the quantile 0.48  
`oceandynamics_rates_quantile_0_49` | mm/y | Ocean dynamics rates for the quantile 0.49  
`oceandynamics_rates_quantile_0_5` | mm/y | Ocean dynamics rates for the quantile 0.5  
`oceandynamics_rates_quantile_0_51` | mm/y | Ocean dynamics rates for the quantile 0.51  
`oceandynamics_rates_quantile_0_52` | mm/y | Ocean dynamics rates for the quantile 0.52  
`oceandynamics_rates_quantile_0_53` | mm/y | Ocean dynamics rates for the quantile 0.53  
`oceandynamics_rates_quantile_0_54` | mm/y | Ocean dynamics rates for the quantile 0.54  
`oceandynamics_rates_quantile_0_55` | mm/y | Ocean dynamics rates for the quantile 0.55  
`oceandynamics_rates_quantile_0_56` | mm/y | Ocean dynamics rates for the quantile 0.56  
`oceandynamics_rates_quantile_0_57` | mm/y | Ocean dynamics rates for the quantile 0.57  
`oceandynamics_rates_quantile_0_58` | mm/y | Ocean dynamics rates for the quantile 0.58  
`oceandynamics_rates_quantile_0_59` | mm/y | Ocean dynamics rates for the quantile 0.59  
`oceandynamics_rates_quantile_0_6` | mm/y | Ocean dynamics rates for the quantile 0.6  
`oceandynamics_rates_quantile_0_61` | mm/y | Ocean dynamics rates for the quantile 0.61  
`oceandynamics_rates_quantile_0_62` | mm/y | Ocean dynamics rates for the quantile 0.62  
`oceandynamics_rates_quantile_0_63` | mm/y | Ocean dynamics rates for the quantile 0.63  
`oceandynamics_rates_quantile_0_64` | mm/y | Ocean dynamics rates for the quantile 0.64  
`oceandynamics_rates_quantile_0_65` | mm/y | Ocean dynamics rates for the quantile 0.65  
`oceandynamics_rates_quantile_0_66` | mm/y | Ocean dynamics rates for the quantile 0.66  
`oceandynamics_rates_quantile_0_67` | mm/y | Ocean dynamics rates for the quantile 0.67  
`oceandynamics_rates_quantile_0_68` | mm/y | Ocean dynamics rates for the quantile 0.68  
`oceandynamics_rates_quantile_0_69` | mm/y | Ocean dynamics rates for the quantile 0.69  
`oceandynamics_rates_quantile_0_7` | mm/y | Ocean dynamics rates for the quantile 0.7  
`oceandynamics_rates_quantile_0_71` | mm/y | Ocean dynamics rates for the quantile 0.71  
`oceandynamics_rates_quantile_0_72` | mm/y | Ocean dynamics rates for the quantile 0.72  
`oceandynamics_rates_quantile_0_73` | mm/y | Ocean dynamics rates for the quantile 0.73  
`oceandynamics_rates_quantile_0_74` | mm/y | Ocean dynamics rates for the quantile 0.74  
`oceandynamics_rates_quantile_0_75` | mm/y | Ocean dynamics rates for the quantile 0.75  
`oceandynamics_rates_quantile_0_76` | mm/y | Ocean dynamics rates for the quantile 0.76  
`oceandynamics_rates_quantile_0_77` | mm/y | Ocean dynamics rates for the quantile 0.77  
`oceandynamics_rates_quantile_0_78` | mm/y | Ocean dynamics rates for the quantile 0.78  
`oceandynamics_rates_quantile_0_79` | mm/y | Ocean dynamics rates for the quantile 0.79  
`oceandynamics_rates_quantile_0_8` | mm/y | Ocean dynamics rates for the quantile 0.8  
`oceandynamics_rates_quantile_0_81` | mm/y | Ocean dynamics rates for the quantile 0.81  
`oceandynamics_rates_quantile_0_82` | mm/y | Ocean dynamics rates for the quantile 0.82  
`oceandynamics_rates_quantile_0_83` | mm/y | Ocean dynamics rates for the quantile 0.83  
`oceandynamics_rates_quantile_0_833` | mm/y | Ocean dynamics rates for the quantile 0.833  
`oceandynamics_rates_quantile_0_84` | mm/y | Ocean dynamics rates for the quantile 0.84  
`oceandynamics_rates_quantile_0_85` | mm/y | Ocean dynamics rates for the quantile 0.85  
`oceandynamics_rates_quantile_0_86` | mm/y | Ocean dynamics rates for the quantile 0.86  
`oceandynamics_rates_quantile_0_87` | mm/y | Ocean dynamics rates for the quantile 0.87  
`oceandynamics_rates_quantile_0_88` | mm/y | Ocean dynamics rates for the quantile 0.88  
`oceandynamics_rates_quantile_0_89` | mm/y | Ocean dynamics rates for the quantile 0.89  
`oceandynamics_rates_quantile_0_9` | mm/y | Ocean dynamics rates for the quantile 0.9  
`oceandynamics_rates_quantile_0_91` | mm/y | Ocean dynamics rates for the quantile 0.91  
`oceandynamics_rates_quantile_0_92` | mm/y | Ocean dynamics rates for the quantile 0.92  
`oceandynamics_rates_quantile_0_93` | mm/y | Ocean dynamics rates for the quantile 0.93  
`oceandynamics_rates_quantile_0_94` | mm/y | Ocean dynamics rates for the quantile 0.94  
`oceandynamics_rates_quantile_0_95` | mm/y | Ocean dynamics rates for the quantile 0.95  
`oceandynamics_rates_quantile_0_96` | mm/y | Ocean dynamics rates for the quantile 0.96  
`oceandynamics_rates_quantile_0_97` | mm/y | Ocean dynamics rates for the quantile 0.97  
`oceandynamics_rates_quantile_0_98` | mm/y | Ocean dynamics rates for the quantile 0.98  
`oceandynamics_rates_quantile_0_99` | mm/y | Ocean dynamics rates for the quantile 0.99  
`oceandynamics_rates_quantile_0_995` | mm/y | Ocean dynamics rates for the quantile 0.995  
`oceandynamics_rates_quantile_0_999` | mm/y | Ocean dynamics rates for the quantile 0.999  
`oceandynamics_rates_quantile_1` | mm/y | Ocean dynamics rates for the quantile 1  
`oceandynamics_values_quantile_0` | mm | Ocean dynamics values for the quantile 0  
`oceandynamics_values_quantile_0_001` | mm | Ocean dynamics values for the quantile 0.001  
`oceandynamics_values_quantile_0_005` | mm | Ocean dynamics values for the quantile 0.005  
`oceandynamics_values_quantile_0_01` | mm | Ocean dynamics values for the quantile 0.01  
`oceandynamics_values_quantile_0_02` | mm | Ocean dynamics values for the quantile 0.02  
`oceandynamics_values_quantile_0_03` | mm | Ocean dynamics values for the quantile 0.03  
`oceandynamics_values_quantile_0_04` | mm | Ocean dynamics values for the quantile 0.04  
`oceandynamics_values_quantile_0_05` | mm | Ocean dynamics values for the quantile 0.05  
`oceandynamics_values_quantile_0_06` | mm | Ocean dynamics values for the quantile 0.06  
`oceandynamics_values_quantile_0_07` | mm | Ocean dynamics values for the quantile 0.07  
`oceandynamics_values_quantile_0_08` | mm | Ocean dynamics values for the quantile 0.08  
`oceandynamics_values_quantile_0_09` | mm | Ocean dynamics values for the quantile 0.09  
`oceandynamics_values_quantile_0_1` | mm | Ocean dynamics values for the quantile 0.1  
`oceandynamics_values_quantile_0_11` | mm | Ocean dynamics values for the quantile 0.11  
`oceandynamics_values_quantile_0_12` | mm | Ocean dynamics values for the quantile 0.12  
`oceandynamics_values_quantile_0_13` | mm | Ocean dynamics values for the quantile 0.13  
`oceandynamics_values_quantile_0_14` | mm | Ocean dynamics values for the quantile 0.14  
`oceandynamics_values_quantile_0_15` | mm | Ocean dynamics values for the quantile 0.15  
`oceandynamics_values_quantile_0_16` | mm | Ocean dynamics values for the quantile 0.16  
`oceandynamics_values_quantile_0_167` | mm | Ocean dynamics values for the quantile 0.167  
`oceandynamics_values_quantile_0_17` | mm | Ocean dynamics values for the quantile 0.17  
`oceandynamics_values_quantile_0_18` | mm | Ocean dynamics values for the quantile 0.18  
`oceandynamics_values_quantile_0_19` | mm | Ocean dynamics values for the quantile 0.19  
`oceandynamics_values_quantile_0_2` | mm | Ocean dynamics values for the quantile 0.2  
`oceandynamics_values_quantile_0_21` | mm | Ocean dynamics values for the quantile 0.21  
`oceandynamics_values_quantile_0_22` | mm | Ocean dynamics values for the quantile 0.22  
`oceandynamics_values_quantile_0_23` | mm | Ocean dynamics values for the quantile 0.23  
`oceandynamics_values_quantile_0_24` | mm | Ocean dynamics values for the quantile 0.24  
`oceandynamics_values_quantile_0_25` | mm | Ocean dynamics values for the quantile 0.25  
`oceandynamics_values_quantile_0_26` | mm | Ocean dynamics values for the quantile 0.26  
`oceandynamics_values_quantile_0_27` | mm | Ocean dynamics values for the quantile 0.27  
`oceandynamics_values_quantile_0_28` | mm | Ocean dynamics values for the quantile 0.28  
`oceandynamics_values_quantile_0_29` | mm | Ocean dynamics values for the quantile 0.29  
`oceandynamics_values_quantile_0_3` | mm | Ocean dynamics values for the quantile 0.3  
`oceandynamics_values_quantile_0_31` | mm | Ocean dynamics values for the quantile 0.31  
`oceandynamics_values_quantile_0_32` | mm | Ocean dynamics values for the quantile 0.32  
`oceandynamics_values_quantile_0_33` | mm | Ocean dynamics values for the quantile 0.33  
`oceandynamics_values_quantile_0_34` | mm | Ocean dynamics values for the quantile 0.34  
`oceandynamics_values_quantile_0_35` | mm | Ocean dynamics values for the quantile 0.35  
`oceandynamics_values_quantile_0_36` | mm | Ocean dynamics values for the quantile 0.36  
`oceandynamics_values_quantile_0_37` | mm | Ocean dynamics values for the quantile 0.37  
`oceandynamics_values_quantile_0_38` | mm | Ocean dynamics values for the quantile 0.38  
`oceandynamics_values_quantile_0_39` | mm | Ocean dynamics values for the quantile 0.39  
`oceandynamics_values_quantile_0_4` | mm | Ocean dynamics values for the quantile 0.4  
`oceandynamics_values_quantile_0_41` | mm | Ocean dynamics values for the quantile 0.41  
`oceandynamics_values_quantile_0_42` | mm | Ocean dynamics values for the quantile 0.42  
`oceandynamics_values_quantile_0_43` | mm | Ocean dynamics values for the quantile 0.43  
`oceandynamics_values_quantile_0_44` | mm | Ocean dynamics values for the quantile 0.44  
`oceandynamics_values_quantile_0_45` | mm | Ocean dynamics values for the quantile 0.45  
`oceandynamics_values_quantile_0_46` | mm | Ocean dynamics values for the quantile 0.46  
`oceandynamics_values_quantile_0_47` | mm | Ocean dynamics values for the quantile 0.47  
`oceandynamics_values_quantile_0_48` | mm | Ocean dynamics values for the quantile 0.48  
`oceandynamics_values_quantile_0_49` | mm | Ocean dynamics values for the quantile 0.49  
`oceandynamics_values_quantile_0_5` | mm | Ocean dynamics values for the quantile 0.5  
`oceandynamics_values_quantile_0_51` | mm | Ocean dynamics values for the quantile 0.51  
`oceandynamics_values_quantile_0_52` | mm | Ocean dynamics values for the quantile 0.52  
`oceandynamics_values_quantile_0_53` | mm | Ocean dynamics values for the quantile 0.53  
`oceandynamics_values_quantile_0_54` | mm | Ocean dynamics values for the quantile 0.54  
`oceandynamics_values_quantile_0_55` | mm | Ocean dynamics values for the quantile 0.55  
`oceandynamics_values_quantile_0_56` | mm | Ocean dynamics values for the quantile 0.56  
`oceandynamics_values_quantile_0_57` | mm | Ocean dynamics values for the quantile 0.57  
`oceandynamics_values_quantile_0_58` | mm | Ocean dynamics values for the quantile 0.58  
`oceandynamics_values_quantile_0_59` | mm | Ocean dynamics values for the quantile 0.59  
`oceandynamics_values_quantile_0_6` | mm | Ocean dynamics values for the quantile 0.6  
`oceandynamics_values_quantile_0_61` | mm | Ocean dynamics values for the quantile 0.61  
`oceandynamics_values_quantile_0_62` | mm | Ocean dynamics values for the quantile 0.62  
`oceandynamics_values_quantile_0_63` | mm | Ocean dynamics values for the quantile 0.63  
`oceandynamics_values_quantile_0_64` | mm | Ocean dynamics values for the quantile 0.64  
`oceandynamics_values_quantile_0_65` | mm | Ocean dynamics values for the quantile 0.65  
`oceandynamics_values_quantile_0_66` | mm | Ocean dynamics values for the quantile 0.66  
`oceandynamics_values_quantile_0_67` | mm | Ocean dynamics values for the quantile 0.67  
`oceandynamics_values_quantile_0_68` | mm | Ocean dynamics values for the quantile 0.68  
`oceandynamics_values_quantile_0_69` | mm | Ocean dynamics values for the quantile 0.69  
`oceandynamics_values_quantile_0_7` | mm | Ocean dynamics values for the quantile 0.7  
`oceandynamics_values_quantile_0_71` | mm | Ocean dynamics values for the quantile 0.71  
`oceandynamics_values_quantile_0_72` | mm | Ocean dynamics values for the quantile 0.72  
`oceandynamics_values_quantile_0_73` | mm | Ocean dynamics values for the quantile 0.73  
`oceandynamics_values_quantile_0_74` | mm | Ocean dynamics values for the quantile 0.74  
`oceandynamics_values_quantile_0_75` | mm | Ocean dynamics values for the quantile 0.75  
`oceandynamics_values_quantile_0_76` | mm | Ocean dynamics values for the quantile 0.76  
`oceandynamics_values_quantile_0_77` | mm | Ocean dynamics values for the quantile 0.77  
`oceandynamics_values_quantile_0_78` | mm | Ocean dynamics values for the quantile 0.78  
`oceandynamics_values_quantile_0_79` | mm | Ocean dynamics values for the quantile 0.79  
`oceandynamics_values_quantile_0_8` | mm | Ocean dynamics values for the quantile 0.8  
`oceandynamics_values_quantile_0_81` | mm | Ocean dynamics values for the quantile 0.81  
`oceandynamics_values_quantile_0_82` | mm | Ocean dynamics values for the quantile 0.82  
`oceandynamics_values_quantile_0_83` | mm | Ocean dynamics values for the quantile 0.83  
`oceandynamics_values_quantile_0_833` | mm | Ocean dynamics values for the quantile 0.833  
`oceandynamics_values_quantile_0_84` | mm | Ocean dynamics values for the quantile 0.84  
`oceandynamics_values_quantile_0_85` | mm | Ocean dynamics values for the quantile 0.85  
`oceandynamics_values_quantile_0_86` | mm | Ocean dynamics values for the quantile 0.86  
`oceandynamics_values_quantile_0_87` | mm | Ocean dynamics values for the quantile 0.87  
`oceandynamics_values_quantile_0_88` | mm | Ocean dynamics values for the quantile 0.88  
`oceandynamics_values_quantile_0_89` | mm | Ocean dynamics values for the quantile 0.89  
`oceandynamics_values_quantile_0_9` | mm | Ocean dynamics values for the quantile 0.9  
`oceandynamics_values_quantile_0_91` | mm | Ocean dynamics values for the quantile 0.91  
`oceandynamics_values_quantile_0_92` | mm | Ocean dynamics values for the quantile 0.92  
`oceandynamics_values_quantile_0_93` | mm | Ocean dynamics values for the quantile 0.93  
`oceandynamics_values_quantile_0_94` | mm | Ocean dynamics values for the quantile 0.94  
`oceandynamics_values_quantile_0_95` | mm | Ocean dynamics values for the quantile 0.95  
`oceandynamics_values_quantile_0_96` | mm | Ocean dynamics values for the quantile 0.96  
`oceandynamics_values_quantile_0_97` | mm | Ocean dynamics values for the quantile 0.97  
`oceandynamics_values_quantile_0_98` | mm | Ocean dynamics values for the quantile 0.98  
`oceandynamics_values_quantile_0_99` | mm | Ocean dynamics values for the quantile 0.99  
`oceandynamics_values_quantile_0_995` | mm | Ocean dynamics values for the quantile 0.995  
`oceandynamics_values_quantile_0_999` | mm | Ocean dynamics values for the quantile 0.999  
`oceandynamics_values_quantile_1` | mm | Ocean dynamics values for the quantile 1  
`verticallandmotion_rates_quantile_0` | mm/y | Vertical land motion rates for the quantile 0  
`verticallandmotion_rates_quantile_0_001` | mm/y | Vertical land motion rates for the quantile 0.001  
`verticallandmotion_rates_quantile_0_005` | mm/y | Vertical land motion rates for the quantile 0.005  
`verticallandmotion_rates_quantile_0_01` | mm/y | Vertical land motion rates for the quantile 0.01  
`verticallandmotion_rates_quantile_0_02` | mm/y | Vertical land motion rates for the quantile 0.02  
`verticallandmotion_rates_quantile_0_03` | mm/y | Vertical land motion rates for the quantile 0.03  
`verticallandmotion_rates_quantile_0_04` | mm/y | Vertical land motion rates for the quantile 0.04  
`verticallandmotion_rates_quantile_0_05` | mm/y | Vertical land motion rates for the quantile 0.05  
`verticallandmotion_rates_quantile_0_06` | mm/y | Vertical land motion rates for the quantile 0.06  
`verticallandmotion_rates_quantile_0_07` | mm/y | Vertical land motion rates for the quantile 0.07  
`verticallandmotion_rates_quantile_0_08` | mm/y | Vertical land motion rates for the quantile 0.08  
`verticallandmotion_rates_quantile_0_09` | mm/y | Vertical land motion rates for the quantile 0.09  
`verticallandmotion_rates_quantile_0_1` | mm/y | Vertical land motion rates for the quantile 0.1  
`verticallandmotion_rates_quantile_0_11` | mm/y | Vertical land motion rates for the quantile 0.11  
`verticallandmotion_rates_quantile_0_12` | mm/y | Vertical land motion rates for the quantile 0.12  
`verticallandmotion_rates_quantile_0_13` | mm/y | Vertical land motion rates for the quantile 0.13  
`verticallandmotion_rates_quantile_0_14` | mm/y | Vertical land motion rates for the quantile 0.14  
`verticallandmotion_rates_quantile_0_15` | mm/y | Vertical land motion rates for the quantile 0.15  
`verticallandmotion_rates_quantile_0_16` | mm/y | Vertical land motion rates for the quantile 0.16  
`verticallandmotion_rates_quantile_0_167` | mm/y | Vertical land motion rates for the quantile 0.167  
`verticallandmotion_rates_quantile_0_17` | mm/y | Vertical land motion rates for the quantile 0.17  
`verticallandmotion_rates_quantile_0_18` | mm/y | Vertical land motion rates for the quantile 0.18  
`verticallandmotion_rates_quantile_0_19` | mm/y | Vertical land motion rates for the quantile 0.19  
`verticallandmotion_rates_quantile_0_2` | mm/y | Vertical land motion rates for the quantile 0.2  
`verticallandmotion_rates_quantile_0_21` | mm/y | Vertical land motion rates for the quantile 0.21  
`verticallandmotion_rates_quantile_0_22` | mm/y | Vertical land motion rates for the quantile 0.22  
`verticallandmotion_rates_quantile_0_23` | mm/y | Vertical land motion rates for the quantile 0.23  
`verticallandmotion_rates_quantile_0_24` | mm/y | Vertical land motion rates for the quantile 0.24  
`verticallandmotion_rates_quantile_0_25` | mm/y | Vertical land motion rates for the quantile 0.25  
`verticallandmotion_rates_quantile_0_26` | mm/y | Vertical land motion rates for the quantile 0.26  
`verticallandmotion_rates_quantile_0_27` | mm/y | Vertical land motion rates for the quantile 0.27  
`verticallandmotion_rates_quantile_0_28` | mm/y | Vertical land motion rates for the quantile 0.28  
`verticallandmotion_rates_quantile_0_29` | mm/y | Vertical land motion rates for the quantile 0.29  
`verticallandmotion_rates_quantile_0_3` | mm/y | Vertical land motion rates for the quantile 0.3  
`verticallandmotion_rates_quantile_0_31` | mm/y | Vertical land motion rates for the quantile 0.31  
`verticallandmotion_rates_quantile_0_32` | mm/y | Vertical land motion rates for the quantile 0.32  
`verticallandmotion_rates_quantile_0_33` | mm/y | Vertical land motion rates for the quantile 0.33  
`verticallandmotion_rates_quantile_0_34` | mm/y | Vertical land motion rates for the quantile 0.34  
`verticallandmotion_rates_quantile_0_35` | mm/y | Vertical land motion rates for the quantile 0.35  
`verticallandmotion_rates_quantile_0_36` | mm/y | Vertical land motion rates for the quantile 0.36  
`verticallandmotion_rates_quantile_0_37` | mm/y | Vertical land motion rates for the quantile 0.37  
`verticallandmotion_rates_quantile_0_38` | mm/y | Vertical land motion rates for the quantile 0.38  
`verticallandmotion_rates_quantile_0_39` | mm/y | Vertical land motion rates for the quantile 0.39  
`verticallandmotion_rates_quantile_0_4` | mm/y | Vertical land motion rates for the quantile 0.4  
`verticallandmotion_rates_quantile_0_41` | mm/y | Vertical land motion rates for the quantile 0.41  
`verticallandmotion_rates_quantile_0_42` | mm/y | Vertical land motion rates for the quantile 0.42  
`verticallandmotion_rates_quantile_0_43` | mm/y | Vertical land motion rates for the quantile 0.43  
`verticallandmotion_rates_quantile_0_44` | mm/y | Vertical land motion rates for the quantile 0.44  
`verticallandmotion_rates_quantile_0_45` | mm/y | Vertical land motion rates for the quantile 0.45  
`verticallandmotion_rates_quantile_0_46` | mm/y | Vertical land motion rates for the quantile 0.46  
`verticallandmotion_rates_quantile_0_47` | mm/y | Vertical land motion rates for the quantile 0.47  
`verticallandmotion_rates_quantile_0_48` | mm/y | Vertical land motion rates for the quantile 0.48  
`verticallandmotion_rates_quantile_0_49` | mm/y | Vertical land motion rates for the quantile 0.49  
`verticallandmotion_rates_quantile_0_5` | mm/y | Vertical land motion rates for the quantile 0.5  
`verticallandmotion_rates_quantile_0_51` | mm/y | Vertical land motion rates for the quantile 0.51  
`verticallandmotion_rates_quantile_0_52` | mm/y | Vertical land motion rates for the quantile 0.52  
`verticallandmotion_rates_quantile_0_53` | mm/y | Vertical land motion rates for the quantile 0.53  
`verticallandmotion_rates_quantile_0_54` | mm/y | Vertical land motion rates for the quantile 0.54  
`verticallandmotion_rates_quantile_0_55` | mm/y | Vertical land motion rates for the quantile 0.55  
`verticallandmotion_rates_quantile_0_56` | mm/y | Vertical land motion rates for the quantile 0.56  
`verticallandmotion_rates_quantile_0_57` | mm/y | Vertical land motion rates for the quantile 0.57  
`verticallandmotion_rates_quantile_0_58` | mm/y | Vertical land motion rates for the quantile 0.58  
`verticallandmotion_rates_quantile_0_59` | mm/y | Vertical land motion rates for the quantile 0.59  
`verticallandmotion_rates_quantile_0_6` | mm/y | Vertical land motion rates for the quantile 0.6  
`verticallandmotion_rates_quantile_0_61` | mm/y | Vertical land motion rates for the quantile 0.61  
`verticallandmotion_rates_quantile_0_62` | mm/y | Vertical land motion rates for the quantile 0.62  
`verticallandmotion_rates_quantile_0_63` | mm/y | Vertical land motion rates for the quantile 0.63  
`verticallandmotion_rates_quantile_0_64` | mm/y | Vertical land motion rates for the quantile 0.64  
`verticallandmotion_rates_quantile_0_65` | mm/y | Vertical land motion rates for the quantile 0.65  
`verticallandmotion_rates_quantile_0_66` | mm/y | Vertical land motion rates for the quantile 0.66  
`verticallandmotion_rates_quantile_0_67` | mm/y | Vertical land motion rates for the quantile 0.67  
`verticallandmotion_rates_quantile_0_68` | mm/y | Vertical land motion rates for the quantile 0.68  
`verticallandmotion_rates_quantile_0_69` | mm/y | Vertical land motion rates for the quantile 0.69  
`verticallandmotion_rates_quantile_0_7` | mm/y | Vertical land motion rates for the quantile 0.7  
`verticallandmotion_rates_quantile_0_71` | mm/y | Vertical land motion rates for the quantile 0.71  
`verticallandmotion_rates_quantile_0_72` | mm/y | Vertical land motion rates for the quantile 0.72  
`verticallandmotion_rates_quantile_0_73` | mm/y | Vertical land motion rates for the quantile 0.73  
`verticallandmotion_rates_quantile_0_74` | mm/y | Vertical land motion rates for the quantile 0.74  
`verticallandmotion_rates_quantile_0_75` | mm/y | Vertical land motion rates for the quantile 0.75  
`verticallandmotion_rates_quantile_0_76` | mm/y | Vertical land motion rates for the quantile 0.76  
`verticallandmotion_rates_quantile_0_77` | mm/y | Vertical land motion rates for the quantile 0.77  
`verticallandmotion_rates_quantile_0_78` | mm/y | Vertical land motion rates for the quantile 0.78  
`verticallandmotion_rates_quantile_0_79` | mm/y | Vertical land motion rates for the quantile 0.79  
`verticallandmotion_rates_quantile_0_8` | mm/y | Vertical land motion rates for the quantile 0.8  
`verticallandmotion_rates_quantile_0_81` | mm/y | Vertical land motion rates for the quantile 0.81  
`verticallandmotion_rates_quantile_0_82` | mm/y | Vertical land motion rates for the quantile 0.82  
`verticallandmotion_rates_quantile_0_83` | mm/y | Vertical land motion rates for the quantile 0.83  
`verticallandmotion_rates_quantile_0_833` | mm/y | Vertical land motion rates for the quantile 0.833  
`verticallandmotion_rates_quantile_0_84` | mm/y | Vertical land motion rates for the quantile 0.84  
`verticallandmotion_rates_quantile_0_85` | mm/y | Vertical land motion rates for the quantile 0.85  
`verticallandmotion_rates_quantile_0_86` | mm/y | Vertical land motion rates for the quantile 0.86  
`verticallandmotion_rates_quantile_0_87` | mm/y | Vertical land motion rates for the quantile 0.87  
`verticallandmotion_rates_quantile_0_88` | mm/y | Vertical land motion rates for the quantile 0.88  
`verticallandmotion_rates_quantile_0_89` | mm/y | Vertical land motion rates for the quantile 0.89  
`verticallandmotion_rates_quantile_0_9` | mm/y | Vertical land motion rates for the quantile 0.9  
`verticallandmotion_rates_quantile_0_91` | mm/y | Vertical land motion rates for the quantile 0.91  
`verticallandmotion_rates_quantile_0_92` | mm/y | Vertical land motion rates for the quantile 0.92  
`verticallandmotion_rates_quantile_0_93` | mm/y | Vertical land motion rates for the quantile 0.93  
`verticallandmotion_rates_quantile_0_94` | mm/y | Vertical land motion rates for the quantile 0.94  
`verticallandmotion_rates_quantile_0_95` | mm/y | Vertical land motion rates for the quantile 0.95  
`verticallandmotion_rates_quantile_0_96` | mm/y | Vertical land motion rates for the quantile 0.96  
`verticallandmotion_rates_quantile_0_97` | mm/y | Vertical land motion rates for the quantile 0.97  
`verticallandmotion_rates_quantile_0_98` | mm/y | Vertical land motion rates for the quantile 0.98  
`verticallandmotion_rates_quantile_0_99` | mm/y | Vertical land motion rates for the quantile 0.99  
`verticallandmotion_rates_quantile_0_995` | mm/y | Vertical land motion rates for the quantile 0.995  
`verticallandmotion_rates_quantile_0_999` | mm/y | Vertical land motion rates for the quantile 0.999  
`verticallandmotion_rates_quantile_1` | mm/y | Vertical land motion rates for the quantile 1  
`verticallandmotion_values_quantile_0` | mm | Vertical land motion values for the quantile 0  
`verticallandmotion_values_quantile_0_001` | mm | Vertical land motion values for the quantile 0.001  
`verticallandmotion_values_quantile_0_005` | mm | Vertical land motion values for the quantile 0.005  
`verticallandmotion_values_quantile_0_01` | mm | Vertical land motion values for the quantile 0.01  
`verticallandmotion_values_quantile_0_02` | mm | Vertical land motion values for the quantile 0.02  
`verticallandmotion_values_quantile_0_03` | mm | Vertical land motion values for the quantile 0.03  
`verticallandmotion_values_quantile_0_04` | mm | Vertical land motion values for the quantile 0.04  
`verticallandmotion_values_quantile_0_05` | mm | Vertical land motion values for the quantile 0.05  
`verticallandmotion_values_quantile_0_06` | mm | Vertical land motion values for the quantile 0.06  
`verticallandmotion_values_quantile_0_07` | mm | Vertical land motion values for the quantile 0.07  
`verticallandmotion_values_quantile_0_08` | mm | Vertical land motion values for the quantile 0.08  
`verticallandmotion_values_quantile_0_09` | mm | Vertical land motion values for the quantile 0.09  
`verticallandmotion_values_quantile_0_1` | mm | Vertical land motion values for the quantile 0.1  
`verticallandmotion_values_quantile_0_11` | mm | Vertical land motion values for the quantile 0.11  
`verticallandmotion_values_quantile_0_12` | mm | Vertical land motion values for the quantile 0.12  
`verticallandmotion_values_quantile_0_13` | mm | Vertical land motion values for the quantile 0.13  
`verticallandmotion_values_quantile_0_14` | mm | Vertical land motion values for the quantile 0.14  
`verticallandmotion_values_quantile_0_15` | mm | Vertical land motion values for the quantile 0.15  
`verticallandmotion_values_quantile_0_16` | mm | Vertical land motion values for the quantile 0.16  
`verticallandmotion_values_quantile_0_167` | mm | Vertical land motion values for the quantile 0.167  
`verticallandmotion_values_quantile_0_17` | mm | Vertical land motion values for the quantile 0.17  
`verticallandmotion_values_quantile_0_18` | mm | Vertical land motion values for the quantile 0.18  
`verticallandmotion_values_quantile_0_19` | mm | Vertical land motion values for the quantile 0.19  
`verticallandmotion_values_quantile_0_2` | mm | Vertical land motion values for the quantile 0.2  
`verticallandmotion_values_quantile_0_21` | mm | Vertical land motion values for the quantile 0.21  
`verticallandmotion_values_quantile_0_22` | mm | Vertical land motion values for the quantile 0.22  
`verticallandmotion_values_quantile_0_23` | mm | Vertical land motion values for the quantile 0.23  
`verticallandmotion_values_quantile_0_24` | mm | Vertical land motion values for the quantile 0.24  
`verticallandmotion_values_quantile_0_25` | mm | Vertical land motion values for the quantile 0.25  
`verticallandmotion_values_quantile_0_26` | mm | Vertical land motion values for the quantile 0.26  
`verticallandmotion_values_quantile_0_27` | mm | Vertical land motion values for the quantile 0.27  
`verticallandmotion_values_quantile_0_28` | mm | Vertical land motion values for the quantile 0.28  
`verticallandmotion_values_quantile_0_29` | mm | Vertical land motion values for the quantile 0.29  
`verticallandmotion_values_quantile_0_3` | mm | Vertical land motion values for the quantile 0.3  
`verticallandmotion_values_quantile_0_31` | mm | Vertical land motion values for the quantile 0.31  
`verticallandmotion_values_quantile_0_32` | mm | Vertical land motion values for the quantile 0.32  
`verticallandmotion_values_quantile_0_33` | mm | Vertical land motion values for the quantile 0.33  
`verticallandmotion_values_quantile_0_34` | mm | Vertical land motion values for the quantile 0.34  
`verticallandmotion_values_quantile_0_35` | mm | Vertical land motion values for the quantile 0.35  
`verticallandmotion_values_quantile_0_36` | mm | Vertical land motion values for the quantile 0.36  
`verticallandmotion_values_quantile_0_37` | mm | Vertical land motion values for the quantile 0.37  
`verticallandmotion_values_quantile_0_38` | mm | Vertical land motion values for the quantile 0.38  
`verticallandmotion_values_quantile_0_39` | mm | Vertical land motion values for the quantile 0.39  
`verticallandmotion_values_quantile_0_4` | mm | Vertical land motion values for the quantile 0.4  
`verticallandmotion_values_quantile_0_41` | mm | Vertical land motion values for the quantile 0.41  
`verticallandmotion_values_quantile_0_42` | mm | Vertical land motion values for the quantile 0.42  
`verticallandmotion_values_quantile_0_43` | mm | Vertical land motion values for the quantile 0.43  
`verticallandmotion_values_quantile_0_44` | mm | Vertical land motion values for the quantile 0.44  
`verticallandmotion_values_quantile_0_45` | mm | Vertical land motion values for the quantile 0.45  
`verticallandmotion_values_quantile_0_46` | mm | Vertical land motion values for the quantile 0.46  
`verticallandmotion_values_quantile_0_47` | mm | Vertical land motion values for the quantile 0.47  
`verticallandmotion_values_quantile_0_48` | mm | Vertical land motion values for the quantile 0.48  
`verticallandmotion_values_quantile_0_49` | mm | Vertical land motion values for the quantile 0.49  
`verticallandmotion_values_quantile_0_5` | mm | Vertical land motion values for the quantile 0.5  
`verticallandmotion_values_quantile_0_51` | mm | Vertical land motion values for the quantile 0.51  
`verticallandmotion_values_quantile_0_52` | mm | Vertical land motion values for the quantile 0.52  
`verticallandmotion_values_quantile_0_53` | mm | Vertical land motion values for the quantile 0.53  
`verticallandmotion_values_quantile_0_54` | mm | Vertical land motion values for the quantile 0.54  
`verticallandmotion_values_quantile_0_55` | mm | Vertical land motion values for the quantile 0.55  
`verticallandmotion_values_quantile_0_56` | mm | Vertical land motion values for the quantile 0.56  
`verticallandmotion_values_quantile_0_57` | mm | Vertical land motion values for the quantile 0.57  
`verticallandmotion_values_quantile_0_58` | mm | Vertical land motion values for the quantile 0.58  
`verticallandmotion_values_quantile_0_59` | mm | Vertical land motion values for the quantile 0.59  
`verticallandmotion_values_quantile_0_6` | mm | Vertical land motion values for the quantile 0.6  
`verticallandmotion_values_quantile_0_61` | mm | Vertical land motion values for the quantile 0.61  
`verticallandmotion_values_quantile_0_62` | mm | Vertical land motion values for the quantile 0.62  
`verticallandmotion_values_quantile_0_63` | mm | Vertical land motion values for the quantile 0.63  
`verticallandmotion_values_quantile_0_64` | mm | Vertical land motion values for the quantile 0.64  
`verticallandmotion_values_quantile_0_65` | mm | Vertical land motion values for the quantile 0.65  
`verticallandmotion_values_quantile_0_66` | mm | Vertical land motion values for the quantile 0.66  
`verticallandmotion_values_quantile_0_67` | mm | Vertical land motion values for the quantile 0.67  
`verticallandmotion_values_quantile_0_68` | mm | Vertical land motion values for the quantile 0.68  
`verticallandmotion_values_quantile_0_69` | mm | Vertical land motion values for the quantile 0.69  
`verticallandmotion_values_quantile_0_7` | mm | Vertical land motion values for the quantile 0.7  
`verticallandmotion_values_quantile_0_71` | mm | Vertical land motion values for the quantile 0.71  
`verticallandmotion_values_quantile_0_72` | mm | Vertical land motion values for the quantile 0.72  
`verticallandmotion_values_quantile_0_73` | mm | Vertical land motion values for the quantile 0.73  
`verticallandmotion_values_quantile_0_74` | mm | Vertical land motion values for the quantile 0.74  
`verticallandmotion_values_quantile_0_75` | mm | Vertical land motion values for the quantile 0.75  
`verticallandmotion_values_quantile_0_76` | mm | Vertical land motion values for the quantile 0.76  
`verticallandmotion_values_quantile_0_77` | mm | Vertical land motion values for the quantile 0.77  
`verticallandmotion_values_quantile_0_78` | mm | Vertical land motion values for the quantile 0.78  
`verticallandmotion_values_quantile_0_79` | mm | Vertical land motion values for the quantile 0.79  
`verticallandmotion_values_quantile_0_8` | mm | Vertical land motion values for the quantile 0.8  
`verticallandmotion_values_quantile_0_81` | mm | Vertical land motion values for the quantile 0.81  
`verticallandmotion_values_quantile_0_82` | mm | Vertical land motion values for the quantile 0.82  
`verticallandmotion_values_quantile_0_83` | mm | Vertical land motion values for the quantile 0.83  
`verticallandmotion_values_quantile_0_833` | mm | Vertical land motion values for the quantile 0.833  
`verticallandmotion_values_quantile_0_84` | mm | Vertical land motion values for the quantile 0.84  
`verticallandmotion_values_quantile_0_85` | mm | Vertical land motion values for the quantile 0.85  
`verticallandmotion_values_quantile_0_86` | mm | Vertical land motion values for the quantile 0.86  
`verticallandmotion_values_quantile_0_87` | mm | Vertical land motion values for the quantile 0.87  
`verticallandmotion_values_quantile_0_88` | mm | Vertical land motion values for the quantile 0.88  
`verticallandmotion_values_quantile_0_89` | mm | Vertical land motion values for the quantile 0.89  
`verticallandmotion_values_quantile_0_9` | mm | Vertical land motion values for the quantile 0.9  
`verticallandmotion_values_quantile_0_91` | mm | Vertical land motion values for the quantile 0.91  
`verticallandmotion_values_quantile_0_92` | mm | Vertical land motion values for the quantile 0.92  
`verticallandmotion_values_quantile_0_93` | mm | Vertical land motion values for the quantile 0.93  
`verticallandmotion_values_quantile_0_94` | mm | Vertical land motion values for the quantile 0.94  
`verticallandmotion_values_quantile_0_95` | mm | Vertical land motion values for the quantile 0.95  
`verticallandmotion_values_quantile_0_96` | mm | Vertical land motion values for the quantile 0.96  
`verticallandmotion_values_quantile_0_97` | mm | Vertical land motion values for the quantile 0.97  
`verticallandmotion_values_quantile_0_98` | mm | Vertical land motion values for the quantile 0.98  
`verticallandmotion_values_quantile_0_99` | mm | Vertical land motion values for the quantile 0.99  
`verticallandmotion_values_quantile_0_995` | mm | Vertical land motion values for the quantile 0.995  
`verticallandmotion_values_quantile_0_999` | mm | Vertical land motion values for the quantile 0.999  
`verticallandmotion_values_quantile_1` | mm | Vertical land motion values for the quantile 1  
**Terms of Use**
This dataset is made available publicly under the Creative Commons by Attribution license(CC-BY-4.0).
Citations:
  * Garner, G. G., T. Hermans, R. E. Kopp, A. B. A. Slangen, T. L. Edwards, A. Levermann, S. Nowikci, M. D. Palmer, C. Smith, B. Fox-Kemper, H. T. Hewitt, C. Xiao, G. Aðalgeirsdóttir, S. S. Drijfhout, T. L. Edwards, N. R. Golledge, M. Hemer, G. Krinner, A. Mix, D. Notz, S. Nowicki, I. S. Nurhati, L. Ruiz, J-B. Sallée, Y. Yu, L. Hua, T. Palmer, B. Pearson, 2021. IPCC AR6 Sea Level Projections. Version 20210809. Dataset accessed [YYYY-MM-DD] at [10.5281/zenodo.5914709](https://doi.org/10.5281/zenodo.5914709)
  * Fox-Kemper, B., et al., 2021: Ocean, Cryosphere and Sea Level Change. In Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the IPCC [Masson-Delmotte, V., et al. (eds.)]. Cambridge University Press, pp. 1211-1362. [doi:10.1017/9781009157896.011](https://doi.org/10.1017/9781009157896.011).
  * Kopp, R. E., Garner, G. G., Hermans, T. H. J., Jha, S., Kumar, P., Reedy, A., Slangen, A. B. A., Turilli, M., Edwards, T. L., Gregory, J. M., Koubbe, G., Levermann, A., Merzky, A., Nowicki, S., Palmer, M. D., & Smith, C. (2023). The Framework for Assessing Changes To Sea-Level (FACTS) v1.0, 16, 7461-7489. [10.5194/gmd-16-7461-2023](https://doi.org/10.5194/gmd-16-7461-2023)


  * [ https://doi.org/10.1017/9781009157896.011 ](https://doi.org/10.1017/9781009157896.011)
  * [ https://doi.org/10.5194/gmd-16-7461-2023 ](https://doi.org/10.5194/gmd-16-7461-2023)
  * [ https://doi.org/10.5281/zenodo.5914709 ](https://doi.org/10.5281/zenodo.5914709)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP#code-editor-javascript-sample) More
```
varimage=
ee.Image('IPCC/AR6/SLP/ssp126_2030').select('total_values_quantile_0_5');
varvisParams={
min:10,
max:150,
palette:['0000FF','00FFFF','FFFF00','FF0000'],
};
Map.addLayer(
image,visParams,'0.5 quantile projection for sea level change in 2030');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/IPCC/IPCC_AR6_SLP)
[ IPCC AR6 Sea Level Projections Regional (Medium Confidence) ](https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP)
The dataset provided by the IPCC features comprehensive global and regional sea level projections from the IPCC 6th Assessment Report (AR6). This collection contains assets for the medium confidence sea level rise projections. The dataset spans from 2020 to 2150 and includes projections for various future scenarios outlined in the …
IPCC/AR6/SLP, ipcc,ocean,oceans 
2020-01-01T00:00:00Z/2120-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5281/zenodo.5914709 ](https://doi.org/https://zenodo.org/records/6382554)
  * [ https://doi.org/10.5281/zenodo.5914709 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/IPCC_AR6_SLP)


