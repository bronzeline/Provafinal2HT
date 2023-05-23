numero1 =int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
numero3 = int(input("Insira o terceiro número: "))
menor = numero1
if (numero2 < menor):
    menor = numero2
if (numero3 < menor):
    menor = numero3
print('Menor número: ',menor)
