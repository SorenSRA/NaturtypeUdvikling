from dataclasses import dataclass, field


@dataclass
class Faelles:
    result_file_suffix: str = ".csv"
    result_path: str = (
        r"C:\Filkassen\PythonMm\VSCode_projects\NaturtypeUdvikling\Resultater"
    )
    basisreg_path: str = (
        r"C:\Filkassen\PythonMm\VSCode_projects\NaturtypeUdvikling\Data"
    )
    tilstklas_navn: str = "Naturtilst"
    nattype_nr_navn: str = "Na_typenr"
    nattype_areal_navn: str = "Naturtype_Areal_ha"
    nattype_tilst_klas_navn: str = "Naturtype_tilst_klasse"


@dataclass
class Basisreg0406(Faelles):
    basisreg_file: str = "LysabenNatur20042006.shp"
    findes_tilstklas: bool = field(
        default=True
    )  # findes naturtilstandsklasse (1-5) i tabellen
    natur_index_navn: str = "Ej relevant"  # kolonnenavn tilstands_index bruges til beregning af tilstandsklasse, findes allerede
    findes_nattype_nr: bool = field(
        default=True
    )  # findes naturtypenr f.eks. '6230' i tabellen
    nattype_tekst_navn: str = "Ej relevant"  # bruges til af danne nattype_nr ud fra, f.eks. "7140 - Hængesæk" altid første 4-karaktere
    arealandel_navn: str = "pct"


@dataclass
class Basisreg1619(Faelles):
    basisreg_file: str = "LysabenNatur20162019.shp"
    findes_tilstklas: bool = field(
        default=False
    )  # findes naturtilstandsklasse (1-5) i tabellen
    natur_index_navn: str = "NaturTilst"  # kolonnenavn tilstands_index bruges til beregning af tilstandsklasse
    findes_nattype_nr: bool = field(
        default=False
    )  # findes naturtype_nr f.eks. '6230' i tabellen
    nattype_tekst_navn: str = "Naturtype"  # bruges til af danne nattype_nr ud fra, f.eks. "7140 - Hængesæk" altid første 4-karaktere
    arealandel_navn: str = "Arealandel"


@dataclass
class Udtraek:
    udt_path: str = r"C:\Filkassen\PythonMm\VSCode_projects\NaturtypeUdvikling\Data"
    udt_file: str = r"UdtraeksPolygoner.shp"
    udt_felt_navn: str = "site_name"
