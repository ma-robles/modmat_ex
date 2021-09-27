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

#euler
#t time array
#y0 init value
#f function f(t,y)
def euler(t,y0,f):
    h=t[1]-t[0]
    y=[y0]
    for ti in t[:-1]:
        y.append(y[-1]+h*f(ti,y[-1]))
    return y

#runge kutta 4 orden
#t time array
#y0 init value
#f function f(t,y)
def rk4(t,y0,f):
    h=t[1]-t[0]
    y_rk=[y0]
    for ti in t[:-1]:
        k1=h*(f(ti,y_rk[-1]))
        k2=h*(f(ti+h/2,y_rk[-1]+k1/2))
        k3=h*(f(ti+h/2,y_rk[-1]+k2/2))
        k4=h*(f(ti+h,y_rk[-1]+k3))
        y_rk.append(y_rk[-1]+(k1+2*k2+2*k3+k4)/6)
    return y_rk

#runge kutta 2 orden
#t time array
#y0 init value
#f function f(t,y)
def rk4(t,y0,f):
    h=t[1]-t[0]
    y_rk=[y0]
    for ti in t[:-1]:
        k1=h*(f(ti,y_rk[-1]))
        k2=h*(f(ti+h/2,y_rk[-1]+k1/2))
        k3=h*(f(ti+h/2,y_rk[-1]+k2/2))
        k4=h*(f(ti+h,y_rk[-1]+k3))
        y_rk.append(y_rk[-1]+(k1+2*k2+2*k3+k4)/6)
    return y_rk
