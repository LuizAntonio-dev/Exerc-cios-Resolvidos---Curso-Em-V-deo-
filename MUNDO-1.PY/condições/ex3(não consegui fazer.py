'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''


num = int(input('digite um número para descobrir se esse número é PAR ou IMPAR:'))

num2 = num % 2 


if num2 == 0:
    print('este numero é par')
else:
    print('este número é impar')