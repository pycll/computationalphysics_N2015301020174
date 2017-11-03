# 摘要
我写的是书上的3-26题，通过Lorenz方程组来计算简单的混沌现象。[Source code](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/schoolwork_7.py)


# 研究背景
在大气现象的研究中，主要依靠于对流体力学的Navier-Stokes方程的研究。数学上来说，在将方程无量纲化后出现的对流项是很难解决的一个问题。方程组中对流项相比较于线性项发挥明显作用的体系，数学上无法解出精确的解；如果是这种情况，在实际操作中，系统对初值的误差非常敏感，这会产生混沌现象。最终通过衡量无量纲化后方程中对流项和线性项的比值（即雷诺数）来衡量产生混沌现象是否产生（在流体力学中便是湍流）。大家一般都不想讲太多数学上的背景（毕竟本人是手算过N-S方程的，那叫一个酸爽。。），所以Lorenz对方程做了简化，即：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_1.gif)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_2.gif)

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/formula_3.gif)

我们使用Lorenz模型来模拟出混沌现象。



# 正文
Lorenz模型依赖于r，通过赋予不同的r的值，可以看到不同的现象。由于r是雷诺数的函数，可以预测，随着r的变化，当超过某一临界值时，体系中的混沌将会产生或者消失。本文采用了书上设定的初始条件和参数设定：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/condition.gif)

带进去算出来如图所示：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/z-t.PNG)

其中，r的取值分别为5，10，15，20，25，30.可以发现，在r的值比较小的情况下，体系的震动显然是符合于谐振子的阻尼振动模型的，随着r的增大，z方向开始概周期性地出现孤峰。一个有名的例子就是求解KdE方程得出的孤立子解，最早在河道中观察到。
另外，稳定性研究在非线性动力学中非常重要，画出x-z截面上的轨迹曲线，如图所示。可以看出，体系的x-z表现出双吸引子的形式，是暂态稳定的。

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_7/x-z.PNG)


# 结论
通过使用Lorenz简化后的模型来计算，可以看到体系的混沌现象。我个人想尝试着用这个方法来直接分析N-S方程。

# 致谢
感谢陈洋遥同学的主要代码结构！
参考书目：《非线性动力学定性理论方法》 高等教育出版社
