# [Source code](https://raw.githubusercontent.com/pycll/computationalphysics_N2015301020174/master/schoolwork_4/schoolwork_4.py) and [Result pic](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_4/schoolwork_4.PNG)
## 题目大意
我做的是教材上的2.6题：使用欧拉法画出炮弹在空中的飞行轨迹；不考虑空气阻力和空气的粘性。

## 我的想法
和第三次作业基本上是一样的。由于这次画图是画出x和y，x和y又分别是t的函数。考虑到y依赖于t的二次关系，从而构造一个新的中间变量v。结果是增加了一个中间变量，但是将二次的微分方程化为一次的方程组。所以，本质上来说，第三次作业是解一次微分方程的图形，这次作业是解一次微分方程组的图形。

### 公式
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_4/Formula%20Latex%20online.png)

### 计算过程
1.确定变量的初值

2.和第三次作业基本上类似，用一次次的迭代的方法计算各个变量的值，储存到一个数组中。通过while语句建立一个循环。

3.画图

### 结果图片
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_4/schoolwork_4.PNG)

## 致谢
非常感谢雅哥（吴文雅）的帮助。我虽然知道过程是怎样一步步实现的，但是写的代码总是有很多的语法错误。在她的帮助下基本上知道了该怎么写。比起上一次作业也是小有进步了。






