# Crie um programa que pergunta a distancia de uma viagem em Km
# Calcule o preço da passagem cobra R$0,50 por Km para viagens de  até 200Km
# e R$0,45 para viagens mais longas.

viagem = float(input("Quantos Km terá essa viagem? "))
preco1 = viagem*0.50
preco2 = viagem*0.45

if (viagem <= 200):
    print(f"Essa viagem custará {preco1} reais!")
else:
    print(f"Essa viagem custará {preco2} reais!")
    