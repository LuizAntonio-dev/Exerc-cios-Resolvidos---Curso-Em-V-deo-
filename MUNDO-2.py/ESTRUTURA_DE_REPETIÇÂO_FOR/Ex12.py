''' Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do 
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
#grupo
idade2 = 0

# homem mais velho
velho1 = []
idade3 = 0

#mulher mais nova
mulher = 0
nome_mulher = []

for c in range(1,4 + 1):
    print("--- {} ª pessoa: ---".format(c))
    nome = str(input("nome:")).upper()
    idade  = int(input("idade:")) 
    sexo = str(input("sexo(M/F):"))
    idade2 = idade2 + idade 

    if sexo == "M":
        if idade > idade3:
            idade3 = idade
            velho1 = nome
        else:
            idade3 = idade3 

    if sexo == "F":
        if idade < 20:
            mulher += 1
            nome_mulher.append(nome)
        


print("a média da idade das pessoas é : {:0f} anos ".format(idade2 / 4))
 
print("o homem mais velho é o {} e ele tem {} anos ".format(velho1,idade3))

print("no grupo há {} mulheres com idade menor que 20 anos, sendo elas {}".format(mulher,nome_mulher))

