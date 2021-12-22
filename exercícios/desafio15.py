# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos Km você percorreu com o carro? '))
dias = int(input('Por quantos dias você alugou o carro? '))
diaria = (60*dias)
kmx = (0.15*km)
precoFinal = (diaria+kmx)

print('O aluguel do carro ficou no valor de R${:.2f}'.format(precoFinal))
print('Sendo R${} da diária e R${} dos Km rodados.'.format(diaria, kmx))

