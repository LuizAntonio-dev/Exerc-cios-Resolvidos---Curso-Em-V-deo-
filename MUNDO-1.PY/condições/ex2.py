
'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
   Km acima do limite.'''
from time import sleep

print("-=-" * 30)
velocidade = float(input('digite a velocidade que vc antigiu com o seu carro:'))
print("-=-" * 30)


velocidade2 = velocidade - 80.0



if velocidade >= 81.0:
    print('PROCESSANDO!!')
    sleep(2)

    print("." * 100)
    
    print( '''VOCÊ ESTA ACIMA DA VELOCIDADE!!''')

    print("." * 100)

    print('''O limite é de 80KM/h e vc estava {} KM/h e o valor da multa é de R$: 7,00 por cada KM/h acima do limite
          o valor da sua multa é de R$:{} '''.format(velocidade,velocidade2 * 7 ))
    
    print("." * 100)


else:
    
    print('PROCESSANDO!!')
    sleep(2)

    print("." * 100)
    print('Parabéns você esta no limite de 80KM/h')
    print("." * 100)
    
    