# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("sources/positions.csv")
print(data.describe())

value = np.array([[8.3]]).reshape(-1,1)

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values

regression = RandomForestRegressor(n_estimators=100, random_state=2) #n_estimators= Kaç DesicionTree içersin, random_state= randomu sabitler
regression.fit(level,salary)

print(regression.predict(value))