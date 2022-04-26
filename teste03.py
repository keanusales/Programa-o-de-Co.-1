import os
def força(a):
  l, n, c = 0, 0, 0
  for i in range(len(a)):
    if 'a' <= a[i] <= 'z': l+=1
    elif 'A' <= a[i] <= 'Z': l+=1
    elif '0' <= a[i] <= '9': n+=1
    elif '!' <= a[i] <= '/': c+=1
  if n > 0 and l == 0 and c == 0: return 1
  elif n == 0 and l > 0 and c == 0: return 2
  elif n > 0 and l > 0 and c == 0: return 3
  elif n > 0 and l > 0 and c > 0: return 4
senha = input("Digite sua senha: ")
while len(senha) == 0:
  os.system('cls' if os.name == 'nt' else 'clear')
  senha = input("Digite algo na sua senha: ")
if força(senha) == 1: print("Seua senha é muito fraca!")
elif força(senha) == 2: print("Seua senha é fraca!")
elif força(senha) == 3: print("Seua senha é forte!")
elif força(senha) == 4: print("Seua senha é muito forte!")
else: print("Sua senha não corresponde a uma classificação.")