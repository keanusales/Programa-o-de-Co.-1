data = input("Digite a data no formato ddmmaa: ")
dia = int(data) / 10000
mes = int(data) % 10000 / 100
ano = int(data) % 100
print("Dia:", int(dia), "Mês:", int(mes), "Ano:", int(ano))