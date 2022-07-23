import numpy as np
import matplotlib.pyplot as plt


def cg(x0, MA, Vb):
    """
    共轭梯度法
    :param x0: 初值x0
    :param MA: 系数矩阵A
    :param Vb: 目标常数向量b
    :return: 近似解，迭代次数
    """
    # 记录残差
    rk_get = []
    # 计算起始条件
    r0 = np.dot(MA, x0) - Vb        # 初始梯度
    p0 = -r0                        # 初试下降方向
    # 计算可迭代参数
    rk = r0                         # 当前位置梯度
    pk = p0                         # 当前下降方向
    xk = x0                         # 当前近似解
    # 运行参数设置
    Times = 0                       # 记录迭代次数
    # 进入迭代程序
    while np.linalg.norm(rk) >= 1e-6:
        # 记录残差
        rk_get.append(np.linalg.norm(rk))
        # 迭代计算
        rk_1_dot = np.dot(rk.T, rk)                     # 计算上一步梯度内积
        ak = rk_1_dot / np.dot(np.dot(pk.T, MA), pk)    # 计算步长
        xk = xk + ak * pk                               # 更新当前解
        rk = rk + ak * np.dot(MA, pk)                   # 更新xk+1下的梯度
        bk = np.dot(rk.T, rk) / rk_1_dot                # 计算rk与rk+1内积比值
        pk = -rk + bk * pk                              # 计算下一步下降方向
        # 记录迭代次数
        Times += 1
    return xk, Times, rk_get


def Hilbert(dim):
    sq = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            sq[i][j] = 1 / (i + j + 1)
    return sq


if __name__ == '__main__':
    dims = [5, 8, 12, 20]
    for n in dims:
        b = np.ones(n)                          # 等式右边的向量b
        A = Hilbert(n)                          # 生成希尔伯特矩阵
        x_start = np.zeros(n)                   # 设置初始解
        result, times, rk_s = cg(x_start, A, b)
        # 绘制残差与次数关系
        plt.plot(range(times), rk_s)
        plt.xlabel('iteration numbers')
        plt.ylabel('residual')
        plt.title(f'dim = {n}')
        plt.show()
        # 结果输出
        print(f"dimensions: {n}")
        print(f"迭代次数为：{times}")
        print("近似值为:", result)




