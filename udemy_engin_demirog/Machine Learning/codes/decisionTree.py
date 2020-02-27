# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("C:/Users/Emre KARA/.spyder-py3/Machine Learning/sources/positions.csv")

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = DecisionTreeRegressor()
regression.fit(level,salary)
#print(regression.predict(8.9).reshape(1,-1))

plt.scatter(level,salary,color="red")
x = np.arange(min(level),max(level),0.01).reshape(-1, 1)
plt.plot(x,regression.predict(x),color="orange")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Model")
plt.show()