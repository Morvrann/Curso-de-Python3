# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math

# Usando HYPOT

cateto1 = float(input('Digite quantos centímetros mede o cateto oposto: '))
cateto2 = float(input('Digite quantos centímetros mede o cateto adjacente: '))
hipotenusa = math.hypot(cateto1, cateto2)
print(f'A hipotenusa desse triângulo retângulo mede {hipotenusa:.2f} centímetros')

# Usando SQRT

cateto1 = float(input('Digite quantos centímetros mede o cateto oposto: '))
cateto2 = float(input('Digite quantos centímetros mede o cateto adjacente: '))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f'A hipotenusa desse triângulo retângulo mede {hipotenusa:.2f} centímetros')
