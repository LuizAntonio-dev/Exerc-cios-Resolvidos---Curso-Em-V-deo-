import math

num1 = float(input('informe um numero aqui o comprimento do cateto oposto!'))
num2 = float(input('informe um numero aqui o comprimento do cateto adjacente!'))

print('valor da hipotenusa é:{:.2f}'.format(math.hypot(num1,num2)))


# outra forma de FAZER!!

co = float(input('informe um numero aqui o comprimento do cateto oposto!'))
ca = float(input('informe um numero aqui o comprimento do cateto adjacente!'))

hi = (co**2 + ca**2 ) **(1/2)

print('valor da hipotenusa é:{:.2f}'.format(hi))