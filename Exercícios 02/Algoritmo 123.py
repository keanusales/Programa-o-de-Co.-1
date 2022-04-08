a = float(input("Digite o 1º lado: "))
b = float(input("Digite o 2º lado: "))
c = float(input("Digite o 3º lado: "))
if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b and a == c: print("Triângulo Equlátero!")
    elif a != b and b != c: print("Triângulo Escaleno!")
    else: print("Triângulo Isósceles!")
else: print("As medidas não formam um triângulo!")