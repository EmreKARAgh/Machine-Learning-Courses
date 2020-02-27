# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:35:46 2019

@author: EmreKARA
"""

sayilar = [1,2,3,4,5]
kareSayilarNormal = []

for sayi in sayilar:
    kareSayilarNormal.append(sayi*sayi)
    
kareSayilarMap = list(map(lambda sayi: sayi*sayi ,sayilar))

print("Normal:      ",kareSayilarNormal)
print("Mapping ile: ", kareSayilarMap)

filtreli = list(filter(lambda sayi: sayi>5,kareSayilarMap))

print("Filtreli:    ",filtreli)

from functools import reduce

# X'i alır bir yandaki ile işlem yapıp yeni X yapar sona doğru devam eder
sayilarReduce = reduce(lambda x,y:x+y , sayilar)

print("Reduce:      ", sayilarReduce) 

