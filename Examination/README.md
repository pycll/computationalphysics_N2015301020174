## 摘要
Nowadays the most succesful theory about gravity is General Relativity which was first introduced by A.Einstein in 1915. In Genaral 
Relativity, gravity was thought of as an effect of the curvature of the 4-dimensional space-time. In this paper, I will mainly
introduce the simplist solution of Einstein Equation: the Schwarzschild slution which was derived by K.Schwarzschild at the year 
of 1916, and try to argue on some famous effect of the Schwarzschild Metric, espacially on the movement of a test particle.

## 背景介绍
In General Relativity, the Einstein Equation that reflects matter having affects on space-time in vaccum is:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Einstein_Equation.png)

If we consider the metric was spherely symmetric, and the body which cause curvature of space-time is neutron, then we derive the metric:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Schwarzschild_Metric.png)

This is called the Schwarzschild Metric that implies the line elemente in a Schwarzschild space-time.
Consider a certain test particle which is free falling, it follows the time-like geodesics:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Geodesic.png)

and 4-dimensional volecity we got the relationship:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Timelike_Vector.png)

Contracting these equations, we can derive the movement equation of such a test particle:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Radius.png)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Degree.png)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Coordinate_time.png)

## 正文
### Mercury Procession
The first success of General Relativity was that is explained the Mercury procession. If we kill the proper time from above 
equations, we can derive:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Mercury_Procession.png)

Using Python, we get the picture

![image]

### Light Bending
A famous prophecy which GR introduced was the light bending. The only difference between light which we can see as photon and test particle was that light follows:

![image]

### Time Dialation
Consider a pilot was approching the Schwarzschild Radius, in which even light cannot escape, can freely falling to the centre 
of the space-time, and we are observing him at infinite. For the pilot, his clock time, which is also his local proper time, 
is:

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Proper_time_BH.png)

And our clock, which is our proper time and also the coordinate time, is

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/Examination/Coodiante_time_BH.png)

Using Python, we get:

![image]

We can get that in our proper time the pilot will never get into the Radius because it will take infinite time. But the pilot 
himself will soon found he get inside the Radius.

## 结论
As the simplest exact solution of Einstein Equation, the Schwarzshild solution remain its simple quantities from GR that differ 
from Newtonian gravitation theory, yet can show us a lot of unique effects that in Newton's theory that is never possible.

## 致谢
Thanks for the guide from Xianggan Liu.
Reference Book：
Robert Wald. General Relativity
Moshe Carmeli. Classical Fields:General Relativity and Gauge Theory



