d1 = input("Entre com o dividendo: ")
d2 = input("Entre com o divisor: ")
d1, d2 = float(d1), float(d2)
q, r = d1 / d2, d1 % d2
print("Dividendo:", int(d1), "\nDivisor:", int(d2))
print("Quociente:", int(q), "\nResto:", int(r))