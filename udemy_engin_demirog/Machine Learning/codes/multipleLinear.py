# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("C:/Users/Emre KARA/.spyder-py3/Machine Learning/sources/insurance.csv")
print(data.columns)

## y ekseni
expenses = data.expenses.values.reshape(-1,1)
## x ekseni
ageBmis = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(ageBmis,expenses)
print(regression.predict(np.array([[30,20],[30,21],[20,22],[20,23],[20,24]])))






