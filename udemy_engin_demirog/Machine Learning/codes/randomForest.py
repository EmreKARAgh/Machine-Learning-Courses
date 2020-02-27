# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

value = np.array([[8.3]]).reshape(-1,1)

data = pd.read_csv("C:/Users/Emre KARA/.spyder-py3/Machine Learning/sources/positions.csv")
level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values

regression = RandomForestRegressor(n_estimators=10, random_state=2)
regression.fit(level,salary)


x= np.arange(min(level),max(level),0.1).reshape(-1,1)

plt.scatter(level,salary,color="red",label="data")
plt.plot(x,regression.predict(x),color="blue",label="Forest Regression")
plt.xlabel('level')
plt.ylabel('salary')
plt.title("Random Forest Model")
plt.legend()
plt.show()



print(regression.predict(value))
