# [Source code](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/schoolwork_6.py)
## 题目大意

教材上的习题3.12

## 我的想法

使用Ruler-Cromer方法。分析在受迫力处于不同相位时单摆的奇异吸引子；最后将各个相位时的吸引子进行对比得出结论。主要是要代入书上单摆在受迫力大于阻尼力的情况下的公式，公式如下图所示：
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/%E6%88%AA%E5%9B%BE_2017-10-28_00-32-51.png)

此时，如果F_D>q，系统将会产生混沌，吸引子成为Poincare Section
使用Euler-Cramer方法得到近似为：
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/Formula.PNG)

## 计算结果
在F_D=1.2 q=1/2 l=g=9.8 Ω_D=2/3 θ0=0.2 ω0=0.2 的情况下，得到如图所示的结果
相图
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/Phase.PNG)

Poincare Section
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/PoincareSection_1.PNG)
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_6/PoincareSection_2.PNG)

## 致谢
感谢马奇云同学的帮助！虽然从数学上我知道混沌是怎么一回事，也在非线性动力学里面大概的处理过类似于混沌的问题，但是这是第一次用计算机计算。真的非常感谢他！！！
