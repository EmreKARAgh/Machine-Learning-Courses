# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

regression = LinearRegression()
regressionPoly = PolynomialFeatures(degree = 4) #? neden 4
regression2 = LinearRegression()

data = pd.read_csv("sources/positions.csv")
print(data.describe())

value = np.array([8.3]).reshape(-1,1)

level = data.iloc[:,1].values.reshape(-1,1) # X data
levelPoly = regressionPoly.fit_transform(level)

salary = data.iloc[:,2].values.reshape(-1,1) # Y data


regression.fit(level, salary)
regression2.fit(levelPoly,salary)

plt.scatter(level,salary,color="red",label="data")
plt.plot(level,regression.predict(level),color="blue",label="linear")
plt.plot(level,regression2.predict(levelPoly),color="yellow",label="polynomial")
plt.xlabel('level')
plt.ylabel('salary')
plt.legend()
plt.show()




result = regression.predict(value)
result2 = regression2.predict(regressionPoly.fit_transform(value))

print("result: " ,result)
print("result2: " ,result2)
