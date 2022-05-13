
import math
import random
import funcoes
import dados
from dados import EARTH_RADIUS

dados = dados.dados()
dadosnormalizados = funcoes.normaliza(dados)


jogando = True
while jogando:

    tentativas = 20
    distancias=" "
    sorteado = funcoes.sorteia_pais(dadosnormalizados)
    print(sorteado)
    lista_cores = funcoes.faz_lista_cores(dadosnormalizados,sorteado)
    dicas_usadas = []
    vezes_usada = 0
    cores_usadas = []
    letrascapital = funcoes.faz_lista_letras(dadosnormalizados,sorteado)
    letrasusadas = []
    lista_paises = []
    areausada = 0
    dica3 = ""
    popusada = 0
    dica4 = ""
    contusada = 0
    dica5=""
    print("-----------------------------")
    print("| Bem Vindo ao acerta pais   |")
    print("-----------------------------")
    print("Comandos:")
    print(" dica     - entra no mercado de dicas")
    print(" desisto  - desiste do jogo")
    print("----------------------------------------")
    print("")
    

    while tentativas > 0:
        
        (funcoes.inventario(cores_usadas,distancias,tentativas,letrasusadas,dica3,dica4,dica5))
        
        resposta = input('Qual seu palpite?: ')

        if resposta == sorteado:
            print('voce acertou')
            jogando = False

        elif resposta in dadosnormalizados.keys():
            distancia = funcoes.haversine(EARTH_RADIUS, dadosnormalizados[sorteado]["geo"]["latitude"], dadosnormalizados[sorteado]["geo"]["longitude"], dadosnormalizados[resposta]["geo"]["latitude"], dadosnormalizados[resposta]["geo"]["longitude"] )
            if 0 < distancia <= 999:
                print('\033[1;36m{0} km -> {1}\033[m'.format(int(distancia), resposta))  
            elif 1999 <= distancia <= 1000:
                print('\033[1;33m{0} km -> {1}\033[m'.format(int(distancia), resposta))
            elif 4999 <= distancia <= 2000:
                print('\033[1;31m{0} km -> {1}\033[m'.format(int(distancia), resposta))
            elif 9999 <= distancia <= 5000:
                print('\033[1;35m{0} km -> {1}\033[m'.format(int(distancia), resposta))
            else:
                print('\033[1;37m{0} km -> {1}\033[m'.format(int(distancia), resposta))
            

            tentativas -= 1


        elif resposta not in dadosnormalizados.keys() and resposta != "dica":
            print('pais desconhecido')

        elif resposta == "dica":     
            print("")
            funcao_dicas = funcoes.funcao_dica( tentativas, dados, sorteado, lista_cores, letrascapital, areausada, popusada, contusada)
            print("")
            resposta = input("escolha: ")
            if resposta == "1" and lista_cores != [] and tentativas > 4:
                dica1 = funcoes.dica_1( lista_cores, cores_usadas)
                lista_cores = dica1[1]
                tentativas -= 4

            if resposta == "2" and letrascapital != [] and tentativas > 3:
                dica2 = funcoes.dica_2( dadosnormalizados, sorteado, letrasusadas)
                letrascapital.remove(dica2)
                letrasusadas.append(dica2)
                tentativas -= 3
            
            if resposta == "3" and areausada == 0 and tentativas > 6:
                dica3 = funcoes.dica_3( dadosnormalizados, sorteado)
                areausada+=1
                tentativas -= 6

            if resposta == "4" and popusada == 0 and tentativas > 5:
                dica4 = funcoes.dica_4( dadosnormalizados, sorteado)
                popusada += 1
                tentativas -= 5
            
            if resposta == "5" and contusada==0 and tentativas > 7:
                dica5 = funcoes.dica_5( dadosnormalizados, sorteado)
                contusada += 1
                tentativas -= 7

    print("")
    print("voce perdeu o pais era: {}".format(sorteado))
    print("")