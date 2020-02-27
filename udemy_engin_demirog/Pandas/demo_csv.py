import pandas as pd

notlar = pd.read_csv("sources/grades.csv")
print("grades.csv:")
print(type(notlar))
print(notlar.head())
print()

print("columns changed.")
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar[3:5])
