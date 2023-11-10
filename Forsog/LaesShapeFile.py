# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:00:42 2023

@author: soren
"""

import geopandas as gpd
import pandas as pd


def readshapefile(filename):
    return gpd.read_file(filename)


def genberegnareal(gdf, col_name):
    gdf[col_name] = gdf['geometry'].area / 10000
    return gdf


def beregnnattypeareal(gdf, col_name, pct_col, areal_col):
    gdf[col_name] = gdf[pct_col] / 100 * gdf[areal_col]
    return gdf


def dannatypenr(gdf, in_col_name, out_col_name):
    gdf[out_col_name] = gdf[in_col_name].str[:4]
    return gdf
    

def beregntilstvaerdi(tilstandsindex):
    if tilstandsindex >= 0.8:
        return 1
    elif tilstandsindex >= 0.6:
        return 2
    elif tilstandsindex >= 0.4:
        return 3
    elif tilstandsindex >= 0.2:
        return 4
    else:
        return 5


def beregnnaturtilstand(gdf, in_col_name, out_col_name):
    gdf[out_col_name] = gdf[in_col_name].apply(beregntilstvaerdi)
    return gdf


def dannattype_tilstand(gdf, col_name):
    naturtype_fld = "Na_typenr"
    naturtilst_fld = "Naturtilst"

    gdf[col_name] = gdf[naturtype_fld] + ' - ' + gdf[naturtilst_fld].astype(str)
    return gdf
    
    
def danarealsammendrag(gdf):
    return gdf.groupby('Nattype_tilst')['Areal_ha'].sum()
    

    
"""

naturtype_fld = "Na_typenr"
naturtilst_fld = "Naturtilst"


#print(type(nt0406_gdf.loc[0,"Na_typenr"]))
#print(type(str(nt0406_gdf.loc[0,"Naturtilst"])))
nt0406_gdf[nyt_felt] = nt0406_gdf[naturtype_fld] + ' - ' + nt0406_gdf[naturtilst_fld].astype(str)


#nattype_tilst = (nt0406_gdf["Nattype_tilst"].unique())

#nattype_liste = sorted(nattype_tilst)

result0406 = nt0406_gdf.groupby('Nattype_tilst')['Areal_ha'].sum()

"""

#def main():

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



nt0406_gdf = readshapefile(shapefiles_path+naturtyper04_06)
nt1619_gdf = readshapefile(shapefiles_path+naturtyper16_19)

nt0406_gdf = genberegnareal(nt0406_gdf, navn_areal_col)
nt0406_gdf = beregnnattypeareal(nt0406_gdf, navn_nattypeareal_col, nt0406_pct_col, navn_areal_col)
nt0406_gdf = dannattype_tilstand(nt0406_gdf, nattype_tilst_col)
sammendrag0406_df = danarealsammendrag(nt0406_gdf)
print(sammendrag0406_df)

nt1619_gdf = genberegnareal(nt1619_gdf, navn_areal_col)
nt1619_gdf = beregnnattypeareal(nt1619_gdf, navn_nattypeareal_col, nt1619_pct_col, navn_areal_col)
nt1619_gdf = dannatypenr(nt1619_gdf, "Naturtype", navn_nattypenr_col)
nt1619_gdf = beregnnaturtilstand(nt1619_gdf, "NaturTilst", "Naturtilst")
nt1619_gdf = dannattype_tilstand(nt1619_gdf, nattype_tilst_col)
sammendrag1619_df = danarealsammendrag(nt1619_gdf)
print(sammendrag1619_df)

sammendrag0406_df.to_csv(shapefiles_path+'nt0406.csv')
sammendrag1619_df.to_csv(shapefiles_path+'nt1619.csv')



    
        
    
    