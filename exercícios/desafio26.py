# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip()
fraseUp = frase.upper()
print(f'A letra "A" aparece {fraseUp.count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {fraseUp.find("A")+1}')
print(f'A letra "A" aparece pela última vez na posição {fraseUp.rfind("A")+1}')
