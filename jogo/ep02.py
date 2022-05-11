import json
import math
import random
import funcoes

with open('jogo/dados.json','r') as arq:
    dados = arq.read()
dados = json.loads(dados)

dadosnormalizados = funcoes.normaliza(dados)

jogando = True
while jogando:

    tentativas = 20
    sorteado = funcoes.sorteia_pais(dadosnormalizados)
    print(sorteado)
    dicas=' '
    dicacoresdabandeira = " "

    while tentativas > 0:
        
        print(" ")
        print("dicas: " + "{} ".format(dicacoresdabandeira))
        print('dicas: '+'{}'.format())
        print(" ")
        print("suas tentativas {}".format(tentativas))
        print(" ")
        resposta = input('Qual seu palpite? ')

        if resposta == sorteado:
            print('voce acertou')
            jogando = False
            
        elif resposta not in dadosnormalizados.keys() and resposta != "dica":
            print('pais desconhecido')

        elif resposta == "dica":
            print(sorteado)
            funcao_dicas=funcoes.funcao_dica(tentativas,dadosnormalizados,sorteado)
            tentativas -= funcao_dicas[0]
            dicacoresdabandeira = dicacoresdabandeira + ", " + "{}".format(funcao_dicas[1]) 
            listacores = funcao_dicas[2]
            capital = funcao_dicas[3]
            area = funcao_dicas[3]


        else:
            tentativas-=1