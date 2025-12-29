
ano = int(input('digite o ano que vc quer descobrir se é bissexto ou não:'))

ano2 = ano % 4 

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano é bissexto')

else:
    print('o ano não é bissexto')

 
