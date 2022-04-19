import math as m
for i in range(15):
    n = float(input("Digite o número: "))
    if n >= 0: print("Raiz:", round((m.sqrt(n)), 4))
    else: print("Não existe raiz de número negativo!")