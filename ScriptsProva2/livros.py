import os; import sqlite3 as sql
con = sql.connect("livros.db"); cur = con.cursor()
cur.execute("""create table if not exists livros
(id txt, livro txt, autor txt, ano txt, sinopse txt, editora txt)""")
data = []; os.system("cls||clear"); cont = False
while opcao not in [1, 2, 3, 4, 5]:
  print("1 - Cadastrar um livro")
  print("2 - Listar todos os títulos")
  print("3 - Busca contextual do livro")
  print("4 - Ver detalhes de um livro")
  print("5 - Sair do programa")
  try: opcao = int(input("Qual opção você escolhe? "))
  except ValueError:
    print("Entrada inválida! Entre com inteiros!")
    opcao = 0
  if opcao == 1:
    os.system("cls||clear")
    id = input("Insira o id do livro: ")
    livro = input("Insira o título do livro: ")
    autor = input("Insira o autor do livro: ")
    ano = input("Insira o ano do livro: ")
    sinopse = input("Insira o sinopse do livro: ")
    editora = input("Insira o editora do livro: ")
    try:
      insert = """insert into livros values (?, ?, ?, ?, ?, ?);"""
      con.execute(insert, (id, livro, autor, ano, sinopse, editora))
      con.commit()
    except sql.Error as error:
      print(f"Ocooreu o erro {error} no sqlite ao armazenar.")
    else:
      os.system("cls||clear"); print("A tarefa foi executada com sucesso.")
  elif opcao == 2:
    for row in cur.execute("select * from livros order by id"):
      data.append(list(row))
    os.system("cls||clear")
    print("A lista de livros disponíveis:")
    for i in range(len(data)):
      print(f"Id: {data[i][0]}, Livro: {data[i][1]},"
        f" Autor: {data[i][2]}, Ano: {data[i][3]},"
        f" Sinopse: {data[i][4]}, Editora: {data[i][5]}")
  elif opcao == 3:
    os.system("cls||clear")
    busca = input("Insira o termo da busca: ")
    for row in cur.execute("select * from livros order by id"):
      data.append(list(row))
    for i in range(len(data)):
      if busca in data[i]:
        os.system("cls||clear")
        print("O resultado da busca:")
        print(f"Id: {data[i][0]}, Livro: {data[i][1]},"\
          f" Autor: {data[i][2]}, Ano: {data[i][3]},"\
          f" Sinopse: {data[i][4]}, Editora: {data[i][5]}")
  elif opcao == 4:
    os.system("cls||clear")
    id = input("Insira o id a ser procurado: ")
    for row in cur.execute("select * from livros order by id"):
      data.append(list(row))
    for i in range(len(data)):
      if busca in data[i]:
        os.system("cls||clear")
        print("O resultado da busca:")
        print(f"Id: {data[i][0]}, Livro: {data[i][1]},"\
          f" Autor: {data[i][2]}, Ano: {data[i][3]},"\
          f" Sinopse: {data[i][4]}, Editora: {data[i][5]}")
  elif opcao == 5:
    os.system("cls||clear")
    print("Até a próxima vez!")
    con.close(); exit(False)
  else:
    os.system("cls||clear")
    print("Valor errado! Escolha de 1 a 5.")