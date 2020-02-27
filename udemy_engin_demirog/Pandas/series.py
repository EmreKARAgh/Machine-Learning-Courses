# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:35:44 2019

@author: EmreKARA
"""

import pandas as pd
import numpy as np

data = np.array(["Emre","Kara","1453"])

s = pd.Series(data, index=[4,5,6])
print(s)

data2 = dict(matematik=100, kimya=25, biyoloji=86 )

s2= pd.Series(data2)
print(s2)
