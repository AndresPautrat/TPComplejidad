{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.002065760027543467\n"
     ]
    }
   ],
   "source": [
    "from math import sqrt\n",
    "def LeerArchivo(filename,filename2):\n",
    "    file =open(filename)\n",
    "    file2 =open(filename2,\"w\")\n",
    "    l=145225\n",
    "    i=-1\n",
    "    for line in file:\n",
    "        s=str(line)\n",
    "        s=s[:len(s)-1]\n",
    "        if i!=-1:\n",
    "            ##print(line.split(';')[2],line.split(';')[0])\n",
    "            jcon=-1\n",
    "            conecciones=[[0,999],[0,999],[0,999],[0,999],[0,999]]\n",
    "            fileaux=open (filename)\n",
    "            for line2 in fileaux:\n",
    "                if jcon!=-1:\n",
    "                    if jcon!=int(line.split(';')[0]):\n",
    "                        p=Pitagoras(float(line.split(';')[2]),float(line.split(';')[3]),float(line2.split(';')[2]),float(line2.split(';')[3]))\n",
    "                        if jcon<5:\n",
    "                            conecciones[jcon]=jcon,p\n",
    "                        else:\n",
    "                            conecciones.sort(key=lambda tup: tup[1])\n",
    "                            for k in range(5):\n",
    "                                if conecciones[k][1]>p:\n",
    "                                    conecciones[4]=jcon,p\n",
    "                                    break\n",
    "                        \n",
    "                        if jcon==l:\n",
    "                           \n",
    "                            break \n",
    "                        \n",
    "                jcon+=1\n",
    "            fileaux.close()\n",
    "            conecciones.sort(key=lambda tup: tup[1])\n",
    "            for k in range(5):\n",
    "                ##print (str(conecciones[k][0])+\";\"+str(conecciones[k][1]))\n",
    "                s=s+\";\"+str(conecciones[k][0])+\";\"+str(conecciones[k][1])\n",
    "        else:\n",
    "            s=s+\"Con1;Dis1;Con2;Dis2;Con3;Dis3;Con4;Dis4;Con5;Dis5\"\n",
    "        file2.write(s)\n",
    "        file2.write(\"\\n\")\n",
    "        i+=1\n",
    "        if 145225%(i+2)==0:\n",
    "            print((i/145225)*100)\n",
    "        if i==l:\n",
    "            break\n",
    "    file.close()\n",
    "    file2.close()\n",
    "def Pitagoras(x,y,x1,y1):\n",
    "    return sqrt((x-x1)**2 + (y-y1)**2)\n",
    "def bubbleSort(alist):\n",
    "    for passnum in range(len(alist)-1,0,-1):\n",
    "        for i in range(passnum):\n",
    "            if alist[i][1]>alist[i+1][1]:\n",
    "                temp = alist[i]\n",
    "                alist[i]= alist[i+1]\n",
    "                alist[i+1] = temp\n",
    "\n",
    "LeerArchivo('BDO.txt','BD.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
