a = float(input("Digite o 1º lado: "))
b = float(input("Digite o 2º lado: "))
c = float(input("Digite o 3º lado: "))
if a < (b + c) and b < (a + c) and c < (a + b):
    if a > b and a > c:
        maior, lados = a ** 2, b ** 2 + c ** 2
    elif b > c:
        maior, lados = b ** 2, a ** 2 + c ** 2
    else:
        maior, lados = c ** 2, a ** 2 + b ** 2
    if maior == lados: print("Triângulo Retângulo!")
    elif maior > lados: print("Triângulo Obtusângulo!")
    else: print("Triângulo Acutângulo!")
else: print("As medidas não formam um triângulo!")