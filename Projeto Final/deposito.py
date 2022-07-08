# Import de bibliotecas necessárias
from os import system; import sqlite3 as sql
from dicionarios import dados, reg, forn, quali, types

data = []

# Módulo do crud

# 1 - Cadastrar um produto
def cadastro(con):
  system("cls||clear")
  print("Insira os valores necessários para o cadastro do novo produto:")
  dados['cod'] = input("Código: ")
  dados['produto'] = input("Nome: ")
  dados['preco'] = input("Preço: R$")
  dados['qtd_adquirida'] = input("Quantidade adquirida: ")
  for key, value in reg.items(): print(f"[{key}] {value}")
  dados['regiao'] = reg[int(input("Digite sua escolha: "))]
  for key, value in quali.items(): print(f"[{key}] {value}")
  dados['qualidade'] = quali[int(input("Digite sua Escolha: "))]
  dados['fabricante'] = input("Fabricante: ")
  for key, value in forn.items(): print(f"[{key}] {value}")
  dados['fornecedor'] = forn[int(input("Digite sua escolha: "))]
  dados['lote'] = input("Insira o lote do produto: ")
  dados['valid'] = input("Insira o validade do produto: ")
  dados['qtd_vendas'] = input("Quantidade de vendas: ")
  try:
    insert = "insert into produtos values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    con.execute(insert, (dados['cod'], dados['prod'], dados['preco'],
      dados['qtd_adquirida'], dados['regiao'], dados['qualidade'], dados['fabricante'],
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
  escolha = 0
  while not escolha:
    try:
      system("cls||clear")
      print("[0] - Código"\
        "\n[1] - Produto"\
        "\n[2] - Preço"\
        "\n[3] - Quantidade adquirida"\
        "\n[4] - Região"\
        "\n[5] - Qualidade"\
        "\n[6] - Fabricante"\
        "\n[7] - Fornecedor"\
        "\n[8] - Lote"\
        "\n[9] - Validade"\
        "\n[10] - Quantidade vendida")
      escolha = int(input("\nDigite o tipo do dado a ser alterado: "))
    except ValueError:
      escolha = 0; system("cls||clear")
      print("Entrada Inválida. Entre com um inteiro.")
    else:
      if 1 <= escolha <= 10:
        try:
          codigo = input("Insira o código do produto: ")
          mod = input("Digite a modificação a ser feita: ")
          con.execute(types[escolha], (mod, codigo))
          con.commit()
        except sql.Error as error:
          system("cls||clear")
          print(f"Ocorreu o seguinte erro no sqlite: {error}\n")
        else:
          system("cls||clear")
          print("A tarefa foi executada com sucesso.\n")
      else:
        escolha = 0; system("cls||clear")
        print("Digite um valor especificado!")

# 3 - Listar os produtos disponíveis
def listagem(cur):
  data.clear()
  for row in cur.execute("select * from produtos order by cod"):
    data.append(row)
    system("cls||clear")
    print("A lista de produtos disponíveis:")
    for linha in data:
      print(f"Código: {linha[0]}, Nome: {linha[1]},"\
        f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
        f" Região: {linha[4]}, Qualidade: {linha[5]},"\
        f" Fabricante: {linha[6]}\nFornecedor: {linha[7]},"\
        f" Lote: {linha[8]}, Validade: {linha[9]},"\
        f" Quantidade vendida: {linha[10]}\n")

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
        print(f"Código: {linha[0]}, Nome: {linha[1]},"\
          f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
          f" Região: {linha[4]}, Qualidade: {linha[5]},"\
          f" Fabricante: {linha[6]}\nFornecedor: {linha[7]},"\
          f" Lote: {linha[8]}, Validade: {linha[9]},"\
          f" Quantidade vendida: {linha[10]}\n")
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
      print(f"Código: {linha[0]}, Nome: {linha[1]},"\
        f" Preço: R${linha[2]}, Quantidade adquirida: {linha[3]},"\
        f" Região: {linha[4]}, Qualidade: {linha[5]},"\
        f" Fabricante: {linha[6]}\nFornecedor: {linha[7]},"\
        f" Lote: {linha[8]}, Validade: {linha[9]},"\
        f" Quantidade vendida: {linha[10]}\n")

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