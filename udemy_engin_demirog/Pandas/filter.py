# -*- coding: utf-8 -*-
import pandas as pd

films = pd.read_csv("sources/imdb-1000.csv")
print(films.title.head(5))

print("filter:")
print(films[(films.star_rating > 8.5) & (films.star_rating < 9)][["title","star_rating"]].head(5))
print()

print("Query")
print(films.query('star_rating > 8.5 & star_rating < 9')[['title','star_rating']].head(5))
print()

print("GroupBy")
print(films.groupby('genre').star_rating.mean())
print()

