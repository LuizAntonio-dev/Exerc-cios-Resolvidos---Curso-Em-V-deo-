
import random

nome1 = str(input("digite o nome da primeira pessoa:"))
nome2 = str(input("digite o nome da segunda pessoa:"))
nome3 = str(input("digite o nome da terceira pessoa:"))

lista = [nome1,nome2,nome3]

random.shuffle(lista)

print("a ordem sorteada será:{}".format(lista))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#outra forma de fazer 


from random import shuffle

nome1 = str(input("digite o nome da primeira pessoa:"))
nome2 = str(input("digite o nome da segunda pessoa:"))
nome3 = str(input("digite o nome da terceira pessoa:"))

lista = [nome1,nome2,nome3]

shuffle(lista)

print("a ordem sorteada será:{}".format(lista))