''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

import datetime
print('\033[1;32;40mCONFERDERAÇÃO NACIONAL DE NATAÇÃO\033[m')

born = int(input('insira aqui a sua data de nascimento:'))
atual = str(datetime.datetime.now())[:4]

idade = int(atual) - born
print(idade)

if idade <= 9:
    print('''O atleta tem \033[1;32;40m{}\033[m anos 
Classificação: MIRIM '''.format(idade))
elif idade > 9 and idade <= 14:
    print('''O atleta tem \033[1;32;40m{}\033[m anos 
Classificação:\033[1;32;40m INFANTIL\033[m '''.format(idade))
elif idade > 14 and idade <= 19:
    print('''O atleta tem \033[1;32;40m{}\033[m anos 
Classificação: \033[1;32;40m JÚNIOR\033[m '''.format(idade))
elif idade > 19 and idade <= 25:
    print('''O atleta tem \033[1;32;40m{}\033[m anos 
Classificação:\033[1;32;40m SÊNIOR\033[m'''.format(idade))
elif idade > 25:
    print('''O atleta tem \033[1;32;40m{}\033[m anos 
Classificação:\033[1;32;40m MASTER\033[m'''.format(idade))

