# import af std-moduler
import geopandas as gpd
import pandas as pd
from os.path import join


def readshapefile(filename):
    return gpd.read_file(filename)


def beregn_tilstklas(tilstandsindex):
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


def tilfoj_tilstklas(gdf, in_col_name, out_col_name):
    gdf[out_col_name] = gdf[in_col_name].apply(beregn_tilstklas)
    return gdf


def tilfoj_nattype_nr(gdf, in_col_name, out_col_name):
    gdf[out_col_name] = gdf[in_col_name].str[:4]
    return gdf


def beregn_nattype_areal(gdf, nattype_areal_navn, arealandel_navn):
    gdf[nattype_areal_navn] = (gdf["geometry"].area / 10000) * (
        gdf[arealandel_navn] / 100
    )
    return gdf


def tilfoj_nattype_tilstklas(gdf, basisreg):
    gdf[basisreg.nattype_tilst_klas_navn] = (
        gdf[basisreg.nattype_nr_navn] + " - " + gdf[basisreg.tilstklas_navn].astype(str)
    )
    return gdf


def homogenisergdf(gdf, basisreg):
    if not basisreg.findes_tilstklas:
        gdf = tilfoj_tilstklas(gdf, basisreg.natur_index_navn, basisreg.tilstklas_navn)

    if not basisreg.findes_nattype_nr:
        gdf = tilfoj_nattype_nr(
            gdf, basisreg.nattype_tekst_navn, basisreg.nattype_nr_navn
        )

    gdf = beregn_nattype_areal(
        gdf, basisreg.nattype_areal_navn, basisreg.arealandel_navn
    )

    gdf = tilfoj_nattype_tilstklas(gdf, basisreg)

    return gdf


def lav_klip_polygon(omraade, udt_gdf, udtraek):
    filt = udt_gdf[udtraek.udt_felt_navn] == omraade
    return udt_gdf.loc[filt, "geometry"]


def findes_klipomr(omraade, udt_gdf, udtraek):
    filt = udt_gdf[udtraek.udt_felt_navn] == omraade
    return not udt_gdf.loc[filt].empty


def lav_klip(klip_polygon, gdf):
    return gdf.clip(klip_polygon)


def lav_nattype_tilst_sammendrag(gdf, basisreg):
    return gdf.groupby(basisreg.nattype_tilst_klas_navn)[
        basisreg.nattype_areal_navn
    ].sum()


def lav_resultat_sammendrag(df1, df2, basisreg):
    result_df = pd.merge(
        df1,
        df2,
        how="outer",
        on=basisreg.nattype_tilst_klas_navn,
        suffixes=("_primo", "_ultimo"),
    )
    result_df.fillna(0, inplace=True)
    result_df.sort_values(by=basisreg.nattype_tilst_klas_navn, inplace=True)
    return result_df


def skriv_df_csv(df, omraade, basisreg):
    file_name = join(basisreg.result_path, omraade + basisreg.result_file_suffix)
    df.to_csv(file_name)
    return
