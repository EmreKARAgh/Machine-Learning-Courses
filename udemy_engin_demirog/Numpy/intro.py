# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:56:56 2019

@author: EmreKARA
"""

import numpy as np

a = np.arange(15).reshape(3,5)

print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b= np.arange(10)
print(b)
print(b.shape)
print(b.ndim)