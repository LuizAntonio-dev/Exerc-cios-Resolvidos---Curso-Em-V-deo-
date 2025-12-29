frase = str(input('digite uma frase:')).upper().strip()
frase2 = frase.split()
#split, deica a o texto em forma de lista 
junto  = "".join(frase2)
#junto = "".join(frase2) = substitui os espaços no meio do texto, dando a possibilidade de retirar ou subtituir por outro caractere, EX :"#".join(frase2)

letras2  = ""
# letras = "" é igual quando temos um acumulador, mas ele junta letras, e não soma numeros 
print(junto)

for letras in range(len(junto)-1 , -1 , -1):
    '''a sequencia dos numeros,  no primeiro caractere, "-1", é de onde ele começa a contar, ou seja do ultimo número, o segundo "-1" diz a até 
    aonde ele pode chegar, ou seja tambem até o ultimo número, e por ultimo -"1", diz o sentido em que vai lançar o texto '''
    letras2 = letras2 + junto[letras]

print(letras2 )


if letras2 == junto:
    print( "Muito bom")
else:
    print("insatisfatório")