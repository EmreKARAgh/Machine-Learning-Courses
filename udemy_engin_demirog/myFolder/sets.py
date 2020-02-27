# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
setA = {1,2,3}
setB = {3,4,5}
 
print("setA: ", setA)
print("setB: ", setB)

print("\n")

print("setA | setB:" , setA | setB)
print("setA.union(setB): ",setA.union(setB))
print("setB.union(setA): ",setB.union(setA))

print("\n")

print("setB & setA:" , setA & setB)
print("setA.intersection(setB): ", setA.intersection(setB)) 
print("setB.intersection(setA): ", setB.intersection(setA)) 

print("\n")

print("setA - setB: ", setA - setB)
print("setA.difference(setB): ", setA.difference(setB))
print("setB.difference(setA): ", setB.difference(setA))

print("\n")

print("setA ^ setB: ", setA ^ setB)
print("setA.symmetric_difference(setB): ", setA.symmetric_difference(setB))
print("setB.symmetric_difference(setA): ", setB.symmetric_difference(setA))


