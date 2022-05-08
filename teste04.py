import os
def ehana(x, y):
  if len(x) == len(y):
    x, y = list(x), list(y)
    for i in range(len(x)):
      if x[i] not in y: return False
      if y[i] not in x: return False
    return True
  return False
os.system("cls")
a = input("Digite a 1ª palavra: ")
b = input("Digite a 2ª palavra: ")
if ehana(a, b) == True:
  print("As palavras são anagramas.")
else:
  print("As palavras não são anagramas.")