#um número é primo quando ele é dividido somente duas vezes.

print("=" * 40)
print('             NÚMEROS PRIMOS')
print("=" * 40)

a = int(input("digite um número:"))
cont = 0

for c in range(1,a + 1 ):
    if a % c == 0:
        print("\033[1;34;40m {}\033[m".format(c), end =" " )
        cont = cont + 1
    else:
        print("\033[1;36;40m {}\033[m".format(c) , end =" " )

if cont == 2 :
    print("\n seu número teve {} divisores, portanto ele é um número prino!".format(cont))
else:
    print(" \nseu número teve {} divisores, portanto ele não é primo!".format(cont))

    