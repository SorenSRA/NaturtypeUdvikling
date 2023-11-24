# import af std-moduler
from os.path import join


# import af egne moduler
from Constants import constants as const
from Hjaelpefunc import hjaelpefunc as sra


def lav_sammendrag(omraader):
    udtraek = const.Udtraek()
    primo = const.Basisreg0406()
    ultimo = const.Basisreg1619()
    udt_gdf = sra.readshapefile(join(udtraek.udt_path, udtraek.udt_file))
    primo_gdf = sra.readshapefile(join(primo.basisreg_path, primo.basisreg_file))
    ultimo_gdf = sra.readshapefile(join(ultimo.basisreg_path, ultimo.basisreg_file))
    for omraade in omraader:
        if sra.findes_klipomr(omraade, udt_gdf, udtraek):
            klip_polygon = sra.lav_klip_polygon(omraade, udt_gdf, udtraek)
            clip_primo_gdf = sra.lav_klip(klip_polygon, primo_gdf)
            clip_ultimo_gdf = sra.lav_klip(klip_polygon, ultimo_gdf)
            clip_primo_gdf = sra.homogenisergdf(clip_primo_gdf, primo)
            clip_ultimo_gdf = sra.homogenisergdf(clip_ultimo_gdf, ultimo)
            sammendrag_primo_df = sra.lav_nattype_tilst_sammendrag(
                clip_primo_gdf, primo
            )
            sammendrag_ultimo_df = sra.lav_nattype_tilst_sammendrag(
                clip_ultimo_gdf, ultimo
            )
            resultat_df = sra.lav_resultat_sammendrag(
                sammendrag_primo_df, sammendrag_ultimo_df, primo
            )
            sra.skriv_df_csv(resultat_df, omraade, primo)
            # sra.skriv_df_csv(clip_primo_gdf, omraade + "_primo", primo)
            # sra.skriv_df_csv(clip_ultimo_gdf, omraade + "_ultimo", primo)

            print(f"Nu er csv-fil for område: {omraade} klar")

        else:
            print(f"Område: {omraade} findes ikke i Udtræks-shape-filen")
            print("Vælg en af nedenstående områdenavne")
            print(udt_gdf[udtraek.udt_felt_navn])

    return
