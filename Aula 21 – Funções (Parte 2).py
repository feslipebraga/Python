# help(print)         # INTERACTIVE HELP

def contador(i, f, p):
    '''
    docstrings
    '''
    for x in range(i, f, p):
        print(x, end=" ")

# help(contador)      # Mostra o significado da funcao criada (docstrings)

# ARGUMENTOS OPCIONAIS

def somar(a=0, b=0, c=0):
    soma = a + b + c
    print(soma)
somar(3)

# ESCOPO DE VARIÁVEIS 

def funcao(x):
    global a    # Transforma o A global/universal. A recebe o valor abaixo:
    a = 5
    b = 4
    c = 2
    print(a, b, c)

a = 2
funcao(a)       # ESCOPO LOCAL, mostra o valor de A *DENTRO* da funcao
print(a)        # ESCOPO GLOBAL, mostra o valor de A *FORA* da funcao

# RETORNANDO VALORES (return)

def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma

a = somar(1, 2, 3)
b = somar(9, 1)
c = somar(6, 6)

print(f"A soma dos valores foram {a}, {b} e {c}")

# PRÁTICA

def fatorial(num=1):
    f = 1
    for x in range(num, 0, -1):
        f = f * x
    return f

numero = int(input("Numero: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")

# PRÁTICA 2
def par(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False

x = int(input("Informe um numero: "))
print(par(x))
if True:            # if par(x): 
    print("é par")
else:
    print("é impar")