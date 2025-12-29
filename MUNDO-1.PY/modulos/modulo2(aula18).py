import math

print('"'*100)
angulo = float(input("digite o valor "))


print('o cosseno de {} é igual a {}'.format(angulo,math.cos(angulo)))
print('-'*100)


print(' o seno de {} é igual a {}'.format(angulo,math.tan(angulo)))
print('-'*100)


print('o cosseno de {} é igual a {}'.format(angulo,math.sin(angulo)))

print('"'*100)

"""eu fiz o exercício de forma errada, era necessario passar o valor do  ângulo para RADIANO

--- O radiano é uma unidade de medida para ângulos. Ele é definido pela razão entre o comprimento 
do arco de um círculo e o raio do círculo.---

Jeito correto de fazer o exercício abaixo.


"""

angulo = float(input('digite um valor'))

seno  = math.sin(math.radians(angulo))
cos  = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('o valor das seguintees especificações dos angulos estão abaixo')
print('o valor de seno é {:.2f}'.format(seno))
print('o valor de seno é {:.2f}'.format(cos))
print('o valor de seno é {:.2f}'.format(tan))
