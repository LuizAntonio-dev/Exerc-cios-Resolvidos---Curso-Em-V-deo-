soma = 0
a = int(input("digite aqui um número:"))

if a % 2 == 0:
    print("\033[1;35;40m parbens o valor está aprovado!!\033[m")
    for c in range(a,a + 6):
        soma = soma + c
        print(c)
    print("\033[1;31;40m {} \033[m".format(soma))
else: 
    print("\033[1;31;40m seu número foi desconsiderado\033[m")



soma = 0
cont = 0 

for c in range(1,7):
    a = int(input("insira um número:"))
    if a % 2 == 0:
        soma = soma + a 
        cont = cont + 1
    else:
        print("começe novamente: seu número foi desconsiderado!!")

print("você informou {} números e a soma deles é {}".format(cont,soma))