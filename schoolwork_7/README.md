# 摘要
我写的是书上的3-26题，通过Lorenz方程组来计算混沌现象。


# 研究背景
在大气现象的研究中，主要依靠于对流体力学的Navier-Stokes方程的研究。数学上来说，在将方程无量纲化后出现的对流项是很难解决的一个问题。方程组中对流项相比较于线性项发挥明显作用的体系，数学上无法解出精确的解；在实际操作中，对初值的误差非常敏感。最终通过衡量无量纲化后方程中对流项和线性项的比值（即雷诺数）来衡量产生混沌现象是否产生（在流体力学中便是湍流）。大家一般都不想讲太多数学上的背景（毕竟本人是手算过N-S方程的，那叫一个酸爽。。），所以Lorenz对方程做了简化，即：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_1.gif)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_2.gif)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_3.gif)



# 正文
Lorenz模型依赖于r，通过赋予不同的r的值，可以看到不同的现象。本文采用了书上设定的初始条件和参数设定：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/condition.gif)

带进去算出来如图所示：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/z-t.PNG)

其中，r的取值分别为5，10，15，20，25，30.可以发现，在r的值比较小的情况下，体系的震动显然是符合于谐振子的阻尼振动模型的，随着r的增大，z方向开始准周期性地出现孤峰。一个有名的例子就是求解KdE方程得出的孤立子解，最早在河道中观察到。
另外，稳定性研究在非线性动力学中非常重要，画出x-z截面上的轨迹曲线，如图所示。可以看出，体系的x-z相关是稳定的。

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/x-z.PNG)

# 结论
通过使用

# 致谢
感谢陈洋遥同学的主要代码结构！
