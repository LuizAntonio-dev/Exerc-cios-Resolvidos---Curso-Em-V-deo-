import time 
import emoji

s = int(input('diga quantos segundos um foguete demora para subir:'))
for c in range(0,s):
    print(c)
    time.sleep(1)
print(emoji.emojize(':rocket:'))