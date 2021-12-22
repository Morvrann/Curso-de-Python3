frase = 'Turma boa de Python'

print(frase[9::3])
print(len(frase)) # conta quantos caracteres tem a string
print(frase.find('boa')) # encontra em qual valor de memoria está o caractere
print('Python' in frase) # verifica se existe a string (true ou false)
print('Queijo' in frase)
print('Pyth' in frase)
frase.replace('Python', 'Farofa') # Nao funciona assim
print(frase)
print(frase.replace('Python', 'Farofa'))
print(frase.upper()) # tudo em maiusculo
print(frase.lower()) # tudo em minusculo
print(frase.capitalize()) # so a primeira palavra começa com uma maiuscula
print(frase.title()) # todas as palavras começam por uma maiuscula
print(frase.strip()) # remove os espaços desnecessários no inicio e no fim da string
print(frase.rstrip()) # remove os espaços só no lado direito
print(frase.lstrip()) # remove os espaços só no lado esquerdo
print(frase.split()) # divide a string em blocos, cada palavra é um bloco com sequencia de valores de memoria

