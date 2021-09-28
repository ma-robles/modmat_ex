import numpy as np
import itertools as it

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

def find_cell(point, axis):
    '''
    devuelve los ìndices en donde se encuentra el punto en los ejes dados
    point - punto a ubicar
    axis - lista de ejes
    si los valores se encuentran fuera de rango regresa -1
    '''
        
    if len(point) != len(axis):
        print('len(axis) debe ser igual a len(point): {} != {}'.format(
            len(axis),
            len(point),
            ))
        return(-1)
    cell=[]
    for p,ax in zip(point, axis):
        if p<ax[0] or p>ax[-1]:
            print('punto fuera de rango')
            return(-1)
        if p==ax[-1]:
            high=-1
        else:
            high,=np.where(p<ax)
            high=high[0]
        cell.append([high-1, high])
    return(np.array(cell))

def mlineal(point, axis, data):
    '''
    Realiza interpolación lineal en varios ejes usando la ecuación:
    fx=fx1*(x2-xi)/dx + fx2*(xi-x1)/dx

    Parámetros:
    point - el punto a interpolar
    axis - la lista de los ejes p. Ej: [lat lon t]
    data - arreglo con los datos, debe coincidir con las dimensiones de los ejes (axis) dados
    '''
    #obtiene índices de la celda donde se encuentra el punto
    idx_cell=find_cell(point, axis)
    # obtiene valores en los vértices
    # se almacenan en f_list
    f_list=[]
    # i representa cada una de las combinaciones posibles
    # la cantidad depende del número de ejes
    #  1 eje = 2 vértices
    # 2 ejes = 4 vértices
    # 3 ejes = 8 vértices
    # etc...
    for i in it.product([0,1],repeat=len(idx_cell)):
        tp_idx=[]
        naxis=len(idx_cell)
        for idx in range(naxis):
            tp_idx.append(idx_cell[naxis-1-idx][i[idx]])
        tp_idx=tuple(tp_idx)
        f_list.append(data[tp_idx])

    #calcula interpolación para cada par de vértices
    #ax_ list contiene la lista de los puntos que se utilizarán para cada operación de interpolación
    #comienza con los vértices
    ax_list=[f_list]
    for n_ax,fx12 in enumerate(ax_list):
        f_list=[]
        for j in range(0,len(fx12),2):
            #print('axis:',axis[n_ax])
            x2=axis[n_ax][idx_cell[n_ax][1]]
            x1=axis[n_ax][idx_cell[n_ax][0]]
            dx=x2-x1
            xi=point[n_ax]
            fx=fx12[j]*(x2-xi)/dx+\
                    fx12[j+1]*(xi-x1)/dx
            # se agregan los nuevos puntos a un nuevo elemento
            f_list.append(fx)
            #print('x1:{},x2:{},xi:{},dx:{}, fx:{}'.format(
                #x1,x2,xi,dx,fx))
        #se deja de agregar cuando sólo se obtiene un punto
        if len(f_list)>1:
            ax_list.append(f_list)
    return f_list

