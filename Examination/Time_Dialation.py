# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:58:48 2017

@author: Administrator
"""

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d
L=1
M=1
E=2
k=1
r0=7
t=[]
T=[]
r=[]
t.append(0)
T.append(0)
r.append(r0)
tot=r0
dr=0.001
for i in range(int(tot/dr)):

        r.append(r[i]-dr)
        t.append(t[i]+r[i]*E/((r[i]-2*M)*(E**2-(1-2*M/r[i])*(k+L**2/r[i]**2))**0.5)*dr)
        T.append(T[i]+1/(E**2-(1-2*M/r[i])*(k+L**2/r[i]**2))**0.5*dr)
    

plot(r,t,color='blue',label="k=1,t=bule",linestyle='-')
plot(r,T,color='red',label="k=1,T=red",linestyle='-')
xlabel('r')
ylabel('t or T')
xlim(0,8)
ylim(0,22)
legend(loc='upper right')
title(u't and T --r', fontsize=16,fontproperties='STSong')
savefig("t-r2.png")
show()
