import numpy as np
import cmm_lib as cmm


#testing interpolación lineal
data=np.array(
        [
        [[2,3,4,5,6,7,8],
        [4,5,6,7,8,9,10],
        [4,5,6,7,8,9,10],
        ],
        [[4,5,6,7,8,9,10],
        [4,5,6,7,8,9,10],
        [4,5,6,7,8,9,10],
        ],
        ]
        )
#data=np.array(
        #[[2,3,4,5,6,7,8],
        #[4,5,6,7,8,9,10],
        #[4,5,6,7,8,9,10],
        #],
        #)
axis=[[1,2,3,4,5,6,7],[2,4,6],[1,5]]
#axis=[[1,2,3,4,5,6,7],[2,4,6]]
for p in np.arange(1,7.5,0.5):
    print('*'*50)
    point=np.array([p,2.5,3])
    #print('data:', data)
    print('point:',point)
    p_inter=cmm.mlineal(point, axis, data)
    print('resultado:', p_inter)

