import os
import random as rdm
v1, v2, v3 = [], [], []; os.system("cls")
n = int(input("Digite até qual número ir: "))
for i in range(10): v1.append(rdm.randrange(n))
for i in range(20): v2.append(rdm.randrange(n))
for i in range(10):
    if v1[i] not in v2: v3.append(v1[i])
if len(v3) > 0: print(f"Os elementos incomuns são: {v3}")
else: print("Não existem elementos incomuns.")