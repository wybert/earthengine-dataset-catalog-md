 
#  LANDFIRE BPS (Biophysical Settings) v1.4.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDFIRE/Vegetation/BPS/v1_4_0](https://developers.google.com/earth-engine/datasets/images/LANDFIRE/LANDFIRE_Vegetation_BPS_v1_4_0_sample.png) 

Dataset Availability
    2014-09-01T00:00:00Z–2014-09-01T00:00:00Z 

Dataset Provider
     [ U.S. Department of Agriculture's (USDA), U.S. Forest Service (USFS), U.S. Department of the Interior's Geological Survey (USGS), and The Nature Conservancy. ](https://landfire.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDFIRE/Vegetation/BPS/v1_4_0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Vegetation_BPS_v1_4_0) 

Tags
     [doi](https://developers.google.com/earth-engine/datasets/tags/doi) [fire](https://developers.google.com/earth-engine/datasets/tags/fire) [forest-biomass](https://developers.google.com/earth-engine/datasets/tags/forest-biomass) [landfire](https://developers.google.com/earth-engine/datasets/tags/landfire) [nature-conservancy](https://developers.google.com/earth-engine/datasets/tags/nature-conservancy) [usda](https://developers.google.com/earth-engine/datasets/tags/usda) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs) [vegetation](https://developers.google.com/earth-engine/datasets/tags/vegetation) [wildfire](https://developers.google.com/earth-engine/datasets/tags/wildfire)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#citations) More
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.
LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees.
LANDFIRE's (LF) Biophysical Settings (BPS) represents the vegetation that may have been dominant on the landscape prior to Euro-American settlement and is based on both the current biophysical environment and an approximation of the historical disturbance regime. Map units are based on NatureServe's Ecological Systems classification and represent the natural plant communities that may have been present during the reference period. Each BPS map unit is matched with a model of vegetation succession, and both serve as key inputs to the LANDSUM landscape succession model. The actual time period for this data set is a composite of both the historical context provided by the fire regime and vegetation dynamics models and the more recent field and geospatial inputs used to create it. LF's current BPS is unchanged from LF National's BPS except for updates made to water, barren, and snow classes (additions or removal), so that non-vegetated cover types within the BPS product matches LF existing vegetation and fuel products. With the final release of LF Remap for CONUS in mid to late 2020, the LF Remap BPS product will include the following as attributes: Mean Fire Return Interval (MFRI), Percent of Low-severity Fire (PLS), Percent of Mixed-severity Fire (PMS), Percent of Replacement-severity Fire (PRS), and Fire Regime Groups (FRG), so that the linkage of these characteristics to BPS is maintained. LF uses BPS to depict reference conditions of vegetation across landscapes.
The LANDIFRE Vegetation datasets include:
  * Biophysical Settings (BPS)
  * Environmental Site Potential (ESP)
  * Existing Vegetation Canopy Cover (EVC)
  * Existing Vegetation Height (EVH).
  * Existing Vegetation Type (EVT) These layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees.


**Pixel Size** 30 meters 
**Bands**
Name | Description  
---|---  
`BPS` | Biophysical Settings  
**BPS Class Table**
Value | Color | Description  
---|---|---  
11 | #005ce6 | Open Water  
12 | #ffffff | PerennialIce/Snow  
31 | #000000 | Barren-Rock/Sand/Clay  
381 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
383 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
384 | #ffffbe | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
385 | #ffffbe | North American Warm Desert Sparsely Vegetated Systems  
386 | #cdcd66 | Western Great Plains Shortgrass Prairie  
387 | #89cd66 | Western Great Plains Foothill and Piedmont Grassland  
388 | #848cc8 | Wyoming Basins Dwarf Sagebrush Shrubland and Steppe  
389 | #86db18 | Southern Colorado Plateau Sand Shrubland  
390 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
391 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
392 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
393 | #e54563 | Chihuahuan Stabilized Coppice Dune and Sand Flat Scrub  
394 | #349bcf | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
395 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
396 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
397 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
398 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
399 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe - Mountain Big Sagebrush  
400 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
401 | #0bbe7f | Inter-Mountain Basins Mat Saltbush Shrubland  
402 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
403 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
404 | #349bcf | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
405 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
406 | #86db18 | Southern Colorado Plateau Sand Shrubland  
407 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
408 | #fff5d7 | Mediterranean California Sparsely Vegetated Systems  
409 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
410 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
411 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
412 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
413 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
414 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
415 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
416 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
417 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Ponderosa Pine-Douglas-fir  
418 | #9624b5 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Larch  
419 | #e60508 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Grand Fir  
420 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
421 | #5f93e5 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest  
422 | #129054 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest - Cedar Groves  
423 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna  
424 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
425 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
426 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
427 | #beffe8 | Columbia Plateau Scabland Shrubland  
428 | #13765c | Rocky Mountain Alpine Dwarf-Shrubland  
429 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
430 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
431 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
432 | #897044 | Inter-Mountain Basins Juniper Savanna  
433 | #ebdaea | Columbia Plateau Steppe and Grassland  
434 | #848cad | Columbia Plateau Low Sagebrush Steppe  
435 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
436 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
437 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
438 | #cdf57a | Columbia Basin Foothill and Canyon Dry Grassland  
439 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
440 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
441 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
442 | #dcdc00 | Columbia Basin Palouse Prairie  
443 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
444 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
445 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
446 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
447 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
448 | #444f89 | Northern Rocky Mountain Conifer Swamp  
449 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
450 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
451 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
452 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
453 | #0bcaaa | Northwestern Great Plains Aspen Forest and Parkland  
454 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
455 | #734c00 | Great Basin Pinyon-Juniper Woodland  
456 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Ponderosa Pine-Douglas-fir  
457 | #9624b5 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Larch  
458 | #e60508 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Grand Fir  
459 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
460 | #5f93e5 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest  
461 | #129054 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest - Cedar Groves  
462 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
463 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna  
464 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
465 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
466 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
467 | #13765c | Rocky Mountain Alpine Dwarf-Shrubland  
468 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
469 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
470 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
471 | #897044 | Inter-Mountain Basins Juniper Savanna  
472 | #848cad | Columbia Plateau Low Sagebrush Steppe  
473 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
474 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
475 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
476 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
477 | #828282 | Rocky Mountain Alpine Fell-Field  
478 | #5d2b1d | Rocky Mountain Alpine Turf  
479 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
480 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
481 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
482 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
483 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
484 | #444f89 | Northern Rocky Mountain Conifer Swamp  
485 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
486 | #ff7800 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland - Fire-maintained Savanna  
487 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
488 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
489 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
490 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
491 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
492 | #734c00 | Great Basin Pinyon-Juniper Woodland  
493 | #0e2e39 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
494 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
495 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
496 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
497 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
498 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
499 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
500 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
501 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
502 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
503 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
504 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
505 | #b00663 | Sonoran Mid-Elevation Desert Scrub  
506 | #86db18 | Southern Colorado Plateau Sand Shrubland  
507 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
508 | #aefaff | Great Basin Semi-Desert Chaparral  
509 | #adfad3 | Mogollon Chaparral  
510 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
511 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
512 | #e9d6f5 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
513 | #897044 | Inter-Mountain Basins Juniper Savanna  
514 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
515 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
516 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
517 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
518 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
519 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
520 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
521 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
522 | #7ba075 | North American Warm Desert Riparian Systems  
523 | #54a075 | North American Warm Desert Riparian Systems - Stringers  
524 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
525 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
526 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
527 | #734c00 | Great Basin Pinyon-Juniper Woodland  
528 | #00a784 | Madrean Encinal  
529 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
530 | #a06a1f | Madrean Pinyon-Juniper Woodland  
531 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
532 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
533 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
534 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
535 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
536 | #ffa000 | Sonoran Granite Outcrop Desert Scrub  
537 | #b00663 | Sonoran Mid-Elevation Desert Scrub  
538 | #adfad3 | Mogollon Chaparral  
539 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
540 | #e9d6f5 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
541 | #897044 | Inter-Mountain Basins Juniper Savanna  
542 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
543 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
544 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
545 | #7ba075 | North American Warm Desert Riparian Systems  
546 | #54a075 | North American Warm Desert Riparian Systems - Stringers  
547 | #ff7878 | North Pacific Oak Woodland  
548 | #a80000 | California Coastal Redwood Forest  
549 | #f5b595 | Klamath-Siskiyou Lower Montane Serpentine Mixed Conifer Woodland  
550 | #ed8b5a | Klamath-Siskiyou Upper Montane Serpentine Mixed Conifer Woodland  
551 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
552 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
553 | #dc6464 | Mediterranean California Mixed Oak Woodland  
554 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
555 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
556 | #ff3b7f | Mediterranean California Red Fir Forest  
557 | #e2c2a2 | Mediterranean California Subalpine Woodland  
558 | #aae3aa | North Pacific Maritime Mesic-Wet Douglas-fir-Western Hemlock Forest  
559 | #a4c48f | Mediterranean California Mixed Evergreen Forest  
560 | #ff8500 | Northern California Mesic Subalpine Woodland  
561 | #c8aa8c | California Maritime Chaparral  
562 | #c8be55 | California Mesic Chaparral  
563 | #d2aa32 | California Montane Woodland and Chaparral  
564 | #ac69cd | California Xeric Serpentine Chaparral  
565 | #f5f6af | Northern and Central California Dry-Mesic Chaparral  
566 | #449170 | California Coastal Live Oak Woodland and Savanna  
567 | #b3ffe8 | California Lower Montane Blue Oak-Foothill Pine Woodland and Savanna  
568 | #94c2a8 | Northern California Coastal Scrub  
569 | #cdbcd6 | California Mesic Serpentine Grassland  
570 | #edf0d8 | California Northern Coastal Grassland  
571 | #00bcff | Mediterranean California Subalpine Meadow  
572 | #c7e69e | North Pacific Montane Grassland  
573 | #4196a7 | California Montane Riparian Systems  
574 | #444f7d | Pacific Coastal Marsh Systems  
575 | #d2eb00 | Klamath-Siskiyou Xeromorphic Serpentine Savanna and Chaparral  
576 | #edcf00 | California Coastal Closed-Cone Conifer Forest and Woodland  
577 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
578 | #fff5d7 | Mediterranean California Sparsely Vegetated Systems  
579 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
580 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
581 | #734c00 | Great Basin Pinyon-Juniper Woodland  
582 | #0e2e39 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
583 | #f5b595 | Klamath-Siskiyou Lower Montane Serpentine Mixed Conifer Woodland  
584 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
585 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
586 | #dc6464 | Mediterranean California Mixed Oak Woodland  
587 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
588 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
589 | #ff3b7f | Mediterranean California Red Fir Forest - Cascades  
590 | #ff9197 | Mediterranean California Red Fir Forest - Southern Sierra  
591 | #e2c2a2 | Mediterranean California Subalpine Woodland  
592 | #73004c | Mediterranean California Mesic Serpentine Woodland and Chaparral  
593 | #a4c48f | Mediterranean California Mixed Evergreen Forest  
594 | #ff8500 | Northern California Mesic Subalpine Woodland  
595 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
596 | #7fea00 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland - Wet  
597 | #b3ff00 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland - Dry  
598 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
599 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
600 | #8c8c8c | Mediterranean California Alpine Fell-Field  
601 | #197d5f | Sierra Nevada Alpine Dwarf-Shrubland  
602 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
603 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
604 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
605 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
606 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
607 | #c8be55 | California Mesic Chaparral  
608 | #d2aa32 | California Montane Woodland and Chaparral  
609 | #aefaff | Great Basin Semi-Desert Chaparral  
610 | #f5f6af | Northern and Central California Dry-Mesic Chaparral  
611 | #b3ffe8 | California Lower Montane Blue Oak-Foothill Pine Woodland and Savanna  
612 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
613 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
614 | #642b1d | Mediterranean California Alpine Dry Tundra  
615 | #00bcff | Mediterranean California Subalpine Meadow  
616 | #c7e69e | North Pacific Montane Grassland  
617 | #4196a7 | California Montane Riparian Systems  
618 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
619 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
620 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
621 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
622 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
623 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
624 | #734c00 | Great Basin Pinyon-Juniper Woodland  
625 | #0e2e39 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
626 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
627 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
628 | #5f93e5 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest  
629 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Mesic  
630 | #a87800 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Xeric  
631 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
632 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
633 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
634 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
635 | #beffe8 | Columbia Plateau Scabland Shrubland  
636 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
637 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
638 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
639 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
640 | #ebdaea | Columbia Plateau Steppe and Grassland  
641 | #848cad | Columbia Plateau Low Sagebrush Steppe  
642 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
643 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
644 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
645 | #cdf57a | Columbia Basin Foothill and Canyon Dry Grassland  
646 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
647 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
648 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
649 | #dcdc00 | Columbia Basin Palouse Prairie  
650 | #828282 | Rocky Mountain Alpine Fell-Field  
651 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
652 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
653 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
654 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
655 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
656 | #444f89 | Northern Rocky Mountain Conifer Swamp  
657 | #ff7800 | Northern Rocky Mountain Foothill Conifer Wooded Steppe  
658 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
659 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
660 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
661 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
662 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
663 | #5f93e5 | Northern Rocky Mountain Mesic Montane Mixed Conifer Forest  
664 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Mesic  
665 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
666 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
667 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
668 | #beffe8 | Columbia Plateau Scabland Shrubland  
669 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
670 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
671 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
672 | #ebdaea | Columbia Plateau Steppe and Grassland  
673 | #848cad | Columbia Plateau Low Sagebrush Steppe  
674 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
675 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
676 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
677 | #cdf57a | Columbia Basin Foothill and Canyon Dry Grassland  
678 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
679 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
680 | #dcdc00 | Columbia Basin Palouse Prairie  
681 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
682 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
683 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
684 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
685 | #ff7800 | Northern Rocky Mountain Foothill Conifer Wooded Steppe  
686 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
687 | #ffd37f | Rocky Mountain Bigtooth Maple Ravine Woodland  
688 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
689 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
690 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
691 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
692 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
693 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
694 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
695 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
696 | #13765c | Rocky Mountain Alpine Dwarf-Shrubland  
697 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland - Basin Big Sagebrush  
698 | #ffa3b4 | Inter-Mountain Basins Big Sagebrush Shrubland - Wyoming Big Sagebrush  
699 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
700 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
701 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
702 | #897044 | Inter-Mountain Basins Juniper Savanna  
703 | #848cad | Columbia Plateau Low Sagebrush Steppe  
704 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
705 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
706 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
707 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
708 | #828282 | Rocky Mountain Alpine Fell-Field  
709 | #5d2b1d | Rocky Mountain Alpine Turf  
710 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
711 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
712 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
713 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
714 | #444f89 | Northern Rocky Mountain Conifer Swamp  
715 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
716 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
717 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
718 | #fff0be | North Pacific Sparsely Vegetated Systems  
719 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
720 | #ff7878 | North Pacific Oak Woodland  
721 | #5f9eb4 | East Cascades Mesic Montane Mixed-Conifer Forest and Woodland  
722 | #894444 | North Pacific Dry Douglas-fir(-Madrone) Forest and Woodland  
723 | #d57fe3 | North Pacific Hypermaritime Sitka Spruce Forest  
724 | #defcde | North Pacific Maritime Dry-Mesic Douglas-fir-Western Hemlock Forest  
725 | #ff9100 | North Pacific Maritime Mesic Subalpine Parkland  
726 | #aae3aa | North Pacific Maritime Mesic-Wet Douglas-fir-Western Hemlock Forest  
727 | #a5e6fc | North Pacific Mountain Hemlock Forest - Wet  
728 | #72d0f2 | North Pacific Mountain Hemlock Forest - Xeric  
729 | #f9bdfc | North Pacific Mesic Western Hemlock-Silver Fir Forest  
730 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
731 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
732 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Mesic  
733 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
734 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
735 | #cd6666 | East Cascades Oak-Ponderosa Pine Forest and Woodland  
736 | #fff7a3 | North Pacific Broadleaf Landslide Forest and Shrubland  
737 | #beffe8 | Columbia Plateau Scabland Shrubland  
738 | #147d7d | North Pacific Dry and Mesic Alpine Dwarf-Shrubland or Fell-field or Meadow  
739 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
740 | #fffa00 | North Pacific Avalanche Chute Shrubland  
741 | #ff00c5 | North Pacific Montane Shrubland  
742 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
743 | #d7d79e | Willamette Valley Upland Prairie and Savanna  
744 | #ebdaea | Columbia Plateau Steppe and Grassland  
745 | #848cad | Columbia Plateau Low Sagebrush Steppe  
746 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
747 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
748 | #c7e69e | North Pacific Montane Grassland  
749 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
750 | #b1b37d | North Pacific Lowland Riparian Forest and Shrubland  
751 | #465589 | North Pacific Swamp Systems  
752 | #bccfd4 | North Pacific Montane Riparian Woodland and Shrubland - Wet  
753 | #acc2c1 | North Pacific Montane Riparian Woodland and Shrubland - Dry  
754 | #ff7800 | Northern Rocky Mountain Foothill Conifer Wooded Steppe  
755 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
756 | #a7c3a7 | North Pacific Alpine and Subalpine Dry Grassland  
757 | #f5ba9d | North Pacific Wooded Volcanic Flowage  
758 | #d9bdfc | North Pacific Dry-Mesic Silver Fir-Western Hemlock-Douglas-fir Forest  
759 | #d7b09e | North Pacific Hypermaritime Western Red-cedar-Western Hemlock Forest  
760 | #ff7878 | North Pacific Oak Woodland  
761 | #a80000 | California Coastal Redwood Forest  
762 | #f5b595 | Klamath-Siskiyou Lower Montane Serpentine Mixed Conifer Woodland  
763 | #ed8b5a | Klamath-Siskiyou Upper Montane Serpentine Mixed Conifer Woodland  
764 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
765 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
766 | #dc6464 | Mediterranean California Mixed Oak Woodland  
767 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
768 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
769 | #ff3b7f | Mediterranean California Red Fir Forest  
770 | #894444 | North Pacific Dry Douglas-fir(-Madrone) Forest and Woodland  
771 | #d57fe3 | North Pacific Hypermaritime Sitka Spruce Forest  
772 | #defcde | North Pacific Maritime Dry-Mesic Douglas-fir-Western Hemlock Forest  
773 | #aae3aa | North Pacific Maritime Mesic-Wet Douglas-fir-Western Hemlock Forest  
774 | #a4c48f | Mediterranean California Mixed Evergreen Forest  
775 | #cd6666 | East Cascades Oak-Ponderosa Pine Forest and Woodland  
776 | #fff7a3 | North Pacific Broadleaf Landslide Forest and Shrubland  
777 | #d7d79e | Willamette Valley Upland Prairie and Savanna  
778 | #94c2a8 | Northern California Coastal Scrub  
779 | #edf0d8 | California Northern Coastal Grassland  
780 | #4196a7 | California Montane Riparian Systems  
781 | #b1b37d | North Pacific Lowland Riparian Forest and Shrubland  
782 | #465589 | North Pacific Swamp Systems  
783 | #bccfd4 | North Pacific Montane Riparian Woodland and Shrubland - Wet  
784 | #acc2c1 | North Pacific Montane Riparian Woodland and Shrubland - Dry  
785 | #d2eb00 | Klamath-Siskiyou Xeromorphic Serpentine Savanna and Chaparral  
786 | #d7b09e | North Pacific Hypermaritime Western Red-cedar-Western Hemlock Forest  
787 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
788 | #fff5d7 | Mediterranean California Sparsely Vegetated Systems  
789 | #fff0be | North Pacific Sparsely Vegetated Systems  
790 | #ff7878 | North Pacific Oak Woodland  
791 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
792 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
793 | #5f9eb4 | East Cascades Mesic Montane Mixed-Conifer Forest and Woodland  
794 | #734c00 | Great Basin Pinyon-Juniper Woodland  
795 | #f5b595 | Klamath-Siskiyou Lower Montane Serpentine Mixed Conifer Woodland  
796 | #ed8b5a | Klamath-Siskiyou Upper Montane Serpentine Mixed Conifer Woodland  
797 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
798 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
799 | #dc6464 | Mediterranean California Mixed Oak Woodland  
800 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
801 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
802 | #ff3b7f | Mediterranean California Red Fir Forest  
803 | #e2c2a2 | Mediterranean California Subalpine Woodland  
804 | #73004c | Mediterranean California Mesic Serpentine Woodland and Chaparral  
805 | #894444 | North Pacific Dry Douglas-fir(-Madrone) Forest and Woodland  
806 | #defcde | North Pacific Maritime Dry-Mesic Douglas-fir-Western Hemlock Forest  
807 | #ff9100 | North Pacific Maritime Mesic Subalpine Parkland  
808 | #aae3aa | North Pacific Maritime Mesic-Wet Douglas-fir-Western Hemlock Forest  
809 | #a5e6fc | North Pacific Mountain Hemlock Forest - Wet  
810 | #72d0f2 | North Pacific Mountain Hemlock Forest - Xeric  
811 | #f9bdfc | North Pacific Mesic Western Hemlock-Silver Fir Forest  
812 | #a4c48f | Mediterranean California Mixed Evergreen Forest  
813 | #ff8500 | Northern California Mesic Subalpine Woodland  
814 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest  
815 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
816 | #a85500 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Mesic  
817 | #a87800 | Northern Rocky Mountain Ponderosa Pine Woodland and Savanna - Xeric  
818 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
819 | #7fea00 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland  
820 | #cd6666 | East Cascades Oak-Ponderosa Pine Forest and Woodland  
821 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
822 | #fff7a3 | North Pacific Broadleaf Landslide Forest and Shrubland  
823 | #147d7d | North Pacific Dry and Mesic Alpine Dwarf-Shrubland or Fell-field or Meadow  
824 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
825 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
826 | #c8be55 | California Mesic Chaparral  
827 | #d2aa32 | California Montane Woodland and Chaparral  
828 | #aefaff | Great Basin Semi-Desert Chaparral  
829 | #f5f6af | Northern and Central California Dry-Mesic Chaparral  
830 | #b3ffe8 | California Lower Montane Blue Oak-Foothill Pine Woodland and Savanna  
831 | #d7d79e | Willamette Valley Upland Prairie and Savanna  
832 | #ebdaea | Columbia Plateau Steppe and Grassland  
833 | #848cad | Columbia Plateau Low Sagebrush Steppe  
834 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
835 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
836 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
837 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
838 | #4196a7 | California Montane Riparian Systems  
839 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
840 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
841 | #b1b37d | North Pacific Lowland Riparian Forest and Shrubland  
842 | #bccfd4 | North Pacific Montane Riparian Woodland and Shrubland - Wet  
843 | #acc2c1 | North Pacific Montane Riparian Woodland and Shrubland - Dry  
844 | #ff7800 | Northern Rocky Mountain Foothill Conifer Wooded Steppe  
845 | #55ff00 | Rocky Mountain Poor-Site Lodgepole Pine Forest  
846 | #d2eb00 | Klamath-Siskiyou Xeromorphic Serpentine Savanna and Chaparral  
847 | #a7c3a7 | North Pacific Alpine and Subalpine Dry Grassland  
848 | #e6ffe6 | Sierran-Intermontane Desert Western White Pine-White Fir Woodland  
849 | #f5ba9d | North Pacific Wooded Volcanic Flowage  
850 | #d9bdfc | North Pacific Dry-Mesic Silver Fir-Western Hemlock-Douglas-fir Forest  
851 | #d7b09e | North Pacific Hypermaritime Western Red-cedar-Western Hemlock Forest  
852 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
853 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
854 | #c8d1ff | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Ponderosa Pine-Douglas-fir  
855 | #8fccb1 | Northern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest - Lodgepole Pine  
856 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
857 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
858 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
859 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
860 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
861 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
862 | #a80084 | Northwestern Great Plains Shrubland  
863 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
864 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
865 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
866 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
867 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
868 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
869 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
870 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
871 | #f5daa9 | Western Great Plains Sand Prairie  
872 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
873 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
874 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
875 | #6699cd | Western Great Plains Floodplain Systems  
876 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
877 | #68009c | Western Great Plains Depressional Wetland Systems  
878 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
879 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
880 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
881 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
882 | #80fb1a | Rocky Mountain Lodgepole Pine Forest  
883 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
884 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
885 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
886 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
887 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
888 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
889 | #0bbe7f | Inter-Mountain Basins Mat Saltbush Shrubland  
890 | #848cc8 | Wyoming Basins Dwarf Sagebrush Shrubland and Steppe  
891 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland - Basin Big Sagebrush  
892 | #ffa3b4 | Inter-Mountain Basins Big Sagebrush Shrubland - Wyoming Big Sagebrush  
893 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
894 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland - No True Mountain Mahogany  
895 | #891987 | Rocky Mountain Lower Montane-Foothill Shrubland - True Mountain Mahogany  
896 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
897 | #897044 | Inter-Mountain Basins Juniper Savanna  
898 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
899 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
900 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
901 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
902 | #5d2b1d | Rocky Mountain Alpine Turf  
903 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
904 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
905 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
906 | #6699cd | Western Great Plains Floodplain Systems  
907 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
908 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
909 | #fff5d7 | Mediterranean California Sparsely Vegetated Systems  
910 | #77ab57 | Central and Southern California Mixed Evergreen Woodland  
911 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
912 | #dc6464 | Mediterranean California Mixed Oak Woodland  
913 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
914 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
915 | #a4c48f | Mediterranean California Mixed Evergreen Forest  
916 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
917 | #c8be55 | California Mesic Chaparral  
918 | #f5f6af | Northern and Central California Dry-Mesic Chaparral  
919 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
920 | #e68282 | California Central Valley Mixed Oak Savanna  
921 | #b3ffe8 | California Lower Montane Blue Oak-Foothill Pine Woodland and Savanna  
922 | #a3ff73 | California Central Valley and Southern Coastal Grassland  
923 | #c7e69e | North Pacific Montane Grassland  
924 | #3eabd7 | California Central Valley Riparian Woodland and Shrubland  
925 | #4196a7 | California Montane Riparian Systems  
926 | #444f7d | Pacific Coastal Marsh Systems  
927 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
928 | #77ab57 | Central and Southern California Mixed Evergreen Woodland  
929 | #a80000 | California Coastal Redwood Forest  
930 | #734c00 | Great Basin Pinyon-Juniper Woodland  
931 | #9ebbd7 | Mediterranean California Dry-Mesic Mixed Conifer Forest and Woodland  
932 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
933 | #dc6464 | Mediterranean California Mixed Oak Woodland  
934 | #b45091 | Mediterranean California Lower Montane Black Oak-Conifer Forest and Woodland  
935 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
936 | #73004c | Mediterranean California Mesic Serpentine Woodland and Chaparral  
937 | #7fea00 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland  
938 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
939 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
940 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
941 | #9ed7c2 | Southern California Coastal Scrub  
942 | #c8aa8c | California Maritime Chaparral  
943 | #c8be55 | California Mesic Chaparral  
944 | #d2aa32 | California Montane Woodland and Chaparral  
945 | #ac69cd | California Xeric Serpentine Chaparral  
946 | #f5f6af | Northern and Central California Dry-Mesic Chaparral  
947 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
948 | #e9d6f5 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
949 | #e2f5ae | Southern California Dry-Mesic Chaparral  
950 | #e68282 | California Central Valley Mixed Oak Savanna  
951 | #449170 | California Coastal Live Oak Woodland and Savanna  
952 | #b3ffe8 | California Lower Montane Blue Oak-Foothill Pine Woodland and Savanna  
953 | #44a082 | Southern California Oak Woodland and Savanna  
954 | #94c2a8 | Northern California Coastal Scrub  
955 | #a3ff73 | California Central Valley and Southern Coastal Grassland  
956 | #cdbcd6 | California Mesic Serpentine Grassland  
957 | #edf0d8 | California Northern Coastal Grassland  
958 | #3eabd7 | California Central Valley Riparian Woodland and Shrubland  
959 | #4196a7 | California Montane Riparian Systems  
960 | #7ba075 | North American Warm Desert Riparian Systems  
961 | #444f7d | Pacific Coastal Marsh Systems  
962 | #edcf00 | California Coastal Closed-Cone Conifer Forest and Woodland  
963 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
964 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
965 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
966 | #ffd37f | Rocky Mountain Bigtooth Maple Ravine Woodland  
967 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
968 | #734c00 | Great Basin Pinyon-Juniper Woodland  
969 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
970 | #80fb1a | Rocky Mountain Lodgepole Pine Forest  
971 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
972 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
973 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
974 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
975 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
976 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
977 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland - Low Elevation  
978 | #c8e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland - High Elevation  
979 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
980 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
981 | #13765c | Rocky Mountain Alpine Dwarf-Shrubland  
982 | #349bcf | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
983 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
984 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
985 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
986 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
987 | #86db18 | Southern Colorado Plateau Sand Shrubland  
988 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
989 | #aefaff | Great Basin Semi-Desert Chaparral  
990 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland - Continuous  
991 | #66cdab | Rocky Mountain Gambel Oak-Mixed Montane Shrubland - Patchy  
992 | #897044 | Inter-Mountain Basins Juniper Savanna  
993 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
994 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
995 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe - Mountain Big Sagebrush  
996 | #ffc5bf | Inter-Mountain Basins Montane Sagebrush Steppe - Low Sagebrush  
997 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
998 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
999 | #5d2b1d | Rocky Mountain Alpine Turf  
1000 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
1001 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1002 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1003 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
1004 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1005 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1006 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1007 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1008 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
1009 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1010 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1011 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
1012 | #80fb1a | Rocky Mountain Lodgepole Pine Forest  
1013 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1014 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1015 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1016 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1017 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
1018 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
1019 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland - Low Elevation  
1020 | #c8e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland - High Elevation  
1021 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1022 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
1023 | #0bbe7f | Inter-Mountain Basins Mat Saltbush Shrubland  
1024 | #349bcf | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
1025 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1026 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1027 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
1028 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1029 | #86db18 | Southern Colorado Plateau Sand Shrubland  
1030 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
1031 | #aefaff | Great Basin Semi-Desert Chaparral  
1032 | #adfad3 | Mogollon Chaparral  
1033 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1034 | #897044 | Inter-Mountain Basins Juniper Savanna  
1035 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1036 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1037 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe - Mountain Big Sagebrush  
1038 | #ffc5bf | Inter-Mountain Basins Montane Sagebrush Steppe - Low Sagebrush  
1039 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1040 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1041 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1042 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1043 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1044 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1045 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1046 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1047 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
1048 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1049 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
1050 | #734c00 | Great Basin Pinyon-Juniper Woodland  
1051 | #0e2e39 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
1052 | #5462a8 | Mediterranean California Mesic Mixed Conifer Forest and Woodland  
1053 | #dc6464 | Mediterranean California Mixed Oak Woodland  
1054 | #a74600 | California Montane Jeffrey Pine(-Ponderosa Pine) Woodland  
1055 | #e2c2a2 | Mediterranean California Subalpine Woodland  
1056 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1057 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
1058 | #7fea00 | Sierra Nevada Subalpine Lodgepole Pine Forest and Woodland  
1059 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1060 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
1061 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1062 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1063 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
1064 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
1065 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
1066 | #aefaff | Great Basin Semi-Desert Chaparral  
1067 | #848cad | Columbia Plateau Low Sagebrush Steppe  
1068 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1069 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1070 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1071 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1072 | #5d2b1d | Rocky Mountain Alpine Turf  
1073 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1074 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
1075 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1076 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1077 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1078 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1079 | #ffd37f | Rocky Mountain Bigtooth Maple Ravine Woodland  
1080 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1081 | #734c00 | Great Basin Pinyon-Juniper Woodland  
1082 | #0e2e39 | Inter-Mountain Basins Subalpine Limber-Bristlecone Pine Woodland  
1083 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1084 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1085 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1086 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1087 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1088 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1089 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
1090 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
1091 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1092 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1093 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
1094 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1095 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
1096 | #aefaff | Great Basin Semi-Desert Chaparral  
1097 | #adfad3 | Mogollon Chaparral  
1098 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1099 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
1100 | #897044 | Inter-Mountain Basins Juniper Savanna  
1101 | #848cad | Columbia Plateau Low Sagebrush Steppe  
1102 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1103 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1104 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1105 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1106 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
1107 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1108 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
1109 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1110 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1111 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1112 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1113 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1114 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1115 | #00a784 | Madrean Encinal  
1116 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
1117 | #a06a1f | Madrean Pinyon-Juniper Woodland  
1118 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1119 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1120 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1121 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1122 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1123 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland - Low Elevation  
1124 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
1125 | #0bbe7f | Inter-Mountain Basins Mat Saltbush Shrubland  
1126 | #349bcf | Colorado Plateau Blackbrush-Mormon-tea Shrubland  
1127 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1128 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1129 | #86db18 | Southern Colorado Plateau Sand Shrubland  
1130 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
1131 | #adfad3 | Mogollon Chaparral  
1132 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1133 | #897044 | Inter-Mountain Basins Juniper Savanna  
1134 | #cf9d8f | Madrean Juniper Savanna  
1135 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1136 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1137 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
1138 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1139 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1140 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1141 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
1142 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1143 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1144 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1145 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
1146 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1147 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1148 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
1149 | #80fb1a | Rocky Mountain Lodgepole Pine Forest  
1150 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1151 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1152 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1153 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1154 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
1155 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
1156 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1157 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1158 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1159 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
1160 | #13765c | Rocky Mountain Alpine Dwarf-Shrubland  
1161 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1162 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1163 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1164 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
1165 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1166 | #897044 | Inter-Mountain Basins Juniper Savanna  
1167 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1168 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1169 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1170 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1171 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1172 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1173 | #828282 | Rocky Mountain Alpine Fell-Field  
1174 | #5d2b1d | Rocky Mountain Alpine Turf  
1175 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
1176 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1177 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1178 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1179 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1180 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1181 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1182 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1183 | #734c00 | Great Basin Pinyon-Juniper Woodland  
1184 | #00a784 | Madrean Encinal  
1185 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
1186 | #a06a1f | Madrean Pinyon-Juniper Woodland  
1187 | #498039 | Madrean Upper Montane Conifer-Oak Forest and Woodland  
1188 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1189 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1190 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1191 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1192 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
1193 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1194 | #e87f69 | Chihuahuan Succulent Desert Scrub  
1195 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1196 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1197 | #d80649 | Mojave Mid-Elevation Mixed Desert Scrub  
1198 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
1199 | #b00663 | Sonoran Mid-Elevation Desert Scrub  
1200 | #f5a27a | Chihuahuan Mixed Desert and Thorn Scrub  
1201 | #ff0000 | Colorado Plateau Pinyon-Juniper Shrubland  
1202 | #adfad3 | Mogollon Chaparral  
1203 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1204 | #e9d6f5 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
1205 | #897044 | Inter-Mountain Basins Juniper Savanna  
1206 | #cf9d8f | Madrean Juniper Savanna  
1207 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1208 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
1209 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1210 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1211 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1212 | #7ba075 | North American Warm Desert Riparian Systems  
1213 | #54a075 | North American Warm Desert Riparian Systems - Stringers  
1214 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1215 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1216 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1217 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
1218 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1219 | #ffd37f | Rocky Mountain Bigtooth Maple Ravine Woodland  
1220 | #0ef562 | Columbia Plateau Western Juniper Woodland and Savanna  
1221 | #734c00 | Great Basin Pinyon-Juniper Woodland  
1222 | #ffaa00 | Northern Rocky Mountain Subalpine Woodland and Parkland  
1223 | #80fb1a | Rocky Mountain Lodgepole Pine Forest  
1224 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1225 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1226 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1227 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
1228 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
1229 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1230 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1231 | #39c2cf | Great Basin Xeric Mixed Sagebrush Shrubland  
1232 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1233 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1234 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1235 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
1236 | #ebdaea | Columbia Plateau Steppe and Grassland  
1237 | #848cad | Columbia Plateau Low Sagebrush Steppe  
1238 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1239 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1240 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1241 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1242 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
1243 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1244 | #9a9c75 | Inter-Mountain Basins Montane Riparian Systems  
1245 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1246 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1247 | #4e4e4e | Rocky Mountain Alpine/Montane Sparsely Vegetated Systems  
1248 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
1249 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1250 | #00734c | Northwestern Great Plains Highland White Spruce Woodland  
1251 | #66cdab | Rocky Mountain Foothill Limber Pine-Juniper Woodland  
1252 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1253 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1254 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1255 | #38a800 | Rocky Mountain Subalpine Mesic-Wet Spruce-Fir Forest and Woodland  
1256 | #e3dfa2 | Rocky Mountain Subalpine-Montane Limber-Bristlecone Pine Woodland  
1257 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1258 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1259 | #0bbe7f | Inter-Mountain Basins Mat Saltbush Shrubland  
1260 | #848cc8 | Wyoming Basins Dwarf Sagebrush Shrubland and Steppe  
1261 | #a80084 | Northwestern Great Plains Shrubland  
1262 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1263 | #894450 | Northern Rocky Mountain Montane-Foothill Deciduous Shrubland  
1264 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1265 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1266 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1267 | #abcd66 | Northern Rocky Mountain Lower Montane-Foothill-Valley Grassland  
1268 | #a7cdc3 | Northern Rocky Mountain Subalpine-Upper Montane Grassland  
1269 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
1270 | #00c5ff | Rocky Mountain Subalpine-Montane Mesic Meadow  
1271 | #f5daa9 | Western Great Plains Sand Prairie  
1272 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1273 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1274 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1275 | #31a5a7 | Rocky Mountain Subalpine/Upper Montane Riparian Systems  
1276 | #6699cd | Western Great Plains Floodplain Systems  
1277 | #d67000 | Middle Rocky Mountain Montane Douglas-fir Forest and Woodland  
1278 | #bd6a40 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna - Low Elevation Woodland  
1279 | #ffaf87 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna - Savanna  
1280 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
1281 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
1282 | #a80084 | Northwestern Great Plains Shrubland  
1283 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1284 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
1285 | #f5daa9 | Western Great Plains Sand Prairie  
1286 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1287 | #6699cd | Western Great Plains Floodplain Systems  
1288 | #bd6a40 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna - Low Elevation Woodland  
1289 | #ffaf87 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna - Savanna  
1290 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
1291 | #9c64a3 | Great Plains Prairie Pothole  
1292 | #68009c | Western Great Plains Depressional Wetland Systems  
1293 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
1294 | #e6cd9c | Atlantic Coastal Plain Dry and Dry-Mesic Oak Forest  
1295 | #a87000 | Atlantic Coastal Plain Mesic Hardwood Forest  
1296 | #4e9c1a | Atlantic Coastal Plain Fall-line Sandhills Longleaf Pine Woodland  
1297 | #87ba18 | Atlantic Coastal Plain Upland Longleaf Pine Woodland  
1298 | #98b000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
1299 | #4cba0a | Florida Longleaf Pine Sandhill  
1300 | #bf9747 | Southern Coastal Plain Mesic Slope Forest  
1301 | #d682ff | East Gulf Coastal Plain Maritime Forest  
1302 | #ba82ff | Southern Atlantic Coastal Plain Maritime Forest  
1303 | #ffc800 | Florida Peninsula Inland Scrub  
1304 | #d1ffb3 | Southern Atlantic Coastal Plain Wet Pine Savanna and Flatwoods  
1305 | #96f567 | Central Florida Pine Flatwoods  
1306 | #95e376 | East Gulf Coastal Plain Near-Coast Pine Flatwoods  
1307 | #a80a00 | Southern Coastal Plain Nonriverine Cypress Dome  
1308 | #bee8ff | Southern Coastal Plain Seepage Swamp and Baygall  
1309 | #444f91 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
1310 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1311 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1312 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1313 | #ffd978 | East Gulf Coastal Plain Savanna and Wet Prairie  
1314 | #f0ff5e | Floridian Highlands Freshwater Marsh  
1315 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1316 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
1317 | #807900 | South Florida Hardwood Hammock  
1318 | #f773ff | Southwest Florida Coastal Strand and Maritime Hammock  
1319 | #e45eff | Southeast Florida Coastal Strand and Maritime Hammock  
1320 | #4cba0a | Florida Longleaf Pine Sandhill  
1321 | #d6aa66 | South Florida Pine Rockland  
1322 | #ffc800 | Florida Peninsula Inland Scrub  
1323 | #ffd6d6 | Florida Dry Prairie  
1324 | #e0007b | South Florida Dwarf Cypress Savanna  
1325 | #a2e68c | South Florida Pine Flatwoods  
1326 | #c80a00 | South Florida Cypress Dome  
1327 | #96f567 | Central Florida Pine Flatwoods  
1328 | #95e376 | East Gulf Coastal Plain Near-Coast Pine Flatwoods  
1329 | #a80a00 | Southern Coastal Plain Nonriverine Cypress Dome  
1330 | #bee8ff | Southern Coastal Plain Seepage Swamp and Baygall  
1331 | #00d9ff | Caribbean Coastal Wetland Systems  
1332 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1333 | #5cedc9 | Caribbean Swamp Systems  
1334 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1335 | #d4ffed | South Florida Everglades Sawgrass Marsh  
1336 | #f0ff5e | Floridian Highlands Freshwater Marsh  
1337 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1338 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1339 | #cdaa66 | Colorado Plateau Pinyon-Juniper Woodland  
1340 | #00a784 | Madrean Encinal  
1341 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
1342 | #a06a1f | Madrean Pinyon-Juniper Woodland  
1343 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1344 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1345 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1346 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1347 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1348 | #df73ff | Chihuahuan Creosotebush Desert Scrub  
1349 | #f4bf00 | Chihuahuan Mixed Salt Desert Scrub  
1350 | #e87f69 | Chihuahuan Succulent Desert Scrub  
1351 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1352 | #349ab8 | Sonora-Mojave Creosotebush-White Bursage Desert Scrub  
1353 | #f5de6e | Sonora-Mojave Mixed Salt Desert Scrub  
1354 | #b00663 | Sonoran Mid-Elevation Desert Scrub  
1355 | #a900e6 | Western Great Plains Sandhill Steppe  
1356 | #f5a27a | Chihuahuan Mixed Desert Shrubland  
1357 | #cd8966 | Chihuahuan Grama Grass-Creosote Steppe  
1358 | #74d4b4 | Madrean Oriental Chaparral  
1359 | #adfad3 | Mogollon Chaparral  
1360 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1361 | #ffc5ad | Sonora-Mojave Semi-Desert Chaparral  
1362 | #e9d6f5 | Sonoran Paloverde-Mixed Cacti Desert Scrub  
1363 | #cf9d8f | Madrean Juniper Savanna  
1364 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1365 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
1366 | #91e600 | Chihuahuan Gypsophilous Grassland and Steppe  
1367 | #c29ed7 | Inter-Mountain Basins Semi-Desert Shrub-Steppe  
1368 | #e5dd85 | Chihuahuan Sandy Plains Semi-Desert Grassland  
1369 | #b9aed3 | Inter-Mountain Basins Semi-Desert Grassland  
1370 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1371 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1372 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1373 | #7ba075 | North American Warm Desert Riparian Systems  
1374 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1375 | #c7d79e | Chihuahuan Loamy Plains Desert Grassland  
1376 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland  
1377 | #fff2bd | North American Warm Desert Sparsely Vegetated Systems  
1378 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
1379 | #a06a1f | Madrean Pinyon-Juniper Woodland  
1380 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1381 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1382 | #df73ff | Chihuahuan Creosotebush Desert Scrub  
1383 | #f4bf00 | Chihuahuan Mixed Salt Desert Scrub  
1384 | #e54563 | Chihuahuan Stabilized Coppice Dune and Sand Flat Scrub  
1385 | #e87f69 | Chihuahuan Succulent Desert Scrub  
1386 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1387 | #a900e6 | Western Great Plains Sandhill Steppe  
1388 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
1389 | #f5a27a | Chihuahuan Mixed Desert and Thorn Scrub  
1390 | #74d4b4 | Madrean Oriental Chaparral  
1391 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1392 | #cf9d8f | Madrean Juniper Savanna  
1393 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1394 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
1395 | #91e600 | Chihuahuan Gypsophilous Grassland and Steppe  
1396 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1397 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1398 | #7ba075 | North American Warm Desert Riparian Systems  
1399 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1400 | #ffcb7d | Edwards Plateau Limestone Shrubland  
1401 | #68009c | Western Great Plains Depressional Wetland Systems - Playa  
1402 | #c7d79e | Chihuahuan Loamy Plains Desert Grassland  
1403 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland - Tobosa Grassland  
1404 | #64964b | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland - Alkali Sacaton  
1405 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland  
1406 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1407 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1408 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub  
1409 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1410 | #a900e6 | Western Great Plains Sandhill Steppe  
1411 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1412 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1413 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna  
1414 | #e600a9 | Inter-Mountain Basins Montane Sagebrush Steppe  
1415 | #70a870 | Central Mixedgrass Prairie  
1416 | #89cd66 | Western Great Plains Foothill and Piedmont Grassland  
1417 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1418 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1419 | #6699cd | Western Great Plains Floodplain Systems  
1420 | #c4b29c | Northwestern Great Plains Canyon  
1421 | #68009c | Western Great Plains Depressional Wetland Systems  
1422 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
1423 | #a900e6 | Western Great Plains Sandhill Steppe  
1424 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1425 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1426 | #70a870 | Central Mixedgrass Prairie  
1427 | #f5daa9 | Western Great Plains Sand Prairie  
1428 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1429 | #6699cd | Western Great Plains Floodplain Systems  
1430 | #ffcb7d | Edwards Plateau Limestone Shrubland  
1431 | #68009c | Western Great Plains Depressional Wetland Systems - Playa  
1432 | #5200c9 | Western Great Plains Depressional Wetland Systems - Saline  
1433 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland - Tobosa Grassland  
1434 | #64964b | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland - Alkali Sacaton  
1435 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
1436 | #db45df | West Gulf Coastal Plain Chenier and Upper Texas Coastal Fringe Forest and Woodland  
1437 | #707f00 | West Gulf Coastal Plain Upland Longleaf Pine Forest and Woodland  
1438 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
1439 | #d1d900 | West Gulf Coastal Plain Sandhill Oak and Shortleaf Pine Forest and Woodland  
1440 | #ff7f7f | Southern Blackland Tallgrass Prairie  
1441 | #ff006e | West Gulf Coastal Plain Northern Calcareous Prairie  
1442 | #ff249e | West Gulf Coastal Plain Southern Calcareous Prairie  
1443 | #dba3df | Texas-Louisiana Coastal Prairie  
1444 | #44f200 | West Gulf Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
1445 | #63eb61 | West Gulf Coastal Plain Pine-Hardwood Flatwoods  
1446 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1447 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1448 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1449 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1450 | #267300 | West Gulf Coastal Plain Nonriverine Wet Hardwood Flatwoods  
1451 | #cf940a | East-Central Texas Plains Post Oak Savanna and Woodland  
1452 | #e6cd9c | Atlantic Coastal Plain Dry and Dry-Mesic Oak Forest  
1453 | #a87000 | Atlantic Coastal Plain Mesic Hardwood Forest  
1454 | #4e9c1a | Atlantic Coastal Plain Fall-line Sandhills Longleaf Pine Woodland  
1455 | #87ba18 | Atlantic Coastal Plain Upland Longleaf Pine Woodland  
1456 | #bf9747 | Southern Coastal Plain Mesic Slope Forest  
1457 | #ed00e5 | Central Atlantic Coastal Plain Maritime Forest  
1458 | #ba82ff | Southern Atlantic Coastal Plain Maritime Forest  
1459 | #640046 | Southern Atlantic Coastal Plain Dune and Maritime Grassland  
1460 | #8fed29 | Central Atlantic Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
1461 | #d1ffb3 | Southern Atlantic Coastal Plain Wet Pine Savanna and Flatwoods  
1462 | #ff7d00 | Atlantic Coastal Plain Peatland Pocosin and Canebrake  
1463 | #ffe84f | Atlantic Coastal Plain Clay-Based Carolina Bay Wetland  
1464 | #444f91 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
1465 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1466 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1467 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1468 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1469 | #63d6ff | Central Atlantic Coastal Plain Nonriverine Swamp and Wet Hardwood Forest  
1470 | #ffffbe | Inter-Mountain Basins Sparsely Vegetated Systems  
1471 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
1472 | #ffff73 | Rocky Mountain Aspen Forest and Woodland  
1473 | #ffd37f | Rocky Mountain Bigtooth Maple Ravine Woodland  
1474 | #a7bd1e | Madrean Lower Montane Pine-Oak Forest and Woodland  
1475 | #bed2ff | Southern Rocky Mountain Dry-Mesic Montane Mixed Conifer Forest and Woodland  
1476 | #7395e6 | Southern Rocky Mountain Mesic Montane Mixed Conifer Forest and Woodland  
1477 | #a83800 | Southern Rocky Mountain Ponderosa Pine Woodland - South  
1478 | #941a36 | Southern Rocky Mountain Ponderosa Pine Woodland - North  
1479 | #d3ffbe | Rocky Mountain Subalpine Dry-Mesic Spruce-Fir Forest and Woodland  
1480 | #b78a2e | Southern Rocky Mountain Pinyon-Juniper Woodland  
1481 | #e6e600 | Inter-Mountain Basins Aspen-Mixed Conifer Forest and Woodland  
1482 | #9eaad7 | Colorado Plateau Mixed Low Sagebrush Shrubland  
1483 | #f5ca7a | Inter-Mountain Basins Mixed Salt Desert Scrub - South  
1484 | #e09691 | Inter-Mountain Basins Mixed Salt Desert Scrub - North  
1485 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1486 | #a900e6 | Western Great Plains Sandhill Steppe  
1487 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
1488 | #73ffdf | Rocky Mountain Gambel Oak-Mixed Montane Shrubland  
1489 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1490 | #ff5500 | Southern Rocky Mountain Ponderosa Pine Savanna - South  
1491 | #ed7d21 | Southern Rocky Mountain Ponderosa Pine Savanna - North  
1492 | #875614 | Southern Rocky Mountain Juniper Woodland and Savanna  
1493 | #ffddd8 | Apacherian-Chihuahuan Semi-Desert Grassland and Steppe  
1494 | #91e600 | Chihuahuan Gypsophilous Grassland and Steppe  
1495 | #a7cdb2 | Southern Rocky Mountain Montane-Subalpine Grassland  
1496 | #89cd66 | Western Great Plains Foothill and Piedmont Grassland  
1497 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1498 | #e1e1e1 | Inter-Mountain Basins Greasewood Flat  
1499 | #7b7c5d | Rocky Mountain Montane Riparian Systems  
1500 | #6699cd | Western Great Plains Floodplain Systems  
1501 | #68009c | Western Great Plains Depressional Wetland Systems  
1502 | #c7d79e | Chihuahuan Loamy Plains Desert Grassland  
1503 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland  
1504 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
1505 | #db45df | West Gulf Coastal Plain Chenier and Upper Texas Coastal Fringe Forest and Woodland  
1506 | #707f00 | West Gulf Coastal Plain Upland Longleaf Pine Forest and Woodland  
1507 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
1508 | #6b3624 | Mississippi Delta Maritime Forest  
1509 | #dba3df | Texas-Louisiana Coastal Prairie  
1510 | #44f200 | West Gulf Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
1511 | #63eb61 | West Gulf Coastal Plain Pine-Hardwood Flatwoods  
1512 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1513 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1514 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1515 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1516 | #ab6138 | Gulf and Atlantic Coastal Plain Sparsely Vegetated Systems  
1517 | #3ef533 | Southern Crowley`s Ridge Mesic Loess Slope Forest  
1518 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
1519 | #e8a1d4 | East Gulf Coastal Plain Northern Loess Bluff Forest  
1520 | #a80836 | East Gulf Coastal Plain Southern Loess Bluff Forest  
1521 | #707f00 | West Gulf Coastal Plain Upland Longleaf Pine Forest and Woodland  
1522 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
1523 | #dec48a | Lower Mississippi River Dune Woodland and Forest  
1524 | #ff249e | West Gulf Coastal Plain Southern Calcareous Prairie  
1525 | #e3e35c | Lower Mississippi Alluvial Plain Grand Prairie  
1526 | #63eb61 | West Gulf Coastal Plain Pine-Hardwood Flatwoods  
1527 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1528 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1529 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1530 | #006b52 | Mississippi River Alluvial Plain Dry-Mesic Loess Slope Forest  
1531 | #ca7af5 | Northern Crowley`s Ridge Sand Forest  
1532 | #620075 | Lower Mississippi River Flatwoods  
1561 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1562 | #4ce696 | Laurentian-Acadian Northern Hardwoods Forest - Hemlock  
1563 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1564 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
1565 | #009c2c | North-Central Interior Beech-Maple Forest  
1566 | #eda166 | North-Central Interior Maple-Basswood Forest  
1567 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1568 | #93c272 | Boreal White Spruce-Fir-Hardwood Forest - Inland  
1569 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1570 | #e6d58a | North-Central Interior Oak Savanna  
1571 | #ffebb0 | North-Central Oak Barrens  
1572 | #994200 | Laurentian Pine-Oak Barrens  
1573 | #994264 | Laurentian-Acadian Jack Pine Barrens and Forest  
1574 | #e3eb75 | Great Lakes Alvar  
1575 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1576 | #e8ffc4 | Central Tallgrass Prairie  
1577 | #45459c | Eastern Boreal Floodplain  
1578 | #b50000 | Great Lakes Wooded Dune and Swale  
1579 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1580 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1581 | #6a008a | Boreal Acidic Peatland Systems  
1582 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1583 | #e8bdff | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp  
1584 | #7af5ca | Great Lakes Coastal Marsh Systems  
1585 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
1586 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1587 | #6a7500 | Paleozoic Plateau Bluff and Talus  
1588 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1589 | #4ce696 | Laurentian-Acadian Northern Hardwoods Forest - Hemlock  
1590 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1591 | #eda166 | North-Central Interior Maple-Basswood Forest  
1592 | #dcf000 | Eastern Great Plains Tallgrass Aspen Parkland  
1593 | #ff8c8c | Boreal Jack Pine-Black Spruce Forest  
1594 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1595 | #ffa77f | Laurentian-Acadian Northern Pine Forest  
1596 | #93c272 | Boreal White Spruce-Fir-Hardwood Forest - Inland  
1597 | #6e8946 | Boreal White Spruce-Fir-Hardwood Forest - Coastal  
1598 | #ffff91 | Boreal White Spruce-Fir-Hardwood Forest - Aspen-Birch  
1599 | #e6d58a | North-Central Interior Oak Savanna  
1600 | #ffebb0 | North-Central Oak Barrens  
1601 | #994200 | Laurentian Pine-Oak Barrens  
1602 | #994264 | Laurentian-Acadian Jack Pine Barrens and Forest  
1603 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1604 | #b8841d | Northern Tallgrass Prairie  
1605 | #45459c | Eastern Boreal Floodplain  
1606 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1607 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1608 | #6a008a | Boreal Acidic Peatland Systems  
1609 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1610 | #e8bdff | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp  
1611 | #7af5ca | Great Lakes Coastal Marsh Systems  
1612 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
1613 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1614 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1615 | #4ce696 | Laurentian-Acadian Northern Hardwoods Forest - Hemlock  
1616 | #266900 | Northern Sugar Maple-Basswood Forest  
1617 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1618 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
1619 | #009c2c | North-Central Interior Beech-Maple Forest  
1620 | #ff8c8c | Great Lakes Pine Barrens  
1621 | #87c872 | Great Lakes Spruce-Fir  
1622 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1623 | #93c272 | Boreal White Spruce-Fir-Hardwood Forest - Inland  
1624 | #6e8946 | Boreal White Spruce-Fir-Hardwood Forest - Coastal  
1625 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1626 | #e6d58a | North-Central Interior Oak Savanna  
1627 | #ffebb0 | North-Central Oak Barrens  
1628 | #994200 | Laurentian Pine-Oak Barrens  
1629 | #994264 | Laurentian-Acadian Jack Pine Barrens and Forest  
1630 | #ebff00 | Great Lakes Wet-Mesic Lakeplain Prairie  
1631 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1632 | #e8ffc4 | Central Tallgrass Prairie  
1633 | #45459c | Eastern Boreal Floodplain  
1634 | #b50000 | Great Lakes Wooded Dune and Swale  
1635 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1636 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1637 | #6a008a | Boreal Acid Peatland Systems  
1638 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1639 | #e8bdff | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp  
1640 | #7af5ca | Great Lakes Coastal Marsh Systems  
1641 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1642 | #dc0000 | Western Great Plains Dry Bur Oak Forest and Woodland  
1643 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
1644 | #f5f596 | Western Great Plains Tallgrass Prairie  
1645 | #6699cd | Western Great Plains Floodplain Systems  
1646 | #fff538 | Boreal Aspen-Birch Forest  
1647 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1648 | #eda166 | North-Central Interior Maple-Basswood Forest  
1649 | #dcf000 | Eastern Great Plains Tallgrass Aspen Parkland  
1650 | #93c272 | Boreal White Spruce-Fir-Hardwood Forest - Inland  
1651 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
1652 | #e6d58a | North-Central Interior Oak Savanna  
1653 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1654 | #b8841d | Northern Tallgrass Prairie  
1655 | #4baabe | Eastern Great Plains Floodplain Systems  
1656 | #6a008a | Boreal Acidic Peatland Systems  
1657 | #9c64a3 | Great Plains Prairie Pothole  
1658 | #68009c | Western Great Plains Depressional Wetland Systems  
1659 | #dc0000 | Western Great Plains Dry Bur Oak Forest and Woodland  
1660 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
1661 | #f5f596 | Western Great Plains Tallgrass Prairie  
1662 | #6699cd | Western Great Plains Floodplain Systems  
1663 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1664 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
1665 | #eda166 | North-Central Interior Maple-Basswood Forest  
1666 | #dcf000 | Eastern Great Plains Tallgrass Aspen Parkland  
1667 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
1668 | #e6d58a | North-Central Interior Oak Savanna  
1669 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1670 | #b8841d | Northern Tallgrass Prairie  
1671 | #4baabe | Eastern Great Plains Floodplain Systems  
1672 | #9c64a3 | Great Plains Prairie Pothole  
1673 | #68009c | Western Great Plains Depressional Wetland Systems  
1674 | #ffebbe | Western Great Plains Sparsely Vegetated Systems  
1675 | #dc0000 | Western Great Plains Dry Bur Oak Forest and Woodland  
1676 | #bf13e6 | Inter-Mountain Basins Curl-leaf Mountain Mahogany Woodland and Shrubland  
1677 | #ffbee8 | Inter-Mountain Basins Big Sagebrush Shrubland  
1678 | #894465 | Rocky Mountain Lower Montane-Foothill Shrubland  
1679 | #a900e6 | Western Great Plains Sandhill Steppe  
1680 | #ff73df | Inter-Mountain Basins Big Sagebrush Steppe  
1681 | #70a870 | Central Mixedgrass Prairie  
1682 | #d7ffe8 | Northwestern Great Plains Mixedgrass Prairie  
1683 | #f5daa9 | Western Great Plains Sand Prairie  
1684 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1685 | #f5f596 | Western Great Plains Tallgrass Prairie  
1686 | #6699cd | Western Great Plains Floodplain Systems  
1687 | #bd6a40 | Northwestern Great Plains-Black Hills Ponderosa Pine Woodland and Savanna  
1688 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
1689 | #e8ffc4 | Central Tallgrass Prairie  
1690 | #4baabe | Eastern Great Plains Floodplain Systems  
1691 | #68009c | Western Great Plains Depressional Wetland Systems  
1692 | #a900e6 | Western Great Plains Sandhill Steppe  
1693 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1694 | #70a870 | Central Mixedgrass Prairie  
1695 | #f5daa9 | Western Great Plains Sand Prairie  
1696 | #6699cd | Western Great Plains Floodplain Systems  
1697 | #737300 | Ozark-Ouachita Dry-Mesic Oak Forest  
1698 | #895a44 | Crosstimbers Oak Forest and Woodland  
1699 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
1700 | #00874a | Ozark-Ouachita Mesic Hardwood Forest  
1701 | #614500 | Ozark-Ouachita Dry Oak Woodland  
1702 | #c4a464 | Ozark-Ouachita Shortleaf Pine-Oak Forest and Woodland  
1703 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
1704 | #d1ff73 | Edwards Plateau Limestone Savanna and Woodland  
1705 | #ffcb7d | Edwards Plateau Limestone Shrubland  
1706 | #ff7f7f | Southern Blackland Tallgrass Prairie  
1707 | #874b78 | Southeastern Great Plains Tallgrass Prairie  
1708 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1709 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1710 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1711 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1712 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland  
1713 | #cf940a | East-Central Texas Plains Post Oak Savanna and Woodland  
1714 | #66ffab | Edwards Plateau Dry-Mesic Slope Forest and Woodland  
1715 | #a900e6 | Western Great Plains Sandhill Steppe  
1716 | #ff3884 | Apacherian-Chihuahuan Mesquite Upland Scrub  
1717 | #9c289c | Western Great Plains Mesquite Woodland and Shrubland  
1718 | #70a870 | Central Mixedgrass Prairie  
1719 | #f5daa9 | Western Great Plains Sand Prairie  
1720 | #cdcd66 | Western Great Plains Shortgrass Prairie  
1721 | #7ba075 | North American Warm Desert Riparian Systems  
1722 | #6699cd | Western Great Plains Floodplain Systems  
1723 | #895a44 | Crosstimbers Oak Forest and Woodland  
1724 | #c25e00 | East-Central Texas Plains Southern Pine Forest and Woodland  
1725 | #d1ff73 | Edwards Plateau Limestone Savanna and Woodland  
1726 | #d79ca0 | Tamaulipan Mixed Deciduous Thornscrub  
1727 | #cd6699 | Tamaulipan Calcareous Thornscrub  
1728 | #ffcb7d | Edwards Plateau Limestone Shrubland  
1729 | #c496f5 | Llano Uplift Acidic Forest-Woodland-Glade  
1730 | #ff7f7f | Southern Blackland Tallgrass Prairie  
1731 | #874b78 | Southeastern Great Plains Tallgrass Prairie  
1732 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1733 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1734 | #68009c | Western Great Plains Depressional Wetland Systems  
1735 | #a6b382 | Chihuahuan-Sonoran Desert Bottomland and Swale Grassland  
1736 | #cf940a | East-Central Texas Plains Post Oak Savanna and Woodland  
1737 | #66ffab | Edwards Plateau Dry-Mesic Slope Forest and Woodland  
1738 | #ffa8e8 | Edwards Plateau Mesic Canyon  
1739 | #7aa3f5 | Edwards Plateau Riparian  
1740 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
1741 | #a5f57a | Central and South Texas Coastal Fringe Forest and Woodland  
1742 | #db45df | West Gulf Coastal Plain Chenier and Upper Texas Coastal Fringe Forest and Woodland  
1743 | #c25e00 | East-Central Texas Plains Southern Pine Forest and Woodland  
1744 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
1745 | #d1ff73 | Edwards Plateau Limestone Savanna and Woodland  
1746 | #d79ca0 | Tamaulipan Mixed Deciduous Thornscrub  
1747 | #cd6699 | Tamaulipan Calcareous Thornscrub  
1748 | #ff7f7f | Southern Blackland Tallgrass Prairie  
1749 | #dba3df | Texas-Louisiana Coastal Prairie  
1750 | #8400cf | Central and Upper Texas Coast Dune and Coastal Grassland  
1751 | #c7d769 | Tamaulipan Savanna Grassland  
1752 | #872600 | South Texas Lomas  
1753 | #eb5700 | Tamaulipan Clay Grassland  
1754 | #ffedcf | South Texas Sand Sheet Grassland  
1755 | #66b5cd | Tamaulipan Floodplain  
1756 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1757 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1758 | #abd6eb | Tamaulipan Riparian Systems  
1759 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1760 | #f5b92f | Texas-Louisiana Saline Coastal Prairie  
1761 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1762 | #68009c | Western Great Plains Depressional Wetland Systems  
1763 | #cf940a | East-Central Texas Plains Post Oak Savanna and Woodland  
1764 | #decd95 | East Gulf Coastal Plain Northern Dry Upland Hardwood Forest  
1765 | #a87c23 | East Gulf Coastal Plain Northern Mesic Hardwood Slope Forest  
1766 | #e8a1d4 | East Gulf Coastal Plain Northern Loess Bluff Forest  
1767 | #c3ff4a | East Gulf Coastal Plain Limestone Forest  
1768 | #a80836 | East Gulf Coastal Plain Southern Loess Bluff Forest  
1769 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
1770 | #98b000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
1771 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1772 | #bf9747 | Southern Coastal Plain Mesic Slope Forest  
1773 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1774 | #df61ff | East Gulf Coastal Plain Interior Shortleaf Pine-Oak Forest  
1775 | #ff8e6b | Southern Coastal Plain Blackland Prairie and Woodland  
1776 | #4d219c | East Gulf Coastal Plain Southern Loblolly-Hardwood Flatwoods  
1777 | #bee8ff | Southern Coastal Plain Seepage Swamp and Baygall  
1778 | #444f91 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
1779 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1780 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1781 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1782 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1783 | #c3ff4a | East Gulf Coastal Plain Limestone Forest  
1784 | #a80836 | East Gulf Coastal Plain Southern Loess Bluff Forest  
1785 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
1786 | #98b000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
1787 | #4cba0a | Florida Longleaf Pine Sandhill  
1788 | #bf9747 | Southern Coastal Plain Mesic Slope Forest  
1789 | #df61ff | East Gulf Coastal Plain Interior Shortleaf Pine-Oak Forest  
1790 | #d682ff | East Gulf Coastal Plain Maritime Forest  
1791 | #8436de | East Gulf Coastal Plain Dune and Coastal Grassland  
1792 | #95e376 | East Gulf Coastal Plain Near-Coast Pine Flatwoods  
1793 | #4d219c | East Gulf Coastal Plain Southern Loblolly-Hardwood Flatwoods  
1794 | #a80a00 | Southern Coastal Plain Nonriverine Cypress Dome  
1795 | #bee8ff | Southern Coastal Plain Seepage Swamp and Baygall  
1796 | #444f91 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
1797 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1798 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1799 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1800 | #ffd978 | East Gulf Coastal Plain Savanna and Wet Prairie  
1801 | #f0ff5e | Floridian Highlands Freshwater Marsh  
1802 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1803 | #ab6138 | Gulf and Atlantic Coastal Plain Sparsely Vegetated Systems  
1804 | #b5e3c2 | Southern Appalachian Oak Forest  
1805 | #63c77d | Southern Piedmont Mesic Forest  
1806 | #8ab1ff | Southern and Central Appalachian Cove Forest  
1807 | #ed5e36 | Piedmont Hardpan Woodland and Forest  
1808 | #8fa11a | Southeastern Interior Longleaf Pine Woodland  
1809 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
1810 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1811 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1812 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1813 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1814 | #a39c2e | Southern Appalachian Northern Hardwood Forest  
1815 | #b5e3c2 | Southern Appalachian Oak Forest  
1816 | #63c77d | Southern Piedmont Mesic Forest  
1817 | #bab894 | Allegheny-Cumberland Dry Oak Forest and Woodland  
1818 | #8ab1ff | Southern and Central Appalachian Cove Forest  
1819 | #b482b4 | Central and Southern Appalachian Montane Oak Forest  
1820 | #478794 | South-Central Interior Mesophytic Forest  
1821 | #cfd633 | Central and Southern Appalachian Spruce-Fir Forest  
1822 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
1823 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1824 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1825 | #de997a | Southern Ridge and Valley/Cumberland Dry Calcareous Forest  
1826 | #f00a0a | Southern Appalachian Grass and Shrub Bald  
1827 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1828 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1829 | #63c77d | Southern Piedmont Mesic Forest  
1830 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
1831 | #a87000 | Atlantic Coastal Plain Mesic Hardwood Forest  
1832 | #4e9c1a | Atlantic Coastal Plain Fall-line Sandhills Longleaf Pine Woodland  
1833 | #98b000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
1834 | #8fa11a | Southeastern Interior Longleaf Pine Woodland  
1835 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
1836 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1837 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1838 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1839 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1840 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1841 | #63c77d | Southern Piedmont Mesic Forest  
1842 | #a1705a | Northern Atlantic Coastal Plain Hardwood Forest  
1843 | #e6cd9c | Atlantic Coastal Plain Dry and Dry-Mesic Oak Forest  
1844 | #a87000 | Atlantic Coastal Plain Mesic Hardwood Forest  
1845 | #87ba18 | Atlantic Coastal Plain Upland Longleaf Pine Woodland  
1846 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
1847 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1848 | #ffa552 | Northern Atlantic Coastal Plain Pitch Pine Barrens  
1849 | #ed00e5 | Central Atlantic Coastal Plain Maritime Forest  
1850 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1851 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1852 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1853 | #e55e63 | Eastern Serpentine Woodland  
1854 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1855 | #ed00b3 | Northern Atlantic Coastal Plain Maritime Forest  
1856 | #ff99e5 | Central Appalachian Alkaline Glade and Woodland  
1857 | #641f57 | Northern Atlantic Coastal Plain Dune and Swale  
1858 | #8fed29 | Central Atlantic Coastal Plain Wet Longleaf Pine Savanna and Flatwoods  
1859 | #ff7d00 | Atlantic Coastal Plain Peatland Pocosin and Canebrake  
1860 | #444f91 | Atlantic Coastal Plain Streamhead Seepage Swamp-Pocosin-Baygall  
1861 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1862 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1863 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
1864 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
1865 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1866 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1867 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1868 | #ab6138 | Gulf and Atlantic Coastal Plain Sparsely Vegetated Systems  
1869 | #63d6ff | Central Atlantic Coastal Plain Nonriverine Swamp and Wet Hardwood Forest  
1870 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1871 | #b5e3c2 | Southern Appalachian Oak Forest  
1872 | #63c77d | Southern Piedmont Mesic Forest  
1873 | #bab894 | Allegheny-Cumberland Dry Oak Forest and Woodland  
1874 | #8ab1ff | Southern and Central Appalachian Cove Forest  
1875 | #b482b4 | Central and Southern Appalachian Montane Oak Forest  
1876 | #478794 | South-Central Interior Mesophytic Forest  
1877 | #9c9c9c | Appalachian Shale Barrens  
1878 | #902bb5 | Central and Southern Appalachian Spruce-Fir Forest  
1879 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
1880 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
1881 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
1882 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1883 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1884 | #de997a | Southern Ridge and Valley/Cumberland Dry Calcareous Forest  
1885 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1886 | #ff99e5 | Central Appalachian Alkaline Glade and Woodland  
1887 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1888 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1889 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1890 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1891 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1892 | #478794 | South-Central Interior Mesophytic Forest  
1893 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1894 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1895 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1896 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1897 | #82a064 | Acadian Low-Elevation Spruce-Fir-Hardwood Forest  
1898 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1899 | #ff99e5 | Central Appalachian Alkaline Glade and Woodland  
1900 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1901 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1902 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1903 | #6a008a | Boreal Acidic Peatland Systems  
1904 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1905 | #e8bdff | Laurentian-Acadian Alkaline Conifer-Hardwood Swamp  
1906 | #7af5ca | Great Lakes Coastal Marsh Systems  
1907 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1908 | #d3ed26 | North-Central Interior Wet Flatwoods  
1909 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1910 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1911 | #009c2c | North-Central Interior Beech-Maple Forest  
1912 | #bab894 | Allegheny-Cumberland Dry Oak Forest and Woodland  
1913 | #478794 | South-Central Interior Mesophytic Forest  
1914 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1915 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1916 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1917 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1918 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
1919 | #d3ed26 | North-Central Interior Wet Flatwoods  
1920 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1921 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1922 | #a1705a | Northern Atlantic Coastal Plain Hardwood Forest  
1923 | #ffa552 | Northern Atlantic Coastal Plain Pitch Pine Barrens  
1924 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1925 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1926 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1927 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1928 | #82a064 | Acadian Low-Elevation Spruce-Fir-Hardwood Forest  
1929 | #906bb5 | Acadian-Appalachian Montane Spruce-Fir Forest  
1930 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1931 | #ed00b3 | Northern Atlantic Coastal Plain Maritime Forest  
1932 | #641f57 | Northern Atlantic Coastal Plain Dune and Swale  
1933 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1934 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1935 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1936 | #6a008a | Boreal Acidic Peatland Systems  
1937 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1938 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1939 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1940 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1941 | #d3ed26 | North-Central Interior Wet Flatwoods  
1942 | #e8a0ff | Laurentian-Acadian Swamp Systems  
1943 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1944 | #d7b964 | Northeastern Interior Dry-Mesic Oak Forest  
1945 | #ffc452 | Northeastern Interior Pine Barrens  
1946 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1947 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1948 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1949 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1950 | #82a064 | Acadian Low-Elevation Spruce-Fir-Hardwood Forest  
1951 | #906bb5 | Acadian-Appalachian Montane Spruce-Fir Forest  
1952 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1953 | #96ffe7 | Acadian-Appalachian Subalpine Woodland and Heath-Krummholz  
1954 | #ff99e5 | Central Appalachian Alkaline Glade and Woodland  
1955 | #e3eb75 | Great Lakes Alvar  
1956 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1957 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1958 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1959 | #6a008a | Boreal Acidic Peatland Systems  
1960 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1961 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1962 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1963 | #d3ed26 | North-Central Interior Wet Flatwoods  
1964 | #e8a0ff | Laurentian-Acadian Swamp Systems  
1965 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
1966 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
1967 | #009c2c | North-Central Interior Beech-Maple Forest  
1968 | #e6d58a | North-Central Interior Oak Savanna  
1969 | #ffebb0 | North-Central Oak Barrens  
1970 | #ebff00 | Great Lakes Wet-Mesic Lakeplain Prairie  
1971 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
1972 | #e8ffc4 | Central Tallgrass Prairie  
1973 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
1974 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1975 | #7af5ca | Great Lakes Coastal Marsh Systems  
1976 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
1977 | #d3ed26 | North-Central Interior Wet Flatwoods  
1978 | #4ce600 | Laurentian-Acadian Northern Hardwoods Forest  
1979 | #a1705a | Northern Atlantic Coastal Plain Hardwood Forest  
1980 | #ff8c8c | Boreal Jack Pine-Black Spruce Forest  
1981 | #ffc452 | Northeastern Interior Pine Barrens  
1982 | #ffbfbf | Laurentian-Acadian Northern Pine(-Oak) Forest  
1983 | #d0ff63 | Laurentian-Acadian Pine-Hemlock-Hardwood Forest  
1984 | #00ffdc | Central Appalachian Dry Oak-Pine Forest  
1985 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
1986 | #82a064 | Acadian Low-Elevation Spruce-Fir-Hardwood Forest  
1987 | #906bb5 | Acadian-Appalachian Montane Spruce-Fir Forest  
1988 | #ff004d | Central Appalachian Pine-Oak Rocky Woodland  
1989 | #c8037d | Acadian-Appalachian Alpine Tundra  
1990 | #96ffe7 | Acadian-Appalachian Subalpine Woodland and Heath-Krummholz  
1991 | #641f57 | Northern Atlantic Coastal Plain Dune and Swale  
1992 | #24ff14 | Central Interior and Appalachian Riparian Systems  
1993 | #7a8ff5 | Laurentian-Acadian Floodplain Systems  
1994 | #6a008a | Boreal Acidic Peatland Systems  
1995 | #cf3dff | Central Interior and Appalachian Swamp Systems  
1996 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
1997 | #ffeb00 | Gulf and Atlantic Coastal Plain Tidal Marsh Systems  
1998 | #00a86b | Laurentian-Acadian Shrub-Herbaceous Wetland Systems  
1999 | #e8a0ff | Laurentian-Acadian Swamp Systems  
2000 | #b89c21 | Southern Interior Low Plateau Dry-Mesic Oak Forest  
2001 | #a39c2e | Southern Appalachian Northern Hardwood Forest  
2002 | #b5e3c2 | Southern Appalachian Oak Forest  
2003 | #bab894 | Allegheny-Cumberland Dry Oak Forest and Woodland  
2004 | #8ab1ff | Southern and Central Appalachian Cove Forest  
2005 | #478794 | South-Central Interior Mesophytic Forest  
2006 | #7547c5 | Southern Appalachian Montane Pine Forest and Woodland  
2007 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
2008 | #e52600 | Central Interior Highlands Dry Acidic Glade and Barrens  
2009 | #d6ff91 | Appalachian (Hemlock-)Northern Hardwood Forest  
2010 | #de997a | Southern Ridge and Valley/Cumberland Dry Calcareous Forest  
2011 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2012 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2013 | #24ff14 | Central Interior and Appalachian Riparian Systems  
2014 | #cf3dff | Central Interior and Appalachian Swamp Systems  
2015 | #737300 | Ozark-Ouachita Dry-Mesic Oak Forest  
2016 | #b89c21 | Southern Interior Low Plateau Dry-Mesic Oak Forest  
2017 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2018 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
2019 | #009c2c | North-Central Interior Beech-Maple Forest  
2020 | #eda166 | North-Central Interior Maple-Basswood Forest  
2021 | #478794 | South-Central Interior Mesophytic Forest  
2022 | #9ced26 | South-Central Interior/Upper Coastal Plain Flatwoods  
2023 | #614500 | Ozark-Ouachita Dry Oak Woodland  
2024 | #e6d58a | North-Central Interior Oak Savanna  
2025 | #ffebb0 | North-Central Oak Barrens  
2026 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2027 | #ebff00 | Great Lakes Wet-Mesic Lakeplain Prairie  
2028 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
2029 | #e8ffc4 | Central Tallgrass Prairie  
2030 | #baed26 | South-Central Interior/Upper Coastal Plain Wet Flatwoods  
2031 | #b50000 | Great Lakes Wooded Dune and Swale  
2032 | #4baabe | Eastern Great Plains Floodplain Systems  
2033 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2034 | #24ff14 | Central Interior and Appalachian Riparian Systems  
2035 | #6a7500 | Paleozoic Plateau Bluff and Talus  
2036 | #d3ed26 | North-Central Interior Wet Flatwoods  
2037 | #737300 | Ozark-Ouachita Dry-Mesic Oak Forest  
2038 | #895a44 | Crosstimbers Oak Forest and Woodland  
2039 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2040 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
2041 | #eda166 | North-Central Interior Maple-Basswood Forest  
2042 | #00874a | Ozark-Ouachita Mesic Hardwood Forest  
2043 | #ffebb0 | North-Central Oak Barrens  
2044 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2045 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
2046 | #e8ffc4 | Central Tallgrass Prairie  
2047 | #874b78 | Southeastern Great Plains Tallgrass Prairie  
2048 | #4baabe | Eastern Great Plains Floodplain Systems  
2049 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2050 | #941433 | Eastern Great Plains Wet Meadow-Prairie-Marsh  
2051 | #d3ed26 | North-Central Interior Wet Flatwoods  
2052 | #dc0000 | Western Great Plains Dry Bur Oak Forest and Woodland  
2053 | #a900e6 | Western Great Plains Sandhill Steppe  
2054 | #70a870 | Central Mixedgrass Prairie  
2055 | #f5daa9 | Western Great Plains Sand Prairie  
2056 | #cdcd66 | Western Great Plains Shortgrass Prairie  
2057 | #f5f596 | Western Great Plains Tallgrass Prairie  
2058 | #6699cd | Western Great Plains Floodplain Systems  
2059 | #895a44 | Crosstimbers Oak Forest and Woodland  
2060 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2061 | #eda166 | North-Central Interior Maple-Basswood Forest  
2062 | #e8ffc4 | Central Tallgrass Prairie  
2063 | #874b78 | Southeastern Great Plains Tallgrass Prairie  
2064 | #4baabe | Eastern Great Plains Floodplain Systems  
2065 | #941433 | Eastern Great Plains Wet Meadow-Prairie-Marsh  
2066 | #68009c | Western Great Plains Depressional Wetland Systems  
2067 | #b89c21 | Southern Interior Low Plateau Dry-Mesic Oak Forest  
2068 | #d994ab | East Gulf Coastal Plain Northern Loess Plain Oak-Hickory Upland  
2069 | #decd95 | East Gulf Coastal Plain Northern Dry Upland Hardwood Forest  
2070 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2071 | #009c2c | North-Central Interior Beech-Maple Forest  
2072 | #478794 | South-Central Interior Mesophytic Forest  
2073 | #a87c23 | East Gulf Coastal Plain Northern Mesic Hardwood Slope Forest  
2074 | #9ced26 | South-Central Interior/Upper Coastal Plain Flatwoods  
2075 | #e8a1d4 | East Gulf Coastal Plain Northern Loess Bluff Forest  
2076 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
2077 | #bf9747 | Southern Coastal Plain Mesic Slope Forest  
2078 | #e52600 | Central Interior Highlands Dry Acidic Glade and Barrens  
2079 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2080 | #c7e394 | Bluegrass Savanna and Woodland  
2081 | #e8e38a | Pennyroyal Karst Plain Prairie and Barrens  
2082 | #fcf5ab | East Gulf Coastal Plain Jackson Plain Prairie and Barrens  
2083 | #baed26 | South-Central Interior/Upper Coastal Plain Wet Flatwoods  
2084 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2085 | #24ff14 | Central Interior and Appalachian Riparian Systems  
2086 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
2087 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
2088 | #cf3dff | Central Interior and Appalachian Swamp Systems  
2089 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
2090 | #006b52 | Mississippi River Alluvial Plain Dry-Mesic Loess Slope Forest  
2091 | #d3ed26 | North-Central Interior Wet Flatwoods  
2092 | #b89c21 | Southern Interior Low Plateau Dry-Mesic Oak Forest  
2093 | #d994ab | East Gulf Coastal Plain Northern Loess Plain Oak-Hickory Upland  
2094 | #decd95 | East Gulf Coastal Plain Northern Dry Upland Hardwood Forest  
2095 | #b5e3c2 | Southern Appalachian Oak Forest  
2096 | #bab894 | Allegheny-Cumberland Dry Oak Forest and Woodland  
2097 | #8ab1ff | Southern and Central Appalachian Cove Forest  
2098 | #b482b4 | Central and Southern Appalachian Montane Oak Forest  
2099 | #478794 | South-Central Interior Mesophytic Forest  
2100 | #a87c23 | East Gulf Coastal Plain Northern Mesic Hardwood Slope Forest  
2101 | #f5e7ba | Southern Coastal Plain Dry Upland Hardwood Forest  
2102 | #98b000 | East Gulf Coastal Plain Interior Upland Longleaf Pine Woodland  
2103 | #8fa11a | Southeastern Interior Longleaf Pine Woodland  
2104 | #ffc861 | Southern Appalachian Low-Elevation Pine Forest  
2105 | #d3baff | Southern Piedmont Dry Oak(-Pine) Forest  
2106 | #de997a | Southern Ridge and Valley/Cumberland Dry Calcareous Forest  
2107 | #f2f252 | Nashville Basin Limestone Glade and Woodland  
2108 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2109 | #f2f529 | Alabama Ketona Glade and Woodland  
2110 | #f2eda8 | Western Highland Rim Prairie and Barrens  
2111 | #fcfcba | Eastern Highland Rim Prairie and Barrens  
2112 | #baed26 | South-Central Interior/Upper Coastal Plain Wet Flatwoods  
2113 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2114 | #24ff14 | Central Interior and Appalachian Riparian Systems  
2115 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
2116 | #cf3dff | Central Interior and Appalachian Swamp Systems  
2117 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2118 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
2119 | #eda166 | North-Central Interior Maple-Basswood Forest  
2120 | #a8a800 | Western Great Plains Wooded Draw and Ravine  
2121 | #e6d58a | North-Central Interior Oak Savanna  
2122 | #ffebb0 | North-Central Oak Barrens  
2123 | #d6009d | North-Central Interior Sand and Gravel Tallgrass Prairie  
2124 | #b8841d | Northern Tallgrass Prairie  
2125 | #e8ffc4 | Central Tallgrass Prairie  
2126 | #4baabe | Eastern Great Plains Floodplain Systems  
2127 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2128 | #cf3dff | Central Interior and Appalachian Swamp Systems  
2129 | #941433 | Eastern Great Plains Wet Meadow-Prairie-Marsh  
2130 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
2131 | #6a7500 | Paleozoic Plateau Bluff and Talus  
2132 | #737300 | Ozark-Ouachita Dry-Mesic Oak Forest  
2133 | #895a44 | Crosstimbers Oak Forest and Woodland  
2134 | #b0a3de | North-Central Interior Dry-Mesic Oak Forest and Woodland  
2135 | #b3cf8f | North-Central Interior Dry Oak Forest and Woodland  
2136 | #002673 | Ouachita Montane Oak Forest  
2137 | #eda166 | North-Central Interior Maple-Basswood Forest  
2138 | #b59e8f | West Gulf Coastal Plain Mesic Hardwood Forest  
2139 | #00874a | Ozark-Ouachita Mesic Hardwood Forest  
2140 | #614500 | Ozark-Ouachita Dry Oak Woodland  
2141 | #c4a464 | Ozark-Ouachita Shortleaf Pine-Oak Forest and Woodland  
2142 | #64a800 | West Gulf Coastal Plain Pine-Hardwood Forest  
2143 | #d1d900 | West Gulf Coastal Plain Sandhill Oak and Shortleaf Pine Forest and Woodland  
2144 | #e6d58a | North-Central Interior Oak Savanna  
2145 | #ffeb14 | Central Interior Highlands Calcareous Glade and Barrens  
2146 | #ff78bb | Arkansas Valley Prairie and Woodland - Prairie  
2147 | #cc8ab3 | Arkansas Valley Prairie and Woodland - Woodland  
2148 | #e8ffc4 | Central Tallgrass Prairie  
2149 | #874b78 | Southeastern Great Plains Tallgrass Prairie  
2150 | #ff006e | West Gulf Coastal Plain Northern Calcareous Prairie  
2151 | #63eb61 | West Gulf Coastal Plain Pine-Hardwood Flatwoods  
2152 | #00bfb0 | Central Interior and Appalachian Floodplain Systems  
2153 | #30ed38 | South-Central Interior Large Floodplain  
2154 | #24ff14 | Central Interior and Appalachian Riparian Systems  
2155 | #6677cd | Gulf and Atlantic Coastal Plain Floodplain Systems  
2156 | #abb9eb | Gulf and Atlantic Coastal Plain Small Stream Riparian Systems  
2157 | #66d4b3 | Gulf and Atlantic Coastal Plain Swamp Systems  
2158 | #f09614 | Central Interior and Appalachian Shrub-Herbaceous Wetland Systems  
2159 | #267300 | West Gulf Coastal Plain Nonriverine Wet Hardwood Flatwoods  
2160 | #448970 | Ozark-Ouachita Shortleaf Pine-Bluestem Woodland  
2161 | #af381c | Alaska Arctic Mesic Alder Shrubland  
2162 | #ccaf93 | Alaska Arctic Mesic-Wet Willow Shrubland  
2163 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Infrequent Fire  
2164 | #bfbfbf | Alaska Arctic Mesic Sedge-Willow Tundra  
2165 | #f9efe5 | Alaska Arctic Mesic Sedge-Dryas Tundra  
2166 | #e5e5f9 | Alaska Arctic Acidic Sparse Tundra  
2167 | #f2f2f2 | Alaska Arctic Non-Acidic Sparse Tundra  
2168 | #c1b7e8 | Alaska Arctic Lichen Tundra  
2169 | #edd8ad | Alaska Arctic Acidic Dryas Dwarf-Shrubland  
2170 | #ffe2c1 | Alaska Arctic Non-Acidic Dryas Dwarf-Shrubland  
2171 | #edc191 | Alaska Arctic Dwarf-Shrubland - Infrequent Fire  
2172 | #bfd8d8 | Alaska Arctic Tussock Tundra - Infrequent Fire  
2173 | #00cccc | Alaska Arctic Pendantgrass Freshwater Marsh  
2174 | #c1ffc1 | Alaska Arctic Wet Sedge Meadow  
2175 | #eded00 | Alaska Arctic Mesic Herbaceous Meadow  
2176 | #ff8247 | Alaska Arctic Coastal Sedge-Dwarf-Shrubland  
2177 | #e0eded | Alaska Arctic Wet Sedge-Sphagnum Peatland  
2178 | #c1cccc | Alaska Arctic Dwarf-Shrub-Sphagnum Peatland  
2179 | #00bfff | Alaska Arctic Sedge Freshwater Marsh  
2180 | #afe2ff | Alaska Arctic Polygonal Ground Wet Sedge Tundra  
2181 | #e2ffe2 | Alaska Arctic Polygonal Ground Shrub-Tussock Tundra  
2182 | #fff28e | Alaska Arctic Marine Beach and Beach Meadow  
2183 | #ede0e5 | Alaska Arctic Tidal Marsh  
2184 | #63b7ff | Alaska Arctic Coastal Brackish Meadow  
2185 | #0f4f8c | Alaska Arctic Floodplain  
2186 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2187 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2188 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2189 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2190 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2191 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2192 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2193 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2194 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2195 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2196 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2197 | #af381c | Alaska Arctic Mesic Alder Shrubland  
2198 | #ccaf93 | Alaska Arctic Mesic-Wet Willow Shrubland  
2199 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Infrequent Fire  
2200 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Frequent Fire  
2201 | #bfbfbf | Alaska Arctic Mesic Sedge-Willow Tundra  
2202 | #f9efe5 | Alaska Arctic Mesic Sedge-Dryas Tundra  
2203 | #e5e5f9 | Alaska Arctic Acidic Sparse Tundra  
2204 | #f2f2d8 | Alaska Arctic Non-Acidic Sparse Tundra  
2205 | #c1b7e8 | Alaska Arctic Lichen Tundra  
2206 | #edd8ad | Alaska Arctic Acidic Dryas Dwarf-Shrubland  
2207 | #ffe2c1 | Alaska Arctic Non-Acidic Dryas Dwarf-Shrubland  
2208 | #edc191 | Alaska Arctic Dwarf-Shrubland - Frequent Fire  
2209 | #edc191 | Alaska Arctic Dwarf-Shrubland - Infrequent Fire  
2210 | #bfd8d8 | Alaska Arctic Tussock Tundra - Frequent Fire  
2211 | #bfd8d8 | Alaska Arctic Tussock Tundra - Infrequent Fire  
2212 | #00cccc | Alaska Arctic Pendantgrass Freshwater Marsh  
2213 | #c1ffc1 | Alaska Arctic Wet Sedge Meadow  
2214 | #eded00 | Alaska Arctic Mesic Herbaceous Meadow  
2215 | #ff8247 | Alaska Arctic Coastal Sedge-Dwarf-Shrubland  
2216 | #e0eded | Alaska Arctic Wet Sedge-Sphagnum Peatland  
2217 | #c1cccc | Alaska Arctic Dwarf-Shrub-Sphagnum Peatland  
2218 | #e0ede0 | Alaska Arctic Permafrost Plateau Dwarf-Shrub Lichen Tundra  
2219 | #00bfff | Alaska Arctic Sedge Freshwater Marsh  
2220 | #afe2ff | Alaska Arctic Polygonal Ground Wet Sedge Tundra  
2221 | #e2ffe2 | Alaska Arctic Polygonal Ground Shrub-Tussock Tundra  
2222 | #ede0e5 | Alaska Arctic Tidal Marsh  
2223 | #63b7ff | Alaska Arctic Coastal Brackish Meadow  
2224 | #e58c4c | Alaska Arctic Active Inland Dune  
2225 | #1c87ed | Alaska Arctic Large River Floodplain  
2226 | #0f4f8c | Alaska Arctic Floodplain  
2227 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2228 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2229 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2230 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2231 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Higher Elevations  
2232 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2233 | #ba6b59 | Alaska Sub-boreal Mesic Subalpine Alder Shrubland  
2234 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2235 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2236 | #ffff00 | Western North American Boreal Dry Grassland  
2237 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2238 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2239 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2240 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2241 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2242 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2243 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2244 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2245 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2246 | #efe58c | Western North American Boreal Alpine Mesic Herbaceous Meadow  
2247 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2248 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2249 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2250 | #af381c | Alaska Arctic Mesic Alder Shrubland  
2251 | #ccaf93 | Alaska Arctic Mesic-Wet Willow Shrubland  
2252 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Frequent Fire  
2253 | #bfbfbf | Alaska Arctic Mesic Sedge-Willow Tundra  
2254 | #f9efe5 | Alaska Arctic Mesic Sedge-Dryas Tundra  
2255 | #e5e5f9 | Alaska Arctic Acidic Sparse Tundra  
2256 | #f2f2d8 | Alaska Arctic Non-Acidic Sparse Tundra  
2257 | #c1b7e8 | Alaska Arctic Lichen Tundra  
2258 | #edd8ad | Alaska Arctic Acidic Dryas Dwarf-Shrubland  
2259 | #ffe2c1 | Alaska Arctic Non-Acidic Dryas Dwarf-Shrubland  
2260 | #edc191 | Alaska Arctic Dwarf-Shrubland - Frequent Fire  
2261 | #bfd8d8 | Alaska Arctic Tussock Tundra - Frequent Fire  
2262 | #00cccc | Alaska Arctic Pendantgrass Freshwater Marsh  
2263 | #c1ffc1 | Alaska Arctic Wet Sedge Meadow  
2264 | #eded00 | Alaska Arctic Mesic Herbaceous Meadow  
2265 | #00bfff | Alaska Arctic Sedge Freshwater Marsh  
2266 | #afe2ff | Alaska Arctic Polygonal Ground Wet Sedge Tundra  
2267 | #e2ffe2 | Alaska Arctic Polygonal Ground Shrub-Tussock Tundra  
2268 | #0f4f8c | Alaska Arctic Floodplain  
2269 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2270 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2271 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2272 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2273 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Lower Elevations  
2274 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Higher Elevations  
2275 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2276 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2277 | #ba6b59 | Alaska Sub-Boreal Mesic Subalpine Alder Shrubland  
2278 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2279 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2280 | #ffff00 | Western North American Boreal Dry Grassland  
2281 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2282 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2283 | #6bf2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2284 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2285 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2286 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2287 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2288 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2289 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2290 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2291 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2293 | #efe58c | Western North American Boreal Alpine Mesic Herbaceous Meadow  
2294 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2295 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2296 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2297 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2298 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2299 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2300 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Lower Elevations  
2301 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Higher Elevations  
2302 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2303 | #ba6b59 | Alaska Sub-Boreal Mesic Subalpine Alder Shrubland  
2304 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2305 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2306 | #f2a360 | Western North American Boreal Active Inland Dune  
2307 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2308 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2309 | #6bf2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2310 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2311 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2312 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2313 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2314 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2315 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2316 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2317 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2318 | #efe58c | Western North American Boreal Alpine Mesic Herbaceous Meadow  
2319 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2320 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2321 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2322 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2323 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2324 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2325 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2326 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2327 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2328 | #ba6d5b | Alaska Sub-boreal Mesic Subalpine Alder Shrubland  
2329 | #a52828 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2330 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2331 | #7fffd3 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2332 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2333 | #6df2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2334 | #63f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2335 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2336 | #a021ef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2337 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2338 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2339 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2340 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2341 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2342 | #af381c | Alaska Arctic Mesic Alder Shrubland  
2343 | #ccaf93 | Alaska Arctic Mesic-Wet Willow Shrubland  
2344 | #fff9cc | Alaskan Pacific Maritime Mesic Herbaceous Meadow  
2345 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Frequent Fire  
2346 | #bfbfbf | Alaska Arctic Mesic Sedge-Willow Tundra  
2347 | #e5e5f9 | Alaska Arctic Acidic Sparse Tundra  
2348 | #c1b7e8 | Alaska Arctic Lichen Tundra  
2349 | #edd8ad | Alaska Arctic Acidic Dryas Dwarf-Shrubland  
2350 | #edc191 | Alaska Arctic Dwarf-Shrubland - Frequent Fire  
2351 | #bfd8d8 | Alaska Arctic Tussock Tundra - Frequent Fire  
2352 | #00cccc | Alaska Arctic Pendantgrass Freshwater Marsh  
2353 | #c1ffc1 | Alaska Arctic Wet Sedge Meadow  
2354 | #eded00 | Alaska Arctic Mesic Herbaceous Meadow  
2355 | #ff8247 | Alaska Arctic Coastal Sedge-Dwarf-Shrubland  
2356 | #e0eded | Alaska Arctic Wet Sedge-Sphagnum Peatland  
2357 | #c1cccc | Alaska Arctic Dwarf-Shrub-Sphagnum Peatland  
2358 | #e0ede0 | Alaska Arctic Permafrost Plateau Dwarf-Shrub Lichen Tundra  
2359 | #00bfff | Alaska Arctic Sedge Freshwater Marsh  
2360 | #afe2ff | Alaska Arctic Polygonal Ground Wet Sedge Tundra  
2361 | #e2ffe2 | Alaska Arctic Polygonal Ground Shrub-Tussock Tundra  
2362 | #fff28e | Alaska Arctic Marine Beach and Beach Meadow  
2363 | #ede0e5 | Alaska Arctic Tidal Marsh  
2364 | #63b7ff | Alaska Arctic Coastal Brackish Meadow  
2365 | #1c87ed | Alaska Arctic Large River Floodplain  
2366 | #0f4f8c | Alaska Arctic Floodplain  
2367 | #f2f2f2 | Alaska Arctic Bedrock and Talus  
2368 | #4c3833 | Aleutian Volcanic Rock and Talus  
2369 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2370 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Alaska Sub-boreal  
2371 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2372 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2373 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Alaska Sub-boreal  
2374 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2375 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Lower Elevations  
2376 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Higher Elevations  
2377 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2378 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2379 | #ba6b59 | Alaska Sub-Boreal Mesic Subalpine Alder Shrubland  
2380 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2381 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Alaska Sub-boreal  
2382 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2383 | #ffff00 | Western North American Boreal Dry Grassland  
2384 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2385 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Alaska Sub-boreal  
2386 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2387 | #6bf2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2388 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2389 | #59edd1 | Western North American Boreal Herbaceous Fen - Alaska Sub-Boreal Complex  
2390 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2391 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Alaska Sub-boreal Complex  
2392 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2393 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2394 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2395 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2396 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2397 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2399 | #efe58c | Western North American Boreal Alpine Mesic Herbaceous Meadow  
2400 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2401 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2402 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2403 | #006300 | Aleutian Kenai Birch-Cottonwood-Poplar Forest  
2404 | #d1b28c | Alaskan Pacific Maritime Alpine Dwarf-Shrubland  
2405 | #edc600 | Alaska Sub-boreal and Maritime Alpine Mesic Herbaceous Meadow  
2406 | #00ff00 | Alaskan Pacific Maritime Sitka Spruce Forest  
2407 | #005600 | Alaskan Pacific Maritime Western Hemlock Forest  
2408 | #3f9900 | Alaskan Pacific Maritime Mountain Hemlock Forest - Southeast  
2409 | #7fff00 | Alaska Sub-boreal White Spruce-Hardwood Forest  
2410 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2411 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Alaska Sub-boreal  
2412 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2413 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2414 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Alaska Sub-boreal  
2415 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2416 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Lower Elevations  
2417 | #00e800 | Western North American Boreal Dry Aspen-Steppe Bluff - Higher Elevations  
2418 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2419 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2420 | #ba6b59 | Alaska Sub-Boreal Mesic Subalpine Alder Shrubland  
2421 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2422 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Alaska Sub-boreal  
2423 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2424 | #ffff00 | Western North American Boreal Dry Grassland  
2425 | #f2a360 | Western North American Boreal Active Inland Dune  
2426 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Boreal  
2427 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Alaska Sub-boreal  
2428 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2429 | #6bf2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2430 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2431 | #59edd1 | Western North American Boreal Herbaceous Fen - Alaska Sub-Boreal Complex  
2432 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Boreal Complex  
2433 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Alaska Sub-boreal Complex  
2434 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2435 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2436 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2437 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2438 | #d8e5d8 | Western North American Boreal Wet Black Spruce-Tussock Woodland  
2439 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2441 | #efe58c | Western North American Boreal Alpine Mesic Herbaceous Meadow  
2442 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2443 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2444 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2445 | #005600 | Alaskan Pacific Maritime Western Hemlock Forest  
2446 | #7fff00 | Alaska Sub-boreal White Spruce-Hardwood Forest  
2447 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2448 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2449 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Alaska Sub-boreal  
2450 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2451 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2452 | #ba6b59 | Alaska Sub-Boreal Mesic Subalpine Alder Shrubland  
2453 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Alaska Sub-boreal  
2454 | #ffd600 | Western North American Sub-boreal Mesic Bluejoint Meadow  
2455 | #ffff00 | Western North American Boreal Dry Grassland  
2456 | #7fffd1 | Western North American Boreal Montane Floodplain Forest and Shrubland - Alaska Sub-boreal  
2457 | #6bf2d1 | Western North American Boreal Riparian Stringer Forest and Shrubland  
2458 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2459 | #59edd1 | Western North American Boreal Herbaceous Fen - Alaska Sub-Boreal Complex  
2460 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-tree Peatland - Alaska Sub-boreal Complex  
2461 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2462 | #ed82ed | Western North American Boreal Deciduous Shrub Swamp  
2463 | #efffef | Western North American Boreal Low Shrub-Tussock Tundra  
2464 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2465 | #ccd8cc | Western North American Boreal Alpine Dwarf-Shrub Summit  
2467 | #f2d1ad | Western North American Boreal Alpine Ericaceous Dwarf-Shrubland - Complex  
2468 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2469 | #afe0e5 | Western North American Boreal Alpine Floodplain - Higher Elevations  
2470 | #d1b28c | Alaskan Pacific Maritime Alpine Dwarf-Shrubland  
2471 | #3f9900 | Alaska Sub-boreal Mountain Hemlock Forest - Northern  
2472 | #3f9900 | Alaskan Pacific Maritime Mountain Hemlock Forest - Northern  
2473 | #b7cc33 | Alaskan Pacific Maritime Periglacial Woodland and Shrubland  
2474 | #7fffd1 | Alaskan Pacific Maritime Wet Low Shrubland  
2476 | #ed82ed | Temperate Pacific Tidal Salt and Brackish Marsh  
2477 | #ffffe0 | Alaskan Pacific Maritime Alpine Wet Meadow  
2478 | #ffb5bf | Alaskan Pacific Maritime Alpine Floodplain  
2479 | #3fff00 | Alaska Sub-boreal Mountain Hemlock-White Spruce Forest  
2480 | #7fff00 | Alaska Sub-boreal White Spruce-Hardwood Forest  
2481 | #d1d1d1 | North Pacific Alpine and Subalpine Bedrock and Scree  
2482 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Boreal  
2483 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Alaska Sub-boreal  
2484 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2485 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Boreal  
2486 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Alaska Sub-boreal  
2487 | #00d100 | Western North American Boreal Mesic Birch-Aspen Forest  
2488 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2489 | #d1b28c | Alaska Sub-boreal Avalanche Slope Shrubland  
2490 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Boreal  
2491 | #75f9d3 | Western North American Boreal Lowland Large River Floodplain Forest and Shrubland  
2492 | #60f2d1 | Western North American Boreal Shrub and Herbaceous Floodplain Wetland  
2493 | #59edd1 | Western North American Boreal Herbaceous Fen - Alaska Sub-Boreal Complex  
2494 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-Tree Peatland - Boreal Complex  
2495 | #3fe0d1 | Western North American Boreal Black Spruce Dwarf-Tree Peatland - Alaska Sub-boreal Complex  
2496 | #9e1eef | Western North American Boreal Black Spruce Wet-Mesic Slope Woodland  
2497 | #e2f2e2 | Western North American Boreal Tussock Tundra  
2498 | #afe0e5 | Western North American Boreal Alpine Floodplain - Lower Elevations  
2499 | #af381c | Alaska Arctic Mesic Alder Shrubland  
2500 | #ccaf93 | Alaska Arctic Mesic-Wet Willow Shrubland  
2501 | #a0512b | Aleutian Mesic-Wet Willow Shrubland  
2502 | #006300 | Aleutian Kenai Birch-Cottonwood-Poplar Forest  
2503 | #edc600 | Alaska Sub-boreal and Maritime Alpine Mesic Herbaceous Meadow  
2504 | #00ff00 | Alaskan Pacific Maritime Sitka Spruce Forest  
2505 | #fff9cc | Alaskan Pacific Maritime Mesic Herbaceous Meadow  
2506 | #3fe0d1 | Alaskan Pacific Maritime Floodplain Forest and Shrubland  
2508 | #ffbfcc | North Pacific Shrub Swamp  
2509 | #ed82ed | Temperate Pacific Tidal Salt and Brackish Marsh  
2510 | #ffff9e | North Pacific Maritime Eelgrass Bed  
2511 | #adaa00 | Aleutian American Dunegrass Grassland  
2512 | #7fff00 | Alaska Sub-boreal White Spruce-Hardwood Forest  
2513 | #f2ddb2 | Alaska Arctic Scrub Birch-Ericaceous Shrubland - Infrequent Fire  
2514 | #bfbfbf | Alaska Arctic Mesic Sedge-Willow Tundra  
2515 | #e5e5f9 | Alaska Arctic Acidic Sparse Tundra  
2516 | #c1b7e8 | Alaska Arctic Lichen Tundra  
2517 | #edc191 | Alaska Arctic Dwarf-Shrubland - Frequent Fire  
2518 | #bfd8d8 | Alaska Arctic Tussock Tundra - Infrequent Fire  
2519 | #c1ffc1 | Alaska Arctic Wet Sedge Meadow  
2520 | #eded00 | Alaska Arctic Mesic Herbaceous Meadow  
2521 | #ff8247 | Alaska Arctic Coastal Sedge-Dwarf-Shrubland  
2522 | #e0eded | Alaska Arctic Wet Sedge-Sphagnum Peatland  
2523 | #00bfff | Alaska Arctic Sedge Freshwater Marsh  
2524 | #fff28e | Alaska Arctic Marine Beach and Beach Meadow  
2525 | #ede0e5 | Alaska Arctic Tidal Marsh  
2526 | #63b7ff | Alaska Arctic Coastal Brackish Meadow  
2527 | #0f4f8c | Alaska Arctic Floodplain  
2528 | #afcec1 | Aleutian Rocky Headland and Sea Cliff  
2529 | #a0515e | Aleutian Mesic Alder-Salmonberry Shrubland  
2530 | #bf8e28 | Aleutian Crowberry-Herbaceous Heath  
2531 | #d1b28c | Aleutian Mixed Dwarf-Shrub-Herbaceous Shrubland  
2532 | #ffa500 | Aleutian Freshwater Marsh  
2533 | #ffd600 | Aleutian Wet Meadow and Herbaceous Peatland - Complex  
2534 | #ffc691 | Aleutian Marine Beach and Beach Meadow  
2535 | #c9e233 | Aleutian Tidal Marsh  
2536 | #a0512b | Aleutian Shrub and Herbaceous Meadow Floodplain  
2537 | #efa000 | Aleutian Floodplain Forest and Shrubland  
2538 | #ba822b | Aleutian Floodplain Wetland  
2539 | #a09677 | Aleutian Sparse Heath and Fell-Field  
2540 | #a52828 | Aleutian Oval-leaf Blueberry Shrubland  
2541 | #4c3833 | Aleutian Volcanic Rock and Talus  
2542 | #007700 | Western North American Boreal Treeline White Spruce Woodland - Alaska Sub-boreal  
2543 | #00a500 | Western North American Boreal White Spruce-Hardwood Forest  
2544 | #00bc00 | Western North American Boreal Mesic Black Spruce Forest - Alaska Sub-boreal  
2545 | #00ff00 | Western North American Boreal Subalpine Balsam Poplar-Aspen Woodland  
2546 | #a52626 | Western North American Boreal Mesic Scrub Birch-Willow Shrubland - Alaska Sub-boreal  
2547 | #d1b28c | Alaskan Pacific Maritime Alpine Dwarf-Shrubland  
2548 | #00ff00 | Alaskan Pacific Maritime Sitka Spruce Forest  
2549 | #edc600 | Alaska Sub-boreal and Maritime Alpine Mesic Herbaceous Meadow  
2550 | #3f9900 | Alaskan Pacific Maritime Mountain Hemlock Forest - Northern  
2551 | #b7cc33 | Alaskan Pacific Maritime Periglacial Woodland and Shrubland  
2552 | #d1b28c | Alaskan Pacific Maritime Subalpine Alder-Salmonberry Shrubland  
2553 | #38c65e | Alaskan Pacific Maritime Sitka Spruce Beach Ridge  
2554 | #38c65e | Alaskan Pacific Maritime Sitka Spruce Beach Ridge  
2555 | #afe0e5 | Alaskan Pacific Maritime Shrub and Herbaceous Floodplain Wetland  
2556 | #008c00 | Alaskan Pacific Maritime Mountain Hemlock Peatland  
2557 | #008c00 | Alaskan Pacific Maritime Mountain Hemlock Peatland  
2558 | #7fffd1 | Alaskan Pacific Maritime Wet Low Shrubland  
2560 | #e0ffff | Alaskan Pacific Maritime Fen and Wet Meadow  
2561 | #afeded | Temperate Pacific Freshwater Emergent Marsh  
2562 | #ffbfcc | North Pacific Shrub Swamp  
2563 | #ffefdb | Alaskan Pacific Maritime Coastal Meadow and Slough-Levee  
2564 | #ed82ed | Temperate Pacific Tidal Salt and Brackish Marsh  
2565 | #ffffe0 | Alaskan Pacific Maritime Alpine Wet Meadow  
2566 | #ffb5bf | Alaskan Pacific Maritime Alpine Floodplain  
2567 | #7fff00 | Alaska Sub-boreal White Spruce-Hardwood Forest  
2568 | #ffa077 | Alaskan Pacific Maritime Avalanche Slope Shrubland  
2569 | #c9ff70 | Alaskan Pacific Maritime Poorly Drained Conifer Woodland  
2570 | #d1b28c | Alaskan Pacific Maritime Alpine Dwarf-Shrubland  
2571 | #00ff00 | Alaskan Pacific Maritime Sitka Spruce Forest  
2572 | #005600 | Alaskan Pacific Maritime Western Hemlock Forest  
2573 | #3f9900 | Alaskan Pacific Maritime Mountain Hemlock Forest - Northern  
2574 | #6b9368 | Aleutian Mesic Herbaceous Meadow  
2575 | #6b9368 | Aleutian Mesic Herbaceous Meadow  
2576 | #d1b28c | Alaskan Pacific Maritime Subalpine Alder-Salmonberry Shrubland  
2577 | #38c65e | Alaskan Pacific Maritime Sitka Spruce Beach Ridge  
2578 | #3fe0d1 | Alaskan Pacific Maritime Floodplain Forest and Shrubland  
2579 | #56a88c | Alaskan Pacific Maritime Shore Pine Peatland  
2580 | #008c00 | Alaskan Pacific Maritime Mountain Hemlock Peatland  
2581 | #7fffd1 | Alaskan Pacific Maritime Wet Low Shrub  
2582 | #7fffd1 | Alaskan Pacific Maritime Wet Low Shrubland  
2584 | #e0ffff | Alaskan Pacific Maritime Fen and Wet Meadow  
2585 | #afeded | Temperate Pacific Freshwater Emergent Marsh  
2586 | #ffbfcc | North Pacific Shrub Swamp  
2587 | #ffefdb | Alaskan Pacific Maritime Coastal Meadow and Slough-Levee  
2588 | #ed82ed | Temperate Pacific Tidal Salt and Brackish Marsh  
2589 | #ffffe0 | Alaskan Pacific Maritime Alpine Wet Meadow  
2590 | #ffa077 | Alaskan Pacific Maritime Avalanche Slope Shrubland  
2591 | #c9ff70 | Alaskan Pacific Maritime Poorly Drained Conifer Woodland  
2592 | #9e512b | Western North American Boreal Alpine Talus and Bedrock  
2593 | #9e512b | Western North American Boreal Alpine Talus and Bedrock  
2594 | #9e512b | Western North American Boreal Alpine Talus and Bedrock  
2595 | #9e512b | Western North American Boreal Alpine Talus and Bedrock  
2596 | #9e1eef | Hawaii Freshwater Marsh  
2597 | #ff00ff | Hawaii Bog  
2598 | #006300 | Hawaii Lowland Rainforest  
2599 | #007700 | Hawaii Montane Cloud Forest  
2600 | #008e00 | Hawaii Montane Rainforest  
2601 | #a52828 | Hawaii Wet Cliff and Ridge Crest Shrubland  
2602 | #00bc00 | Hawaii Lowland Dry Forest  
2603 | #00d100 | Hawaii Lowland Mesic Forest  
2604 | #00e800 | Hawaii Montane-Subalpine Dry Forest and Woodland - Lava  
2605 | #00ff00 | Hawaii Montane-Subalpine Mesic Forest  
2606 | #aa3f3a | Hawaii Lowland Dry Shrubland  
2607 | #b55949 | Hawaii Lowland Mesic Shrubland  
2608 | #ffd600 | Hawaii Lowland Dry Grassland  
2609 | #ffe200 | Hawaii Lowland Mesic Grassland  
2610 | #ba705b | Hawaii Montane-Subalpine Dry Shrubland  
2611 | #fff200 | Hawaii Montane-Subalpine Dry Grassland  
2612 | #ffff00 | Hawaii Montane-Subalpine Mesic Grassland  
2613 | #c1876b | Hawaii Alpine Dwarf-Shrubland  
2614 | #c99e77 | Hawaii Dry Cliff  
2615 | #afe0e5 | Hawaii Dry Coastal Strand  
2616 | #47d1cc | Hawaii Wet-Mesic Coastal Strand  
2617 | #d1b58c | Hawaii Subalpine Mesic Shrubland  
**Image Properties**
Name | Type | Description  
---|---|---  
BPS_classes | DOUBLE | Class values of the Biophysical Settings.  
BPS_names | STRING | Descriptive names of the Biophysical Settings.  
**Terms of Use**
LANDFIRE data are public domain data with no use restrictions, though if modifications or derivatives of the product(s) are created, then please add some descriptive modifier to the data set to avoid confusion.
Citations:
  * The suggested way to cite LANDFIRE products is specific to each product, so the model for citation is provided, with an example for a particular product. Producer. Year released. Product xxxxx:
    * Individual model name.
    * BpS Models and Descriptions, Online. LANDFIRE. Washington, DC. U.S. Department of Agriculture, Forest Service
    * U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA
    * The Nature Conservancy (Producers). Available- URL. Access date.
Example Citation: LANDFIRE Biophysical Settings. 2018. Biophysical setting 14420: South Texas sand sheet grassland. In: LANDFIRE Biophysical Setting Model: Map zone 36, [Online]. In: BpS Models and Descriptions. In: LANDFIRE. Washington, DC: U.S. Department of Agriculture, Forest Service; U.S. Department of the Interior; U.S. Geological Survey; Arlington, VA: The Nature Conservancy (Producers). Available: <https://www.landfire.gov/bps-models.php> [2018, June 27]. Additional guidance on citation of LANDFIRE products can be found [here](https://landfire.gov/data/citation)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDFIRE/Vegetation/BPS/v1_4_0');
varvisualization={
bands:['BPS'],
};
Map.setCenter(-121.671,40.699,5);
Map.addLayer(dataset,visualization,'BPS');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDFIRE/LANDFIRE_Vegetation_BPS_v1_4_0)
[ LANDFIRE BPS (Biophysical Settings) v1.4.0 ](https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0)
LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy. LANDFIRE (LF) layers are created using predictive landscape models based on extensive …
LANDFIRE/Vegetation/BPS/v1_4_0, doi,fire,forest-biomass,landfire,nature-conservancy,usda,usgs,vegetation,wildfire 
2014-09-01T00:00:00Z/2014-09-01T00:00:00Z
17.52 -175.1 71.48 -63.66 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://landfire.gov/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDFIRE_Vegetation_BPS_v1_4_0)


