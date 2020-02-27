# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("sources/positions.csv")
print(data.describe())

value = np.array([[8.5]]).reshape(-1,1)

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = DecisionTreeRegressor()
regression.fit(level,salary)

x= np.arange(min(level),max(level),0.01).reshape(-1,1)

plt.scatter(level,salary,color="red",label="data")
plt.plot(x,regression.predict(x),color="blue",label="Tree Regression")
plt.xlabel('level')
plt.ylabel('salary')
plt.title("Decision Tree Model")
plt.legend()
plt.show()

print(regression.predict(value))