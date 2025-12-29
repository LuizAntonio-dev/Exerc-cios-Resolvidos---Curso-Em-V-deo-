
import time
import random

print('{} PEDRA, PAPEL e TESOURA{}'.format(20*"=",20*"="))
print(''' ESCOLHA UMA OPÇÃO PARA JOGAR!!!
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

a = int(input('QUAL OPÇÃO VOCÊ ESCOLHEU?:'))

print('JÓ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!')
time.sleep(1)

b = ['2','3','1']
e = random.choice(b)

print(e)

if str(a) == e:
    print("Empate")
elif str(a) == '1' and e == '2':
    print("você perdeu, comp escolheu papel ")
elif str(a) == '1' and  e == '3':
    print("você gnahou, comp escolheu tesoura ")
elif str(a) == '2' and  e == '1':
    print("você gnahou, comp escolheu pedra ")
elif str(a) == '2' and  e == '3':
    print("você perdeu, comp escolheu tesoura ")
elif str(a) == '3' and e == '2':
    print("você ganhou, comp escolheu papel ")
elif str(a) == '3' and  e == '1':
    print("você perdeu , comp escolheu pedra ")
else:
    print('escolha uma das opções acima')





