import os
import itertools as tls
v, a = [], 0
for i in range(12):
    os.system("cls")
    v.insert(i, input(f"Digite o {i+1}º time: "))
    while len(v[i]) == 0 or len(v[i]) > 20:
        os.system("cls")
        print("O nome deve ter de 0 a 20 caracteres.")
        v.insert(i, input(f"Digite o {i+1}º time: "))
while a not in ['1', '2']:
    try:
        os.system("cls")
        print("Todos contra Todos (1) / Mata-Mata (2)")
        a = input("Escolha um dos 2 modos de jogo: ")
    except ValueError: a = 0
os.system("cls")
if a == 1:
    print("Todos contra Todos:")
    for i in range(11):
        for j in range(i+1, 12):
            print(f"{v[i]} vs {v[j]}")
else:
    p = list(tls.permutations(v, 2))
    print("Mata-Mata das Equipes:")
    for i in range(132):
        print(f"{p[i][0]} vs {p[i][1]}")