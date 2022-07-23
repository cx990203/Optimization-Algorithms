# -------------------------------------------------
# BFGS法求解the Powellsingular function最小值
# -------------------------------------------------
import numpy as np


def Powellsingular(x: np.ndarray):
    if x.size != 4:
        return np.array([])
    ret = (x[0] + 10 * x[1]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4
    return ret


def grad(x: np.ndarray):
    if x.size != 4:
        return np.array([])
    ret = np.array([
        2 * (x[0] + 10 * x[1]) + 40 * (x[0] - x[3]) ** 3,
        20 * (x[0] + 10 * x[1]) + 4 * (x[1] - 2 * x[2]) ** 3,
        10 * (x[2] - x[3]) - 8 * (x[1] - 2 * x[2]) ** 3,
        -10 * (x[2] - x[3]) - 40 * (x[0] - x[3]) ** 3
    ])
    return ret


def BFGS(x):
    maxk = 10000  # 设置最大次数
    W = np.zeros((4, maxk))  # 结果记录buffer
    W[:, 0] = x0
    x = x0  # 设置起始点
    i = 0  # 记录迭代次数
    df_max = 1e-5  # 停止迭代时梯度阈值
    Bk = np.eye(4)  # 初始化为单位矩阵
    while np.linalg.norm(grad(x)) > df_max and i < maxk:
        # 计算前进方向
        p = -np.linalg.solve(Bk, grad(x))
        # Armijo求解步长
        rho = 0.55
        sigma = 0.2
        m = 0
        alpha = 0
        while m < 20:
            newf = Powellsingular(x + rho ** m * p)
            oldf = Powellsingular(x)
            if newf < oldf + sigma * rho ** m * np.dot(grad(x).T, p):
                alpha = rho ** m
                break
            m += 1
        # 计算新的迭代点
        xk_1 = x + alpha * p
        # 更新Bk
        sk = xk_1 - x
        yk = grad(xk_1) - grad(x)
        Bk = Bk - np.outer(np.dot(Bk, sk), np.dot(sk.T, Bk)) / np.dot(np.dot(sk.T, Bk), sk) + np.outer(yk, yk.T) / np.dot(yk.T, sk)
        # 数据迭代
        x = xk_1
        # 数据记录
        W[:, i + 1] = x  # 记录当前位置
        i += 1  # 计算迭代次数
    print(f"迭代次数为：{i}")
    print(f"近似解为：{x}")
    print(f"函数值为：{Powellsingular(x)}")
    print(f"当前位置梯度范数：{np.linalg.norm(grad(x))}")
    W = W[:, 0:i + 1]
    return W


if __name__ == '__main__':
    x0 = np.array([3, -1, 0, 1])
    W = BFGS(x0)
