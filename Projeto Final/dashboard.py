import os
from matplotlib import pyplot as plt

def teste(cur):
    # um vetor de vetores de tuplas: [[[x,y],[x,y],[x,y]],[[x,y],[x,y],[x,y]]]
    varx, vary, cont1 = {}, {}, 1
    cur.execute("select * from produtos order by cod")
    cont = len(cur.fetchall())
    
    data = []
    for row in cur.execute("select * from produtos order by cod"):
        data.append(row)
    qtd_graficos = int(input("\nForneça a quantidade de gráficos que deseja criar (no máximo 5): "))

    for q in range(qtd_graficos):
        
        #VARIÁVEL X:
        escolhax = int(input('''
        Forneça a coluna desejada para corresponder aos eixo x:
        [0] Código
        [1] Nome
        [2] Preço
        [3] Quantidade adquirida
        [4] Região de fabrição
        [5] Classificação
        [6] Fabricante
        [7] Fornecedor
        [8] Lote
        [9] Validade
        [10] Quantidade de vendas

        : '''))
        
        os.system("cls||clear")
        aux = []
        for i in range(cont):
            for j in range(10):
                if escolhax == j:
                    aux.append(data[i][j])
        varx[cont1] = aux

        #VARIÁVEL Y:
        escolhay = int(input('''
        Forneça a coluna desejada para corresponder aos eixo y:
        [0] Código
        [1] Nome
        [2] Preço
        [3] Quantidade adquirida
        [4] Região de fabrição
        [5] Classificação
        [6] Fabricante
        [7] Fornecedor
        [8] Lote
        [9] Validade
        [10] Quantidade de vendas

        : 
        '''))
        os.system("cls||clear")
        aux = []
        for i in range(cont):
            for j in range(10):
                if escolhay == j:
                    aux.append(data[i][j])
        vary[cont1] = aux
        
        #CRIAR GRÁFICO
        escolhatipo = int(input('''
        Forneça o tipo do gráfico:
        [1] Linha
        [2] Em barra
        [3] Pizza
        [4] Em rede
        
        '''))
        
        
        if(escolhatipo == 1):
            escolhatitulo = input('''
            Forneça o título do gráfico: ''')
            escolhanomex = input('''
            Forneça um título para as variáveis x: ''')
            escolhanomey = input('''
            Forneça um título para as variáveis y: ''')
            plt.subplot(1, qtd_graficos, cont1)
            plt.plot(varx[cont1], vary[cont1]) 
            plt.title(escolhatitulo) 
            plt.xlabel(escolhanomex) 
            plt.ylabel(escolhanomey) 

        elif(escolhatipo == 2):
            auxx = []
            auxy = []
            auxx.append(varx[cont1])
            auxy.append(vary[cont1])
            for i in range(cont1):
                plt.bar(auxx[i], auxy[i], color = 'r')

        elif(escolhatipo == 3):
            print("line")
        elif(escolhatipo == 4):
            print("line")
        elif(escolhatipo == 5):
            print("line")
        elif(escolhatipo == 6):
            print("line")
        
        cont1 += 1

def visualizar(): plt.show()