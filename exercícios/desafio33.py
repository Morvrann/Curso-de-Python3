# Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
# Utilize uma estrutura condicional.

a = int(input("Digite o 1° valor: "))
b = int(input("Digite o 2° valor: "))
c = int(input("Digite o 3° valor: "))

if (a > b > c):
    print(f"O maior valor é {a} e o menor valor é {c}.")
if (a > c > b):
    print(f"O maior valor é {a} e o menor valor é {b}")
if (b > a > c):
    print(f"O maior valor é {b} e o menor valor é {c}.")
if (b > c > a):
    print(f"O maior valor é {b} e o menor valor é {a}")
if (c > b > a):
    print(f"O maior valor é {c} e o menor valor é {a}.")
if (c > a > b):
    print(f"O maior valor é {c} e o menor valor é {b}")
if (a==b or a==c or b==c):
    print("Não digite valores repetidos!")
    
