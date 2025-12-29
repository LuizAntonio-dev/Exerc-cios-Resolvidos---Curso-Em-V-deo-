print("meu primeiro codigo")

frase = str(input('digite seu nome completo:'))

frase0 = frase.lstrip()

frase2 = frase0.find(" ")

frase3 = frase0[:frase2]

print('analisando seu nome...')

print("seu nome completo é:{}".format(frase0))
print("seu nome comletras minúsculas é:{} ".format(frase0.lower()))
print("seu nome comletras minúsculas é:{} ".format(frase0.upper()))
print("seu nome ao todo tem {} letras".format(len(frase0)))
print('seu primeiro nome é {} e ele tem {} letras.'.format(frase3,len(frase3)))

'''no meu esboço faltou tirar os espaços na contagem de letras do nome '''

print("meu segundo codigo")

print("<->" * 100)

nome = str(input('insira seu primeiro nome:')).strip()

print('seu nome em minúsculo é:{}'.format(nome.lower()))
print('seu nome em maiúscula é:{}'.format(nome.upper()))
print('seu nome tem {} letras'.format(len(nome)- nome.count(" ")))
print('seu primeiro nome é {}, e ele tem {}'.format(nome[:nome.find(" ")],len(nome[:nome.find(" ")])))

'''outra forma de fazer de acorco com o video é:'''

separa = nome.split()

print(' seu primeiro nome é {}, e ele tem {} letras.'.format(separa[0],len(separa[0])))