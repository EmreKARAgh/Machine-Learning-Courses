# -*- coding: utf-8 -*-
f = open("musteriler.txt","w")
f.write("AA11\n")
f.write("BB22\n")
f.write("CC33\n")



f = open("musteriler.txt","r")



for l in f:
    print(l,end='')
f.close()

print()

f = open("musteriler.txt","r")

print(f.read())

f.close()

import os
    
if os.path.exists("musteriler.txt"):
    os.remove("musteriler.txt")
    print("Dosya Silindi")
else:
    print("Dosya Yok")
    
if os.path.exists("empty"):
    os.rmdir("empty")    
else:
    os.makedirs("empty")    

