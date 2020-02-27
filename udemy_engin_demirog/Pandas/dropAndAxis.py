# -*- coding: utf-8 -*-
import pandas as pd

films = pd.read_csv("sources/imdb-1000.csv")
print("films.columns:")
print(films.columns)
print()

films = films.drop("content_rating",axis=1)

print("films.columns:")
print(films.columns)
print()

print("films.head():")
print(films.head())
print()

films = films.drop([2,3],axis=0)

print("films.head():")
print(films.head())
print()