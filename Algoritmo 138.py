v = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
n = int(input("Digite o número do mês correspondente: "))
if n > 0 and n < 13: print("O mês correspondente é {}.".format(v[n-1]))
else: print("Digite um número correspondente aos meses do ano.")