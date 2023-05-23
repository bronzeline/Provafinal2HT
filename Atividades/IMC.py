peso = float(input("Insira seu peso(kg): "))
altura = float(input("Insira sua altura(m): "))
imc = peso / (altura ** 2)
print("Seu índice de massa corporal é: {:.1f}".format(imc))
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("intervalo Normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif 30 <= imc <= 34.9:
    print("obesidade classe I")
elif 35 <= imc <= 39.9:
    print("Obesidade classe II")
elif imc >= 40:
    print("Obesidade classe III")
