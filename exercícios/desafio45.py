# GAME: Crie um programa para jogar jokenpô com você.
import random
from time import sleep

print('-='*21)
print('\033[1;36mBem vindo ao jogo Pedra, Papel e Tesoura!\033[m')
print('-='*21)

lista = ['pedra', 'papel', 'tesoura']
jogador = str(input("As opções são: Pedra, Papel ou Tesoura \nDigite qual você escolheu: "))
npc = random.choice(lista)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)

if jogador.lower() == npc:
    print("EMPATE!")
    print(f"Eu também escolhi {npc}.")
elif jogador.lower() == 'pedra' and npc == 'papel':
    print("VOCÊ PERDEU!")
    print(f"Eu escolhi {npc}.")
elif jogador.lower() == 'pedra' and npc == 'tesoura':
    print("VOCÊ VENCEU!")
    print(f"Eu escolhi {npc}.")
elif jogador.lower() == 'papel' and npc == 'pedra':
    print("VOCÊ VENCEU!")
    print(f"Eu escolhi {npc}.")
elif jogador.lower() == 'papel' and npc == 'tesoura':
    print("VOCÊ PERDEU!")
    print(f"Eu escolhi {npc}.")
elif jogador.lower() == 'tesoura' and npc == 'papel':
    print("VOCÊ VENCEU!")
    print(f"Eu escolhi {npc}.")
elif jogador.lower() == 'tesoura' and npc == 'pedra':
    print("VOCÊ PERDEU!")
    print(f"Eu escolhi {npc}.")
else:
    print("OPÇÃO INVÁLIDA.")
