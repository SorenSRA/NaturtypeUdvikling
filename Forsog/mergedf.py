

import pandas as pd

csvfiles_path = "C:/Filkassen/PythonMm/GeoPandas/"

nt0406_csv = "nt0406.csv"
nt1619_csv = "nt1619.csv"

nt0406_df = pd.read_csv(csvfiles_path+nt0406_csv)
nt1619_df = pd.read_csv(csvfiles_path+nt1619_csv)

result = pd.merge(nt0406_df, nt1619_df, \
                  how="outer", \
                  on="Nattype_tilst", \
                  suffixes=("_0406", "_1619"))


result = result.fillna(0)

result = result.sort_values(by="Nattype_tilst")
