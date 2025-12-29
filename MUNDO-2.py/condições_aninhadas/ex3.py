
'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma 
mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais'''

print('\033[7;30;42m INSIRA DOIS NÚMEROS INTEIROS PARA COMPARA-LOS\033[m')

num1 = int(input('insira aqui o primeiro valor:'))
num2 = int(input('insira aqui o segundo valor:'))

if num1 > num2:
    print( 'o \033[7;30;42mprimeiro\033[m valor é maior')
elif num2 > num1:
    print( 'o \033[7;30;42msegundo\033[m valor é maior')
elif num2 == num1:
    print( 'os valores são \033[7;30;42miguais\033[m')
