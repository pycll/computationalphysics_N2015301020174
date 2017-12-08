    from functools import reduce
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    #delta=0.1
    delta=0.05
    deltaV,times=10,0
    #1.initialize-V
    V=[[0.]*(int(1+1/delta))for i in range(int(1+1/delta))]
    for i in range(1+int(round(0.3/delta))):#boundary conditions   tips: int(0.3/0.1)=2 why?????
        V[int(round(0.3/delta))][i]=-1.
    #2.calculation
    def updateV(V_old):#function to update-V
        V_new=[[0.]*len(V_old)for i in range(len(V_old))]
        for i in range(1,len(V_old)-1):
            for j in range(1,len(V_old)-1):
                V_new[i][j]=(V_old[i-1][j]+V_old[i+1][j]+V_old[i][j-1]+V_old[i][j+1])/4
        for j in range(1,len(V_old)-1):#boundary of x=0 or i=0 while 0<y<1,1<=j<=len()-1
            V_new[0][j]=(V_old[0][j-1]+V_old[0][j+1])/4
        for k in range(1,len(V_old)-1):#boundary of y=0 or j=0 while 0<x<1,1<=i<=len()-1
            V_new[k][0]=(V_old[k-1][0]+V_old[k+1][0]+2*V_old[k][1])/4
        V_new[0][0]=V_old[0][1]/2
        for l in range(1+int(round(0.3/delta))):#boundary conditions V(x=0.3,0<=y<=0.3)=-1
            V_new[int(round(0.3/delta))][l]=-1.
        return V_new
    #3.loop and check the limit of deltaV
    while deltaV > len(V)**2*10**(-5):#alternatively,for n in range(1):
        V1=updateV(V)#update
        V=updateV(V1)
        v=[]
        for i in range(len(V)):
            v.append(reduce(lambda x,y:x+y,(map(lambda a,b:abs(a-b),V1[i],V[i]))))
        deltaV=reduce(lambda x,y:x+y,v)
        times=times+1#V is in the 1st Quadrant
    print (times)
    #4.extend the potential to the interest regime to get V_whole
    N=len(V)
    V1=np.transpose(V)#1st Quadrant
    V3=[[0.]*(N-1) for i in range(N)]#3rd quadrant
    for i in range(N):
        for j in range(N-1):
            V3[i][j]=-V1[N-1-i][N-1-j]
    #add the 4th qudrant to V3 using extend
    for i in range(N):
        V3[i].extend(V1[N-1-i])
    #add the 1st&2nd qudrant using +
    V_whole=V3
    for i in range(N-1):
        V_whole=V_whole+[V3[N-2-i]]
    del V1,V3
    #check:print len(V_whole)
    #3D figure
    fig = plt.figure()
    ax = Axes3D(fig)
    x=np.linspace(-1,1,len(V_whole))
    X,Y= np.meshgrid(x,x)
    ax.plot_surface(X,Y,V_whole, rstride=1, cstride=1, cmap='Greys_r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Electric Potential/V')
    ax.set_title('Electric Potential  Near Two Metal Plates')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1.2,1.2)
    ax.contourf(X, Y, V_whole, zdir='z', offset=-1.2, cmap=plt.cm 
    .Greys_r)
    plt.show()
    #2D contour
    x=np.linspace(-1,1,len(V_whole))
    X,Y= np.meshgrid(x,x)
    plt.contourf(X, Y, V_whole, 10, alpha=.75, cmap='Greys_r')
    C = plt.contour(X, Y, V_whole, 10, colors='white', linewidth=.5)
    plt.clabel(C, inline=1, fontsize=10)
    plt.title(r'Electric Potential Near Two Metal Plate')
    plt.show()
    #2D electric field plot
    EY,EX=np.gradient(V_whole)
    EX,EY=-EX,-EY
    R=np.sqrt(EX**2+EY**2)
    x=np.linspace(-1,1,len(V_whole))
    X,Y= np.meshgrid(x,x)
    plt.quiver(X,Y,EX,EY,R, alpha=10)
    plt.quiver(X,Y,EX,EY, edgecolor='w', facecolor='k', linewidth=.3)
    plt.title(r'Electric Field Distribution Near Two Metal Plates,$\Delta=$%s'%delta)
    plt.xlabel('x'),plt.ylabel('y'),
    plt.xlim(-1.,1.), plt.xticks([])
    plt.ylim(-1.,1.), plt.yticks([])
    plt.show()