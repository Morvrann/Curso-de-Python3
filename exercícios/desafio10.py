# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela possa comprar. Considere 1 USD = 3.27 BRL

cruzado = float(input('Quantos reais você tem na carteira? '))
doleta = cruzado/3.27
print ('Com {} reais você consegue comprar {:.2f} dólares.'.format(cruzado, doleta))
