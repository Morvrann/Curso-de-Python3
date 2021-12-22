# Escreva um programa que leia velocidade de um carro.
# Se ele ultrapassar 80Km/H mostre uma msg dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada Km acima do limite.

velocidade = int(input("Qual era a velocidade do carro em Km/h? "))
multa = (velocidade-80)*7
if (velocidade <=80):
    print("Você estava dentro do limite de velocidade, continue assim!")
else:
    print(f"Infelizmente você estava {velocidade-80} Km/h acima do limite permitido, você será multado em R${multa} reais.")
    