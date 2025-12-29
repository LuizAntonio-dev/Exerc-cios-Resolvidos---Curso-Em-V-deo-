

print('\033[1;30;41m-=-\033[m'* 30 )

print('\033[7;31;44m ANALISADOR DE TRIÂNGULOS\033[m')

print('\033[1;30;41m-=-\033[m'* 30 )

a = int(input('insira o primeiro valor:'))
b = int(input('insira o segundo valor:'))
c = int(input('insira o terceiro valor:'))

if a + b > c and b + c > a and a + c > b:
    print('PARABÉNS, ESTES VALORES FORMAM UM TRIÂNGULO')
else:
    print('QUE PENA!!, ESTES VALORES NÃO FORMAM UM TRIÂNGULO')