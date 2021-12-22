# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome tudo em maiúsculo: {nome.upper()}')
print(f'Seu nome tudo em minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras') # Usando replace pra remover espaços
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras: ') # Subtraindo os espaços
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
print(f'Seu segundo nome é {separa[1]} e tem {len(separa[1])} letras')
