
frase = str(input("digite uma frase:")).strip().upper()

print(" A Letra {} aparece {} vezes".format(frase[0],frase.count(frase[0])))

print(' A primeira letra é a letra {} e ela esta na posição {}'.format(frase[0], 1))

print(' A ultima letra  {} esta na posição {}'.format(frase[0], frase.rfind(frase[0]) ))
