def linha():                                # linha()
    print("--------------------")           # Cria uma linha.

def mensagem(msg):
    print("--------------------")
    print(msg)                              # mensagem("SISTEMAS DE INFORMAÇÃO")
    print("--------------------")           # Cria uma frase personalizada

mensagem("SISTEMAS DE INFORMAÇÃO")

# SOMANDO VALORES 1.0

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma entre A + B é igual a {s}")
soma(b = 1, a = 5)
soma(1, 3)                                  # A será 1 e B = 3.

# EMPACOTAMENTO 
def contador(* num):
    tamanho = len(num)
    print(f"A tupla {num} possui {tamanho} números.")

contador(1, 3, 5, 4)
contador(3, 3, 9, 1, 6, 9)
contador(2, 0)

# DOBRANDO VALORES DE UMA LISTA

def dobra(lista):
    for d in range(len(lista)):
        lista[d] *= 2

valores = [1, 2, 3, 4, 5]
copiaValores = valores[:]
dobra(copiaValores)
print(valores)
print(copiaValores)

# SOMANDO VALORES 2.0
def soma(* num):
    soma = 0
    for s in num:
        soma += s
    print(f"Somando os valores {num} temos = {soma}")

soma(1, 2)
soma(5, 5)