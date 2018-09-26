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

def camino(path,s,t):
    lista=[]
    h = n = s
    while n != t:
        n=path[h]
        lista.append(n)
        h =n
    print(len(lista))
    print('Porcentaje resuelto: ',(len(lista)/145224)*100)
    return lista
a = LeerListAP('LAP2.txt')
#145224
sg=0
tg=2017
b=0

print('Ida')
print('\n')
for i in range(72):
    path, weight = UCS(a,sg,tg)
    print(camino(path,tg,sg))
    r=len(camino(path,tg,sg))
    r=r+b
    b=r
    sg+=2017
    tg+=2017
print('porcentaje resuelto', (r/145224)*100)

print('Regreso')
print('\n')

sg=0
tg=8068

for i in range(18):
    path, weight = UCS(a,sg,tg)
    print(camino(path,tg,sg))
    r=len(camino(path,tg,sg))
    r=r+b
    b=r
    sg+=8068
    tg+=8068
print('porcentaje resuelto', (r/145224)*100)

