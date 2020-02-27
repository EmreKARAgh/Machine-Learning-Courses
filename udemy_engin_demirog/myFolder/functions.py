# -*- coding: utf-8 -*-

def myFunc(ad = "Emre", soyad= "Kara"):
    print("Merhaba " + ad + " "  + soyad)

def myFunc2(ad, soyad= "Kara"):
    print("Merhaba " + ad + " " + soyad)

def myFunc3(soyad,ad = "Emre"): #Her zaman önce default değeri olmayanlar yazılır. (soldan sağa)
    print("Merhaba " + ad + " " + soyad)


myFunc(soyad = "Yıldız")

myFunc2("Emre")

myFunc3("Kara")



