import os, sqlite3 as sql
import deposito, dashboard, csvtosqlite

con = sql.connect("produtos.db"); cur = con.cursor()
cur.execute("""create table if not exists produtos
  (cod txt, nome txt, preco real, qtd_adquirida integer, regiao txt, nota integer,
  fabricante txt, fornecedor txt, lote txt, valid txt, qtd_vendas integer)""")

os.system("cls||clear")
while True:
  opcao = 0
  while not opcao:
    print('''
    [1] Cadastrar um produto
    [2] Modificar um produto
    [3] Listar todos os produtos
    [4] Busca contextual do produto
    [5] Ver um produto pelo código
    [6] Deletar um produto
    [7] Criar gráficos
    [8] Visualizar gráficos
    [9] Importar um arquivo csv
    [10] Sair do programa
    ''')
    try: opcao = int(input('Qual opção você escolhe? '))
    except ValueError:
      opcao = 0; os.system("cls||clear")
      print("Entrada inválida! Entre com um inteiro.")
    else:

      # 1 - Cadastrar um produto
      if opcao == 1:
        deposito.cadastro(con)
      
      # 2 - Modificar um produto
      elif opcao == 2:
        deposito.modificacao(con)
      
      # 3 - Listar todos os produtos
      elif opcao == 3:
        deposito.listagem(cur)
      
      # 4 - Busca contextual do produto
      elif opcao == 4:
        deposito.busca_conceitual(cur)
      
      # 5 - Ver um produto pelo código
      elif opcao == 5:
        deposito.visualizar_codigo(cur)
      
      # 6 - Deletar um produto
      elif opcao == 6:
        deposito.deletar_produto(con)
      
      # 7 - Criar gráficos
      elif opcao == 7:
        dashboard.teste(cur)
      
      # 8 - Visualizar gráficos
      elif opcao == 8:
        dashboard.visualizar()
      
      # 9 - Importar um arquivo csv
      elif opcao == 9:
        arquivo = input("Digite o nome do arquivo: ")
        csvtosqlite.csv_to_sql(arquivo, con)
      
      elif opcao == 10:
        os.system("cls||clear")
        print("Até a próxima vez!")
        con.close(); break
      
      else:
        os.system("cls||clear")
        print("Entre com um dos valores especificados!")