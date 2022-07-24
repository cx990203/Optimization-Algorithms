# Optimization-Algorithms
一些优化算法方面的程序源码。</br>
每一个文件就是一种方法，可以单独执行文件。</br>
其中部分算法不是很理想，在某一初值条件下求解结果有一定的问题</br>

## RosenbrockBySteepest.py
最速下降法求解Rosenbrock function</br>
函数原型：</br>
![image](https://user-images.githubusercontent.com/77096562/180644370-b1ea99b9-025a-477b-bc09-e21e538cc63f.png)</br>
运行后迭代次数：8318</br>
迭代路径：</br>
![RosenbrockBySteepest py](https://user-images.githubusercontent.com/77096562/180644870-e3b5c187-a37a-4d94-b463-394ac8a5ffb7.png)

## RosenbrockByNewton.py
牛顿法求解Rosenbrock function</br>
函数原型：</br>
![image](https://user-images.githubusercontent.com/77096562/180644370-b1ea99b9-025a-477b-bc09-e21e538cc63f.png)</br>
运行后迭代次数：5</br>
迭代路径：</br>
![RosenbrockByNewton](https://user-images.githubusercontent.com/77096562/180644921-e48eb678-8214-49d3-a5ff-7c05523c05dc.png)

## BealeBySteepest.py
最速下降法求解the Beale function</br>
函数原型：</br>
![image](https://user-images.githubusercontent.com/77096562/180644956-6d5987c0-3573-4829-8887-528174588c16.png)</br>
运行后迭代次数：NAN，算法在（-1.2,1.0）位置作为起始位置时无法收敛</br>
迭代路径：</br>
![BealeBySteepest](https://user-images.githubusercontent.com/77096562/180645042-1ab651a2-3a8f-4a31-8e75-8829bb235b6a.png)

## BealeByNewton.py
牛顿法求解the Beale function
函数原型：</br>
![image](https://user-images.githubusercontent.com/77096562/180644956-6d5987c0-3573-4829-8887-528174588c16.png)</br>
运行后迭代次数：1，算法在（-1.2,1.0）位置作为起始位置时收敛到函数鞍点，并非全局最小值</br>
迭代路径：</br>
![BealeByNewton](https://user-images.githubusercontent.com/77096562/180645126-d25f0614-e0ad-4332-bb19-1a9e8a52d89f.png)

## HilbertByCG.py
共轭梯度法求解线性系统问题：Ax=b。其中A是希尔伯特矩阵，元素表达式为：</br>
![image](https://user-images.githubusercontent.com/77096562/180645359-b1fa6821-cbba-4784-89b1-4745ccd2b31e.png)。</br>
右边为常数向量矩阵：</br>
![image](https://user-images.githubusercontent.com/77096562/180645395-a2323a8c-97d3-4475-bb80-e5bccf1f0308.png)。</br>
算法求解结果如下：</br>
![image](https://user-images.githubusercontent.com/77096562/180645457-3eb50bb8-f78d-4851-a074-e4c743ffcd1b.png)
维度为5时，其残差与迭代关系折线图：</br>
![image](https://user-images.githubusercontent.com/77096562/180645505-cc7077a7-edc0-49b8-88e2-210424bf82c5.png)</br>
维度为8时，其残差与迭代关系折线图：</br>
![image](https://user-images.githubusercontent.com/77096562/180645522-dd54866a-ef7a-41a6-811f-e2ee4b85b4a3.png)</br>
维度为12时，其残差与迭代关系折线图：</br>
![image](https://user-images.githubusercontent.com/77096562/180645528-ae7b3b71-0bc8-4957-b6ab-582e7f990e66.png)</br>
维度为20时，其残差与迭代关系折线图：</br>
![image](https://user-images.githubusercontent.com/77096562/180645536-e448432f-6e7c-49c2-8def-2fc24ae7ef28.png)</br>


