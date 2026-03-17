import numpy as np

# 定义两个矩阵
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 矩阵乘法运算
c = np.dot(a, b)
print("矩阵a：")
print(a)
print("矩阵b：")
print(b)
print("矩阵乘积c：")
print(c)