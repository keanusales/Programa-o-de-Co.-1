# Imports necessários
from os import system
import csv, sqlite3 as sql
from dicionarios import dados

# 1 - Importar uma db de csv para sqlite3
def csv_to_sql(arquivo, con):
  try:
    with open(arquivo, encoding = "utf-8") as file:
      system("cls||clear")
      print("Arquivo csv aberto com sucesso.")
      tabela = list(csv.reader(file, delimiter = ","))
      if len(tabela[0]) == len(dados):
        tam = 4 if len(tabela) > 4 else len(tabela)
        keys, pos = list(dados.keys()), []
        j, erros, saida = 0, 0, []
        while len(pos) != len(keys):
          saida.clear()
          print("Exemplo do que está na coluna:")
          for i in range(tam): saida.append(tabela[i][j])
          print(", ".join(saida) + "\n")
          try:
            print("Tipos de dados da base da dados:")
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
            entry = int(input("\nDigite o correspondente a coluna: "))
          except ValueError:
            system("cls||clear")
            print("Entrada inválida! Entre com um inteiro!")
          else:
            if 0 <= entry <= 10:
              if entry not in pos:
                system("cls||clear"); j += 1; pos.append(entry)
              else:
                system("cls||clear")
                print("Digite um valor que não é repetido.")
            else:
              system("cls||clear")
              print("Entre com um dos valores especificados!")
        for linha in tabela:
          dados[keys[pos[0]]] = linha[0]
          dados[keys[pos[1]]] = linha[1]
          dados[keys[pos[2]]] = linha[2]
          dados[keys[pos[3]]] = linha[3]
          dados[keys[pos[4]]] = linha[4]
          dados[keys[pos[5]]] = linha[5]
          dados[keys[pos[6]]] = linha[6]
          dados[keys[pos[7]]] = linha[7]
          dados[keys[pos[8]]] = linha[8]
          dados[keys[pos[9]]] = linha[9]
          dados[keys[pos[10]]] = linha[10]
          try:
            insert = "insert into produtos values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
            con.execute(insert, (dados['cod'], dados['prod'], dados['preco'],
              dados['qtd_adquirida'], dados['regiao'], dados['qualidade'], dados['fabricante'],
              dados['fornecedor'], dados['lote'], dados['valid'], dados['qtd_vendas']))
          except sql.Error as error:
            index = tabela.index(linha) + 1; erros += 1
            print(f"Ocorreu o erro {error} no sqlite ao armazenar na linha {index}")
        if not erros: con.commit(); print("Arquivo importado com sucesso!")
        else: print(f"Ocorreram {erros} erros, não foi possível armazenar.")
      else: print(f"A quantidade de colunas tem que ser igual a {len(dados)}.")
  except FileNotFoundError: system("cls||clear"); print("Arquivo não encontrado!")