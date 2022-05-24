import re; g1, g2 = {}, {}; y1, y2 = [], []
from matplotlib import pyplot as plt
a = open("txt1.txt", encoding = "utf-8")
b = open("txt2.txt", encoding = "utf-8")
c = open("stop.txt", encoding = "utf-8")
txt1 = a.read().split()
txt2 = b.read().split()
stop = c.read().split()
a.close(); b.close(); c.close
for i in range(len(stop)):
  while stop[i] in txt1: txt1.remove(stop[i])
for i in range(len(stop)):
  while stop[i] in txt2: txt2.remove(stop[i])
for i in range(len(txt1)):
  txt1[i] = re.sub(r"[\W\s\d]", "", txt1[i]).lower()
for i in range(len(txt2)):
  txt2[i] = re.sub(r"[\W\s\d]", "", txt2[i]).lower()
while "" in txt1: txt1.remove("")
while "" in txt2: txt2.remove("")
for i in range(len(txt1)):
  if txt1[i] in g1: g1[txt1[i]] += 1
  else: g1[txt1[i]] = 1
for i in range(len(txt2)):
  if txt2[i] in g2: g2[txt2[i]] += 1
  else: g2[txt2[i]] = 1
x1 = sorted(g1, key = g1.get, reverse = True)
for i in x1: y1.append(g1[i])
x2 = sorted(g2, key = g2.get, reverse = True)
for i in x2: y2.append(g2[i])
plt.plot(x1[:10], y1[:10], color = "k")
plt.plot(x2[:10], y2[:10], color = "r")
plt.xticks(rotation = 90); plt.show()