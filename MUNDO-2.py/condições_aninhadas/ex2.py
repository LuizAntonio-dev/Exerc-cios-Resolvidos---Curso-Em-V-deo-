
num = int(input('insira um numero inteiro qualquer:'))

print('''escolha uma das bases para conversão
      [1] Binário
      [2] Octal
      [3] Exadecimal''')
opção = int(input('sua opção:'))

if opção == 1:
    bin1 = bin(num)[2:]
    print('o número {} foi convertido para {}'.format(num, bin1))
    
elif opção == 2:
    octal = oct(num)[2:]
    print('o número {} foi convertido para {}'.format(num, octal))

elif opção == 3:
    hexa = hex(num)[2:]
    print('o número {} foi convertido para {}'.format(num, hexa ))
