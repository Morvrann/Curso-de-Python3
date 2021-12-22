# Escreva um programa que converta uma temperatura 
# digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Informe uma temperatura em °C '))
far = (cel * 9/5) + 32
print('{}°C é equivalente a {}°F'.format(cel, far))
