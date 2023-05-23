peso = float(input("Insira o peso do peixe(KG): "))
multa = (peso-50) * 4
if peso > 50:
    excesso = peso - 50
    print("Excesso de peso, uma multa será aplicada no valor de: ", multa)
else:
    print("Não há excesso de peso, logo não terá multa")
