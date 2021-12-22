# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
# ou então o empréstimo será negado.

print("=+"*22)
print("\033[1;35mSeja bem vindo a Financeira Dinheiro na Mão!\033[m")
print("=+"*22)

casa = float(input("Qual o valor da casa que você pretende comprar? "))
salario = float(input("Qual é o seu salário mensal? "))
parcela = int(input("Em quantas parcelas você pretende pagar? "))

valorParcela = (casa/parcela)

print(f"O valor de cada prestação será de: R$ {valorParcela:.2f}")

if valorParcela > (salario*0.3):
    print("Empréstimo negado.\nInfelizmente esse valor de prestação excede o limite de 30% do seu salário.")
else:
    print("Parabéns, seu empréstimo foi aceito!")
    