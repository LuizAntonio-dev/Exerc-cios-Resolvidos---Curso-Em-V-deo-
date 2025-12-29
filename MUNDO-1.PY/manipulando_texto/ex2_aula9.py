
'''faça um programa que leia um numero de 0 a 99990 e mostre na tela cada um dos digitos separados
ex: numero = 1879
unidade = 9/ dezena = 7/ centena = 8/ milhar = 1'''

frase = int(input("insira um número que tenha no maximo 4 digitos "))

frase2 = str(frase).strip()

if len(frase2) < 4:
    print(' vc inseriu errado:, digite novamente seu otário')

elif len(frase2) > 4:
    print('vc inseriu o número errado, tente novamente')
    
else:
    print('''           vc inseriu corretamente!!! 
          a unidade do seu numero é: {}
          a dezena do seu número é: {}
          a centena do seu número é: {}
          o milhar so seu número é:{}'''.format(frase2[3],frase2[2],frase2[1],frase2[0]))

    