a = float(input("Digite o 1º lado: "))
b = float(input("Digite o 2º lado: "))
c = float(input("Digite o 3º lado: "))
if a < (b + c) and b < (a + c) and c < (a + b):
    print("Podem ser lados de um triângulo!")
else: print("Não podem ser lados de um triângulo!")