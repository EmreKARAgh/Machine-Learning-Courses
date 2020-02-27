# -*- coding: utf-8 -*-
import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"
data2 = pd.read_csv(url)

data = data2

print(data['Shape Reported'].value_counts()) #null değerleri drop eder.göstermez
print()

print(data['Shape Reported'].value_counts(dropna=False)) #Boş değerleri göz ardı eder
print()


data['Shape Reported'].fillna("Belirsiz",inplace=True)
print(data['Shape Reported'].value_counts())
print()

