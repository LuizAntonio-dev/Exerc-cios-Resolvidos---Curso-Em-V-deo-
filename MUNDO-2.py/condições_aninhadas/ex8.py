
'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''
import time
print('\033[1;35;40m ============== LOJAS TUNHOSE ==============\033[m')

valor = float(input('insira aqui o valor da compra:'))

print('''
FORMAS DE PAGAMENTOS
[ 1 ] Á vista dinheiro / cheque 
[ 2 ] Á vista no cartão
[ 3 ] Á 2x no cartão
[ 4 ] 3x ou mais no cartão''')

num = int(input('selecione a opção de pagamento:'))

if num == 1:

    a = int(valor * 0.10)
    b = valor - a
    print('o valor a pagar será de R$: \033[1;31;40m{}\033[m'.format( b ))

elif num == 2:
    c = int(valor * 0.050)
    d = valor - c
    print('o valor a pagar será de R$:  \033[1;31;40m{}\033[m'.format( d ))
elif num == 3:
    print('o valor total a pagar será de R$:  \033[1;31;40m{}\033[m  e a sua parcela será de 2x de R$:  \033[1;31;40m{}\033[m'.format( valor, valor / 2  ))
elif num == 4:
    h = (int(input('quantas vezes no cartão você quer parcelar?')))
    e = int(valor * 0.050)
    f = valor + e
    print('o valor a pagar será de R$: \033[1;31;40m {} \033[m  e a sua parcela será de  \033[1;31;40m{}x \033[m de R$:  \033[1;31;40m{}\033[m'.format( f, h ,f / h ))
