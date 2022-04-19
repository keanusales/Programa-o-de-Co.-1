f1 = float(input("Menor temperatura em Fahrenheit: "))
f2 = float(input("Maior temperatura em Fahrenheit: "))
d, t = float(input("Entre com o decremento: ")), f1
while (t >= f2):
    t, c = t-d, round((5*(t-32)/9), 2)
    print("Temperatura em celcius:", c)