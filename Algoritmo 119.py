t, troca, v = "Digite o {}º: ", 1, []
n = int(input("Entre com o tamanho: "))
for i in range(n):
    v.append(float(input(t.format(i+1))))
while(troca == 1):
    troca = 0
    for i in range(n-1):
        if v[i] > v[i+1]:
            troca = 1
            aux = v[i]
            v[i] = v[i+1]
            v[i+1] = aux
print("Organizado fica dessa forma:", v)