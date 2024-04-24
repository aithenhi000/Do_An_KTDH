import math as m 
import numpy as np


def tinh_tien(pos, delta_x, delta_y):
    
    mul_matrix = np.array(( [1, 0, 0],
                            [0, 1, 0],
                            [delta_x, delta_y, 1]))
    if pos.ndim == 1:
        pos = np.matmul(pos, mul_matrix)
    else:
        for x in range(0,pos.shape[0]):        
            pos[x]=np.matmul(pos[x],mul_matrix)
            
    return pos

arr= np.array(([4,5,1]))
arr = tinh_tien(arr,10,10)
print(arr)
        
def xoay_goc_x_do(pos, deg):
    
    cos=  m.cos(deg*m.pi/180)
    sin = m.sin(deg*m.pi/180)
    
    mul_matrix = np.array(( [cos,     sin,  0],
                            [-1*sin,  cos,  0],
                            [0,         0,  1]))
    if pos.ndim == 1:
        pos = np.matmul(pos, mul_matrix) 
    else:
        for x in range(0,pos.shape[0]):        
            pos[x]=np.matmul(pos[x],mul_matrix)
            
    return pos

def ti_le(pos, ratio):
    
    mul_matrix = np.array(( [ratio, 0,      0],
                            [0,     ratio,  0],
                            [0,     0,      1]))
    if pos.ndim == 1:
        pos = np.matmul(pos, mul_matrix)
    else :
        for x in range(0,pos.shape[0]):        
            pos[x]=np.matmul(pos[x],mul_matrix)
        
    return pos


def doi_xung(pos, choice):
    mul_matrix = np.array(( [-choice[1], 0,          0],
                            [0,         -choice[0],  0],
                            [0,          0,          1]))
     
    if pos.ndim == 1:
        pos = np.matmul(pos, mul_matrix)
    else:
        for x in range(0,pos.shape[0]):        
            pos[x]=np.matmul(pos[x],mul_matrix)
    
    return pos

#Hàm chính, nhập các giá trị độ dài tại đây (từ tọa độ 2 điểm ban đầu), tính toán vị trí để putpixel
def draw(a,b, right, up):
    
    pos = np.array([[0,0],[a,0],[a,b],[0,b]])
    pos = np.insert(pos,2,1,1)
    
    
    xoay_goc_x_do(pos,45)
    tinh_tien(pos, 35, 12)
    doi_xung(pos,[1,1]) #doi xung truc [x,y] - yes/no
    
    for x in range(0,pos.shape[0]): 
        if x == pos.shape[0]-1:
            next = 0
        else:
            next = x + 1
        drawA_to_B(pos[x],pos[next])