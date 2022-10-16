dados = {"Pedro", 25}

dados = dict()          # Declaro que "dados" é um dicionário
dados = {}

dados = {"nome": "Pedro", "idade": 25}

print(dados["nome"])    # Retorna "Pedro"
print(dados["idade"])   # Retorna a idade 25.

dados["sexo"] = "M"     # Adiciona valor ao dicionario
dados = {"nome": "Pedro", "idade": 25, "sexo": "M"}

del dados["idade"]      # Deleta um item, nesse caso, deleta idade.

filme = {"titulo": "star wars", "ano": 1977 , "diretor": "george lucas"}

# Tudo que está contido em "filme" são items()

# Os titulos são keys()

# Os valores dos titulos são values()

print(filme.keys())     # Printa os titulos "titulo", "ano" e "diretor"
print(filme.values())   # Printa os valores: "star wars", 1977 e "george lucas"
print(filme.items())    # Printa todo o dicionário

for keys, values in filme.items():
    print(f"O {keys} é {values}")

filme.copy()            # Cria uma cópia do dicionário.