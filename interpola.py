import itertools as it

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
    return(cell)

def mlineal(point,idx_cell,data,axis):
    cell=[]
    for i in it.product([0,1],repeat=len(idx_cell)):
        #idx=(idx_cell[0][i[0]],idx_cell[1][i[1]])
        cell.append(data[i])
    print('cell:',cell)
    for i in range(int(2**(len(cell)/2))-1):
        print('axis:',axis[i])
        x2=axis[i][idx_cell[i][1]]
        x1=axis[i][idx_cell[i][0]]
        dx=x2-x1
        xi=point[i]
        print('dx:',dx)
        vi=cell[2*i]*(x2-xi)/dx+cell[2*i+1]*(xi-x1)
        print(vi)


import numpy as np
a=np.array([1,2,3,4,5,6,7])
b=np.tile(a,(3,1))
c=[a,[2,4,6]]#,[5,6,7,8,9,10,11]]
a=np.reshape(a,(1,a.size))
d=np.zeros((2,0))
for p in np.arange(1,7.5,0.5):
    idx_cell=find_cell(np.array([p,2.5]),c)
    print('idx_cell:',idx_cell,)
    print('data:', b)
    print('point:',[p,2.5])
    mlineal([p,2.5],idx_cell,b,c)

exit()
def bilineal(data,P):
    '''
    data - arreglo con datos
    P - arreglo con puntos
    data y P deben tener el mismo número de ejes
    '''
'''
bilineal(x,y,qinfo)
Calcula la interpolación bilineal
parámetros:
    x - coordenada x del punto a interpolar. puede ser un arreglo de numpy
    y - coordenada y del punto a interpolar. puede ser un arreglo de numpy
    qinfo - diccionario con los siguientes elementos:
        x1,x2 - coordenadas en x
        y1,y2 - coordenadas en y
        fqXY - valores en los 4 puntos cercanos. 
ejemplo:
qinfo={}
qinfo['x1']=0
qinfo['x2']=1
qinfo['y1']=0
qinfo['y2']=1
qinfo['fq11']=5
qinfo['fq12']=10
qinfo['fq21']=10
qinfo['fq22']=10
x=np.array([0.1,0.5])
y=np.array([0.1,0.5])
r=bilineal(x,y,qinfo)
'''

def bilineal_a(x,y,qinfo):
    x1=qinfo['x1']
    x2=qinfo['x2']
    y1=qinfo['y1']
    y2=qinfo['y2']
    q11=qinfo['fq11']
    q12=qinfo['fq12']
    q21=qinfo['fq21']
    q22=qinfo['fq22']
    dx=x2-x1
    dy=y2-y1
    fr1=q11*(x2-x)/dx + q21*(x-x1)/dx
    fr2=q12*(x2-x)/dx + q22*(x-x1)/dx
    fp=fr1*(y2-y)/dy+fr2*(y-y1)/dy
    return fp

'''
get_qinfo(x,y,P)
obtiene los valores de qinfo a partir de datos de la malla
x - arreglo con coordenadas en el eje x
y - arreglo con coordenadas en el eje y
var - arreglo con los valores de la variable
P - diccionario con coordenadas del punto P
    x - coordenada x
    y - coordenada y
regresa qinfo
'''

def get_qinfo(x,y,var,P):
    qinfo={}
    def check_v(v,P):
        axis=['x', 'y']
        for ax in axis:
            if P[ax]<v[0] or P[ax]>v[-1]:
                return None
            elif P[ax]==v[-1]:
                qinfo[ax+'1']=v[-1]
                qinfo[ax+'2']=v[-1]
            else:
                for i in range(len(v)-1):
                    if P[ax]==v[i]:
                        qinfo[ax+'1']=v[i]
                        qinfo[ax+'2']=v[i]
                        break
                    if P[ax]>v[i] and P[ax]<v[i+1]:
                        qinfo[ax+'1']=v[i]
                        qinfo[ax+'2']=v[i+1]
                        break
                qinfo['fq11']=var
        return qinfo
    qinfo=check_v(x,P)
    return qinfo

import numpy as np

x=np.arange(0,5,1)
y=np.arange(0,5,1)
xx,yy= np.meshgrid(x,y)
var=np.sin(xx**2+yy**2)/(xx**2+yy**2)
P={'x':4,
        'y':2.5}
r=get_qinfo(x,y,var,P)
print(x)
print(y)
print(var)
print(P)

print(r)
        
