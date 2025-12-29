
frase = str("curso em video")
frase2 = str("CURSO EM viDEO")
frase3 = str("   frase com espaço inicio e fim    ")


print(frase[9])

print("-" * 100  )

frase = str("curso em video")


print(frase[9:14])

print("-" * 100  )
# a parte 9:14 é o intervalo da frase  que vai aparecer na tela, a letra v é 9 e a letra o é a 13, mas para ela aparecer é preciso colocar um número seguinte 



print('-' * 100)

print(frase[9:14:2])   
#este :2 depois do 14 é o numero de intervalo que vai pular na frase ou seja ao invés de aparecer a frase toda ele vai aparecer a frase comçando com a  primeira letra"V" vai pular uma
# e vai para a letra "D" e por fim a letra "o"


print('-' * 100)
  
print(frase[9:])
print(frase[:5])   
# quando não é colocado nenhum numero antes dos dois pontos ele começa a contar da letra 0 e vai até a letra 4, e não aparece o 5, isso vale tambem ao contrario 

print('-' * 100)
  
print(frase[9::2])
#este duplo dois pontos pode ser utilizado da seguinte forma, o 9: é aonde vai começar a pegar a frase, e :2 é o intervalo que vai pular entre caractere

# c u r s o   e m   v i  d   e   o
# 0 1 2 3 4 5 6 7 8 9 10 11  12  13

print(len(frase))
''' a função LEN é para contar quantas letras tem na frase (contando com os espaços), é IMPORTANTE prestar atenção que ele conta a quantidade de letras a partir do numero 1, e a LISTA conta 
 as letras a partir do 0 ou seja  na LISTA teria 13 numeros, e com a Função LEN tem 14 '''


print(frase.count("e"))
print(frase.count("e",0,12))

'''esta função mostra a quantidade de letras "e" que contem na frase, o ,0,13  é o intervalo que vai contar a ltera desejada, LEMBRANDO QUE O ULTIMO NUMERO NÃO VAI APARECER A LETRA CORRESPONDENTE
OU SEJA MESMO QUE VC TENHA COLOCADO O NUMERO 12 ELE VAI APARECER ATÉ O NUMERO 11 POIS A LISTA COMEÇA A CONTAR DO 0'''

print(frase.find("android"))
print(frase.find("video"))
'''a função find é para identificar qual o primeiro numero da frase desejada, ou seja, a frase android não existe então o valor retornado é -1, isso significa que a frase não existe 
 outro exemplo é encontrar o video ele vai indicar qual o primeiro numero da primeira letra, ou seja 9, lembrando que ele usa o numero da lista como valor retornado '''

print("curso" in frase)
print("cur" in frase )
print("dife" in frase )

'''a função IN vai mostrar se existe a palavra curso na variavel frase, mas diferente da função FIND ele não vai mostrar o numero que começa ele apenas vai dizer se tem ou não
isso vale tambem para pedaços de frase  
 caso tenha na variael = true
 caso não tenha =  false '''

print(frase.replace("curso", "phyton"))

'''a função replace vai substituir oque aparece na tela, ela não substitui a string '''

print(frase.upper())

'''deixa as letras maiúculas '''

print(frase2.lower())

'''deixa as letras minusculas  '''

print(frase2.capitalize())

'''deixa a primeira letra em maiusculo'''

print(frase2.title())
'''deixa cada palavra com a primeira letra em maiúscula '''

print(frase3.strip())
'''tira os espaços existentes no inicio e no final da frase'''

print(frase3.lstrip())
'''tira os espaços apenas do lado direito da frase'''

print(frase3.rstrip())
'''tira os espaços do lado direitto da frase '''

print(frase.split())

'''cria uma divisão entre os espaços da frase, colocando a frase em uma lista separadas por virgulas
cada caixa é uma lista ou seja ['curso'] é uma lista'''

print(frase.split('8'.join(frase)))
            


      

