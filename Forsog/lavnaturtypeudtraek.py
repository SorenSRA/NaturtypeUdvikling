# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:21:57 2023

@author: B006207



projectsites_name = "projectsites.shp"
navn_areal_col = "Areal_ha"
navn_nattypeareal_col = "Naturtype_areal"
navn_nattypenr_col = "Na_typenr"
nt0406_pct_col = "pct"
nt1619_pct_col = "Arealandel"
nattype_tilst_col = "Nattype_tilst"



"""



import geopandas as gpd
import pandas as pd


def readshapefile(filename):
    return gpd.read_file(filename)

def lavudtraekclip(gdf, omraader):
    gdf = gdf.set_index("site_name")
    return gdf.loc[udtraek_omraader,['geometry']]
    
def lavbasisreg_clip(basis_gdf, clip_polygoner)    :
    return basis_gdf.clip(clip_polygoner)


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

def dannatypenr(gdf):
    gdf["Na_typenr"] = gdf["Naturtype"].str[:4]
    return gdf
 

def genberegnareal(gdf):
    gdf["Areal_ha"] = gdf['geometry'].area / 10000
    return gdf

def beregnnattypeareal(gdf):
    gdf["Naturtype_areal"] = gdf["pct"] / 100 * gdf["Areal_ha"]
    return gdf

def dannattype_tilstand(gdf):
    gdf["Nattype_tilst"] = gdf["Na_typenr"] + ' - ' + gdf["Naturtilst"].astype(str)
    return gdf



"""
homnogeniser1619()
Basisregistrering 2016-2019 følgende felthomogenisering er nødvendig!
    Feltet/Kolonnen "Arealandel" skal renames til "pct"
    Naturtilstand skal omklassificeres fra index float mellem 0.0 og 1.0 til klasse (1, 2, 3, 4, 5) Felt-navn i Basisreg1619 NaturTilst Nye felt Naturtilst
    NaturtypeNr "2320" - skal oprettes på baggrund Naturtype "2320 - Revling-indlandsklit" Nye felt Na_typenr
"""
def homogeniser1619(gdf):
    gdf = gdf.rename(columns={"Arealandel": "pct"})
    gdf = beregnnaturtilstand(gdf, "NaturTilst", "Naturtilst")
    gdf = dannatypenr(gdf)
    return gdf


"""
klargor_clip()
Basisregistrering 2004-2006 & Basisregistrering 2016-2019
    "genberegnareal()" - Areal af registeringspolygonet skal genberegnes, feltet "Areal_ha" oprettes/genberegnes
    "beregnnattypeareal()" - Areal af naturtypearealet skal beregnes, der skal oprettes et nyt felt feltnavn = "Naturtype_areal"
    "dannatype_tilstand()" - Naturtype - tilstandsklasse feltet skal oprettes, feltnavn = "Nattype_tilst"
"""
def klargor_clip(gdf):
    gdf = genberegnareal(gdf)
    gdf = beregnnattypeareal(gdf)
    gdf = dannattype_tilstand(gdf)
    return gdf

    
def danarealsammendrag(gdf):
    return gdf.groupby('Nattype_tilst')['Areal_ha'].sum()
    

def resultatsammendrag(df_1, df_2):
    return pd.merge(df_1, df_2, \
                      how="outer", \
                      on="Nattype_tilst", \
                      suffixes=("_0406", "_1619"))

def skrivdataframe(df, path, file_name):
    df.to_csv(path+file_name)
    return
    





#indlæser de relevante shape_filer til geopandas dataframes
basis0406_gdf = readshapefile(basisreg_path+basisreg0406_file)
basis1619_gdf = readshapefile(basisreg_path+basisreg1619_file)
udtraek_gdf = readshapefile(udtraek_path+udtraek_file)

udtraek_clip = lavudtraekclip(udtraek_gdf, udtraek_omraader)

basis0406_clip = lavbasisreg_clip(basis0406_gdf, udtraek_clip)
basis1619_clip = lavbasisreg_clip(basis1619_gdf, udtraek_clip)

basis1619_clip = homogeniser1619(basis1619_clip)

basis0406_clip = klargor_clip(basis0406_clip)
basis1619_clip = klargor_clip(basis1619_clip)

sammendrag0406_df = danarealsammendrag(basis0406_clip)
sammendrag1619_df = danarealsammendrag(basis1619_clip)

result = resultatsammendrag(sammendrag0406_df, sammendrag1619_df)
result = result.fillna(0)
result = result.sort_values(by="Nattype_tilst")

skrivdataframe(result, udtraek_path, result_filename+file_ext)

print("Færdigt arebjde")



