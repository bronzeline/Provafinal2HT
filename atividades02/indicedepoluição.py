indc = float(input("Insira o índice de poluição média: "))
if indc <= 0.25:
    print("O Indíce de poluição está aceitável")
elif indc <= 0.3:
    print("As indústrias do 1° grupo devem suspender as atividades")
elif indc <= 0.4:
    print("As indústrias do 1° e 2° grupo devem suspender as atividades")
elif indc <= 0.5:
    print("Todos os grupos devem cessar suas atividades")
else:
    print("Indíce indefinido")
