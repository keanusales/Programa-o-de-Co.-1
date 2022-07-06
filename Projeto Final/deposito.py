# Import de bibliotecas necessárias
from os import system
import sqlite3 as sql
from dicionarios import reg, forn, dados, quali

data = []

# Módulo do crud

# 1 - Cadastrar um produto
def cadastro(con):
  system("cls||clear")
  print("Insira os valores necessários para o cadastro de um novo produto")
  dados['cod'] = input("Código: ")
  dados['produto'] = input("Nome: ")
  dados['preco'] = input("Preço: R$")
  dados['qtd_adquirida'] = input("Quantidade adquirida: ")
  for key, value in reg.items(): print(f"[{key}] {value}")
  dados['regiao'] = reg[int(input("Digite sua escolha: "))]
  for key, value in quali.items(): print(f"[{key}] {value}")
  dados['nota'] = quali[int(input("Digite sua Escolha: "))]
  dados['fabricante'] = input("Fabricante: ")
  for key, value in forn.items(): print(f"[{key}] {value}")
  dados['fornecedor'] = forn[int(input("Digite sua escolha: "))]
  dados['lote'] = input("Insira o lote do produto: ")
  dados['valid'] = input("Insira o validade do produto: ")
  dados['qtd_vendas'] = input("Quantidade de vendas: ")
  try:
    insert = "insert into produtos values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    con.execute(insert, (dados['cod'], dados['produto'], dados['preco'],
      dados['qtd_adquirida'], dados['regiao'], dados['nota'], dados['fabricante'],
      dados['fornecedor'], dados['lote'], dados['valid'], dados['qtd_vendas']))
    con.commit()
  except sql.Error as error:
    system("cls||clear")
    print(f"Ocorreu o seguinte erro no sqlite: {error}")
  else:
    system("cls||clear")
    print("A tarefa foi executada com sucesso.")

# 2 - Modificar um produto
def modificacao(con):
  system("cls||clear")
  print('''
    [1] Produto
    [2] Preço
    [3] Quantidade adquirida
    [4] Região
    [5] Nota
    [6] Fabricante
    [7] Fornecedor
    [8] Lote
    [9] Validade
    [10] Quantidade de produtos vendidos
    ''')
  tipo = int(input("\n\nDigite o tipo do dado a ser alterado: "))
  try:
    if tipo == 1:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite o novo nome do produto: ")
      con.execute(f"update produtos set prod = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 2:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite o novo preço do produto: ")
      con.execute(f"update produtos set preco = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 3:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite a nova nova quantidade adquirida do produto: ")
      con.execute(f"update produtos set qtd_adquirida = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 4:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite a nova região do produto: ")
      con.execute(f"update produtos set regiao = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 5:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite a nova nota do produto: ")
      con.execute(f"update produtos set nota = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 6:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite o novo fabricante do produto: ")
      con.execute(f"update produtos set fabricante = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 7:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite o novo fornecedor do produto: ")
      con.execute(f"update produtos set fornecedor = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 8:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite o novo lote do produto: ")
      con.execute(f"update produtos set lote = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 9:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite a nova validade do produto: ")
      con.execute(f"update produtos set valid = {mod} where cod = {codigo}")
      con.commit()
    elif tipo == 10:
      codigo = input("Insira o código do produto: ")
      mod = input("Digite a nova quantidade de produtos vendidos: ")
      con.execute(f"update produtos set qtd_vendas = {mod} where cod = {codigo}")
      con.commit()
  except sql.Error as error:
    system("cls||clear")
    print(f"Ocorreu o seguinte erro no sqlite: {error}\n\n")
  else:
    system("cls||clear")
    print("A tarefa foi executada com sucesso.\n\n")

# 3 - Listar os produtos disponíveis
def listagem(cur):
  data.clear()
  for row in cur.execute("select * from produtos order by cod"):
    data.append(row)
    system("cls||clear")
    print("A lista de produtos disponíveis:")
    for linha in data:
      print(f"\n\nCódigo: {linha[0]}, Nome: {linha[1]},"\
        f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
        f" Região: {linha[4]}, Nota: {linha[5]}"\
        f" Fabricante: {linha[6]}, Fornecedor: {linha[7]}"\
        f" Lote: {linha[8]}, Validade: {linha[9]}"\
        f" Quantidade de produtos vendidos: {linha[10]}\n\n")  

# 4 - Busca Conceitual do produto
def busca_conceitual(cur):
  data.clear()
  system("cls||clear")
  busca = input("Insira o termo da busca: ")
  for row in cur.execute("select * from produtos order by cod"):
    data.append(row)
  system("cls||clear")
  print("O(s) resultado(s) da busca:")
  for linha in data:
    for coluna in linha:
      if busca in str(coluna):
        print(f"\n\nCódigo: {linha[0]}, Nome: {linha[1]},"\
          f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
          f" Região: {linha[4]}, Nota: {linha[5]}"\
          f" Fabricante: {linha[6]}, Fornecedor: {linha[7]}"\
          f" Lote: {linha[8]}, Validade: {linha[9]}"\
          f" Quantidade de produtos vendidos: {linha[10]}\n\n")
        break

# 5 - Busca pelo código do produto
def visualizar_codigo(cur):
  data.clear()
  system("cls||clear")
  codigo = int(input("Insira o código a ser procurado: "))
  for row in cur.execute("select * from produtos order by cod"):
    data.append(row)
  system("cls||clear")
  for linha in data:
    if codigo == linha[0]:
      print("O resultado da busca pelo código:")
      print(f"\n\nCódigo: {linha[0]}, Nome: {linha[1]},"\
        f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
        f" Região: {linha[4]}, Nota: {linha[5]}"\
        f" Fabricante: {linha[6]}, Fornecedor: {linha[7]}"\
        f" Lote: {linha[8]}, Validade: {linha[9]}"\
        f" Quantidade de produtos vendidos: {linha[10]}\n\n")

# 6 - Deletar um produto da db
def deletar_produto(con):
  system("cls||clear")
  codigo = input("Insira o código do produto a ser deletado: ")
  try:
    con.execute(f"delete from produtos where cod = {codigo}")
    con.commit()
  except sql.Error as error:
    system("cls||clear")
    print(f"Ocorreu o seguinte erro no sqlite: {error}")
  else:
    system("cls||clear")
    print("A tarefa foi executada com sucesso.")