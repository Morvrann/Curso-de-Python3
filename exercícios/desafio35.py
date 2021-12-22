# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario
# se elas podem ou não formar um triangulo.

print("-="*12)
print("ANALISADOR DE TRIÂNGULOS")
print("-="*12)
n1 = float(input("Digite o comprimento da 1° reta: "))
n2 = float(input("Digite o comprimento da 2° reta: "))
n3 = float(input("Digite o comprimento da 3° reta: "))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print("O triangulo existe")
else:
    print("O triangulo nao existe")
