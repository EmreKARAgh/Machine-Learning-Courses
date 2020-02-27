# -*- coding: utf-8 -*-
import preprocess
from sklearn.linear_model import LinearRegression
import pandas as pd
from matplotlib import pyplot as plt

obj = preprocess.preprocessing()
x_train,x_test, y_train, y_test = obj.getData()

lr = LinearRegression()

lr.fit(x_train,y_train)

predict = lr.predict(x_test)

predict = pd.DataFrame(data = predict , index =y_test.index, columns=['tahmin'])

comparision = pd.concat([y_test, predict], axis = 1)

x_train = x_train.sort_index() #indexe göre sıralama. ay-satis eşleşmesini bozmaz
y_train = y_train.sort_index()

plt.title('Aylara Göre Satış Tahmin Grafiği', color='r')
plt.xlabel('Aylar',color='r')
plt.ylabel('Satışlar',color='r')

plt.scatter(x_train,y_train)
plt.plot(x_train,y_train)
plt.plot(x_test,predict)

plt.show()

