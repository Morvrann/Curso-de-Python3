# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nomeSep = nome.split()
print(f'Prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {nomeSep[0]}')
print(f'Seu último nome é {nomeSep[-1]}')
