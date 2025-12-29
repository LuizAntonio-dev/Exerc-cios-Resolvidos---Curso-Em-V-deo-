sexo = str(input("digite aqui o seu sexo")).strip().upper() [0]

while sexo not in "mfMF":
    
    sexo = str(input("digite novamente:")).strip().upper() [0]

print("sexo {} registrado!!".format(sexo))
