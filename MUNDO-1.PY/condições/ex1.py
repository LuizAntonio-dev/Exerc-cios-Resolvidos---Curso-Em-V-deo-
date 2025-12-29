
import random
import time

num = random.randint(0,5)

print('-=-'*20)

num2 = str(input('tente acertar o número o computador escolheu:')).strip()

print('-=-'*20)

print('processando...')
time.sleep(2)
      

if num2 == num:
    print('PARABÉNS vc acertou o número!!')
elif num2 >= "6":
    print('Tente novamente')
else:
    print(' vc escreveu o número {} e vc digitou o número {}, tente novamente'.format(num2, num))


