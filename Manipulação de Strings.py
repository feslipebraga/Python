# Manipulando textos

frase = 'Curso em vídeo Python'
print(frase)

# Fatiamento de strings

frase[9:21]         # Analisa a frase da posição 9 até a 21    
frase[9:21:2]       # Pula de 2 em 2
frase[:5]           # Vai do início até a pos 5
frase[15:]          # Vai da pos 15 até o final
frase[9::3]         # Vai do 9 até o final pulando 3 em 3

len(frase)          # conta os numeros de caracteres
frase.count()       # conta quantas vezes o item aparece
frase.find()        # encontra a 1 posição 
frase.replace()     # troca os caracteres
frase.upper()       # transforma em maiscula
frase.lower()       # transforma em minuscula
frase.capitalize()  # 1 letra em maiuscula
frase.title()       # iniciais em maiuscula
frase.strip()       # remove espacos em brancos
frase.split()       # transforma em lista
frase.join()        # junta os componentes da lista.


frase.index()       # localiza a 1 posicao na lista/tupla
frase.index(3)      # index mostra em qual posicao está o numero, pega somente a primeira ocorrencia
frase.index(3, 3)   # o 1nd 3 está na posicao 2. usamos o ,3 pra encontrar o proximo 3 a partir da posicao 3.