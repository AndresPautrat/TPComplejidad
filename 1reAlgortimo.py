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
def UCS(G,s,t,visited):
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

def CrearTxt(lista,filename, listaux): 
    file = open(filename,"w")
    for i in range(len(lista)-1):
        listaux[lista[i]]=lista[i+1]
    for i in listaux:
        file.write(str(i))
        file.write('\n')
    file.close()
    
def camino(path,s,t):
    lista=[]
    h = n = s
    while n != t:
        n=path[h]
        lista.append(n)
        h =n
    lista.reverse()
    return lista
a = LeerListAP('LAP2.txt')
#145224

listaux = [-1]*len(a)
def Recorrido(a,sg,tg,b,cont,interador):
    lista = []
    for i in range(interador):
        path, weight = UCS(a,sg,tg)
        camino(path,tg,sg)
        lista.extend(camino(path,tg,sg))
        r=len(camino(path,tg,sg))
        r=r+b
        b=r
        sg+=cont
        tg+=cont
    print('porcentaje resuelto', (r/145224)*100)
    return lista

lista = Recorrido(a,0,2017,0,2017,72)
CrearTxt(lista,'UCS.txt',listaux)

lista0 = Recorrido(a,0,8068*2,0,8068*2,9)
CrearTxt(lista0,'UCS0.txt',listaux)

