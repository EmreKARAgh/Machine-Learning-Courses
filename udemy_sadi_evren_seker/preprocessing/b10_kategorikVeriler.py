# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


veriler = pd.read_csv('sources/eksikveriler.csv')
print(veriler)

ulke = veriler[['ulke']]
ulke = veriler.iloc[:,0:1]
print(ulke)
print(ulke.values.ravel())

le = LabelEncoder()
ulke_le = le.fit_transform(ulke.values.ravel())
print("\nulke_le:\n" , ulke_le , "\n")

ohe = OneHotEncoder(categories='auto')
ulke_ohe = ohe.fit_transform(ulke).toarray()
print("\nulke_ohe:\n",ulke_ohe, "\n")

ulke_ohe_r = ohe.inverse_transform([[0, 1, 0], [0, 0, 1],[1, 0, 0]])
print("\nulke_ohe_r:\n",ulke_ohe_r, "\n")

