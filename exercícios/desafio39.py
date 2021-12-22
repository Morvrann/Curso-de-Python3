# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.

from datetime import date
anoatual = date.today().year


print('-='*23)
print('\033[1;35mPrograma de alistamento do Exército Brasileiro\033[m')
print('-='*23)

nascimento = int(input("Em que ano você nasceu? "))
idade = (anoatual-nascimento)
falta = (18-idade)
if (idade == 18):
    print(f"Quem nasceu em {nascimento} completa {idade} anos em {anoatual}.")
    print(f"Você precisa se alistar IMEDIATAMENTE!")
elif (idade < 18):
    print(f"Quem nasceu em {nascimento} completa {idade} anos em {anoatual}.")
    print(f"Ainda faltam {falta} anos para o seu alistamento.")
    print(f"Seu alistamento será em {anoatual+falta}")
elif (idade > 18):
    print(f"Quem nasceu em {nascimento} completa {idade} anos em {anoatual}.")
    print("O ano do seu alistamento já passou!")
    print(f"Você deveria ter se alistado em {nascimento+18}.")
    