import time

s = int(input("até qual número você deseja gerar numeros pares ?"))
for c in range(0,(s + 2),2):
    print(c)
    time.sleep(0.5)
    print("-")
    