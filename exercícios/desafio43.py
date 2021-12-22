# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 = abaixo do peso
# Entre 18.5 e 25 = peso ideal
# 25 até 30 = sobrepeso
# 30 a 40 = obesidade
# Mais de 40 = obesidade mórbida

print('-='*9)
print('\033[1;36mCalculadora de IMC\033[m')
print('-='*9)

peso = float(input("Quantos kilos você pesa? "))
altura = float(input("Quantos centímetros você tem de altura? "))
imc = (peso/(altura*altura))*10000

print(f"O valor do seu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc>=18.5 and imc<=25.0:
    print("Você está com o peso ideal!")
elif imc>25.0 and imc<=30.0:
    print("Você está com sobrepeso!")
elif imc>30.0 and imc<=40.0:
    print("Você está com obesidade.")
elif imc>40.0:
    print("Cuidado! Você está com obesidade mórbida.")
