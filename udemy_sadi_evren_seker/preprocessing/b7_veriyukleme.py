# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:21:27 2020

@author: EmreKARA
"""

import pandas as pd
import matplotlib as plt 
import numpy as np

veriler = pd.read_csv('sources/veriler.csv')
print(veriler)

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)