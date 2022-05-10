import json
import math
import random
import funcoes

with open('dados.json','r') as arq:
    dados = arq.read()
dados = json.loads(dados)

dadosnormalizados = funcoes.normaliza(dados)

jogando = True
while jogando:

    tentativas = 20
    sorteado = funcoes.sorteia_pais(dadosnormalizados)
    print(sorteado)

    while tentativas > 0:

        resposta = input('Qual seu palpite? ')

        if resposta == sorteado:
            print('voce acertou')
            jogando = False

        elif resposta not in dadosnormalizados.keys():
            print('pais desconhecido')