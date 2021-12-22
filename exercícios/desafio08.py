# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

valor = int(input('Digite um valor em metros: '))
print ('{} metro(s) é igual a: \n{} centímetros \n{} milímetros'.format(valor, valor*100, valor*1000))
