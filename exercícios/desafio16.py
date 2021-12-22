# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção inteira. Ex: o n° 6.3658 tem a parte inteira 6.

import math # Ou: --> from math import trunc <-- pra importar só o trunc

numero = float(input('Informe um número real: '))
parteInteira = math.trunc(numero)
print('A parte inteira do número real {} é {}.'.format(numero, parteInteira))
