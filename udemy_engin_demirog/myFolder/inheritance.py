# -*- coding: utf-8 -*-

class Person:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        
class Worker(Person):
    def __init__(self,salary):
        self.salary=salary
        
class Customer(Person):
    def __init__(self,ad,soyad,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        self.ad = ad
        self.soyad = soyad
    
    def getData(self):
        print("ad: ",self.ad)
        print("soyad: ", self.soyad)
        print("Credit Card Number: ",self.creditCardNumber)

customer = Customer("Emre","Kara",12)
customer.getData()
