from dataclasses import dataclass

@dataclass
class Faelles:
    udtraek_path: str = "C:/Filkassen/QGIS/DiverseArbejdsProjekter/"
    udtraek_file: str = "UdtraeksPolygoner.shp"
    result_file_suffix: str = ".csv"
    basisreg_path: str = "C:/Filkassen/QGIS/Naturforvaltkonference/"

@dataclass
class Basisreg0406(Faelles):
    basisreg_file = "LysabenNatur20042006.shp"

@dataclass
class Basisreg0406(Faelles):
    basisreg_file = "LysabenNatur20162019.shp"


udtraek_omraader = ["ReWet", "WetHab"]
result_filename = "ReWetHab"

