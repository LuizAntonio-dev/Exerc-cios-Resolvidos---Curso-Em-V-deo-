"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

print("~~~~~ OPERAÇÕES ~~~~~ ")

a = int(input("insira o primeiro valor:"))
        
b = int(input("insira o segundo valor:"))

c = int(input("Qual operação você quer realizar? \n [1] multiplicar\n [2] somar \n [3] maior \n [4] novos número\n [5]sair do programa?\n >>>>>> Qual opção você escolheu ?"))

# [1] multiplicar [2] somar  [3] maior [4] novos número [5]sair do programa

# while b > 0 or a > 0:
#     if c == 1:
#         print("a multiplicação entre os valores adicionados é igual a {}".format(a * b) )
#     elif c == 2:
#         print("a soma entre os dados adicionados é igual a {}".format(a + b ))
#     elif c ==3:
#         if a > b:
#            print("{} é o maior número ".format(a))
#         else:
#            print("{} é o maior número ".format(b))
    