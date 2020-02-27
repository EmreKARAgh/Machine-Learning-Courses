# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:57:44 2019

@author: EmreKARA
"""

import numpy as np


a = np.array([20,30,40,50])
print("a: ", a)

b= np.arange(4)
print("b= np.arange(4): ", b)

c = a -b
print("c= a-b: ", c) 

d= b**2
print("d= b**2: ",d)

e= 10 * np.sin(a) 
print("e= 10 * np.sin(a): ", e)
print("e<7: ", e<7)

print("a*b: ",a*b) #Elementwise Product

print("a@b: ",a@b)#Matrix multiplication
print("a.dot(b): ",a.dot(b))

f= np.zeros((5,5))
print("f= np.zeros((5,5)): ",f)
g= np.ones((5,5))
print("g= np.ones((5,5)): ",g)
h= np.random.random((5,5))
print("h= np.random.random((5,5)): ",h)
i = np.sum(g)
print("i= np.sum(g): ",i)
