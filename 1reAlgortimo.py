import math as mt
import heapq as hp

def asd(x):
    num = x.split(',')
    return int(num[0]),float(num[1])

def LeerListAP(filename):
    G=[]
    file= open(filename)
    for line in file:
        G.append([asd(x) for x in line.split(' ')])
    return G
# solo recorre un camino
def UCS(G,s,t):
    n = len(G)
    visited = [False]*n
    path = [None]*n
    weight = [mt.inf]*n
    queue = []
    weight[s] = 0
    hp.heappush(queue,(0,s))
    while len(queue)>0:
        g , u = hp.heappop(queue)
        if visited[u] : continue
        visited[u]= True
        if u == t: break
        for v,h in G[u]:
            f = g+h
            if f<weight[v]:
                path[v]= u
                weight[v]=f
                hp.heappush(queue,(f,v))
    return path, weight

a = LeerListAP('LAP2.txt')

path, weight= UCS(a,0,145224)

def camino(path,s):
    lista=[]
    h = n = s
    while n != 0:
        n=path[h]
        lista.append(n)
        h =n
    print(len(lista))
    print('Porcentaje resuelto: ',(len(lista)/145224)*100)
    return print(lista)

camino(path,145224)

