# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

base = float(input('Quantos metros de largura tem a parede? '))
alt = float(input('Quantos metros de altura tem a parede? '))
ar = base*alt
tinta = ar/2
print('A área dessa parede é de {} metros²'.format(ar))
print('Será necessário {} litros de tinta para pintar essa parede.'.format(tinta))
