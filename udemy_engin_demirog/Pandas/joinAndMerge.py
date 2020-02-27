# -*- coding: utf-8 -*-
import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'ad':["Emre","Mahmut","Omer","Onur"],
            'soyad':["Kara","Kaptan","Karayazi","Kaplan"]
        }

data2 = {
            'id':[1,3,4,7],
            'ad':["2Emre2","2Mahmut2","2Omer2","2Onur2"],
            'soyad':["2Kara2","2Kaptan2","2Karayazi2","2Kaplan2"]
        }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("df1:")
print(df1)
print()

print("df2:")
print(df2)
print()

df3= pd.merge(df1,df2,on= 'id', how= "inner") #inner: id sütunu örtüşen verileri getirir.
print("df3:")
print(df3)
print()

df4= pd.merge(df1,df2,on= 'id', how= "left") #left: soldaki sütunların sağdaki eşlerini getirir.
print("df4:")
print(df4)
print()

df5= pd.merge(df1,df2,on= 'id', how= "right") #right: sağdaki sutünların soldaki eşlerini getirir. 
print("df5:")
print(df5)
print()

df6 = pd.concat([df1,df2],axis=1) #üzerine ekler default axis=0'dır
print("concate:")
print(df6)
print()

