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



def inventario(cores_usadas,distancias, tentativas,letrasusadas):
    dicas_usadas={
        "cores": cores_usadas,
        "letra": letrasusadas,
    }
    
    print("distâncias: ")
    print(" ")
    print("dicas: - cores da bandeira: {}".format((', ').join(dicas_usadas["cores"])))
    print("       - letras da capital: {}".format((", ").join(dicas_usadas["letra"])))

    print(" ")
    print("tentativas: - {}".format(tentativas))
    print(" ")
    return 


# funcao da dica             
def funcao_dica(tentativas,dadosnormalizados,sorteado,lista_cores,letrascapital):
    tentativasgastas=0
    cor = "1. Cor da bandeira  - custa 4 tentativas"
    letra = "2. Letra da capital - custa 3 tentativas"
    area = "3. Área             - custa 6 tentativas" 
    pop = "4. População        - custa 5 tentativas"
    cont = "5. Continente       - custa 7 tentativas"
    if lista_cores==[]:
        cor = ""
    if letrascapital==[]:
        letra = ""


    print("Mercado de Dicas:")
    print("----------------------------------------")
    print(cor)
    print(letra)
    print(area)
    print(pop)
    print(cont)
    print("0. Sem dica")
    print("----------------------------------------")

    return " "


def faz_lista_cores(dadosnormalizados,sorteado):
    lista_cores=[]
    cordabandeira = dadosnormalizados[sorteado]["bandeira"]
    for cor, num in cordabandeira.items():
        if num > 0 and cor != "outras":
            lista_cores.append(cor)
    return lista_cores

def dica_1(lista_cores,coresusadas):
    corsorteada = random.choice(lista_cores)
    lista_cores.remove(corsorteada)
    coresusadas.append(corsorteada)
    
    return [corsorteada,lista_cores,coresusadas]

def faz_lista_letras(dadosnormalizados,sorteado):
    letrascapital = []
    capital = dadosnormalizados[sorteado]["capital"]
    for i in capital:
        letrascapital.append(i.lower())
    return letrascapital

def dica_2(letrascapital, letrasusadas):
    letrasorteada = random.choice(letrascapital)
    letrascapital.remove(letrasorteada)
    letrasusadas.append(letrasorteada)
    return [letrasorteada, letrascapital, letrasusadas]

