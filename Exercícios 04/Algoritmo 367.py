import os
import random as rdm
v = []
for i in range(100):
    v.append(rdm.randrange(1000))
maior = menor = soma = v[0]
pares = 1 if v[0] % 2 == 0 else 0
for i in range(1, 100):
    if v[i] % 2 == 0: pares += 1
    soma += v[i]
    if v[i] > maior: maior = v[i]
    elif v[i] < menor: menor = v[i]
os.system("cls")
pares = str(pares)
print("Maior:", maior, "Menor:", menor)
print("Percentual de Pares:", pares + "%")
print("Média:", soma / 100)