
'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o 
preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta 
viagens mais longas.'''

dis = float(input('coloque quantos quilômetros você quer  percorrer para descobrir o valor da sua viajem:'))


if dis <= 200.00:
    print('o valor da sua viajem é de: R$:{}'.format(dis * 0.50))
else:
    print('o valor da sua viajem é de: R${}'.format(dis * 0.45))


'''outra forma de fazer com OPERADOR TERNÁRIO OU IF SIPLIFICADO'''

print('-=-'* 30 )

dis = float(input('coloque quantos quilômetros você quer  percorrer para descobrir o valor da sua viajem:'))

preço = dis * 0.50 if dis <= 200.00 else dis * 0.45

print(preço)

