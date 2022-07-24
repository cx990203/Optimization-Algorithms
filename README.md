# Optimization-Algorithms
一些优化算法方面的程序源码</br>
每一个文件就是一种方法，可以单独执行文件</br>

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

