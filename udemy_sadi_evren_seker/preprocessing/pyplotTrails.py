# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(1,100,20)
y = np.logspace(1,2,20)


fig = plt.figure('1. Grafik')
fig.suptitle('İç Başlık 1', fontsize=16)
fig2 = plt. figure('2. Grafik')
fig2.suptitle('İç Başlık 2', fontsize=16)

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('ortak x label', color='r')
ax.set_ylabel('ortak y label',color='r')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

subplot1 = fig.add_subplot(2,1,1)
subplot2 = fig.add_subplot(2,1,2)
subplot3 = fig2.add_subplot(1, 2, 1)  
plt.title('Veri Grafiği', color='r')
plt.xlabel('X indexi',color='r')
plt.ylabel('Y indexi',color='r')

subplot1.plot(x, y, color='b', label='Y')
subplot1.legend()

subplot2.plot(x, y, color='y', label='Y')
subplot2.legend()

subplot3.plot(x, y, color='g', label='Y')
subplot3.legend()
plt.show()
