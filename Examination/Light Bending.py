# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:56:57 2017

@author: Administrator
"""

from numpy import *
import matplotlib.pyplot as plt
class BENDING(object):
    '''
    class BENDING solves for bending of light
    where:
        E: Energy L: angular momentum M: mass of central star
        r0, ph0: initial distance and angle between star and source
        dt, time :time step size and total time
    '''
    def __init__(self, _E=2.2, _L=1.2, _M=1., _r0=6,_ph0=0., _dt=0.001, _time =500.):
        self.E, self.L, self.M=_E, _L, _M
        self.r, self.ph, self.t=[_r0], [_ph0], [0.]
        self.dt= _dt
        self.time=_time
        self.n= int(_time/_dt)
    def cal(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
            self.r.append((sqrt(self.E**2-(1-2*self.M/self.r[-1])*(1+(self.L**2)/self.r[-1]**2))/self.E*(1-self.M*2/self.r[-1]))*self.dt+self.r[-1])
            self.ph.append((self.L/(self.r[-2]**2)/self.E*(1-2*self.M/self.r[-2]))*self.dt+self.ph[-1])

    def plot_trajectory(self,_ax):
        self.x=array(self.r)*cos(array(self.ph))
        self.y=array(self.r)*sin(array(self.ph))
        _ax.plot(self.x,self.y,'-y',label='E=%.2f'%self.E)
        _ax.plot([self.x[0]],[self.y[0]],'ob',markersize=5)
        _ax.plot([self.x[-1]],[self.y[-1]],'or',markersize=5)
        _ax.plot([0],[0],'og',markersize=10)
    #def find_min(self,_search):
        #for i in range(len(self.r)-2):
            #if self.r[i]>self.r[i+1] and self.r[i+1]<self.r[i+2]:
                #return (i+1)
fig=plt.figure(figsize=(10,5))
ax1=plt.subplot(111)
cmp=BENDING()
cmp.cal()
cmp.plot_trajectory(ax1)
plt.savefig("bend1.png")
plt.show()
