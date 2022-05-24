def cleartxt(txt):
    import re
    for i in range(len(txt)):
        txt[i] = re.sub(r"[\W\s\d]", "", txt[i]).lower()
    return txt
def removeStop(txt, stop):
    for i in range(len(stop)):
        while stop[i] in txt: txt.remove(stop[i])
    return txt
def contWords(txt):
    dict = {}
    for i in range(len(txt)):
        if txt[i] in dict: dict[txt[i]] += 1
        else: dict[txt[i]] = 1
    return dict
