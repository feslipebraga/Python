# TUPLAS ()
# Variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura.

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
print(sorted(lanche)) # Mostra os itens da tupla em ordem alfabética.

a = (1, 2 , 3)
b = (3, 4, 5, 6)
c = a + b
print(c)
print(len(c)) # len conta quantos itens tem a tupla
print(c.count(5)) # count conta quantos 5 tem a tupla
print(c.index(3)) # index mostra em qual posicao está o numero, pega somente a primeira ocorrencia
print(c.index(3, 3)) # o 1nd 3 está na posicao 2. usamos o ,3 pra encontrar o proximo 3 a partir da posicao 3.

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")

# for pos, x in enumerate(lanche):          # Caso precise colocar a posição
#    print(f"{pos}: {x}")

# for x in range(0, len(lanche)):           # Outra forma
#    print(f"{x}: {lanche[x]}")

for x in lanche:
    print(x)