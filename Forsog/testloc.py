# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:15:23 2023

@author: B006207
"""
shapefiles_path = "C:/SraDiverse/GeoPandas/ShapeFiles/"
projectsites_name = "projectsites.shp"
naturtyper04_06 = "LysabenNatur20042006.shp"
naturtyper16_19 = "LysabenNatur20162019.shp"
navn_areal_col = "Areal_ha"
navn_nattypeareal_col = "Naturtype_areal"
navn_nattypenr_col = "Na_typenr"
nt0406_pct_col = "pct"
nt1619_pct_col = "Arealandel"
nattype_tilst_col = "Nattype_tilst"


nye_felt_navne = {
    "areal_col": "Areal_ha",
    "nattypeareal_col": "Naturtype_areal",
    "nattypenr_col":  "Na_typenr",
    "nattype_tilst_col": "Nattype_tilst"
    }

for k, v in nye_felt_navne.items():
    print(k + '  ' + v)
    
print(nye_felt_navne['areal_col'])

