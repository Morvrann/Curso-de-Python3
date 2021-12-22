# Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será mostrado.
# Equilátero = todos os lados iguais
# Escaleno = todos os lados diferentes
# Isósceles = dois lados iguais e um diferente

print("-="*12)
print("ANALISADOR DE TRIÂNGULOS")
print("-="*12)
n1 = float(input("Digite o comprimento da 1° reta: "))
n2 = float(input("Digite o comprimento da 2° reta: "))
n3 = float(input("Digite o comprimento da 3° reta: "))
if n1 == n2 and n2 == n3:
    tipo = ("Equilátero")
elif n1 != n2 and n2 != n3:
    tipo = ("Escaleno")
else:
    tipo = ("Isósceles")

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print("O triangulo existe")
    print(f"O tipo desse triângulo é: {tipo}")
else:
    print("O triangulo nao existe")
