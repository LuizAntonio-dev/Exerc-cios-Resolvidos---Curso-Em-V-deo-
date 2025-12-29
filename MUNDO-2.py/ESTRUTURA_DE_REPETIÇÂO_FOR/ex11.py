'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, 
mostre qual foi o maior e o menor peso lidos.'''

respostas = []  # lista (plural)


for c in range(1, 6):  # 1 até 5
    resposta = float(input("Insira aqui o peso da {}ª pessoa: ".format(c)))
    respostas.append(resposta)  # adiciona na lista
    
    

print("Pesos registrados:", respostas)
print("maior peso:",max(respostas),"kg")
print("menor peso", min(respostas),"kg")

 