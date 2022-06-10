import os; import sqlite3 as sql
from datetime import datetime as dt
con = sql.connect("produtos.db"); cur = con.cursor()
cur.execute("""create table if not exists produtos
  (cod txt, prod txt, preco real, lote integer, valid txt)""")
data = []; os.system("cls||clear")
while True:
  opcao = 0; data.clear()
  while not opcao:
    print("1 - Cadastrar um produto")
    print("2 - Modificar um produto")
    print("3 - Listar todos os produtos")
    print("4 - Busca contextual do produto")
    print("5 - Ver um produto pelo código")
    print("6 - Ver produtos perto da validade")
    print("7 - Sair do programa")
    try: opcao = int(input("Qual opção você escolhe? "))
    except ValueError:
      opcao = 0; os.system("cls||clear")
      print("Entrada inválida! Entre com um inteiro.")
  if opcao == 1:
    os.system("cls||clear")
    cod = input("Insira o código do produto: ")
    prod = input("Insira o tipo do produto: ")
    preco = input("Insira o preço do produto: R$")
    lote = input("Insira o lote do produto: ")
    valid = input("Insira a validade do produto: ")
    try:
      insert = "insert into produtos values (?, ?, ?, ?, ?)"
      con.execute(insert, (cod, prod, preco, lote, valid))
      con.commit()
    except sql.Error as error:
      os.system("cls||clear")
      print(f"Ocooreu o erro {error} no sqlite ao armazenar.")
    else:
      os.system("cls||clear")
      print("A tarefa foi executada com sucesso.")
  elif opcao == 2:
    os.system("cls||clear")
    print("1 - Produto, 2 - Preco, 3 - Lote, 4 - Validade")
    tipo = int(input("Digite o que vai ser alterado: "))
    mod = input("Digite a modificação do dado: ")
    cod = input("Insira o código do produto: ")
    try:
      if tipo == 1:
        con.execute(f"""update produtos set prod = {mod}
          where cod = {cod}"""); con.commit()
      elif tipo == 2:
        con.execute(f"""update produtos set preco = {mod}
          where cod = {cod}"""); con.commit()
      elif tipo == 3:
        con.execute(f"""update produtos set lote = {mod}
          where cod = {cod}"""); con.commit()
      elif tipo == 4:
        con.execute(f"""update produtos set valid = {mod}
          where cod = {cod}"""); con.commit()
    except sql.Error as error:
      os.system("cls||clear")
      print(f"Ocooreu o erro {error} no sqlite ao armazenar.")
    else:
      os.system("cls||clear")
      print("A tarefa foi executada com sucesso.")
  elif opcao == 3:
    for row in cur.execute("select * from produtos order by cod"):
      data.append(row)
    os.system("cls||clear")
    print("A lista de produtos disponíveis:")
    for linha in data:
      print(f"Código: {linha[0]}, Tipo: {linha[1]},"\
        f" Preço: R${linha[2]}, Lote: {linha[3]},"\
        f" Validade: {linha[4]}")
  elif opcao == 4:
    os.system("cls||clear")
    busca = input("Insira o termo da busca: ")
    for row in cur.execute("select * from produtos order by cod"):
      data.append(row)
    os.system("cls||clear")
    print("O(s) resultado(s) da busca:")
    for linha in data:
      for coluna in linha:
        if busca in str(coluna):
          print(f"Código: {linha[0]}, Tipo: {linha[1]},"\
            f" Preço: R${linha[2]}, Lote: {linha[3]},"\
            f" Validade: {linha[4]}")
          break
  elif opcao == 5:
    os.system("cls||clear")
    codigo = int(input("Insira o código a ser procurado: "))
    for row in cur.execute("select * from produtos order by cod"):
      data.append(row)
    os.system("cls||clear")
    for linha in data:
      if codigo == linha[0]:
        print("O resultado da busca pelo código:")
        print(f"Código: {linha[0]}, Tipo: {linha[1]},"\
          f" Preço: R${linha[2]}, Lote: {linha[3]},"\
          f" Validade: {linha[4]}")
  elif opcao == 6:
    os.system("cls||clear")
    mes, ano = dt.today().strftime('%m'), dt.today().strftime('%Y')
    for row in cur.execute("select * from produtos order by cod"):
      data.append(row)
    for linha in data:
      if int(linha[4][3:5]) - int(mes) <= 1:
        if int(linha[4][6:]) == int(ano):
          print(f"O produto {linha[1]} está quase vencendo!")
  elif opcao == 7:
    os.system("cls||clear")
    print("Até a próxima vez!")
    con.close(); exit(False)
  elif opcao != 0:
    os.system("cls||clear")
    print("Valor Inválido! Entre com valor de 1 a 7.")