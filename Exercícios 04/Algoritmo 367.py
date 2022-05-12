import os
import random as rdm
v = []; os.system("cls")
n = int(input("Até qual número? "))
for i in range(100):
    v.append(rdm.randrange(n))
maior = menor = soma = v[0]
pares = 1 if v[0] % 2 == 0 else 0
for i in range(1, 100):
    if v[i] % 2 == 0: pares += 1
    soma += v[i]
    if v[i] > maior: maior = v[i]
    elif v[i] < menor: menor = v[i]
print(f"Maior: {maior}, Menor: {menor}")
print(f"Percentual de Pares: {pares}%")
print(f"Média: {soma/100}")