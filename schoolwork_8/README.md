## 摘要
本次作业是关于行星运动中的二体问题。[source code](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/schoolwork_8.py)

## 背景介绍
从数学上可以证明，对于N体问题，能够严格求解的只有N=<的情况。从算法设计上来说，如果是3体或者3体以上的问题，程序设计的复杂度往往难以界定。而对于多体问题，其所遵循的物理规律和二体问题相同，均是牛顿的万有引力定律或者是爱因斯坦场方程所求出的matric所对应的geodesics(可能是类光，也可能是类时）。所以对于两题问题的研究具有很重要的意义。
考虑二体问题的经典体系，满足牛顿的万有引力定律。其公式为：

![iamge](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/formula_1.PNG)

由此可以在引力场较弱的情况下准确的解出行星之间的运动轨迹。对于太阳和地球构成的双星系统，考虑约化质量:

![iamge](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/formula_3.PNG)

并且由于体系不受外力作用（实际上由于体系所受外力在各个方向的平均对该系统影响较小，故可以忽略），从而得到：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/formula_2.PNG)
其中l为偏心率。
## 正文
通过把体系转化到质心系，

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/circulalr_orbit.PNG)

由此可见，选择较好的初始条件，可以使二体做一个完美的圆轨道。这是显而易见的，假使初始时刻两星的速度与其连线垂直，并且体系总能量不至于使其运动到无穷远处，那么就是这种情况。
但是如果二星的初始速度和连线不垂直，而是成一个其他的角度，那么可能的情况之一如图所示：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_8/elliptical_orbit.PNG)


## 结论
可以看出在万有引力定律的情况下，行星的运动轨迹都是完美的椭圆，但是椭圆的形状大小由初始条件决定。

## 致谢
感谢刘祥干学长！顺便希望蔡老师没事 :)
