p = input("Qual é o seu peso? ")
a = input("Qual é a sua altura? ")
try:
    p, a = float(p), float(a)
    if p > 0 and a > 0:
        imc = round((p/a**2), 1)
        if imc < 18.5: print("Abaixo do peso!")
        elif imc < 24.9: print("Peso Normal!")
        elif imc < 29.9: print("Sobrepeso!")
        elif imc < 34.9: print("Obesidade G1!")
        elif imc < 39.9: print("Obesidade G2!")
        else: print("Obesidade Mórbida!")
    else: print("O peso e a altura são positivos!")
except ValueError:
    print("Digite um valor numérico e positivo!")