# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
print('''Escolha para qual base você quer converter esse número:
      [ 1 ] para converter o número para binário
      [ 2 ] para converter o número para octal
      [ 3 ] para converter o número para hexadecimal''')
opção = int(input("Digite o número da opçao desejada: "))

if opção == 1:
    print(f"O número inteiro {num} convertido para binário é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"O número inteiro {num} convertido para octal é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"O número inteiro {num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print("Opção inválida.")
    
    