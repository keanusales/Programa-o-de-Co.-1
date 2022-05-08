import os
controle = False
while controle == False:
    try:
        os.system("cls")
        controle = True
        n = int(input("Digite a quantidade de alunos: "))
    except ValueError: controle = False
opção, nomes, notas = 0, [], []
while opção != 5:
    while opção not in [1, 2, 3, 4, 5]:
        try:
            os.system("cls")
            print("------ MENU ------")
            print("1 - Ler Nomes e Notas")
            print("2 - Média Geral")
            print("3 - Classificação")
            print("4 - Busca Candidato")
            print("5 - Sair do Programa")
            opção = int(input("Escolha uma opção: "))
        except ValueError: opção = 0
    if opção == 1:
        opção, erro = 0, True
        for i in range(n):
            os.system("cls")
            nomes.insert(i, input("Digite o nome: "))
            while erro == True:
                try:
                    erro = False
                    print("Entre somente com números!")
                    notas.insert(i, float(input("Digite a nota: ")))
                except ValueError: erro = True
            erro = True
    elif opção == 2:
        opção, media = 0, 0
        os.system("cls")
        for i in range(n):
            media = media + notas[i]
        print("Média Geral:", media/n)
        sair = input("Pressione enter para sair! ")
    elif opção == 3:
        opção = 0
        os.system("cls")
        for i in range(n-1):
            for j in range(i+1, n):
                if notas [i] < notas[j]:
                    auxnota = notas[i]
                    notas[i] = notas[j]
                    notas[j] = auxnota
                    auxnome = nomes[i]
                    nomes[i] = nomes[j]
                    nomes[j] = auxnota
        print("Relação em ordem decrescente de nota:")
        for i in range(n):
            print("{} - Nome: {}\tNota: {}".format(i+1,nomes[i],notas[i]))
        sair = input("Pressione enter para sair! ")
    elif opção == 4:
        opção = 0
        os.system("cls")
        def procura(nome):
            for i in range(n):
                if nome == nomes[i]: return i
            return None
        nome = input("Digite o nome a ser procurado: ")
        if procura(nome) == None: print("Não existe nome correspondente!")
        else: print("Nome:", nomes[procura(nome)], "Nota:", notas[procura(nome)])
        sair = input("Pressione enter para sair! ")