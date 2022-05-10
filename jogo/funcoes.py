import math
import random

def normaliza(cont):
    dic={}
    for c in cont:
        for pais in cont[c]:
            dic[pais]=cont[c][pais]
            dic[pais]["continente"]= c
    return dic

def sorteia_pais(dic):
    nl=[]
    for pais in dic:
        nl.append(pais)
    return random.choice(nl)

def adiciona_em_ordem(pais,dist,lista):
    nl=[pais, dist]
    i=0
    if nl not in lista:
        while i <len(lista):
            if nl not in lista:
                if lista[i][1] > dist:
                    lista.insert(i, nl)
            i+=1
        if len(lista)==0:
            lista.append(nl)
        if dist>lista[-1][1]:
            lista.append(nl)
    
    return lista

def esta_na_lista(pais,lista):
    for i in lista:
        if pais == i[0]:
            return True
    return False

def sorteia_letra(palavras,l):
    p=palavras.lower()
    lista=list(p)
    restritos=['.', ',', '-', ';', ' ']
    sorteio=random.choice(lista).lower()
    t=True
    for i in p:
        if i not in l and i not in restritos:
            t=False
    if t==True:
        return " "
    else:
        while sorteio in l or sorteio in restritos:
            sorteio=random.choice(lista)
    return sorteio

def haversine(raio, phi1, lambda1, phi2, lambda2):
    
    phi1_rad = math.radians(phi1)
    phi2_rad = math.radians(phi2)
    lambda1_rad = math.radians(lambda1)
    lambda2_rad = math.radians(lambda2)

    p1 = (math.sin((phi2_rad - phi1_rad)/2))**2
    p2 = math.cos(phi1_rad)
    p3 = math.cos(phi2_rad)
    p4 = (math.sin((lambda2_rad - lambda1_rad)/2))**2
    pt = p1 + (p2 * p3 * p4)

    d = 2 * raio * math.asin((pt)**(1/2))

    return d