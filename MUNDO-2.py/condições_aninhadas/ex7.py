

'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
'''

peso = float(input("\033[1;35;40m  insira aqui o seu peso:\033[m"))
altura = float(input("\033[1;35;40m insira aqui a sua altura:\033[m"))
if altura > 100.00: 
    print('Sua altura é {} m'.format(altura))
elif altura < 100.00:
    print("\033[1;36;40m Sua altura é {} cm \033[m ".format(altura))

imc = peso / altura ** 2

print('\033[1;36;40m Seu peso é {}, logo o seu IMC é de {:.2f}\033[m '.format(peso,imc))

if imc < 18.5:
    print("\033[1;36;40m E você esta abaixo do peso\033[m ")
elif imc >= 18.5 < 25.0:
    print('\033[1;36;40m E você esta no peso ideal!!\033[m ')
elif imc >=25 < 30.0:
    print('\033[1;36;40m E você esta com sobrepeso\033[m ')
elif imc >= 30 < 40.0:
    print('\033[1;36;40m E você é obeso seu otário ahaha\033[m ')
elif imc > 40.0:
    print('\033[1;36;40m E você vai morrer afogado na banha\033[m ')