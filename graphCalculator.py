

import numpy as np




def ConnCreator(lst):
    out = np.zeros((6,6))
    for i in range(4):
        for j in range(6):
            out[1+i,j]=lst[6*i+j]
    out[0,0]=1
    out[-1,-1]=1
    return out
            


def MatCreator(connexion):
    n = [0,0,0,0,0,0]
    for i in range(len(connexion)):
        n[i]=sum(connexion[i])
    m = np.zeros((6,6))
    for i in range(len(m)):
        m[i,i]=1/n[i]
    return np.transpose(np.matmul(m,connexion))

def Result(lst):
    connexion = ConnCreator(lst)
    B = MatCreator(connexion)
    
    out = np.array([1,0,0,0,0,1])
    
    cond=True
    i=0
    while cond:
        i+=0
        out = np.matmul(out,B)
        if not 0 in out:
            cond=False
        if i==20:
            print("DNF")
            cond=False
    print(out)

