import numpy as np

A = np.matrix([
    [4, 5, 3, 6],
    [1, 4, 9, 1],
    [3, 7, 0, 3]
])

print(f'A:\n{A}\n')

U_eigen_values, U = np.linalg.eig(A @ A.T)
V_eigen_values, V = np.linalg.eig(A.T @ A)

U = U[:, np.argsort(U_eigen_values)[::-1]]
U[:, 0] *= -1
V = V[:, np.argsort(V_eigen_values)[::-1]] * -1

U_eigen_values = np.sqrt(U_eigen_values)
U_eigen_values.sort()
S = np.diag(U_eigen_values[::-1])
S = np.hstack([S, np.zeros([3, 1])])

print(f'U:\n{U}\n')
print(f'VT:\n{V.T}\n')

print('S:\n', S, '\n')

print('USVT:\n', U @ S @ V.T, '\n')

L1 = U[:, 0] @ V.T[0, :] * U_eigen_values[::-1][0]
L2 = U[:, 1] @ V.T[1, :] * U_eigen_values[::-1][1]
L3 = U[:, 2] @ V.T[2, :] * U_eigen_values[::-1][2]

print("Layer1\n", L1, "\n")
print("Layer2\n", L2, "\n")
print("Layer3\n", L3, "\n")

print("Layer1 + Layer2\n", L1 + L2, "\n")
print("Layer1 + Layer2 + Layer3\n", L1 + L2 + L3, "\n")
