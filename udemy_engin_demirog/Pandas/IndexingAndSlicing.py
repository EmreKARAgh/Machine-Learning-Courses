# -*- coding: utf-8 -*-
import pandas as pd

notlar = pd.read_csv("sources/grades.csv")
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]

print("grades.csv İsimden Test1' e kadar olan sütunlar 3 sonuç")
print(notlar.loc[:3,"İsim":"Test1"])
print()

print("grades.csv İsim ve Test1' sütunları 3 sonuç")
print(notlar.loc[:3,["İsim","Test1"]])
print()

print("grades.csv İsim sütunu tersten")
print(notlar.loc[::-1,"İsim"])
print()


