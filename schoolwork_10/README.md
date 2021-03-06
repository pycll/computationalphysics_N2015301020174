## 摘要
我做的是书上的第三题，要求画出在一个象限内的静电场分布图。[Source code](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_10/schoolwork_10.py)

## 背景介绍
对于能动张量为零的区域，场方程为Laplace方程。在给定边界条件的情况下，原则上可以进行求解。这一题主要考虑的是如何在算法上实现偏微分方程的求解，这要归结于松弛算法(Relaxed Arithmetic)，下面进行较为详细的叙述。

## 正文
对于无源区域，静电势能分布满足Laplace方程：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_10/Formula_1.png)

考虑数值求解，上述方程可以简化为：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_10/Formula_2.png)

由此可以看出，一点的电势依赖于这一点周围的点的电势，并且可以正好是三个方向的平均。很容易可以知道，对于这样方程的求解，需要预先给出若干点的电势值，然后逐步推测出整个空间的电势分布。松弛算法的思想在于，我们不需要预先测试出若干点的电势，只需要随便取一个函数，然后带入上式，通过不断迭代，最终函数收敛至稳定解。

## 结论
最终所求得解如图所示：
2D图像：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_10/2D%20Equipotential%20Line.png)

3D图像：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_10/3D%20Equipotential%20Line.png)

## 致谢
这次作业参考了马奇云同学的代码，在此感谢！

