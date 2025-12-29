#Calcular quanto é o preço de um produto com 5% de desconto

preco = float(input('digite o valor do produto:'))
desc = (preco*5/100)

print('o valor do produto que vc escolheu tem o preço de R$:{:.2f}, mas com o desconto de 5%  aplicado o valor agor a é de R$:{:.2f} '.format(preco,preco-desc))