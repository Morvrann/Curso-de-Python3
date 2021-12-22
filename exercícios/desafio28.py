# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randint(0, 5)
print("Eu pensei em um valor entre 0 e 5, tente advinhar qual foi! ")
numD = int (input("Digite seu palpite: "))
print("PROCESSANDO...")
sleep(3)
if num == numD:
    print(f"Parabéns! {numD} é a resposta correta!")
else:
    print(f"Infelizmente você errou! A resposta correta era {num}")
    