# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

a = input('Digite alguma coisa: ')
print('O tipo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('Só tem números? ', a.isnumeric())
print('São apenas letras? ', a.isalpha())
print('Tem números e/ou letras? ', a.isalnum())
print('Está em minúsculas? ', a.islower())
print('Está em maiúsculas? ', a.isupper())
print('Está capitalizado? ', a.istitle())
print('Essa palavra é um identificador Python válido?', a.isidentifier())
