n = int(input("Insira o número de horas trabalhadas: "))
c = int(input("Insira o código: "))
if n > 50:
    e = (n-50) * 20
    total = 50 * 10 + e
else:
    total= n * 10
    e = 0
print("O salário total é de R$: ", total)
print("O salário excedente é de R$: ", e)
