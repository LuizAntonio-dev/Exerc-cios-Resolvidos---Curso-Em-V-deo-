import datetime
hoje = datetime.date.today().year
cont = 0
maior = 0
menor = 0

for c in range(1,5 + 1):
    cont = cont + 1
    ano = int(input("digite o ano de nascimento da {}ª pessoa:".format(cont)))
    if (hoje - ano) >= 18:
        maior = maior +  1 
    elif (hoje - ano) < 18:
        menor += 1

print("=" * 40)
print('\033[31;35m ao todo tivemos {} maiores de idade \n e tivemos {} menores de idade\033[m'.format(maior,menor))
print("=" * 40)






