def openArchive(filename):
    a = open(filename, encoding = "utf-8")
    filename = a.read().split(); a.close()
    return filename
def removeStop(txt, stop):
    for i in range(len(stop)):
        while stop[i] in txt: txt.remove(stop[i])
    return txt
def cleartxt(txt):
    import re
    for i in range(len(txt)):
        txt[i] = re.sub(r"[\W\s\d]", "", txt[i]).lower()
    while "" in txt: txt.remove("")
    return txt
def countWords(txt):
    dict = {}
    for i in range(len(txt)):
        if txt[i] in dict: dict[txt[i]] += 1
        else: dict[txt[i]] = 1
    return dict
def orderWords(txt):
    x, y = [], []
    x = sorted(txt, key = txt.get, reverse = True)
    for i in x: y.append(txt[i])
    return x, y
def addSpace(celula, num, lado):
    dif = num - len(celula)
    if lado == "right":
        return celula + (dif * " ")
    else: return (dif * " ") + celula
def printTable(data):
    max = []
    for j in range(len(data[0])):
        max.insert(j, len(data[0][j]))
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if len(data[i][j]) > max[j]: max.insert(j, len(data[i][j]))
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(addSpace(data[i][j], max[j]), end = " | ")
        print("")
def plotGraph(txt, stop, color):
    from matplotlib import pyplot as plt
    txt = openArchive(txt)
    stop = openArchive(stop)
    txt = removeStop(txt, stop)
    txt = cleartxt(txt)
    txt = countWords(txt)
    x, y = orderWords(txt)
    plt.plot(x[:10], y[:10], color = color)
    plt.xticks(rotation = 90); plt.show()