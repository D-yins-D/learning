import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = np.dot(v1, v2)
print(f"向量v1和v2的点积为：{dot_product}")

A = np.array([[1, 2],
             [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
matrix_product = A @ B
print(f"矩阵A和B的乘积为{matrix_product}")

print("A的转置：\n", A.T)
det_A = np.linalg.det(A)
print(f"A的行列式{det_A:.2f}")

A_inv = np.linalg.inv(A)
print(f"A的逆矩阵\n", A_inv)

identity_matrix = A @ A_inv
print("验证A乘以A的逆矩阵为（单位矩阵）:\n", np.round(identity_matrix))

import numpy as np

def f(x, y):
    return x**2 + y**2

x, y = 1, 2
h = 1e-5
grad_x = (f(x+h, y) - f(x, y)) / h
grad_y = (f(x, y+h) - f(x, y)) / h
grad = np.array([grad_x, grad_y])
print("梯度为：", grad)