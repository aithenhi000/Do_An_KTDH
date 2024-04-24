import math as m 
import numpy as np



def tinh_tien(pos, delta_x, delta_y):
    
    mul_matrix = np.array(( [1, 0, 0],
                            [0, 1, 0],
                            [delta_x, delta_y, 1]))
    
    for x in range(0,pos.shape[0]):        
        pos[x]=np.matmul(pos[x],mul_matrix)
    return pos[x]
 
arr  = np.array([1, 2, 1])
print(tinh_tien(arr, 5, 10))   