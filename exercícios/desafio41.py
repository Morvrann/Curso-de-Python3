# A confederação nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos = mirim
# Até 12 anos = infantil
# Até 18 anos = junior
# Até 21 anos = senior
# Mais de 21 anos = master

from datetime import date

print('-='*16)
print('\033[1;36mConfederação Nacional de Natação\033[m')
print('-='*16)

nasc = int(input("Em que ano você nasceu? "))
anoatual = date.today().year
idade = anoatual-nasc

if idade<=9:
    print(f"Você tem {idade} anos.")
    print(f"A sua categoria é a MIRIM.")
elif idade>=10 and idade<=12:
    print(f"Você tem {idade} anos.")
    print(f"A sua categoria é a INFANTIL.")
elif idade>=13 and idade<=18:
    print(f"Você tem {idade} anos.")
    print(f"A sua categoria é a JUNIOR.")
elif idade>=19 and idade <=21:
    print(f"Você tem {idade} anos.")
    print(f"A sua categoria é a SENIOR.")
elif idade>21:
    print(f"Você tem {idade} anos.")
    print(f"A sua categoria é a MASTER.")
