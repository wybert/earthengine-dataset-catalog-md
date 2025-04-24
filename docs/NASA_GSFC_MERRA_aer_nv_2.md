 
#  MERRA-2 M2I3NVAER: Aerosol Mixing Ratio V5.12.4 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![NASA/GSFC/MERRA/aer_nv/2](https://developers.google.com/earth-engine/datasets/images/NASA/NASA_GSFC_MERRA_aer_nv_2_sample.png) 

Dataset Availability
    1980-01-01T00:00:00Z–2025-03-01T21:00:00Z 

Dataset Provider
     [ NASA/MERRA ](https://disc.gsfc.nasa.gov/datasets/M2I3NVAER_5.12.4/summary) 

Earth Engine Snippet
     `    ee.ImageCollection("NASA/GSFC/MERRA/aer_nv/2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GSFC_MERRA_aer_nv_2) 

Cadence
    3 Hours 

Tags
     [aerosol](https://developers.google.com/earth-engine/datasets/tags/aerosol) [atmosphere](https://developers.google.com/earth-engine/datasets/tags/atmosphere) [dust](https://developers.google.com/earth-engine/datasets/tags/dust) [mass](https://developers.google.com/earth-engine/datasets/tags/mass) [merra](https://developers.google.com/earth-engine/datasets/tags/merra) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [sea-salt](https://developers.google.com/earth-engine/datasets/tags/sea-salt) [so2](https://developers.google.com/earth-engine/datasets/tags/so2) [so4](https://developers.google.com/earth-engine/datasets/tags/so4)
[Description](https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2#terms-of-use) More
M2I3NVAER (or inst3_3d_aer_Nv) is an instantaneous 3-dimensional 3-hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2). This collection consists of assimilations of aerosol mixing ratio parameters at 72 model layers, such as dust, sulphur dioxide, sea salt, black carbon, and organic carbon. The data field is available every three hour starting from 00:00 UTC, e.g.: 00:00, 03:00,... ,21:00 UTC. Section 4.2 of the [MERRA-2 File Specification document](https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf) provides pressure values nominal for a 1000 hPa surface pressure and refers to the top edge of the layer. The lev=1 is for the top layer, and lev=72 is for the bottom (or surface) model layer.
MERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4. The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month.
**Pixel Size** 69375 meters 
**Y Pixel Size** 55000 meters 
**Bands**
Name | Units | Description  
---|---|---  
`AIRDENS_1` | kg/m^3 | Air density  
`SO2_1` | Mass fraction | Sulphur dioxide  
`DELP_1` | Pa | Pressure thickness  
`SS004_1` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_1` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_1` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_1` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_1` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_1` | Mass fraction | Hydrophobic Black Carbon  
`SS002_1` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_1` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_1` | Mass fraction | Dimethylsulphide  
`SO4_1` | Mass fraction | Sulphate aerosol  
`DU002_1` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_1` | Pa | Surface Pressure  
`SS003_1` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_1` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_1` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_1` | Mass fraction | Hydrophilic Black Carbon  
`MSA_1` | Mass fraction | Methanesulphonic acid  
`SS001_1` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_2` | kg/m^3 | Air density  
`SO2_2` | Mass fraction | Sulphur dioxide  
`DELP_2` | Pa | Pressure thickness  
`SS004_2` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_2` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_2` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_2` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_2` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_2` | Mass fraction | Hydrophobic Black Carbon  
`SS002_2` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_2` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_2` | Mass fraction | Dimethylsulphide  
`SO4_2` | Mass fraction | Sulphate aerosol  
`DU002_2` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_2` | Pa | Surface Pressure  
`SS003_2` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_2` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_2` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_2` | Mass fraction | Hydrophilic Black Carbon  
`MSA_2` | Mass fraction | Methanesulphonic acid  
`SS001_2` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_3` | kg/m^3 | Air density  
`SO2_3` | Mass fraction | Sulphur dioxide  
`DELP_3` | Pa | Pressure thickness  
`SS004_3` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_3` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_3` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_3` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_3` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_3` | Mass fraction | Hydrophobic Black Carbon  
`SS002_3` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_3` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_3` | Mass fraction | Dimethylsulphide  
`SO4_3` | Mass fraction | Sulphate aerosol  
`DU002_3` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_3` | Pa | Surface Pressure  
`SS003_3` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_3` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_3` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_3` | Mass fraction | Hydrophilic Black Carbon  
`MSA_3` | Mass fraction | Methanesulphonic acid  
`SS001_3` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_4` | kg/m^3 | Air density  
`SO2_4` | Mass fraction | Sulphur dioxide  
`DELP_4` | Pa | Pressure thickness  
`SS004_4` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_4` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_4` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_4` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_4` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_4` | Mass fraction | Hydrophobic Black Carbon  
`SS002_4` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_4` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_4` | Mass fraction | Dimethylsulphide  
`SO4_4` | Mass fraction | Sulphate aerosol  
`DU002_4` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_4` | Pa | Surface Pressure  
`SS003_4` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_4` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_4` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_4` | Mass fraction | Hydrophilic Black Carbon  
`MSA_4` | Mass fraction | Methanesulphonic acid  
`SS001_4` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_5` | kg/m^3 | Air density  
`SO2_5` | Mass fraction | Sulphur dioxide  
`DELP_5` | Pa | Pressure thickness  
`SS004_5` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_5` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_5` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_5` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_5` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_5` | Mass fraction | Hydrophobic Black Carbon  
`SS002_5` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_5` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_5` | Mass fraction | Dimethylsulphide  
`SO4_5` | Mass fraction | Sulphate aerosol  
`DU002_5` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_5` | Pa | Surface Pressure  
`SS003_5` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_5` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_5` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_5` | Mass fraction | Hydrophilic Black Carbon  
`MSA_5` | Mass fraction | Methanesulphonic acid  
`SS001_5` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_6` | kg/m^3 | Air density  
`SO2_6` | Mass fraction | Sulphur dioxide  
`DELP_6` | Pa | Pressure thickness  
`SS004_6` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_6` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_6` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_6` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_6` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_6` | Mass fraction | Hydrophobic Black Carbon  
`SS002_6` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_6` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_6` | Mass fraction | Dimethylsulphide  
`SO4_6` | Mass fraction | Sulphate aerosol  
`DU002_6` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_6` | Pa | Surface Pressure  
`SS003_6` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_6` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_6` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_6` | Mass fraction | Hydrophilic Black Carbon  
`MSA_6` | Mass fraction | Methanesulphonic acid  
`SS001_6` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_7` | kg/m^3 | Air density  
`SO2_7` | Mass fraction | Sulphur dioxide  
`DELP_7` | Pa | Pressure thickness  
`SS004_7` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_7` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_7` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_7` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_7` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_7` | Mass fraction | Hydrophobic Black Carbon  
`SS002_7` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_7` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_7` | Mass fraction | Dimethylsulphide  
`SO4_7` | Mass fraction | Sulphate aerosol  
`DU002_7` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_7` | Pa | Surface Pressure  
`SS003_7` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_7` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_7` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_7` | Mass fraction | Hydrophilic Black Carbon  
`MSA_7` | Mass fraction | Methanesulphonic acid  
`SS001_7` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_8` | kg/m^3 | Air density  
`SO2_8` | Mass fraction | Sulphur dioxide  
`DELP_8` | Pa | Pressure thickness  
`SS004_8` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_8` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_8` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_8` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_8` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_8` | Mass fraction | Hydrophobic Black Carbon  
`SS002_8` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_8` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_8` | Mass fraction | Dimethylsulphide  
`SO4_8` | Mass fraction | Sulphate aerosol  
`DU002_8` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_8` | Pa | Surface Pressure  
`SS003_8` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_8` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_8` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_8` | Mass fraction | Hydrophilic Black Carbon  
`MSA_8` | Mass fraction | Methanesulphonic acid  
`SS001_8` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_9` | kg/m^3 | Air density  
`SO2_9` | Mass fraction | Sulphur dioxide  
`DELP_9` | Pa | Pressure thickness  
`SS004_9` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_9` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_9` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_9` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_9` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_9` | Mass fraction | Hydrophobic Black Carbon  
`SS002_9` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_9` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_9` | Mass fraction | Dimethylsulphide  
`SO4_9` | Mass fraction | Sulphate aerosol  
`DU002_9` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_9` | Pa | Surface Pressure  
`SS003_9` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_9` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_9` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_9` | Mass fraction | Hydrophilic Black Carbon  
`MSA_9` | Mass fraction | Methanesulphonic acid  
`SS001_9` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_10` | kg/m^3 | Air density  
`SO2_10` | Mass fraction | Sulphur dioxide  
`DELP_10` | Pa | Pressure thickness  
`SS004_10` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_10` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_10` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_10` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_10` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_10` | Mass fraction | Hydrophobic Black Carbon  
`SS002_10` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_10` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_10` | Mass fraction | Dimethylsulphide  
`SO4_10` | Mass fraction | Sulphate aerosol  
`DU002_10` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_10` | Pa | Surface Pressure  
`SS003_10` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_10` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_10` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_10` | Mass fraction | Hydrophilic Black Carbon  
`MSA_10` | Mass fraction | Methanesulphonic acid  
`SS001_10` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_11` | kg/m^3 | Air density  
`SO2_11` | Mass fraction | Sulphur dioxide  
`DELP_11` | Pa | Pressure thickness  
`SS004_11` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_11` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_11` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_11` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_11` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_11` | Mass fraction | Hydrophobic Black Carbon  
`SS002_11` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_11` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_11` | Mass fraction | Dimethylsulphide  
`SO4_11` | Mass fraction | Sulphate aerosol  
`DU002_11` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_11` | Pa | Surface Pressure  
`SS003_11` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_11` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_11` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_11` | Mass fraction | Hydrophilic Black Carbon  
`MSA_11` | Mass fraction | Methanesulphonic acid  
`SS001_11` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_12` | kg/m^3 | Air density  
`SO2_12` | Mass fraction | Sulphur dioxide  
`DELP_12` | Pa | Pressure thickness  
`SS004_12` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_12` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_12` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_12` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_12` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_12` | Mass fraction | Hydrophobic Black Carbon  
`SS002_12` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_12` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_12` | Mass fraction | Dimethylsulphide  
`SO4_12` | Mass fraction | Sulphate aerosol  
`DU002_12` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_12` | Pa | Surface Pressure  
`SS003_12` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_12` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_12` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_12` | Mass fraction | Hydrophilic Black Carbon  
`MSA_12` | Mass fraction | Methanesulphonic acid  
`SS001_12` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_13` | kg/m^3 | Air density  
`SO2_13` | Mass fraction | Sulphur dioxide  
`DELP_13` | Pa | Pressure thickness  
`SS004_13` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_13` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_13` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_13` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_13` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_13` | Mass fraction | Hydrophobic Black Carbon  
`SS002_13` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_13` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_13` | Mass fraction | Dimethylsulphide  
`SO4_13` | Mass fraction | Sulphate aerosol  
`DU002_13` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_13` | Pa | Surface Pressure  
`SS003_13` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_13` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_13` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_13` | Mass fraction | Hydrophilic Black Carbon  
`MSA_13` | Mass fraction | Methanesulphonic acid  
`SS001_13` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_14` | kg/m^3 | Air density  
`SO2_14` | Mass fraction | Sulphur dioxide  
`DELP_14` | Pa | Pressure thickness  
`SS004_14` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_14` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_14` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_14` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_14` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_14` | Mass fraction | Hydrophobic Black Carbon  
`SS002_14` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_14` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_14` | Mass fraction | Dimethylsulphide  
`SO4_14` | Mass fraction | Sulphate aerosol  
`DU002_14` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_14` | Pa | Surface Pressure  
`SS003_14` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_14` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_14` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_14` | Mass fraction | Hydrophilic Black Carbon  
`MSA_14` | Mass fraction | Methanesulphonic acid  
`SS001_14` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_15` | kg/m^3 | Air density  
`SO2_15` | Mass fraction | Sulphur dioxide  
`DELP_15` | Pa | Pressure thickness  
`SS004_15` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_15` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_15` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_15` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_15` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_15` | Mass fraction | Hydrophobic Black Carbon  
`SS002_15` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_15` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_15` | Mass fraction | Dimethylsulphide  
`SO4_15` | Mass fraction | Sulphate aerosol  
`DU002_15` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_15` | Pa | Surface Pressure  
`SS003_15` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_15` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_15` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_15` | Mass fraction | Hydrophilic Black Carbon  
`MSA_15` | Mass fraction | Methanesulphonic acid  
`SS001_15` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_16` | kg/m^3 | Air density  
`SO2_16` | Mass fraction | Sulphur dioxide  
`DELP_16` | Pa | Pressure thickness  
`SS004_16` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_16` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_16` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_16` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_16` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_16` | Mass fraction | Hydrophobic Black Carbon  
`SS002_16` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_16` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_16` | Mass fraction | Dimethylsulphide  
`SO4_16` | Mass fraction | Sulphate aerosol  
`DU002_16` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_16` | Pa | Surface Pressure  
`SS003_16` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_16` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_16` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_16` | Mass fraction | Hydrophilic Black Carbon  
`MSA_16` | Mass fraction | Methanesulphonic acid  
`SS001_16` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_17` | kg/m^3 | Air density  
`SO2_17` | Mass fraction | Sulphur dioxide  
`DELP_17` | Pa | Pressure thickness  
`SS004_17` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_17` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_17` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_17` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_17` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_17` | Mass fraction | Hydrophobic Black Carbon  
`SS002_17` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_17` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_17` | Mass fraction | Dimethylsulphide  
`SO4_17` | Mass fraction | Sulphate aerosol  
`DU002_17` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_17` | Pa | Surface Pressure  
`SS003_17` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_17` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_17` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_17` | Mass fraction | Hydrophilic Black Carbon  
`MSA_17` | Mass fraction | Methanesulphonic acid  
`SS001_17` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_18` | kg/m^3 | Air density  
`SO2_18` | Mass fraction | Sulphur dioxide  
`DELP_18` | Pa | Pressure thickness  
`SS004_18` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_18` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_18` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_18` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_18` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_18` | Mass fraction | Hydrophobic Black Carbon  
`SS002_18` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_18` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_18` | Mass fraction | Dimethylsulphide  
`SO4_18` | Mass fraction | Sulphate aerosol  
`DU002_18` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_18` | Pa | Surface Pressure  
`SS003_18` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_18` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_18` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_18` | Mass fraction | Hydrophilic Black Carbon  
`MSA_18` | Mass fraction | Methanesulphonic acid  
`SS001_18` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_19` | kg/m^3 | Air density  
`SO2_19` | Mass fraction | Sulphur dioxide  
`DELP_19` | Pa | Pressure thickness  
`SS004_19` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_19` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_19` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_19` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_19` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_19` | Mass fraction | Hydrophobic Black Carbon  
`SS002_19` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_19` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_19` | Mass fraction | Dimethylsulphide  
`SO4_19` | Mass fraction | Sulphate aerosol  
`DU002_19` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_19` | Pa | Surface Pressure  
`SS003_19` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_19` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_19` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_19` | Mass fraction | Hydrophilic Black Carbon  
`MSA_19` | Mass fraction | Methanesulphonic acid  
`SS001_19` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_20` | kg/m^3 | Air density  
`SO2_20` | Mass fraction | Sulphur dioxide  
`DELP_20` | Pa | Pressure thickness  
`SS004_20` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_20` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_20` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_20` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_20` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_20` | Mass fraction | Hydrophobic Black Carbon  
`SS002_20` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_20` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_20` | Mass fraction | Dimethylsulphide  
`SO4_20` | Mass fraction | Sulphate aerosol  
`DU002_20` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_20` | Pa | Surface Pressure  
`SS003_20` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_20` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_20` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_20` | Mass fraction | Hydrophilic Black Carbon  
`MSA_20` | Mass fraction | Methanesulphonic acid  
`SS001_20` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_21` | kg/m^3 | Air density  
`SO2_21` | Mass fraction | Sulphur dioxide  
`DELP_21` | Pa | Pressure thickness  
`SS004_21` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_21` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_21` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_21` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_21` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_21` | Mass fraction | Hydrophobic Black Carbon  
`SS002_21` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_21` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_21` | Mass fraction | Dimethylsulphide  
`SO4_21` | Mass fraction | Sulphate aerosol  
`DU002_21` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_21` | Pa | Surface Pressure  
`SS003_21` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_21` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_21` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_21` | Mass fraction | Hydrophilic Black Carbon  
`MSA_21` | Mass fraction | Methanesulphonic acid  
`SS001_21` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_22` | kg/m^3 | Air density  
`SO2_22` | Mass fraction | Sulphur dioxide  
`DELP_22` | Pa | Pressure thickness  
`SS004_22` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_22` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_22` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_22` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_22` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_22` | Mass fraction | Hydrophobic Black Carbon  
`SS002_22` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_22` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_22` | Mass fraction | Dimethylsulphide  
`SO4_22` | Mass fraction | Sulphate aerosol  
`DU002_22` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_22` | Pa | Surface Pressure  
`SS003_22` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_22` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_22` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_22` | Mass fraction | Hydrophilic Black Carbon  
`MSA_22` | Mass fraction | Methanesulphonic acid  
`SS001_22` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_23` | kg/m^3 | Air density  
`SO2_23` | Mass fraction | Sulphur dioxide  
`DELP_23` | Pa | Pressure thickness  
`SS004_23` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_23` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_23` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_23` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_23` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_23` | Mass fraction | Hydrophobic Black Carbon  
`SS002_23` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_23` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_23` | Mass fraction | Dimethylsulphide  
`SO4_23` | Mass fraction | Sulphate aerosol  
`DU002_23` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_23` | Pa | Surface Pressure  
`SS003_23` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_23` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_23` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_23` | Mass fraction | Hydrophilic Black Carbon  
`MSA_23` | Mass fraction | Methanesulphonic acid  
`SS001_23` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_24` | kg/m^3 | Air density  
`SO2_24` | Mass fraction | Sulphur dioxide  
`DELP_24` | Pa | Pressure thickness  
`SS004_24` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_24` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_24` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_24` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_24` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_24` | Mass fraction | Hydrophobic Black Carbon  
`SS002_24` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_24` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_24` | Mass fraction | Dimethylsulphide  
`SO4_24` | Mass fraction | Sulphate aerosol  
`DU002_24` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_24` | Pa | Surface Pressure  
`SS003_24` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_24` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_24` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_24` | Mass fraction | Hydrophilic Black Carbon  
`MSA_24` | Mass fraction | Methanesulphonic acid  
`SS001_24` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_25` | kg/m^3 | Air density  
`SO2_25` | Mass fraction | Sulphur dioxide  
`DELP_25` | Pa | Pressure thickness  
`SS004_25` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_25` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_25` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_25` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_25` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_25` | Mass fraction | Hydrophobic Black Carbon  
`SS002_25` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_25` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_25` | Mass fraction | Dimethylsulphide  
`SO4_25` | Mass fraction | Sulphate aerosol  
`DU002_25` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_25` | Pa | Surface Pressure  
`SS003_25` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_25` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_25` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_25` | Mass fraction | Hydrophilic Black Carbon  
`MSA_25` | Mass fraction | Methanesulphonic acid  
`SS001_25` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_26` | kg/m^3 | Air density  
`SO2_26` | Mass fraction | Sulphur dioxide  
`DELP_26` | Pa | Pressure thickness  
`SS004_26` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_26` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_26` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_26` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_26` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_26` | Mass fraction | Hydrophobic Black Carbon  
`SS002_26` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_26` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_26` | Mass fraction | Dimethylsulphide  
`SO4_26` | Mass fraction | Sulphate aerosol  
`DU002_26` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_26` | Pa | Surface Pressure  
`SS003_26` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_26` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_26` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_26` | Mass fraction | Hydrophilic Black Carbon  
`MSA_26` | Mass fraction | Methanesulphonic acid  
`SS001_26` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_27` | kg/m^3 | Air density  
`SO2_27` | Mass fraction | Sulphur dioxide  
`DELP_27` | Pa | Pressure thickness  
`SS004_27` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_27` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_27` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_27` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_27` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_27` | Mass fraction | Hydrophobic Black Carbon  
`SS002_27` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_27` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_27` | Mass fraction | Dimethylsulphide  
`SO4_27` | Mass fraction | Sulphate aerosol  
`DU002_27` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_27` | Pa | Surface Pressure  
`SS003_27` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_27` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_27` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_27` | Mass fraction | Hydrophilic Black Carbon  
`MSA_27` | Mass fraction | Methanesulphonic acid  
`SS001_27` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_28` | kg/m^3 | Air density  
`SO2_28` | Mass fraction | Sulphur dioxide  
`DELP_28` | Pa | Pressure thickness  
`SS004_28` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_28` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_28` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_28` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_28` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_28` | Mass fraction | Hydrophobic Black Carbon  
`SS002_28` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_28` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_28` | Mass fraction | Dimethylsulphide  
`SO4_28` | Mass fraction | Sulphate aerosol  
`DU002_28` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_28` | Pa | Surface Pressure  
`SS003_28` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_28` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_28` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_28` | Mass fraction | Hydrophilic Black Carbon  
`MSA_28` | Mass fraction | Methanesulphonic acid  
`SS001_28` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_29` | kg/m^3 | Air density  
`SO2_29` | Mass fraction | Sulphur dioxide  
`DELP_29` | Pa | Pressure thickness  
`SS004_29` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_29` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_29` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_29` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_29` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_29` | Mass fraction | Hydrophobic Black Carbon  
`SS002_29` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_29` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_29` | Mass fraction | Dimethylsulphide  
`SO4_29` | Mass fraction | Sulphate aerosol  
`DU002_29` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_29` | Pa | Surface Pressure  
`SS003_29` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_29` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_29` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_29` | Mass fraction | Hydrophilic Black Carbon  
`MSA_29` | Mass fraction | Methanesulphonic acid  
`SS001_29` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_30` | kg/m^3 | Air density  
`SO2_30` | Mass fraction | Sulphur dioxide  
`DELP_30` | Pa | Pressure thickness  
`SS004_30` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_30` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_30` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_30` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_30` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_30` | Mass fraction | Hydrophobic Black Carbon  
`SS002_30` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_30` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_30` | Mass fraction | Dimethylsulphide  
`SO4_30` | Mass fraction | Sulphate aerosol  
`DU002_30` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_30` | Pa | Surface Pressure  
`SS003_30` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_30` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_30` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_30` | Mass fraction | Hydrophilic Black Carbon  
`MSA_30` | Mass fraction | Methanesulphonic acid  
`SS001_30` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_31` | kg/m^3 | Air density  
`SO2_31` | Mass fraction | Sulphur dioxide  
`DELP_31` | Pa | Pressure thickness  
`SS004_31` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_31` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_31` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_31` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_31` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_31` | Mass fraction | Hydrophobic Black Carbon  
`SS002_31` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_31` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_31` | Mass fraction | Dimethylsulphide  
`SO4_31` | Mass fraction | Sulphate aerosol  
`DU002_31` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_31` | Pa | Surface Pressure  
`SS003_31` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_31` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_31` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_31` | Mass fraction | Hydrophilic Black Carbon  
`MSA_31` | Mass fraction | Methanesulphonic acid  
`SS001_31` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_32` | kg/m^3 | Air density  
`SO2_32` | Mass fraction | Sulphur dioxide  
`DELP_32` | Pa | Pressure thickness  
`SS004_32` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_32` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_32` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_32` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_32` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_32` | Mass fraction | Hydrophobic Black Carbon  
`SS002_32` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_32` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_32` | Mass fraction | Dimethylsulphide  
`SO4_32` | Mass fraction | Sulphate aerosol  
`DU002_32` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_32` | Pa | Surface Pressure  
`SS003_32` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_32` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_32` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_32` | Mass fraction | Hydrophilic Black Carbon  
`MSA_32` | Mass fraction | Methanesulphonic acid  
`SS001_32` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_33` | kg/m^3 | Air density  
`SO2_33` | Mass fraction | Sulphur dioxide  
`DELP_33` | Pa | Pressure thickness  
`SS004_33` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_33` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_33` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_33` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_33` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_33` | Mass fraction | Hydrophobic Black Carbon  
`SS002_33` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_33` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_33` | Mass fraction | Dimethylsulphide  
`SO4_33` | Mass fraction | Sulphate aerosol  
`DU002_33` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_33` | Pa | Surface Pressure  
`SS003_33` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_33` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_33` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_33` | Mass fraction | Hydrophilic Black Carbon  
`MSA_33` | Mass fraction | Methanesulphonic acid  
`SS001_33` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_34` | kg/m^3 | Air density  
`SO2_34` | Mass fraction | Sulphur dioxide  
`DELP_34` | Pa | Pressure thickness  
`SS004_34` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_34` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_34` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_34` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_34` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_34` | Mass fraction | Hydrophobic Black Carbon  
`SS002_34` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_34` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_34` | Mass fraction | Dimethylsulphide  
`SO4_34` | Mass fraction | Sulphate aerosol  
`DU002_34` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_34` | Pa | Surface Pressure  
`SS003_34` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_34` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_34` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_34` | Mass fraction | Hydrophilic Black Carbon  
`MSA_34` | Mass fraction | Methanesulphonic acid  
`SS001_34` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_35` | kg/m^3 | Air density  
`SO2_35` | Mass fraction | Sulphur dioxide  
`DELP_35` | Pa | Pressure thickness  
`SS004_35` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_35` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_35` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_35` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_35` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_35` | Mass fraction | Hydrophobic Black Carbon  
`SS002_35` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_35` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_35` | Mass fraction | Dimethylsulphide  
`SO4_35` | Mass fraction | Sulphate aerosol  
`DU002_35` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_35` | Pa | Surface Pressure  
`SS003_35` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_35` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_35` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_35` | Mass fraction | Hydrophilic Black Carbon  
`MSA_35` | Mass fraction | Methanesulphonic acid  
`SS001_35` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_36` | kg/m^3 | Air density  
`SO2_36` | Mass fraction | Sulphur dioxide  
`DELP_36` | Pa | Pressure thickness  
`SS004_36` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_36` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_36` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_36` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_36` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_36` | Mass fraction | Hydrophobic Black Carbon  
`SS002_36` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_36` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_36` | Mass fraction | Dimethylsulphide  
`SO4_36` | Mass fraction | Sulphate aerosol  
`DU002_36` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_36` | Pa | Surface Pressure  
`SS003_36` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_36` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_36` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_36` | Mass fraction | Hydrophilic Black Carbon  
`MSA_36` | Mass fraction | Methanesulphonic acid  
`SS001_36` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_37` | kg/m^3 | Air density  
`SO2_37` | Mass fraction | Sulphur dioxide  
`DELP_37` | Pa | Pressure thickness  
`SS004_37` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_37` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_37` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_37` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_37` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_37` | Mass fraction | Hydrophobic Black Carbon  
`SS002_37` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_37` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_37` | Mass fraction | Dimethylsulphide  
`SO4_37` | Mass fraction | Sulphate aerosol  
`DU002_37` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_37` | Pa | Surface Pressure  
`SS003_37` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_37` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_37` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_37` | Mass fraction | Hydrophilic Black Carbon  
`MSA_37` | Mass fraction | Methanesulphonic acid  
`SS001_37` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_38` | kg/m^3 | Air density  
`SO2_38` | Mass fraction | Sulphur dioxide  
`DELP_38` | Pa | Pressure thickness  
`SS004_38` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_38` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_38` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_38` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_38` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_38` | Mass fraction | Hydrophobic Black Carbon  
`SS002_38` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_38` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_38` | Mass fraction | Dimethylsulphide  
`SO4_38` | Mass fraction | Sulphate aerosol  
`DU002_38` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_38` | Pa | Surface Pressure  
`SS003_38` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_38` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_38` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_38` | Mass fraction | Hydrophilic Black Carbon  
`MSA_38` | Mass fraction | Methanesulphonic acid  
`SS001_38` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_39` | kg/m^3 | Air density  
`SO2_39` | Mass fraction | Sulphur dioxide  
`DELP_39` | Pa | Pressure thickness  
`SS004_39` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_39` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_39` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_39` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_39` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_39` | Mass fraction | Hydrophobic Black Carbon  
`SS002_39` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_39` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_39` | Mass fraction | Dimethylsulphide  
`SO4_39` | Mass fraction | Sulphate aerosol  
`DU002_39` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_39` | Pa | Surface Pressure  
`SS003_39` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_39` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_39` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_39` | Mass fraction | Hydrophilic Black Carbon  
`MSA_39` | Mass fraction | Methanesulphonic acid  
`SS001_39` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_40` | kg/m^3 | Air density  
`SO2_40` | Mass fraction | Sulphur dioxide  
`DELP_40` | Pa | Pressure thickness  
`SS004_40` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_40` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_40` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_40` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_40` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_40` | Mass fraction | Hydrophobic Black Carbon  
`SS002_40` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_40` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_40` | Mass fraction | Dimethylsulphide  
`SO4_40` | Mass fraction | Sulphate aerosol  
`DU002_40` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_40` | Pa | Surface Pressure  
`SS003_40` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_40` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_40` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_40` | Mass fraction | Hydrophilic Black Carbon  
`MSA_40` | Mass fraction | Methanesulphonic acid  
`SS001_40` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_41` | kg/m^3 | Air density  
`SO2_41` | Mass fraction | Sulphur dioxide  
`DELP_41` | Pa | Pressure thickness  
`SS004_41` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_41` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_41` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_41` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_41` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_41` | Mass fraction | Hydrophobic Black Carbon  
`SS002_41` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_41` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_41` | Mass fraction | Dimethylsulphide  
`SO4_41` | Mass fraction | Sulphate aerosol  
`DU002_41` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_41` | Pa | Surface Pressure  
`SS003_41` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_41` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_41` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_41` | Mass fraction | Hydrophilic Black Carbon  
`MSA_41` | Mass fraction | Methanesulphonic acid  
`SS001_41` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_42` | kg/m^3 | Air density  
`SO2_42` | Mass fraction | Sulphur dioxide  
`DELP_42` | Pa | Pressure thickness  
`SS004_42` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_42` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_42` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_42` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_42` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_42` | Mass fraction | Hydrophobic Black Carbon  
`SS002_42` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_42` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_42` | Mass fraction | Dimethylsulphide  
`SO4_42` | Mass fraction | Sulphate aerosol  
`DU002_42` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_42` | Pa | Surface Pressure  
`SS003_42` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_42` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_42` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_42` | Mass fraction | Hydrophilic Black Carbon  
`MSA_42` | Mass fraction | Methanesulphonic acid  
`SS001_42` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_43` | kg/m^3 | Air density  
`SO2_43` | Mass fraction | Sulphur dioxide  
`DELP_43` | Pa | Pressure thickness  
`SS004_43` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_43` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_43` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_43` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_43` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_43` | Mass fraction | Hydrophobic Black Carbon  
`SS002_43` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_43` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_43` | Mass fraction | Dimethylsulphide  
`SO4_43` | Mass fraction | Sulphate aerosol  
`DU002_43` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_43` | Pa | Surface Pressure  
`SS003_43` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_43` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_43` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_43` | Mass fraction | Hydrophilic Black Carbon  
`MSA_43` | Mass fraction | Methanesulphonic acid  
`SS001_43` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_44` | kg/m^3 | Air density  
`SO2_44` | Mass fraction | Sulphur dioxide  
`DELP_44` | Pa | Pressure thickness  
`SS004_44` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_44` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_44` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_44` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_44` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_44` | Mass fraction | Hydrophobic Black Carbon  
`SS002_44` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_44` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_44` | Mass fraction | Dimethylsulphide  
`SO4_44` | Mass fraction | Sulphate aerosol  
`DU002_44` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_44` | Pa | Surface Pressure  
`SS003_44` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_44` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_44` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_44` | Mass fraction | Hydrophilic Black Carbon  
`MSA_44` | Mass fraction | Methanesulphonic acid  
`SS001_44` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_45` | kg/m^3 | Air density  
`SO2_45` | Mass fraction | Sulphur dioxide  
`DELP_45` | Pa | Pressure thickness  
`SS004_45` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_45` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_45` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_45` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_45` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_45` | Mass fraction | Hydrophobic Black Carbon  
`SS002_45` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_45` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_45` | Mass fraction | Dimethylsulphide  
`SO4_45` | Mass fraction | Sulphate aerosol  
`DU002_45` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_45` | Pa | Surface Pressure  
`SS003_45` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_45` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_45` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_45` | Mass fraction | Hydrophilic Black Carbon  
`MSA_45` | Mass fraction | Methanesulphonic acid  
`SS001_45` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_46` | kg/m^3 | Air density  
`SO2_46` | Mass fraction | Sulphur dioxide  
`DELP_46` | Pa | Pressure thickness  
`SS004_46` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_46` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_46` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_46` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_46` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_46` | Mass fraction | Hydrophobic Black Carbon  
`SS002_46` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_46` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_46` | Mass fraction | Dimethylsulphide  
`SO4_46` | Mass fraction | Sulphate aerosol  
`DU002_46` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_46` | Pa | Surface Pressure  
`SS003_46` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_46` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_46` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_46` | Mass fraction | Hydrophilic Black Carbon  
`MSA_46` | Mass fraction | Methanesulphonic acid  
`SS001_46` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_47` | kg/m^3 | Air density  
`SO2_47` | Mass fraction | Sulphur dioxide  
`DELP_47` | Pa | Pressure thickness  
`SS004_47` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_47` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_47` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_47` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_47` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_47` | Mass fraction | Hydrophobic Black Carbon  
`SS002_47` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_47` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_47` | Mass fraction | Dimethylsulphide  
`SO4_47` | Mass fraction | Sulphate aerosol  
`DU002_47` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_47` | Pa | Surface Pressure  
`SS003_47` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_47` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_47` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_47` | Mass fraction | Hydrophilic Black Carbon  
`MSA_47` | Mass fraction | Methanesulphonic acid  
`SS001_47` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_48` | kg/m^3 | Air density  
`SO2_48` | Mass fraction | Sulphur dioxide  
`DELP_48` | Pa | Pressure thickness  
`SS004_48` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_48` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_48` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_48` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_48` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_48` | Mass fraction | Hydrophobic Black Carbon  
`SS002_48` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_48` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_48` | Mass fraction | Dimethylsulphide  
`SO4_48` | Mass fraction | Sulphate aerosol  
`DU002_48` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_48` | Pa | Surface Pressure  
`SS003_48` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_48` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_48` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_48` | Mass fraction | Hydrophilic Black Carbon  
`MSA_48` | Mass fraction | Methanesulphonic acid  
`SS001_48` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_49` | kg/m^3 | Air density  
`SO2_49` | Mass fraction | Sulphur dioxide  
`DELP_49` | Pa | Pressure thickness  
`SS004_49` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_49` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_49` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_49` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_49` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_49` | Mass fraction | Hydrophobic Black Carbon  
`SS002_49` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_49` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_49` | Mass fraction | Dimethylsulphide  
`SO4_49` | Mass fraction | Sulphate aerosol  
`DU002_49` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_49` | Pa | Surface Pressure  
`SS003_49` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_49` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_49` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_49` | Mass fraction | Hydrophilic Black Carbon  
`MSA_49` | Mass fraction | Methanesulphonic acid  
`SS001_49` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_50` | kg/m^3 | Air density  
`SO2_50` | Mass fraction | Sulphur dioxide  
`DELP_50` | Pa | Pressure thickness  
`SS004_50` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_50` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_50` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_50` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_50` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_50` | Mass fraction | Hydrophobic Black Carbon  
`SS002_50` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_50` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_50` | Mass fraction | Dimethylsulphide  
`SO4_50` | Mass fraction | Sulphate aerosol  
`DU002_50` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_50` | Pa | Surface Pressure  
`SS003_50` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_50` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_50` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_50` | Mass fraction | Hydrophilic Black Carbon  
`MSA_50` | Mass fraction | Methanesulphonic acid  
`SS001_50` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_51` | kg/m^3 | Air density  
`SO2_51` | Mass fraction | Sulphur dioxide  
`DELP_51` | Pa | Pressure thickness  
`SS004_51` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_51` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_51` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_51` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_51` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_51` | Mass fraction | Hydrophobic Black Carbon  
`SS002_51` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_51` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_51` | Mass fraction | Dimethylsulphide  
`SO4_51` | Mass fraction | Sulphate aerosol  
`DU002_51` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_51` | Pa | Surface Pressure  
`SS003_51` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_51` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_51` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_51` | Mass fraction | Hydrophilic Black Carbon  
`MSA_51` | Mass fraction | Methanesulphonic acid  
`SS001_51` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_52` | kg/m^3 | Air density  
`SO2_52` | Mass fraction | Sulphur dioxide  
`DELP_52` | Pa | Pressure thickness  
`SS004_52` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_52` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_52` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_52` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_52` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_52` | Mass fraction | Hydrophobic Black Carbon  
`SS002_52` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_52` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_52` | Mass fraction | Dimethylsulphide  
`SO4_52` | Mass fraction | Sulphate aerosol  
`DU002_52` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_52` | Pa | Surface Pressure  
`SS003_52` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_52` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_52` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_52` | Mass fraction | Hydrophilic Black Carbon  
`MSA_52` | Mass fraction | Methanesulphonic acid  
`SS001_52` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_53` | kg/m^3 | Air density  
`SO2_53` | Mass fraction | Sulphur dioxide  
`DELP_53` | Pa | Pressure thickness  
`SS004_53` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_53` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_53` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_53` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_53` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_53` | Mass fraction | Hydrophobic Black Carbon  
`SS002_53` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_53` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_53` | Mass fraction | Dimethylsulphide  
`SO4_53` | Mass fraction | Sulphate aerosol  
`DU002_53` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_53` | Pa | Surface Pressure  
`SS003_53` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_53` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_53` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_53` | Mass fraction | Hydrophilic Black Carbon  
`MSA_53` | Mass fraction | Methanesulphonic acid  
`SS001_53` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_54` | kg/m^3 | Air density  
`SO2_54` | Mass fraction | Sulphur dioxide  
`DELP_54` | Pa | Pressure thickness  
`SS004_54` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_54` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_54` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_54` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_54` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_54` | Mass fraction | Hydrophobic Black Carbon  
`SS002_54` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_54` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_54` | Mass fraction | Dimethylsulphide  
`SO4_54` | Mass fraction | Sulphate aerosol  
`DU002_54` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_54` | Pa | Surface Pressure  
`SS003_54` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_54` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_54` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_54` | Mass fraction | Hydrophilic Black Carbon  
`MSA_54` | Mass fraction | Methanesulphonic acid  
`SS001_54` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_55` | kg/m^3 | Air density  
`SO2_55` | Mass fraction | Sulphur dioxide  
`DELP_55` | Pa | Pressure thickness  
`SS004_55` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_55` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_55` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_55` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_55` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_55` | Mass fraction | Hydrophobic Black Carbon  
`SS002_55` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_55` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_55` | Mass fraction | Dimethylsulphide  
`SO4_55` | Mass fraction | Sulphate aerosol  
`DU002_55` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_55` | Pa | Surface Pressure  
`SS003_55` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_55` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_55` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_55` | Mass fraction | Hydrophilic Black Carbon  
`MSA_55` | Mass fraction | Methanesulphonic acid  
`SS001_55` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_56` | kg/m^3 | Air density  
`SO2_56` | Mass fraction | Sulphur dioxide  
`DELP_56` | Pa | Pressure thickness  
`SS004_56` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_56` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_56` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_56` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_56` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_56` | Mass fraction | Hydrophobic Black Carbon  
`SS002_56` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_56` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_56` | Mass fraction | Dimethylsulphide  
`SO4_56` | Mass fraction | Sulphate aerosol  
`DU002_56` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_56` | Pa | Surface Pressure  
`SS003_56` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_56` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_56` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_56` | Mass fraction | Hydrophilic Black Carbon  
`MSA_56` | Mass fraction | Methanesulphonic acid  
`SS001_56` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_57` | kg/m^3 | Air density  
`SO2_57` | Mass fraction | Sulphur dioxide  
`DELP_57` | Pa | Pressure thickness  
`SS004_57` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_57` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_57` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_57` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_57` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_57` | Mass fraction | Hydrophobic Black Carbon  
`SS002_57` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_57` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_57` | Mass fraction | Dimethylsulphide  
`SO4_57` | Mass fraction | Sulphate aerosol  
`DU002_57` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_57` | Pa | Surface Pressure  
`SS003_57` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_57` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_57` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_57` | Mass fraction | Hydrophilic Black Carbon  
`MSA_57` | Mass fraction | Methanesulphonic acid  
`SS001_57` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_58` | kg/m^3 | Air density  
`SO2_58` | Mass fraction | Sulphur dioxide  
`DELP_58` | Pa | Pressure thickness  
`SS004_58` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_58` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_58` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_58` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_58` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_58` | Mass fraction | Hydrophobic Black Carbon  
`SS002_58` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_58` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_58` | Mass fraction | Dimethylsulphide  
`SO4_58` | Mass fraction | Sulphate aerosol  
`DU002_58` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_58` | Pa | Surface Pressure  
`SS003_58` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_58` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_58` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_58` | Mass fraction | Hydrophilic Black Carbon  
`MSA_58` | Mass fraction | Methanesulphonic acid  
`SS001_58` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_59` | kg/m^3 | Air density  
`SO2_59` | Mass fraction | Sulphur dioxide  
`DELP_59` | Pa | Pressure thickness  
`SS004_59` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_59` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_59` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_59` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_59` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_59` | Mass fraction | Hydrophobic Black Carbon  
`SS002_59` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_59` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_59` | Mass fraction | Dimethylsulphide  
`SO4_59` | Mass fraction | Sulphate aerosol  
`DU002_59` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_59` | Pa | Surface Pressure  
`SS003_59` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_59` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_59` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_59` | Mass fraction | Hydrophilic Black Carbon  
`MSA_59` | Mass fraction | Methanesulphonic acid  
`SS001_59` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_60` | kg/m^3 | Air density  
`SO2_60` | Mass fraction | Sulphur dioxide  
`DELP_60` | Pa | Pressure thickness  
`SS004_60` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_60` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_60` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_60` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_60` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_60` | Mass fraction | Hydrophobic Black Carbon  
`SS002_60` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_60` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_60` | Mass fraction | Dimethylsulphide  
`SO4_60` | Mass fraction | Sulphate aerosol  
`DU002_60` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_60` | Pa | Surface Pressure  
`SS003_60` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_60` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_60` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_60` | Mass fraction | Hydrophilic Black Carbon  
`MSA_60` | Mass fraction | Methanesulphonic acid  
`SS001_60` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_61` | kg/m^3 | Air density  
`SO2_61` | Mass fraction | Sulphur dioxide  
`DELP_61` | Pa | Pressure thickness  
`SS004_61` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_61` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_61` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_61` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_61` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_61` | Mass fraction | Hydrophobic Black Carbon  
`SS002_61` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_61` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_61` | Mass fraction | Dimethylsulphide  
`SO4_61` | Mass fraction | Sulphate aerosol  
`DU002_61` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_61` | Pa | Surface Pressure  
`SS003_61` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_61` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_61` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_61` | Mass fraction | Hydrophilic Black Carbon  
`MSA_61` | Mass fraction | Methanesulphonic acid  
`SS001_61` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_62` | kg/m^3 | Air density  
`SO2_62` | Mass fraction | Sulphur dioxide  
`DELP_62` | Pa | Pressure thickness  
`SS004_62` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_62` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_62` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_62` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_62` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_62` | Mass fraction | Hydrophobic Black Carbon  
`SS002_62` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_62` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_62` | Mass fraction | Dimethylsulphide  
`SO4_62` | Mass fraction | Sulphate aerosol  
`DU002_62` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_62` | Pa | Surface Pressure  
`SS003_62` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_62` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_62` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_62` | Mass fraction | Hydrophilic Black Carbon  
`MSA_62` | Mass fraction | Methanesulphonic acid  
`SS001_62` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_63` | kg/m^3 | Air density  
`SO2_63` | Mass fraction | Sulphur dioxide  
`DELP_63` | Pa | Pressure thickness  
`SS004_63` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_63` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_63` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_63` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_63` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_63` | Mass fraction | Hydrophobic Black Carbon  
`SS002_63` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_63` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_63` | Mass fraction | Dimethylsulphide  
`SO4_63` | Mass fraction | Sulphate aerosol  
`DU002_63` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_63` | Pa | Surface Pressure  
`SS003_63` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_63` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_63` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_63` | Mass fraction | Hydrophilic Black Carbon  
`MSA_63` | Mass fraction | Methanesulphonic acid  
`SS001_63` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_64` | kg/m^3 | Air density  
`SO2_64` | Mass fraction | Sulphur dioxide  
`DELP_64` | Pa | Pressure thickness  
`SS004_64` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_64` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_64` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_64` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_64` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_64` | Mass fraction | Hydrophobic Black Carbon  
`SS002_64` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_64` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_64` | Mass fraction | Dimethylsulphide  
`SO4_64` | Mass fraction | Sulphate aerosol  
`DU002_64` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_64` | Pa | Surface Pressure  
`SS003_64` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_64` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_64` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_64` | Mass fraction | Hydrophilic Black Carbon  
`MSA_64` | Mass fraction | Methanesulphonic acid  
`SS001_64` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_65` | kg/m^3 | Air density  
`SO2_65` | Mass fraction | Sulphur dioxide  
`DELP_65` | Pa | Pressure thickness  
`SS004_65` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_65` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_65` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_65` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_65` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_65` | Mass fraction | Hydrophobic Black Carbon  
`SS002_65` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_65` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_65` | Mass fraction | Dimethylsulphide  
`SO4_65` | Mass fraction | Sulphate aerosol  
`DU002_65` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_65` | Pa | Surface Pressure  
`SS003_65` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_65` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_65` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_65` | Mass fraction | Hydrophilic Black Carbon  
`MSA_65` | Mass fraction | Methanesulphonic acid  
`SS001_65` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_66` | kg/m^3 | Air density  
`SO2_66` | Mass fraction | Sulphur dioxide  
`DELP_66` | Pa | Pressure thickness  
`SS004_66` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_66` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_66` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_66` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_66` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_66` | Mass fraction | Hydrophobic Black Carbon  
`SS002_66` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_66` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_66` | Mass fraction | Dimethylsulphide  
`SO4_66` | Mass fraction | Sulphate aerosol  
`DU002_66` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_66` | Pa | Surface Pressure  
`SS003_66` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_66` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_66` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_66` | Mass fraction | Hydrophilic Black Carbon  
`MSA_66` | Mass fraction | Methanesulphonic acid  
`SS001_66` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_67` | kg/m^3 | Air density  
`SO2_67` | Mass fraction | Sulphur dioxide  
`DELP_67` | Pa | Pressure thickness  
`SS004_67` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_67` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_67` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_67` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_67` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_67` | Mass fraction | Hydrophobic Black Carbon  
`SS002_67` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_67` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_67` | Mass fraction | Dimethylsulphide  
`SO4_67` | Mass fraction | Sulphate aerosol  
`DU002_67` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_67` | Pa | Surface Pressure  
`SS003_67` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_67` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_67` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_67` | Mass fraction | Hydrophilic Black Carbon  
`MSA_67` | Mass fraction | Methanesulphonic acid  
`SS001_67` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_68` | kg/m^3 | Air density  
`SO2_68` | Mass fraction | Sulphur dioxide  
`DELP_68` | Pa | Pressure thickness  
`SS004_68` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_68` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_68` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_68` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_68` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_68` | Mass fraction | Hydrophobic Black Carbon  
`SS002_68` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_68` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_68` | Mass fraction | Dimethylsulphide  
`SO4_68` | Mass fraction | Sulphate aerosol  
`DU002_68` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_68` | Pa | Surface Pressure  
`SS003_68` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_68` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_68` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_68` | Mass fraction | Hydrophilic Black Carbon  
`MSA_68` | Mass fraction | Methanesulphonic acid  
`SS001_68` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_69` | kg/m^3 | Air density  
`SO2_69` | Mass fraction | Sulphur dioxide  
`DELP_69` | Pa | Pressure thickness  
`SS004_69` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_69` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_69` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_69` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_69` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_69` | Mass fraction | Hydrophobic Black Carbon  
`SS002_69` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_69` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_69` | Mass fraction | Dimethylsulphide  
`SO4_69` | Mass fraction | Sulphate aerosol  
`DU002_69` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_69` | Pa | Surface Pressure  
`SS003_69` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_69` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_69` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_69` | Mass fraction | Hydrophilic Black Carbon  
`MSA_69` | Mass fraction | Methanesulphonic acid  
`SS001_69` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_70` | kg/m^3 | Air density  
`SO2_70` | Mass fraction | Sulphur dioxide  
`DELP_70` | Pa | Pressure thickness  
`SS004_70` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_70` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_70` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_70` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_70` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_70` | Mass fraction | Hydrophobic Black Carbon  
`SS002_70` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_70` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_70` | Mass fraction | Dimethylsulphide  
`SO4_70` | Mass fraction | Sulphate aerosol  
`DU002_70` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_70` | Pa | Surface Pressure  
`SS003_70` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_70` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_70` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_70` | Mass fraction | Hydrophilic Black Carbon  
`MSA_70` | Mass fraction | Methanesulphonic acid  
`SS001_70` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_71` | kg/m^3 | Air density  
`SO2_71` | Mass fraction | Sulphur dioxide  
`DELP_71` | Pa | Pressure thickness  
`SS004_71` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_71` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_71` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_71` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_71` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_71` | Mass fraction | Hydrophobic Black Carbon  
`SS002_71` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_71` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_71` | Mass fraction | Dimethylsulphide  
`SO4_71` | Mass fraction | Sulphate aerosol  
`DU002_71` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_71` | Pa | Surface Pressure  
`SS003_71` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_71` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_71` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_71` | Mass fraction | Hydrophilic Black Carbon  
`MSA_71` | Mass fraction | Methanesulphonic acid  
`SS001_71` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`AIRDENS_72` | kg/m^3 | Air density  
`SO2_72` | Mass fraction | Sulphur dioxide  
`DELP_72` | Pa | Pressure thickness  
`SS004_72` | Mass fraction | Sea Salt Mixing Ratio (bin 004)  
`DU005_72` | Mass fraction | Dust Mixing Ratio (bin 005)  
`DU004_72` | Mass fraction | Dust Mixing Ratio (bin 004)  
`SS005_72` | Mass fraction | Sea Salt Mixing Ratio (bin 005)  
`OCPHILIC_72` | Mass fraction | Hydrophilic Organic Carbon (Particulate Matter)  
`BCPHOBIC_72` | Mass fraction | Hydrophobic Black Carbon  
`SS002_72` | Mass fraction | Sea Salt Mixing Ratio (bin 002)  
`DU003_72` | Mass fraction | Dust Mixing Ratio (bin 003)  
`DMS_72` | Mass fraction | Dimethylsulphide  
`SO4_72` | Mass fraction | Sulphate aerosol  
`DU002_72` | Mass fraction | Dust Mixing Ratio (bin 002)  
`PS_72` | Pa | Surface Pressure  
`SS003_72` | Mass fraction | Sea Salt Mixing Ratio (bin 003)  
`DU001_72` | Mass fraction | Dust Mixing Ratio (bin 001)  
`OCPHOBIC_72` | Mass fraction | Hydrophobic Organic Carbon (Particulate Matter)  
`BCPHILIC_72` | Mass fraction | Hydrophilic Black Carbon  
`MSA_72` | Mass fraction | Methanesulphonic acid  
`SS001_72` | Mass fraction | Sea Salt Mixing Ratio (bin 001)  
`LWI` | land(1)_water(0)_ice(2)_flag  
`RH` | relative_humidity_after_moist  
**Terms of Use**
NASA promotes the full and open sharing of all data with research and applications communities, private industry, academia, and the general public.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('NASA/GSFC/MERRA/aer_nv/2')
.filter(ee.Filter.date('1985-02-01','1985-02-02'));
dataset=dataset.first()
varpressure_thickness=dataset.select('DELP_72');
varbccVis={
min:1188.8580904647688,
max:1761.7886613672472,
palette:['001137','01abab','e7eb05','620500']
};
Map.setCenter(-95.62,39.91,2);
Map.addLayer(pressure_thickness,bccVis);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/NASA/NASA_GSFC_MERRA_aer_nv_2)
[ MERRA-2 M2I3NVAER: Aerosol Mixing Ratio V5.12.4 ](https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2)
M2I3NVAER (or inst3_3d_aer_Nv) is an instantaneous 3-dimensional 3-hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2). This collection consists of assimilations of aerosol mixing ratio parameters at 72 model layers, such as dust, sulphur dioxide, sea salt, black carbon, and organic carbon. The data field …
NASA/GSFC/MERRA/aer_nv/2, aerosol,atmosphere,dust,mass,merra,nasa,sea-salt,so2,so4 
1980-01-01T00:00:00Z/2025-03-01T21:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://disc.gsfc.nasa.gov/datasets/M2I3NVAER_5.12.4/summary)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/NASA_GSFC_MERRA_aer_nv_2)


