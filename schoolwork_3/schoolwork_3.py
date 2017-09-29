import matplotlib.pyplot as plt
v=0.0
Δt=0.1
n=10/Δt
a=1
g=-9.8
t=0
v_list=[0]
t_list=[0]
while a<=n:
    v=v+g*Δt
    v_list.append(v)
    t=t+Δt
    t_list.append(t)
    a+=1
print(t_list)
print(v_list)
plt.plot(t_list,v_list)
plt.xlabel('time(s)')
plt.ylabel('voltage(mV)')
plt.title('About as simple as it gets,folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
