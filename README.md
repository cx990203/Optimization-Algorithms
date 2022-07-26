# Optimization-Algorithms
一些优化算法方面的程序源码。</br>
每一个文件就是一种方法，可以单独执行文件。</br>
其中部分算法不是很理想，在某一初值条件下求解结果有一定的问题。</br>
<strong>ps:理论解释部分中公式是我从自己的报告中截图得到的，因此可能会比较模糊。</strong></br></br>
---------------仓库内涉及到的所有算法：</br>
<a href='#ActiveMethod'>ActiveMethod.py——积极集方法</a></br>
<a href='#QuadraticPenalty'>QuadraticPenalty.py——二次罚函数方法</a></br>
<a href='#ClassicalL1Penalty'>ClassicalL1Penalty.py——经典的l1精确罚函数方法</a></br>
<a href='#AugmentedLagrangian'>AugmentedLagrangian.py——增广拉格朗日乘子法</a></br>
<a href='#FunctionByNewton'>FunctionByNewton.py——牛顿法</a></br>
<a href='#Powellsingular_BFGS'>Powellsingular_BFGS.py——BFGS</a></br>
<a href='#Rosenbrock_BFGS'>Rosenbrock_BFGS.py——BFGS</a></br>
<a href='#Rosenbrock_n_BFGS'>Rosenbrock_n_BFGS.py——BFGS</a></br>
<a href='#RosenbrockBySteepest'>RosenbrockBySteepest.py——最速下降法</a></br>
<a href='#RosenbrockByNewton'>RosenbrockByNewton.py——牛顿法</a></br>
<a href='#BealeBySteepest'>BealeBySteepest.py——最速下降法</a></br>
<a href='#BealeByNewton'>BealeByNewton.py——牛顿法</a></br>
<a href='#HilbertByCG'>HilbertByCG.py——共轭梯度法</a></br>

<span id='ActiveMethod'></span>
## ActiveMethod.py
使用积极集方法求解指定问题。</br>
其中问题可以描述为为：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652899-cbda333e-c9ad-4443-ac4e-524b08fd0f93.png>
</div>
理论解释：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654739-2ebc86c4-4d4e-4f21-921b-2c4e7788f034.png>
  <img src=https://user-images.githubusercontent.com/77096562/180654795-8a543e97-b5b8-488a-8891-308a1d5b5322.png>
  <img src=https://user-images.githubusercontent.com/77096562/180654826-28f7fd0c-60d8-4b5c-8a17-89f70614af73.png>
</div>
算法流程图：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652973-48696510-41a4-4a44-8920-4f0a83576ac1.png>
</div>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654119-800f6e64-e886-497b-81e9-ec2d256e03d9.png></br>
  <strong>初值为(1/4,1/3)时的迭代路径</strong>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654351-ea24c564-02a4-4192-a1de-bd50e5da92b4.png></br>
  <strong>初值为(2,0)时的迭代路径</strong>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654378-2335ac89-5186-40a0-a8e6-eacc9f7df875.png></br>
  <strong>初值为(1,0.5)时的迭代路径</strong>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654504-ce75e8ff-bcb8-4f35-b207-e72af15acc82.png></br>
  <strong>初值为(0,0)时的迭代路径</strong>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654528-d0c63407-79cd-4c35-a7cd-c93ba5cd94be.png></br>
  <strong>初值为(1,0)时的迭代路径</strong>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180654557-b915ece6-b555-4cc6-ae5d-060cf94f2665.png></br>
  <strong>初值为(0.5,0)时的迭代路径</strong>
</div>

<span id='QuadraticPenalty'></span>
## QuadraticPenalty.py
二次罚函数方法求解相关问题</br>
其中问题可以描述为为：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652899-cbda333e-c9ad-4443-ac4e-524b08fd0f93.png>
</div>
求解思路：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180656003-e2879ef7-3da7-493e-ab21-da81a74dfb2f.png>
</div>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180656063-5c61e03a-9204-4a35-8bb2-40643cdb8911.png>
</div>

<span id='ClassicalL1Penalty'></span>
## ClassicalL1Penalty.py
经典的l1精确罚函数方法求解相关问题</br>
其中问题可以描述为为：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652899-cbda333e-c9ad-4443-ac4e-524b08fd0f93.png>
</div>
求解思路：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180656117-4311ff56-2e42-425e-aff1-e0e35957e212.png>
  <img src=https://user-images.githubusercontent.com/77096562/180656140-65e31162-193d-45f9-80f6-0773d0876f89.png>
</div>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/181872737-ba609ecf-3495-4d80-aa4c-fa5bb6e84064.png>
</div>

<span id='AugmentedLagrangian'></span>
## AugmentedLagrangian.py
增广拉格朗日方法求解相关问题</br>
其中问题可以描述为为：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652899-cbda333e-c9ad-4443-ac4e-524b08fd0f93.png>
</div>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180656266-73603440-65ee-4ad3-9281-7c9c0411eecc.png>
  <img src=https://user-images.githubusercontent.com/77096562/180656274-00bb18f2-b556-4af8-a957-eb3402f8ac30.png>
</div>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180656301-d23c5463-4104-4430-a34a-011f86e9e987.png>
</div>

