# Faça um programa que leia um ano qualquer e mostre se ele é ou não bissexto.

from datetime import date
ano = int(input("Digite um ano qualquer: (Digite 0 para utilizar o ano atual) "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto.')
    