# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:50:12 2019

@author: EmreKARA
"""

import pandas as pd

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data2 = [["Emre",21,"Kocaeli"],["Omer",22,"Kocaeli"],["Mahmut",24,"Ordu"]]
df2 = pd.DataFrame(data2)
print(df2)


data3 = { "İsim":["Emre","Omer","Mahmut"],
         "Yaş":[21,22,24],
         "Şehir":["Kocaeli","Kocaeli","Ordu"]
        }
df3 = pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index = [1,2,3])
print("\ndf3:")
print(df3)
print()

print("df3[isim]:")
print(df3["İsim"])
print()

print("df3(!şehir):")
#del(df3["Şehir"])
df3.pop("Şehir")
print(df3)
print()

print("df3[2]:")
print(df3.loc[2])
print(df3.loc[1])
print()

print("df4:")
df4 = df3.append(df3)
print(df4)
print()


print("head of df4:")
print(df4.head(2)) #default: 5
print()

print("tail of df4:")
print(df4.tail(2)) #♣ default: 5
print()