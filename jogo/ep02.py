import json
import math
import random
from termcolor import colored
from funcoes import sorteia_pais
from funcoes import normaliza
from funcoes import haversine
from funcoes import adiciona_em_ordem
from funcoes import esta_na_lista
from funcoes import sorteia_letra
from dados import EARTH_RADIUS
import dados

dados = dados.dados()
dadosnormalizados = normaliza(dados)

jogando = True
while jogando:

    tentativas = 20
    sorteado = sorteia_pais(dadosnormalizados)
    print(sorteado)
    dicas=' '
    dicacoresdabandeira = " "
    lista_distancias = []
    while tentativas > 0:
        
        print(" ")
        print("dicas: " + "{} ".format(dicacoresdabandeira))
        print(" ")
        print("suas tentativas {}".format(tentativas))
        print(" ")
        resposta = input('Qual seu palpite? ')

        if resposta == sorteado:
            print('voce acertou')
            jogando = False
        
        elif resposta in dadosnormalizados.keys():
            distancia = haversine(EARTH_RADIUS, dadosnormalizados[sorteado]["geo"]["latitude"], dadosnormalizados[sorteado]["geo"]["longitude"], dadosnormalizados[resposta]["geo"]["latitude"], dadosnormalizados[resposta]["geo"]["longitude"] )
            if distancia <= 1000:
                print('\033[1;36m{0:.0f} -> {1}\033[m'.format(distancia, resposta))  
            elif 1001 <= distancia <= 1999:
                print('\033[1;33m{0:.0f} -> {1}\033[m'.format(distancia, resposta))
            elif 2000 <= distancia <= 4999:
                print('\033[1;31m{0:.0f} -> {1}\033[m'.format(distancia, resposta))
            elif 5000 <= distancia <= 9999:
                print('\033[1;35m{0:.0f} -> {1}\033[m'.format(distancia, resposta))
            elif distancia <= 10000:
                print('\033[1;37m{0:.0f} -> {1}\033[m'.format(distancia, resposta))            
            
            # resp_cor = print('\033[1;37m{0:.0f} -> {1}\033[m'.format(distancia, resposta))            
            # lista_distancias =[]
            # if distancia not in lista_distancias:
            #     lista_cores = lista_distancias.append(resp_cor)
            #     print(lista_cores)


        elif resposta not in dadosnormalizados.keys() and resposta != "dica":
            print('pais desconhecido')

        # elif resposta == "dica":
        #     print(sorteado)
        #     funcao_dicas=funcao_dica(tentativas,dadosnormalizados,sorteado)
        #     tentativas -= funcao_dicas[0]
        #     dicacoresdabandeira = dicacoresdabandeira + ", " + "{}".format(funcao_dicas[1])
        #     listacores = funcao_dicas[2]
        #     capital = funcao_dicas[3]
        #     area = funcao_dicas[3]

        else:
            tentativas-=1