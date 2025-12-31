"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
opção = 0

a = int(input("insira o primeiro valor"))

b = int(input("insira o segundo valor"))

print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa 
      ''')
opção = int(input("A opção que você escolheu foi:"))


if opção == 1:
    print(a * b)
elif opção == 2:
    print(a + b)
elif opção == 3:
    if a > b:
        print(a)
    elif a == b:
           print("os valores são iguais")
    else:
        print(b)
elif opção == 4:
    while opção == 4:
        a = int(input("insira o primeiro valor"))

        b = int(input("insira o segundo valor"))

        print('''   [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa 
            ''')
        opção = int(input("A opção que você escolheu foi:"))
elif opção == 5:
    print("finalizado")
else:
    print("opção inválida, tente novamente")
    a = int(input("insira o primeiro valor"))

    b = int(input("insira o segundo valor"))

    print('''  [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa 
        ''')
    opção = int(input("A opção que você escolheu foi:")) 