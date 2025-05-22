vendas_cursos01 = int(input("Digite o número de vendas do curso 1:  "))
vendas_cursos02 = int(input("DIgite o número de vendas do curso 2:  "))

if vendas_cursos01 > vendas_cursos02:
   print("O curso 1 é maior.")
elif vendas_cursos02 > vendas_cursos01:
   print("O curso 2 é maior.")
else:
    print("As vendas empataram.")