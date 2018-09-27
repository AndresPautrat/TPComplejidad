# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:16:30 2018

@author: Emmanuel
"""
from operator import itemgetter
from time import time

def LeerCPS(CPS):
    cps=open(CPS,"r")
    G = []
    for line in cps:
        a,b=[float(i) for i in line.split(',')]
        G.append((a,b))
    return G

cpsY=LeerCPS("SortedYBDO.txt")
#cpsX=LeerCPS("SortedXBDO.txt")

def CrearCaminos(cps,filename,filename2):
    file = open(filename,"w")
    file2 = open(filename2,"w")
    n=len(cps)
    c=0
    
    for u in cps:
        s=""
        s2=""
        s2+=str(u[0]) + "," + str(u[1]) + " "
        cercanos=[]
        for j in range(1,10000):
            v1=(c+j)%145225
            v2=(c-j)%145225
            xv1,yv1= cps[v1][0], cps[v1][1]
            d1=((xv1-u[0])**2+(yv1-u[1])**2)**0.5
            xv2,yv2= cps[v2][0], cps[v2][1]
            d2=((xv2-u[0])**2+(yv2-u[1])**2)**0.5
            cercanos.append([v1,xv1,yv1,d1])
            cercanos.append([v2,xv2,yv2,d2])
        cercanos.sort(key=itemgetter(3))
        for j in cercanos[:10]: 
            s+= str(j[0]) + "," + str(j[3])+" "
            s2+=str(j[1]) + "," + str(j[2]) + " "
        file.write(s[:-1]+"\n")
        file2.write(s2[:-1]+"\n")
        p=n//100
        if not(c%p):print(c//p,"%")
        c+=1
def CrearCaminosGraf(cps,filename2):
    file2 = open(filename2,"w")
    n=len(cps)
    c=0
    
    for u in cps:
        s2=""
        s2+=str(u[0]) + "," + str(u[1]) + " "
        cercanos=[]
        for j in range(1,10000):
            v1=(c+j)%145225
            v2=(c-j)%145225
            xv1,yv1= cps[v1][0], cps[v1][1]
            d1=((xv1-u[0])**2+(yv1-u[1])**2)**0.5
            xv2,yv2= cps[v2][0], cps[v2][1]
            d2=((xv2-u[0])**2+(yv2-u[1])**2)**0.5
            cercanos.append([v1,xv1,yv1,d1])
            cercanos.append([v2,xv2,yv2,d2])
        cercanos.sort(key=itemgetter(3))
        for j in cercanos[:10]: 
            s2+=str(j[1]) + "," + str(j[2]) + " "
        file2.write(s2[:-1]+"\n")
        p=n//100
        if not(c%p):print(c//p,"%")
        c+=1
#CrearCaminos(cpsY,"LAP3.txt","Roads3.txt")
CrearCaminosGraf(cpsY,"Roads3.txt")
