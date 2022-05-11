import math
import random
import json

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

def continuar ():
    resposta = input('Quer continuar?[s/n]')
    if resposta == 'n':
        print('Ate a proxima!')
    if resposta == 's':
        print('Um pais foi escolhido')
    else:
        print('escolha outra resposta')

# funcao da dica             
def funcao_dica(tentativas,dados,paissorteado):
    tentativasgastas=0
    listacores=[]
    print("Mercado de Dicas:")
    print("----------------------------------------")
    cor = "1. Cor da bandeira  - custa 4 tentativas"
    print(cor)
    letra = "2. Letra da capital - custa 3 tentativas"
    print(letra)
    area = "3. Área             - custa 6 tentativas"
    print(area)
    pop = "4. População        - custa 5 tentativas"
    print(pop)
    cont = "5. Continente       - custa 7 tentativas"
    print(cont)
    print("0. Sem dica")
    print("----------------------------------------")
    resposta = input(" escolha: |1|2|3|4|5|0| ")

    cordabandeira=dados[paissorteado]["bandeira"]
    for cor, num in cordabandeira.items():
        if num > 0 and cor != "outras":
            listacores.append(cor)
    if resposta == '1':
        tentativasgastas +=4
        for cor, num in cordabandeira.items():
            if num > 0 and cor != "outras":
                listacores.append(cor)
        corsorteada=random.choice(listacores)
        listacores.remove(corsorteada)
        dica=corsorteada 

    elif resposta == '2':
        tentativasgastas += 3
        letra_capital = funcao_capital(paissorteado, dados)
        dica = letra_capital

    elif resposta == '3':
        tentativas += 6
        area = dados[paissorteado]['area']
        dica = area
        return [tentativasgastas,dica,listacores, area]

    return [tentativasgastas,dica,listacores, letra_capital]

def funcao_capital(paissorteado, dados):
    capital = dados[paissorteado]['capital']
    dica_2 = sorteia_letra(capital, []) 
    return dica_2

def lista_de_cores(dados,paissorteado):
    listacores=[]
    cordabandeira=dados[paissorteado]["bandeira"]
    for cor, num in cordabandeira.items():
        if num > 0 and cor != "outras":
            listacores.append(cor)
    return listacores
