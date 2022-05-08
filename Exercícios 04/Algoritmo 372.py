import os
v, a = [], 0
for i in range(12):
    os.system("cls")
    v.insert(i, input("Digite o {}º time: ".format(i+1)))
    while len(v[i]) == 0 or len(v[i]) > 20:
        os.system("cls")
        print("O nome tem que ter de 0 a 20 caracteres.")
        v.insert(i, input("Digite o {}º time: ".format(i+1)))
    t = 20 - len(v[i])
    for j in range(t): v[i] = v[i] + " "
while a not in ['1', '2']:
    os.system("cls")
    print("Todos contra Todos (1) / Mata-Mata (2)")
    a = input("Escolha um dos 2 modos de jogo: ")
os.system("cls")
if a == 1:
    print("Rodada Simples:")
    for i in range(10):
        for j in range(i+1, 11):
            print(v[i], "\t", v[j])
else:
    print("Rodada Simples:")
    for i in range(10):
        for j in range(i+1, 11):
            print(v[i], "\t", v[j])