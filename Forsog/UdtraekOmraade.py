# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:26:27 2023

@author: B006207
"""


import geopandas as gpd
import matplotlib.pyplot as plt


naturtyper_path = "C:/Filkassen/QGIS/Naturforvaltkonference/LysabenNatur20042006.shp"
udtraek_path = "C:/Filkassen/QGIS/DiverseArbejdsProjekter/UdtraeksPolygoner.shp"

udtraek_omraader = ["NSTMolsBjerge", "WetHab"]
udtraek_omraader = ["NSTMolsBjerge"]




gdfnattyp = gpd.read_file(naturtyper_path)
udtraek_sites = gpd.read_file(udtraek_path)


udtraek_sites = udtraek_sites.set_index("site_name")

clip_polygoner = udtraek_sites.loc[udtraek_omraader,['geometry']]


#plot udtræksområdet
clip_polygoner.plot()
plt.show()

nt0406omraade_clip = gdfnattyp.clip(clip_polygoner)