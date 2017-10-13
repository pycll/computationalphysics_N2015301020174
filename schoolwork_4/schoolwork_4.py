# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:45:30 2017

@author: Administrator
"""

import math
import pylab as pl

dt=0.1
g=9.8
a=30*math.pi/180
angle=[a]
v0=50.0

t=[0]
v_x1=[v0*math.cos(angle[0])]
v_y1=[v0*math.sin(angle[0])]
x1=[0]
y1=[0]

while x1[-1]<=300:
    x1.append(x1[-1]+v_x1[-1]*dt)
    y1.append(y1[-1]+v_y1[-1]*dt)
    v_x1.append(v_x1[-1])
    v_y1.append(v_y1[-1] - g*dt)
    t.append(t[-1]+dt) 
print ('初始速度：',v0,
       '\n','落点：', 'x:',x1[-1],'y:',y1[-1],
       '\n''飞行时间：',t[-1])

pl.figure(figsize=(7,5))
pl.plot(x1,y1,label="$30^\circ$",color="red",linewidth=2)
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.title('schoolwork_4')

pl.ylim(0,100)
pl.show()





