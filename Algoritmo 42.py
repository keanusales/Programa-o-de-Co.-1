import math as m
a = input("Digite um ângulo em graus: ")
r = m.radians(float(a))
s, c, t = m.sin(r), m.cos(r), m.tan(r)
sc, csc, ctg = 1 / c, 1 / s, 1 / t
print("O seno é:", s)
print("O cosseno é:", c)
print("A tangente é:", t)
print("A secante é:", sc)
print("A cossecante é:", csc)
print("A cotangente é:", ctg)