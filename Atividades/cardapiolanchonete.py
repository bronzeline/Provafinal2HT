print("Escolha o produto que deseja:")
print("Cachorro quente(100)/Bauru(101)/Hambúrguer(102)/Cheeseburguer(103)/Refrigerante(104)")
codigo = float(input("Insira o código do produto: "))
quant = float(input("Insira a quantidade do produto: "))
valorfinal = 0 
if codigo == 100:
    valorfinal = 1.20 *quant
    print("O total é de R$", valorfinal)
elif codigo == 101:
    valorfinal = 1.30 * quant
    print("O total é de R$", valorfinal)
elif codigo == 102:
    valorfinal = 1.20 * quant
    print("O total é de R$", valorfinal)
elif codigo == 103:
    valorfinal = 1.30 * quant
    print("O total é de R$", valorfinal)
elif codigo == 104:
    valorfinal = 1.00 * quant
    print("O total é de R$", valorfinal)
else:
    print("Valor Inválido")
