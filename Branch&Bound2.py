# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 02:44:45 2018

@author: Emmanuel
"""
import heapq as hq

def str2pair(x):
    """
    Recibe una cadena como '4,5' y retorna una tupla (4, 5)
    """
    nums = x.split(',')
    return int(nums[0]), float(nums[1])

def LeeLAP2LAP(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de lista de adyacencia
    con pesos y retorna una lista de adyacencia con pesos
    """
    G = []
    file = open(filename)
    for line in file:
        G.append([str2pair(x) for x in line.split(' ')])
    return G
'''
GLOBALS
'''
ways=LeeLAP2LAP("LAP2.txt")
n=len(ways[:15000])
final_path=[]
visited=[False]*n
upperB = [float('Inf')]
def CopiarPath(filename,path):
    file=open(filename,"w")
    s=""
    N=len(path)
    c=0
    p=[-1]*N
    for i in path:
        p[c]=i
        c=i
    for i in p:
        s+=str(i)+"\n"
    file.write(s[:-1])
    
def TSP(G, s,t):
    curr_path=[]
    curr_bound = 0
    
    for i in G:
        curr_bound+=i[0][1]+i[1][1]
    curr_bound/=2
    queue=[]
    level=0
    hq.heappush(queue,(curr_bound,s,level,curr_path))
    c=0
    while len(queue)>0:
        if 100*level/t > c:
            print(c,"%")
            c+=1
        curr_bound,u,lv,path = hq.heappop(queue)
        print(path)
        if visited[u] or curr_bound>upperB[0]:
            continue
        for i in range(len(visited)):
            visited[i]=False
        for node in path:
            visited[node]=True
        visited[u]=True
        if len(path)==t:
            print(path)
            final_path=path[:]
            final_path.append(s)
            upperB[0]=curr_bound
        paux=path[:]
        paux.append(u)
        for v,e in G[u]:
            if not level:
                vBound=curr_bound+e-(G[u][0][1]+G[v][0][1])/2
            else:
                vBound=curr_bound+e-(G[u][1][1]+G[v][0][1])/2
            if vBound<upperB[0]:
                if lv>level:
                    level=lv
                hq.heappush(queue,(vBound,v,lv+1,paux[:]))
        
    return upperB

TSP(ways,0,15)
CopiarPath("Ruta2.txt",final_path[1:])

