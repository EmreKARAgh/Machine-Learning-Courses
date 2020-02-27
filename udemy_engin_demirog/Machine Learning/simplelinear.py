# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score

data = pd.read_csv("sources/hw_25000.csv")
height = data.Height.values.reshape(-1,1) #Sütun matrisi şeklinde
weight = data.Weight.values.reshape(-1,1) #Sütun matrisi şeklinde


value = np.array(69.685).reshape(-1,1)
regression = LinearRegression()
regression.fit(height,weight)
print(regression.predict(value))

x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x), color="red")
plt.scatter(data.Height,data.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.show()

print(r2_score(weight,regression.predict(height)))

