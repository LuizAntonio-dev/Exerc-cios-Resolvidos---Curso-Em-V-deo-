
''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o 
aumento é de 15%. '''

sl = float(input('informe aqui o seu salário para receber um aumento:'))

if sl <= 1250.00:
    sl2 = sl + (sl * 0.15)
    print("seu salário agora é:  R$:{}".format(sl2))
elif sl > 1250.00:
    sl3 = sl + (sl * 0.10 )
    print("seu salário agora é:  R$:{}".format(sl3))