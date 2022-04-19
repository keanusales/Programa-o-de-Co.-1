a1 = int(input("Entre com o 1º termo: "))
a2 = int(input("Entre com o 2º termo: "))
print(a1, a2, end = ' ')
for i in range(3, 11):
    t = a2 - a1 if i % 2 == 0 else a2 + a1
    print(t, end = ' ')
    a1, a2 = a2, t