
''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
 tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import  datetime

ano  = int(input('''\033[1;32;40mDigite aqui o seu ano de nasciemnto e descubra se esta em dia com os 
deveres da pátria:\033[m'''))

ano1 = str(datetime.datetime.now())[:4]
a = (int(ano1) - ano) 

sobra1 = int(a) - 18
sobra2 = 18 - int(a)

if a > 18 and sobra1 > 1:
    print('''           QUE ISSO RECRUTA!!, VAI SER PRESO IMEDIATAMENTE
VOCÊ ESTÁ \033[1;32;40m{}\033[m ANOS ATRASADO... VOCÊ DEVERIA TER SE ALISTADO NO ANO \033[1;32;40m{}\033[m'''.format(sobra1 , ano + 18))

elif  a > 18 and sobra1 == 1:
    print('''           QUE ISSO RECRUTA!!, VAI SER PRESO IMEDIATAMENTE
VOCÊ ESTÁ \033[1;32;40m{}\033[m ANO ATRASADO... VOCÊ DEVERIA TER SE ALISTADO NO ANO \033[1;32;40m{}\033[m'''.format(sobra1, ano + 18))
    
elif a < 18 and sobra2 > 1:
    print('''           SE PREPARE RECRUTA A SUA HORA ESTÁ CHEGANDO!!
AINDA FALTA \033[1;32;40m{}\033[m ANOS PARA VC SE ALISTAR NO EXÉRCITO O SEU ANO DE ALISTAMENTO VAI SER EM \033[1;32;40m{}\033[m '''.format(sobra2 , ano + 18))
    
elif a < 18 and sobra2 == 1:
    print('''           SE PREPARE RECRUTA A SUA HORA ESTÁ CHEGANDO!!
AINDA FALTA \033[1;32;40m{}\033[m ANO PARA VC SE ALISTAR NO EXÉRCITO O SEU ANO DE ALISTAMENTO VAI SER EM \033[1;32;40m{}\033[m '''.format(sobra2 , ano + 18)) 

else:
    print('MUITO BOM RECRUTA VOCÊ ESTÁ COM 18 ANOS, ESTÁ NA HORA DE VIRAR HOMEM!!! , PEGUE O SEU FUZIL E ME ACOMPANHE POR FAVOR')