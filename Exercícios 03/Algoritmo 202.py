n = int(input("Digite com o número > 15: "))
if n > 15:
    for i in range(15, n + 1, 15):
        print("O número é:", i)
else: print("Não existe multiplo de 3 e 5 menor que 15.")