import os
from matplotlib import pyplot as plt

def teste(cur):
    # um vetor de vetores de tuplas: [[[x,y],[x,y],[x,y]],[[x,y],[x,y],[x,y]]]
    varxy, data = [], []
    cur.execute("select * from produtos order by cod")
    cont = len(cur.fetchall())
    
    for row in cur.execute("select * from produtos order by cod"):
        data.append(row)
    qtd_graficos = int(input("\nForneça a quantidade de gráficos que deseja criar (no máximo 5): "))

    for q in range(qtd_graficos):
        #CRIAR GRÁFICO
        escolhatipo = int(input('''
        Forneça o tipo do gráfico:
        [1] Linha
        [2] Histograma
        [3] Pizza
        [4] Em rede
        [5] Em barra
        
        '''))
        #linha
        if(escolhatipo == 1):
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

            : 
            '''))
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
            controlevar(escolhax, escolhay, os, data, cont, varxy)
            escolhatitulo = input("\nForneça o título do gráfico: ")
            escolhanomex = input("\nForneça um título para o eixo x: ")
            escolhanomey = input("\nForneça um título para o eixo y: ")
            plt.subplot(1,qtd_graficos,q+1)
            
            plt.plot(varxy[q].keys(), varxy[q].values()) 
            plt.title(escolhatitulo) 
            plt.xlabel(escolhanomex) 
            plt.ylabel(escolhanomey) 
        #histograma
        elif(escolhatipo == 2):
            escolha = int(input('''
            Forneça a coluna desejada analisar:
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
            controlevar(escolha, escolha, os, data, cont, varxy)
            plt.subplot(1,qtd_graficos,q+1)
            escolhatitulo = input("\nForneça o título do gráfico: ")
            escolhanomex = input("\nForneça um título para o eixo x: ")
            escolhanomey = input("\nForneça um título para o eixo y: ")
            
            plt.hist(varxy[q].keys(), 5, rwidth=0.9)
            plt.title(escolhatitulo) 
            plt.xlabel(escolhanomex) 
            plt.ylabel(escolhanomey) 
        #pizza
        elif(escolhatipo == 3):
        #tratamento de dados
            escolha = int(input('''
            Forneça a coluna desejada analisar:
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
            controlevar(escolha, escolha, os, data, cont, varxy)
            valores = [*varxy[q].values()]
            cont={}
            for i in range(len(valores)):
                if valores[i] not in cont:
                    cont[valores[i]] = 1*100/len(valores)
                else:
                    cont[valores[i]] +=1*100/len(valores)
            varxy[q]=cont

            plt.subplot(1,qtd_graficos,q+1).axis('equal')
            escolhatitulo = input("\nForneça o título do gráfico: ")

            plt.pie(varxy[q].values(), labels= varxy[q].keys(), autopct='%1.1f%%',startangle=90)
            plt.title(escolhatitulo) 

        elif(escolhatipo == 4):
            print("line")
        elif(escolhatipo == 5):
            print("line")
        elif(escolhatipo == 6):
            print("line")
"""        
        cont1+=1
       

    plt.subplot(1, 2, 1)  
    plt.plot(x, y_1, 'r', linewidth=5, linestyle=':') 
    plt.title('FIRST PLOT') 
    plt.xlabel('x-axis') 
    plt.ylabel('y-axis') 
    plt.subplot(1, 2, 2) 
    plt.plot(x, y_2, 'g', linewidth=5) 
    plt.title('SECOND PLOT') 
    plt.xlabel('x-axis') 
    plt.ylabel('y-axis') 
    plt.tight_layout(4) 
    plt.show()

    x = np.linspace(0, 2, 21) # 21 pontos no intervalo [0, 2]
    for i in range(2):
        plt.subplot(1, 2, i+1)  
        plt.plot(x, x)       
    plt.show()
 """
def visualizar():
    plt.show()

def controlevar(escolhax, escolhay, os, data, cont, varxy):
    aux = {}
    aux1 = {}
    aux2 = []
    
    os.system("cls||clear")
    for i in range(cont):
        for j in range(10):
            if escolhax == j:
                aux2.append(data[i][j])
                aux[data[i][j]]=" "       
    os.system("cls||clear")
    for i in range(cont):
        for j in range(10):
            if escolhay == j:
                aux[aux2[i]]=data[i][j]
    aux3 = sorted([*aux])
    print(aux3)
    for i in(aux3):
        aux1[i]= aux[i]
    print(aux1)    
    varxy.append(aux1)

    """aux.values()
    vary.append(x)
    varx.append([*aux])"""
    #vary.append(aux.values())
    #print(varx)
    #print(vary[0][1])
    #print(vary)'
"""
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
    '''))"""