import os; import sqlite3 as sql
con = sql.connect("livros.db"); cur = con.cursor()
cur.execute("""create table if not exists livros
(id txt, livro txt, autor txt, ano txt, sinopse txt, editora txt)""")
data = []; os.system("cls||clear")
while True:
  opcao = 0; data.clear()
  while not opcao:
    print("1 - Cadastrar um livro")
    print("2 - Listar todos os títulos")
    print("3 - Busca contextual do livro")
    print("4 - Ver detalhes de um livro")
    print("5 - Sair do programa")
    try: opcao = int(input("Qual opção você escolhe? "))
    except ValueError:
      opcao = 0; os.system("cls||clear")
      print("Entrada inválida! Entre com um inteiro.")
  if opcao == 1:
    os.system("cls||clear")
    id = input("Insira o id do livro: ")
    livro = input("Insira o título do livro: ")
    autor = input("Insira o autor do livro: ")
    ano = input("Insira o ano do livro: ")
    sinopse = input("Insira o sinopse do livro: ")
    editora = input("Insira o editora do livro: ")
    try:
      insert = "insert into livros values (?, ?, ?, ?, ?, ?);"
      con.execute(insert, (id, livro, autor, ano, sinopse, editora))
      con.commit()
    except sql.Error as error:
      os.system("cls||clear")
      print(f"Ocooreu o erro {error} no sqlite ao armazenar.")
    else:
      os.system("cls||clear")
      print("A tarefa foi executada com sucesso.")
  elif opcao == 2:
    for row in cur.execute("select * from livros order by id"):
      data.append(row)
    os.system("cls||clear")
    print("A lista de livros disponíveis:")
    for linha in data:
      print(f"Id: {linha[0]}, Livro: {linha[1]},"\
        f" Autor: {linha[2]}, Ano: {linha[3]},"\
        f" Sinopse: {linha[4]}, Editora: {linha[5]}")
  elif opcao == 3:
    os.system("cls||clear")
    busca = input("Insira o termo da busca: ")
    for row in cur.execute("select * from livros order by id"):
      data.append(row)
    os.system("cls||clear")
    print("O(s) resultado(s) da busca:")
    for linha in data:
      for coluna in linha:
        if busca in str(coluna):
          print(f"Id: {linha[0]}, Livro: {linha[1]},"\
            f" Autor: {linha[2]}, Ano: {linha[3]},"\
            f" Sinopse: {linha[4]}, Editora: {linha[5]}")
          break
  elif opcao == 4:
    os.system("cls||clear")
    id = int(input("Insira o id a ser procurado: "))
    for row in cur.execute("select * from livros order by id"):
      data.append(row)
    os.system("cls||clear")
    for linha in data:
      if id == linha[0]:
        print("O resultado da busca pelo id:")
        print(f"Id: {linha[0]}, Livro: {linha[1]},"\
          f" Autor: {linha[2]}, Ano: {linha[3]},"\
          f" Sinopse: {linha[4]}, Editora: {linha[5]}")
  elif opcao == 5:
    os.system("cls||clear")
    print("Até a próxima vez!")
    con.close(); exit(False)
  elif opcao != 0:
    os.system("cls||clear")
    print("Valor Inválido! Entre com valor de 1 a 5.")