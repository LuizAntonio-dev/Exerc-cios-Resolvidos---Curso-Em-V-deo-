#faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada.
n = float(input('digite um número:'))

a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10

print('a tabuada referente ao número que você digitou é:')
print("-"*15)
print(" TABUADA ")
print("-"*15)
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n,a,n,b,n,c,n,d,n,e,n,f,n,g,n,h,n,i,n,j))
print("-"*15)

#---------------------------------------------------------------------------------------------------------------------------------
#jeito diferente de fazer  a tabuada:
print('°'* 30)
print('outra forma de fazer a tabuada de {} é:'.format(n))
print('°'* 30)
print('a tabuada de {} é:'.format(n))
print('{} x {:1} = {:2}'.format(n,1,n*1))
print('{} x {:1} = {:2}'.format(n,2,n*2))
print('{} x {:1} = {:2}'.format(n,3,n*3))
print('{} x {:1} = {:2}'.format(n,4,n*4))
print('{} x {:1} = {:2}'.format(n,5,n*5))
print('{} x {:1} = {:2}'.format(n,6,n*6))
print('{} x {:1} = {:2}'.format(n,7,n*7))
print('{} x {:1} = {:2}'.format(n,8,n*8))
print('{} x {:1} = {:2}'.format(n,9,n*9))
print('{} x {} = {:2}'.format(n,10,n*10))
print('°'* 30)

