# -*- coding: utf-8 -*-
import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"

data = pd.read_csv(url)
print(data.columns)
print(data.isnull().head())
print()

print("null values:")
print(data.isnull().sum())
print()

print("null city value rows:")
print(data[data.City.isnull()])
print()

