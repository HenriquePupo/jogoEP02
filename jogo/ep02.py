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
            distancia=haversine(EARTH_RADIUS, dadosnormalizados[sorteado]["geo"]["latitude"], dadosnormalizados[sorteado]["geo"]["longitude"], dadosnormalizados[resposta]["geo"]["latitude"], dadosnormalizados[resposta]["geo"]["longitude"] )
            print(f'O país está a {distancia } kilometros de distancia')

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