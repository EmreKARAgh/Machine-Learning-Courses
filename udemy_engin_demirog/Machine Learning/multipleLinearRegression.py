# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score


data = pd.read_csv("sources/insurance.csv")
print(data.describe())

value = np.array([[20,16],[20,17]])

expenses = data.expenses.values.reshape(-1,1) #target column

sourceValues = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(sourceValues, expenses)



result = regression.predict(value)
print(result)


