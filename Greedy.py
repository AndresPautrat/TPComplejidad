
# coding: utf-8

# In[ ]:


import heapq as hp
from math import sqrt
def asd(x):
    num = x.split(',')
    return int(num[0]),float(num[1])

def LeerListAP(filename):
    G=[]
    file= open(filename)
    for line in file:
        G.append([asd(x) for x in line.split(' ')])
    file.close()
    return G
def Leerxy(filename):
    G=[]
    file= open(filename)
    for line in file:
        s=str(line)[:len(str(line))-1]
        G+=[[float(s.split(';')[2]),float(s.split(';')[3])]]
    file.close()
    return G
def distancias_init(init,xy):
    distancias=[]
    for i in xy:
        distancias+=[sqrt((i[0]-xy[init][0])**2 + (i[1]-xy[init][1])**2)]
    return distancias
def Greedy(visited,conex,distancias,init,actual,sol,paso):
    visited[actual]=True
    if init==actual:
        if paso!=0:
            if paso==len(conex)-1:
                sol[paso]=init
                return True
            else: return False
        else: visited[actual]=False
    
    dsts=[]
    for i in range(len(conex[actual])):
        dsts+=[[conex[actual][i][0],distancias[conex[actual][i][0]]]]
    dsts.sort(key=lambda tup: tup[1])
    dsts=dsts[::-1]
    completado=False
    
    for j in range(len(dsts)):
        if visited[dsts[j][0]]==False:
            if Greedy(visited,conex, distancias,init, dsts[j][0],sol,paso+1):
                sol[paso]=actual
                completado= True
                break
            else: visited[dsts[j][0]]=False

    return completado
    
conec=LeerListAP("LAP2.txt")
dst=distancias_init(0,Leerxy('BDO.txt'))
sol=[-1]*len(conec)
visited = [False]*len(conec)
Greedy(visited,conec,dst,0,0,sol,0)
print(sol)

