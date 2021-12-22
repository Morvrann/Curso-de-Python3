# Elabora um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.
# à vista no dinheiro: 10% de desconto
# à vista no cartão: 5% de desconto
# parcelado em até 4x: preço normal
# parcelado em 5x ou mais: 20% de juros

preço = float(input("Quantos reais custa o produto? "))
forma = int(input('''Qual a forma de pagamento? Digite uma opção.
(1) para Pagamento a vista no dinheiro
(2) para Pagamento a vista no cartão
(3) para Pagamento no cartão em até 4x
(4) para Pagamento no cartão em 5x ou mais\n'''))

avistadin = preço - (preço*0.1)
avistacart = preço - (preço*0.05)
cartao4x = preço
cartao5x = preço + (preço*0.2)

if forma == 1:
    print(f"Você ganhou 10% de desconto! O valor do produto será R${avistadin:.2f}")
elif forma == 2:
    print(f"Você ganhou 5% de desconto! O valor do produto será R${avistacart:.2f}")
elif forma == 3:
    print(f"Você pagará o preço normal do produto. R${cartao4x:.2f}")
elif forma == 4:
    print(f"Você pagará 20% de juros. O valor do produto será R${cartao5x:.2f}")
else:
    print("Opção inválida.")
