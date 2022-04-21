v = input("Digite o verbo regular no infinitivo: ")
pa = ["Eu", "Tu", "Ele(a)", "Nós", "Vós", "Eles(as)"]
if v[-2] == "a" and v[-1] == "r":
    pr = ["ei", "aste", "ou", "amos", "astes", "aram"]
    ps = ["o", "as", "a", "amos", "ais", "am"]
    fu = ["arei", "arás", "ará", "aremos", "areis", "arão"]
    print("\nO verbo {} no pretérito perfeito:".format(v))
    for i in range(6): print(pa[i], v[:-2] + pr[i])
    print("\nO verbo {} no presente do indicativo:".format(v))
    for i in range(6): print(pa[i], v[:-2] + ps[i])
    print("\nO verbo {} no futuro do presente:".format(v))
    for i in range(6): print(pa[i], v[:-2] + fu[i])
elif v[-2] == "e" and v[-1] == "r":
    pr = ["i", "este", "eu", "emos", "estes", "eram"]
    ps = ["o", "es", "e", "emos", "eis", "em"]
    fu = ["erei", "erás", "erá", "eremos", "ereis", "erão"]
    print("\nO verbo {} no pretérito perfeito:".format(v))
    for i in range(6): print(pa[i], v[:-2] + pr[i])
    print("\nO verbo {} no presente do indicativo:".format(v))
    for i in range(6): print(pa[i], v[:-2] + ps[i])
    print("\nO verbo {} no futuro do presente:".format(v))
    for i in range(6): print(pa[i], v[:-2] + fu[i])
elif v[-2] == "i" and v[-1] == "r":
    pr = ["i", "iste", "iu", "imos", "istes", "iram"]
    ps = ["o", "es", "e", "imos", "is", "em"]
    fu = ["irei", "irás", "irá", "iremos", "ireis", "irão"]
    print("\nO verbo {} no pretérito perfeito:".format(v))
    for i in range(6): print(pa[i], v[:-2] + pr[i])
    print("\nO verbo {} no presente do indicativo:".format(v))
    for i in range(6): print(pa[i], v[:-2] + ps[i])
    print("\nO verbo {} no futuro do presente:".format(v))
    for i in range(6): print(pa[i], v[:-2] + fu[i])
else: print("Digite um verbo regular no infinitivo!")