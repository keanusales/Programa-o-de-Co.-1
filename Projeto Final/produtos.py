from os import system
import sqlite3 as sql, deposito, dashboard, csvtosqlite

con = sql.connect("produtos.db"); cur = con.cursor()
cur.execute("""create table if not exists produtos
  (cod txt, prod txt, preco real, qtd_adquirida integer, regiao txt, qualidade integer,
  fabricante txt, fornecedor txt, lote txt, validade txt, qtd_vendida integer)""")

system("cls||clear")
opcao = 0
while not opcao:
  print("[1] Cadastrar um produto"\
    "\n[2] Modificar um produto"\
    "\n[3] Listar todos os produtos"\
    "\n[4] Busca contextual do produto"\
    "\n[5] Ver um produto pelo código"\
    "\n[6] Deletar um produto"\
    "\n[7] Criar gráficos"\
    "\n[8] Visualizar gráficos"\
    "\n[9] Importar um arquivo csv"\
    "\n[10] Sair do programa")
  try: opcao = int(input('Qual opção você escolhe? '))
  except ValueError:
    opcao = 0; system("cls||clear")
    print("Entrada inválida! Entre com um inteiro.")
  else:
    # 1 - Cadastrar um produto
    if opcao == 1:
      opcao = 0
      deposito.cadastro(con)
    
    # 2 - Modificar um produto
    elif opcao == 2:
      opcao = 0
      deposito.modificacao(con)
    
    # 3 - Listar todos os produtos
    elif opcao == 3:
      opcao = 0
      deposito.listagem(cur)
    
    # 4 - Busca contextual do produto
    elif opcao == 4:
      opcao = 0
      deposito.busca_conceitual(cur)
    
    # 5 - Ver um produto pelo código
    elif opcao == 5:
      opcao = 0
      deposito.visualizar_codigo(cur)
    
    # 6 - Deletar um produto
    elif opcao == 6:
      opcao = 0
      deposito.deletar_produto(con)
    
    # 7 - Criar gráficos
    elif opcao == 7:
      opcao = 0
      dashboard.teste(cur)
    
    # 8 - Visualizar gráficos
    elif opcao == 8:
      opcao = 0
      dashboard.visualizar()
    
    # 9 - Importar um arquivo csv
    elif opcao == 9:
      opcao = 0
      arquivo = input("Digite o nome do arquivo: ")
      csvtosqlite.csv_to_sql(arquivo, con)
    
    elif opcao == 10:
      system("cls||clear")
      print("Até a próxima vez!")
      con.close()
    
    else:
      opcao = 0; system("cls||clear")
      print("Entre com um dos valores especificados!")