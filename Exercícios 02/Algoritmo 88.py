print("CALCULADORA")
print("+ p/ Soma, - p/ Subtração, * p/ Multiplicação, / p/ Divisão")
e = input("Digite sua escolha: ")
txt = "Digite o {}º número: "
a = float(input(txt.format(1)))
b = float(input(txt.format(2)))
if e == '+':
    print("A soma é", a + b)
elif e == '-':
    print("A subtração é", a - b)
elif e == '*':
    print("A multiplicação é", a * b)
elif e == '/':
    print("A divisão é", a / b)
else: print("Digite uma entrada válida!")