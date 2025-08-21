import numpy as np

A = np.array([[1,2,3],
              [0,1,4],
              [5,6,0]])

inv_A = np.linalg.inv(A)
print("inverse of A")
print(inv_A)

product_1 = np.matmul(A, inv_A)
print("product of A and inv_A\n", product_1)

product_2 = np.matmul(inv_A, A)
print("product of A and A\n", product_2)








