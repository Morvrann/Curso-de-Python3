# Crie um programa que leia um número inteiro qualquer e mostre
# na tela se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))
resto = num%2

if (resto == 0):
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar!")
    