'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

print('\033[7;30;41m-=-\033[m'* 40 )

print('\033[7;30;41m                               ANALISADOR DE TRIÂNGULOS\033[m')

print('\033[7;30;41m-=-\033[m'* 40)

a = int(input('\033[7;30;42m insira o primeiro valor:\033[m'))
b = int(input('\033[7;30;42m insira o segundo valor:\033[m'))
c = int(input('\033[7;30;42m insira o terceiro valor:\033[m'))

if a + b > c and b + c > a and a + c > b and a == b != c or c == b != a or a == c != b:
    print('\033[7;30;41m-=-\033[m'* 40 )
    print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO \033[7;30;42mISÓCELES\033[m')
    print('\033[7;30;41m-=-\033[m'* 40 )

elif a + b > c and b + c > a and a + c > b and a != b and b != c and a != c:
    print('\033[7;30;41m-=-\033[m'* 40 )
    print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGUL \033[7;30;42mESCALENO\033[m')
    print('\033[7;30;41m-=-\033[m'* 40 )

elif  a + b > c and b + c > a and a + c > b and a == b == c == a == c:
    print('\033[7;30;41m-=-\033[m'* 40 )
    print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO \033[7;30;42mEQUILÁTERO \033[m')
    print('\033[7;30;41m-=-\033[m'* 40 )

else:
    print('QUE PENA!!, ESTES VALORES \033[7;30;42m NÃO FORMAM UM TRIÂNGULO\033[m')


''' Outra forma de FAZER '''

a = int(input('\033[7;30;42m Insira o primeiro valor:\033[m '))
b = int(input('\033[7;30;42m Insira o segundo valor:\033[m '))
c = int(input('\033[7;30;42m Insira o terceiro valor:\033[m '))

# Verifica se os valores formam um triângulo
if a + b > c and b + c > a and a + c > b:
    print('\033[7;30;41m-=-\033[m' * 40)
    if a == b == c:
        print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO \033[7;30;42mEQUILÁTERO\033[m')
    elif a == b or b == c or a == c:
        print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO \033[7;30;42mISÓSCELES\033[m')
    else:
        print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO \033[7;30;42mESCALENO\033[m')
    print('\033[7;30;41m-=-\033[m' * 40)
else:
    print('QUE PENA!! ESTES VALORES \033[7;30;42mNÃO FORMAM UM TRIÂNGULO\033[m')