# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:17:29 2019

@author: EmreKARA
"""
import sys
try:
    data = int(input("Sayi Giriniz: "))
    print(data," girdiniz")
except (ValueError, ZeroDivisionError):
    print("Uygun olmayan tipte veri girişi hatası alındı")
except:
    print("Anlaşılamayan Hata")
    
try:
    l = [1,2,3]
    print(l[4])
except IndexError:
    print("Indeks hatası Alındı")

try:
    import fadas
except ModuleNotFoundError:
    print("Modul bulunamadı hatası alındı")

try:
    D= {'1':"aa",'2':"bb"}
    print(D['3'])
except KeyError:
    print("Anahtar Hatası alındı")
    
try:
    from math import cube
except ImportError:
    print("Import Hatası alındı")
    
try:
    it= iter([1,2,3])
    next(it)
    next(it)
    next(it)
    
    next(it)
except StopIteration:
    print("İterasyon Hatası alındı")

try:
    a = '2' + 2
except TypeError:
    print("Tip hatası alındı")

try:
    a= 3 * b
except NameError:
    print("Önceden tanımlanmamış kullanım hatası alındı")

try: 
    x = 100/0
except ZeroDivisionError:
    print("0'a bölme hatası alındı")

#       SYTNAX ERROR VARKEN YÜRÜTME BAŞLAMIYOR
#try:
#    print "hello"
#except:
#    print("Syntax hatası alındı")

try: 
    a = 1/0
except:
    print("alınan hata" , sys.exc_info()[0])
finally: 
    print("Finally İşlem Bitti")