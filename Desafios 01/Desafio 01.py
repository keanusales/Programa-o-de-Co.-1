import re; exit = []; y = []; gfc = {}
from matplotlib.pyplot import plot as plt
from matplotlib.pyplot import show as shw
txt1 = open("txt1.txt", encoding = "utf-8").read().split()
txt2 = open("txt2.txt", encoding = "utf-8").read().split()
stpw = open("stpw.txt", encoding = "utf-8").read().split()
open("txt1.txt", encoding = "utf-8").close()
open("txt2.txt", encoding = "utf-8").close()
open("stpw.txt", encoding = "utf-8").close()
for i in range(len(txt1)):
    if txt1[i] not in stpw: exit.append(txt1[i])
for i in range(len(txt2)):
    if txt2[i] not in stpw: exit.append(txt2[i])
for i in range(len(exit)):
    exit[i] = re.sub(r"[\W\s\d]", "", exit[i]).lower()
while "" in exit: exit.remove("")
for i in range(len(exit)):
    if exit[i] in gfc: gfc[exit[i]] += 1
    else: gfc[exit[i]] = 1
x = sorted(gfc, key = gfc.get, reverse = True)
for i in x: y.append(gfc[i])
plt(x[:7], y[:7], color = "k"); shw()