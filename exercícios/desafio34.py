# Escreva um programa que pergunte o salário de um funcionario e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para salários inferiores ou iguais o aumento será de 15%

salario = float(input("Digite o seu salário atual: "))
aumentoA = (salario*0.10)+salario
aumentoB = (salario*0.15)+salario

if (salario > 1250):
    print(f"Você recebeu um aumento de 10%!\nSeu novo salário é: {aumentoA}")
else:
    print(f"Você recebeu um aumento de 15%!\nSeu novo salário é: {aumentoB}")
    
