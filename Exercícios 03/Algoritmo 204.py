n, m = int(input("Quntos números vão ser lidos? ")), -1
for i in range(n):
    n1 = float(input("Digite o número: "))
    if n1 > m: m = n1
print("Esse foi o maior número digitado:", m)