### 摘要[Source code](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_11/schoolwork_11.py)
波动是物理学中应用非常广泛，也是使用起来非常强有力的模型。这类模型可以推广至谐振子模型。无论是电磁理论中的Lorentz谐振子模型，还是量子力学中的Schwinger谐振子模型。对于这类模型的求解，最终往往归结于一个波动方程的求解。这可以看作是经典的波动的推广。在此，我们讨论波在弹性绳上的传播（不考虑损耗）。

### 背景
对于一维的波动问题，在不考虑损耗的情况下，由波动方程描述：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_11/Formula_1.png)

如果考虑固定边界条件，即绳子的两个端点在此坐标系下不会发生移动，此时波在绳上的传播会在端点发生反射；此时将上式写成差分方程的形式：

![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_11/Formula_2.png)

### 正文
考虑最开始的波形为一个高斯型波包，使用如上的差分方程，可以的出如图所示的图示：
![image](https://github.com/pycll/computationalphysics_N2015301020174/blob/master/schoolwork_11/schoolwork_11.gif)

### 结论
由此可以对机械波在弹性绳上的传播进行模拟。

### 致谢
我主要参考了刘洋干学长和陈遥祥学长的代码。知识点参考了《数学物理方法》（希尔伯特，柯朗）
