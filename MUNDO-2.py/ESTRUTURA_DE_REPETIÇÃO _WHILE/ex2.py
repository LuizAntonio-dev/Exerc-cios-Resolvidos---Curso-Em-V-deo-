
"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador 
vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer."""

import random
c = 0

print("computador: acabei de pensar em um número... tente acertar!!")


b = random.randint(1,10)
a = int(input("digite um número, e veja se você acertou:"))

if a < 0 or a > 10:
    print( "números acima de 10 ou abaixo de 0 não são permitidos")
    a = int(input("tente novamente"))
else:
    while a != b:
        if a < b:
            print("mais... tente novamente:")
            a = int(input("insira aqui o número:"))
            c = c + 1
        else:
            print("menos... tente novamente:")
            a = int(input("insira aqui o número:"))
            c = c + 1

print(""" vc acertou!!, o número gerado pelo pc foi {}, 
e você acertou depois de {} vezes """.format(b,c))