<span id='FunctionByNewton'></span>
## FunctionByNewton.py
给定一个函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180651760-5bcc622c-d106-4fe9-a2a7-f367204a9c83.png>
</div>
使用牛顿法求解极小值（其中已知全局最小值位于x=(1,1)处）：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180651823-b7dbb040-7681-4bd2-98c4-4a900dd33795.png>
</div>
理论证明：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180652048-2e1f159c-d56c-4854-8411-cd457050b913.png>
</div>
由于没有给定初值，因此程序当中随机在[-10, 10]的范围内生成一个随机初值，并带入求解。最后生成了10组随机初值，带入程序，得到结果，如下表格：</br>

|   随机初值        | 迭代次数 |   得到结果位置  |
| :---             |  :---:   |     :---:      |
| (1.57,-0.10)     | 5        |  (1.00,1.00)   |
| (0.14,-4.19)     | 4        |  (-0.00,0.50)  |
| (-5.94,-2.21)    | 9        |  (-1.00,1.00)  |
| (-1.19,-0.64)    | 4        |  (-1.00,1.00)  |
| (-1.08,-1.86)    | 4        |  (-1.00,1.00)  |
| (-3.66,2.69)     | 8        |  (-1.00,1.00)  |
| (-4.86,6.88)     | 8        |  (-1.00,1.00)  |
| (-0.13,0.01)     | 8        |  (-1.00,1.00)  |
| (2.37,-1.82)     | 7        |  (1.00,1.00)   |
| (4.01,-3.00)     | 8        |  (1.00,1.00)   |

最后结果可以看出，并不是每一个初值都可以迭代得到全局最优解。</br>经过验证，函数存在两个最优解：x=(1,1)与x=(-1,1)，以及一个极小值点x=(0,0.5)

<span id='Powellsingular_BFGS'></span>
## Powellsingular_BFGS.py
BFGS方法求解the Powellsingular function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180646534-c9fba3fc-14b4-4f89-9266-db07437dc221.png>
</div>

<span id='Rosenbrock_BFGS'></span>
## Rosenbrock_BFGS.py
BFGS方法求解the Rosenbrock function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644370-b1ea99b9-025a-477b-bc09-e21e538cc63f.png>
</div>

<span id='Rosenbrock_n_BFGS'></span>
## Rosenbrock_n_BFGS.py
BFGS方法求解the extended Rosenbrock function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180646429-bf412a05-f638-41b5-af8d-6e8fa23602be.png>
</div>
求解维度：n=6,8,10</br>
bilibili教程链接：https://www.bilibili.com/video/BV1R34y187zE?spm_id_from=333.999.0.0&vd_source=a28ee82944bc8187d1409ca0e4e99a1c</br>

<span id='RosenbrockBySteepest'></span>
## RosenbrockBySteepest.py
最速下降法求解Rosenbrock function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644370-b1ea99b9-025a-477b-bc09-e21e538cc63f.png>
</div>
运行后迭代次数：8318</br>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644870-e3b5c187-a37a-4d94-b463-394ac8a5ffb7.png>
</div>

<span id='RosenbrockByNewton'></span>
## RosenbrockByNewton.py
牛顿法求解Rosenbrock function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644370-b1ea99b9-025a-477b-bc09-e21e538cc63f.png>
</div>
运行后迭代次数：5</br>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644921-e48eb678-8214-49d3-a5ff-7c05523c05dc.png>
</div>

<span id='BealeBySteepest'></span>
## BealeBySteepest.py
最速下降法求解the Beale function</br>
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644956-6d5987c0-3573-4829-8887-528174588c16.png>
</div>
运行后迭代次数：NAN，算法在（-1.2,1.0）位置作为起始位置时无法收敛</br>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645042-1ab651a2-3a8f-4a31-8e75-8829bb235b6a.png>
</div>

<span id='BealeByNewton'></span>
## BealeByNewton.py
牛顿法求解the Beale function
目标函数表达式：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180644956-6d5987c0-3573-4829-8887-528174588c16.png>
</div>
运行后迭代次数：1，算法在（-1.2,1.0）位置作为起始位置时收敛到函数鞍点，并非全局最小值</br>
迭代路径：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645126-d25f0614-e0ad-4332-bb19-1a9e8a52d89f.png>
</div>

<span id='HilbertByCG'></span>
## HilbertByCG.py
共轭梯度法求解线性系统问题：Ax=b。其中A是希尔伯特矩阵，元素表达式为：</br>
![image](https://user-images.githubusercontent.com/77096562/180645359-b1fa6821-cbba-4784-89b1-4745ccd2b31e.png)</br>
右边为常数向量矩阵：</br>
![image](https://user-images.githubusercontent.com/77096562/180645395-a2323a8c-97d3-4475-bb80-e5bccf1f0308.png)</br>
算法求解结果如下：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645457-3eb50bb8-f78d-4851-a074-e4c743ffcd1b.png>
</div>
维度为5时，其残差与迭代关系折线图：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645505-cc7077a7-edc0-49b8-88e2-210424bf82c5.png>
</div>
维度为8时，其残差与迭代关系折线图：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645522-dd54866a-ef7a-41a6-811f-e2ee4b85b4a3.png>
</div>
维度为12时，其残差与迭代关系折线图：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645528-ae7b3b71-0bc8-4957-b6ab-582e7f990e66.png>
</div>
维度为20时，其残差与迭代关系折线图：</br>
<div align="center">
  <img src=https://user-images.githubusercontent.com/77096562/180645536-e448432f-6e7c-49c2-8def-2fc24ae7ef28.png>
</div>
