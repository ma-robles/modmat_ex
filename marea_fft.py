'''
Aproximación de marea a partir de sus principales componentes
Requiere especificar el archivo con los datos
calcula las componentes usando fft
toma todas las que son mayores a un límite
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as mpltext
import datetime as dt
import sys
import math
sys.path.append('../')
import cmm_lib as cmm

data_file=sys.argv[1]
#ncom=int(sys.argv[2])

pcom=[
        12.4206012,
        12,
        12.65834751,
        11.96723606,
        23.93447213,
        25.81933871,
        24.0659,
        ]
pcom=np.array(pcom)
#load data
time=[]
time_s=[]
nivel=[]
with open(data_file) as dfile:
    for i,line in enumerate(dfile):
        text_data=line.split()
        t=dt.datetime(int(text_data[0]),
            int(text_data[1]),
            int(text_data[2]),
            int(text_data[3]),
            int(text_data[4]),
            int(text_data[5]),
            )
        time.append(t)
        time_s.append((t-time[0]).total_seconds())
        h=float(text_data[6])
        nivel.append(h)

nivel=np.array(nivel)
#obtención de las componentes
fou=np.fft.fft(nivel)
fou=np.abs(fou)/fou.size
#se toma únicamente la mitad
fou=2*fou[:fou.size//2]
#cálculo de valores de frecuencia d es el periodo en s
freq=np.fft.fftfreq(nivel.size, d=60)
freq=freq[:freq.size//2]
#transformamos a periodo en horas
#factor de conversión
kT=60*60
T_h =1/(freq*kT)

lim=0.015
#cond=(fou>lim)|(fou>0.0005)&(T_h>0.0202)&(T_h<0.0204)
cond=(fou>lim)
#componentes de alta freq
#cond|=(fou>0.00037)&(T_h>0.005)&(T_h<0.01)
#cond|=(fou>0.00025)&(T_h>0.0035)&(T_h<0.0040)
fou_opt=fou[cond]
freq_opt=freq[cond]
T_opt_h=1/(freq_opt*kT)
ncom=freq_opt.size-1
functions=(lambda x: x/24, lambda x: x*24)
xlabels=[
        'Periodo [Horas]',
        'Periodo [Días]',
        ]
titles=[
        'Espectro obtenido con FFT(escalas log)',
        #'Componentes con magnitud A>{} ({})'.format(lim, ncom+1),
        'Componentes semidiurnas con magnitud A>{}'.format(lim),
        'Componentes diurnas con magnitud A>{}'.format(lim),
        ]
geoms=[
        '211',
        #'312',
        '223',
        '224',
        ]
axs=[]

fig=plt.figure(figsize=(9,9), frameon=False)
#subplot format
for i,g in enumerate(geoms):
    axs.append([plt.subplot(g) , None])
    axs[-1][0].set_title(titles[i], {'fontsize': 10,})
    axs[-1][0].set_xlabel(xlabels[0], fontsize=8, horizontalalignment='right', x=1.0)
    axs[-1][0].tick_params(labelsize=8)
    axs[-1][1]=axs[-1][0].secondary_xaxis('top', functions=functions)
    axs[-1][1].set_xlabel(xlabels[1],fontsize=8, horizontalalignment='right',x=1.0)
    axs[-1][1].tick_params(labelsize=8)
    
#ploting
mstyle={'color':'C0',
        'linestyle':'None',
        'marker':'o',
        'markersize':3,
        'fillstyle':'none',
        }
xscale="log"
color='#37224860'
colorp='#F46036'
colorf=color[:-2]
colorv='#4E4B5C'
fontsize=8
#extra markers
i=0
#axs[i][0].plot(T_h, fou, **mstyle)
axs[i][0].vlines(T_h,0,fou,colors=color,
        label='Todas las componentes ({})'.format(fou.size))
axs[i][0].vlines(T_opt_h,0,fou_opt, colors=colorp,
        label='Componentes magnitud A>{} ({})'.format(lim, ncom+1))
axs[i][0].set_xscale(xscale)
axs[i][0].set_yscale(xscale)
axs[i][0].set_xlim(0.01,10000)
axs[i][0].set_ylim(0.0001,0.15)
axs[i][0].legend(fontsize='small')
axs[i][0].annotate('Componentes semidiurnas\n(~12 horas)',
        fontsize='x-small',ha='right',
        xy=(11,.01),
        xytext=(4, .015),
        arrowprops=dict(arrowstyle="->",
            #connectionstyle="angle3,angleA=0,angleB=-90"),
            )
        )
axs[i][0].annotate('Componentes diurnas\n(~24 horas)',
        fontsize='x-small',
        xy=(28,.01),
        xytext=(100, .015),
        arrowprops=dict(arrowstyle="->",
            #connectionstyle="angle3,angleA=0,angleB=-90"),
            )
        )
#i+=1
##axs[i][0].plot(T_opt_h,fou_opt, **mstyle)
#axs[i][0].vlines(T_opt_h,0,fou_opt, colors=color)
#axs[i][0].set_xscale(xscale)
i+=1
xmin=11.9
xmax=12.7
xcond=(T_opt_h>xmin)&(T_opt_h<xmax)
X=T_opt_h[xcond]
Y=fou_opt[xcond]
#axs[2][0].plot(X,Y,'.')
axs[i][0].vlines(X,0,Y,colors=(colorp))
axs[i][0].vlines(pcom[(pcom>xmin)&(pcom<xmax)],0,np.max(Y),
    colors=(colorv),
    linestyles=('dotted'),
    )
axs[i][0].text(12.43,.12,'M2',fontsize=fontsize)
axs[i][0].text(12.01,.12,'S2',fontsize=fontsize)
axs[i][0].text(12.66,.12,'N2',fontsize=fontsize)
axs[i][0].text(11.93,.12,'K2',fontsize=fontsize)
i+=1
xmin=23.5
xmax=27
xcond=(T_opt_h>xmin)&(T_opt_h<xmax)
X=T_opt_h[xcond]
Y=fou_opt[xcond]
#axs[i][0].plot(X,Y,'o',fillstyle='none', markersize=4)
axs[i][0].vlines(X,0,Y,colors=(colorp))
axs[i][0].vlines(pcom[(pcom>xmin)&(pcom<xmax)],0,np.max(Y),
    colors=(colorv),
    linestyles=('dotted'),
    )
axs[i][0].text(23.74,.10,'K1',fontsize=fontsize)
axs[i][0].text(25.83,.10,'O1',fontsize=fontsize)
axs[i][0].text(24.08,.10,'P1',fontsize=fontsize)

plt.tight_layout()

time_s=np.array(time_s)
H=[np.ones(len(time))]
W=[]
for f in freq_opt[1:]:
    w=2*np.pi*f
    W.append(w)
    H.append(np.sin(w*time_s))
    H.append(np.cos(w*time_s))
H=np.array(H).T
A=cmm.min2_mtx(H[::60,:],nivel[::60])
#A=cmm.min2_mtx(H[:],nivel[:])
Am=[]
Af=[]
W=np.array(W)
nivel_C=A[0]*np.ones(len(time_s))
text_table=[['Periodo[h]\tMagn\tfase[°]'],]
print('\t'.join(text_table[-1]))
text_table.append(['{:8.3f}'.format(0),'{:4.3f}'.format(A[0]),'-'])
print('\t'.join(text_table[-1]))
for i,w in enumerate(W):
    new_comp=A[i*2+1]*np.sin(w*time_s)+A[i*2+2]*np.cos(w*time_s)
    text_table.append([
        '{:8.3f}'.format(T_opt_h[i+1]),
        '{:4.3f}'.format(np.sqrt(A[i*2+2]**2+A[i*2+1]**2)),
        '{:4.3f}'.format(math.degrees(math.atan2(A[i*2+1],A[i*2+2]))),
        ])
    print('\t'.join(text_table[-1]))
    nivel_C+=new_comp

error_abs=nivel_C-nivel
RMSE=math.sqrt(np.sum(error_abs**2)/len(nivel))

title="Marea (Acercamiento a 3 días)"
tsize=10
plt.figure(figsize=(9,6.5))
axm1=plt.subplot(2,1,1)
axm1.set_title(title, fontsize=tsize)
axm1.plot_date(time,nivel, marker='.',ms=3,ls='',c='#5158BB',label='datos')
axm1.plot_date(time,nivel_C,'#EF271B',label='aproximación ({}componentes)'.format(ncom+1))
axm1.set_xlim(time[0],time[3*24*60])
axm1.legend(fontsize='small')
axm1.tick_params(labelsize=8)
axm2=plt.subplot(2,1,2)
axm2.set_title("error para todo el año (aprox-dato) RMSE={:6.5f}".format(RMSE),
        fontsize=tsize)
#axm2.plot_date(time,error_abs, 'm', label='error (aprox-dato)')
axm2.vlines(time,0,error_abs, colors='#4381C1', label='error(aprox-dato)')
axm2.tick_params(labelsize=8)

#plt.table(text_table,
        #loc='right',
        #colWidths=[0.1,0.1, 0.1],
        #bbox=[1,-1,0.3,2],
        #)
plt.tight_layout()
plt.show()
#plt.savefig("acapulco_cmp{:02}.png".format(ncom))

