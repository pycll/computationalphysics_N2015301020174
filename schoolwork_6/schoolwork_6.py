import math
import matplotlib.pyplot as plt
F_D=1.2
q=1/2
l=9.8
g=9.8
Ω_D=2/3
dt=0.04
θ0=0.2
ω0=0
ω=ω0
θ=θ0
t=0
ω_list=[ω0]
θ_list=[θ0]
while t<10000:
    ω=ω-((g/l)*math.sin(θ)+q*ω-F_D*math.sin(Ω_D*t))*dt
    θ=θ+ω*dt
    
    if θ>math.pi:
        θ=θ-2*math.pi
    elif θ<-math.pi:
        θ=θ+2*math.pi
    t=t+dt
    for n in range(4244):
        if abs(t-math.pi*n/(2*Ω_D))<0.02:
            θ_list.append(θ)
            ω_list.append(ω)
    