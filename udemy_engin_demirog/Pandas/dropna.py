# -*- coding: utf-8 -*-
import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"
data2 = pd.read_csv(url)

data = data2

print("null values:")
print(data.isnull().sum())
print()

print("drop all null values")
data = data.dropna()
print()

print("null values:")
print(data.isnull().sum())
print()

data = data2

print("null values:")
print(data.isnull().sum())
print()

print("drop some null values")
data = data.dropna(subset=['City', 'Colors Reported'], how = "all") #her ikisin de null olduğu satırları siler
print()

print("null values:")
print(data.isnull().sum())
print()

data = data2

print("null values:")
print(data.isnull().sum())
print()

print("drop some null values 2")
data = data.dropna(subset=['City', 'Colors Reported'], how = "any") #herhangi birinin null olduğu satırları siler
print()

print("null values:")
print(data.isnull().sum())
print()

