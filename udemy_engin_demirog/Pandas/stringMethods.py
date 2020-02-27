# -*- coding: utf-8 -*-

import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"
data2 = pd.read_csv(url)

data = data2

print(data['Shape Reported'].str.contains("oval".upper()))

data['Shape Reported'] = data['Shape Reported'].str.replace("OVAL","OVAAAAAL")
print(data.head())