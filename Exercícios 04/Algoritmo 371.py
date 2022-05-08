import os
import random as rdm
v1, v2, v3 = [], [], []
for i in range(10): v1.append(rdm.randrange(1000))
for i in range(20): v2.append(rdm.randrange(1000))
for i in range(10):
    if v1[i] not in v2: v3.append(v1[i])
os.system("cls")
if len(v3) > 0: print("Os elementos incomuns são:", v3)
else: print("Não existem elementos incomuns.")