# import af std-moduler
import geopandas as gpd
import pandas as pd
from os.path import join


# import af egne moduler
from Constants import constants as const


def readshapefile(filename):
    return gpd.read_file(filename)


def indlaes(omraader):
    udtraek = const.Udtraek()
    primo = const.Basisreg0406()
    ultimo = const.Basisreg1619()
    udt_gdf = readshapefile(join(udtraek.udt_path, udtraek.udt_file))
    primo_gdf = readshapefile(join(primo.basisreg_path, primo.basisreg_file))
    ultimo_gdf = readshapefile(join(ultimo.basisreg_path, ultimo.basisreg_file))
    print(udt_gdf)

    for omraade in omraader:
        print(omraade)

    return
