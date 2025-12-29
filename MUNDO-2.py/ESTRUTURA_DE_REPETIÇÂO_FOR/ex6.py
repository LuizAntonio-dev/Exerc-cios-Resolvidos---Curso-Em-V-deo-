'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a 
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print("="*50)
print('     10 TERMOS DE UMA PA(prgressão aritmétrica)')
print("="*50)

a = int(input("primeiro termo:"))
b = int(input("razão:"))
c = a  + (10 - 1)* b

for c in range(a,c,b):
    print(c,end=" -> ")
print("ACABOU")