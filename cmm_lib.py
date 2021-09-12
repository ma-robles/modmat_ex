import numpy as np

#solve
#A.T*Ax=A.T*b
#x=inv(A.T*A)*A.T*b
#Z=inv(H.T*H)*H.T*y
def min2_mtx(A,b):
    x=np.matmul(A.T,A)
    x=np.linalg.inv(x)
    x=np.matmul(x,A.T)
    x=np.matmul(x,b)
    return x
