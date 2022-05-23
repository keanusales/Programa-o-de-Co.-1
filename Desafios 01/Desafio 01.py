import re; exit = []; y = []; gfc = {}
from matplotlib.pyplot import plot as plt
from matplotlib.pyplot import show as shw
a = open("txt1.txt", encoding = "utf-8")
b = open("txt2.txt", encoding = "utf-8")
c = open("stpw.txt", encoding = "utf-8")
txt1 = a.read().split()
txt2 = b.read().split()
stpw = c.read().split()
a.close(); b.close(); c.close
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
plt(x[:10], y[:10], color = "k"); shw()