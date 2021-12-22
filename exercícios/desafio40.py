# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0 reprovado;
# Média entre 5.0 e 6.9 recuperação;
# Média 7.0 ou superior aprovado!

print('-='*11)
print('\033[1;36mColégio São Silvestre\033[m')
print('-='*11)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
print(f"Sua média foi {media:.1f}.")
if media<5.0:
    print("Infelizmente você foi reprovado!")
elif media>4.9 and media<7.0:
    print("Você vai precisar fazer a recuperação!")
elif media>=7.0:
    print("Parabéns! Você foi aprovado.")
