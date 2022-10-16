# Mutáveis

lanche = ["Hambúrguer", "Suco", "Pizza", "Picolé"]

lanche.append()     # Adiciona um item a mais no final da lista
lanche.insert()     # Escolhe a posição para adionar um item, Ex: (0, "Hot-Dog")
del lanche[]        # Deleta um item selecionado e reposiciona a contagem dos itens.
lanche.pop()        # Deleta o último item por padrão ou você pode indicar qual deseja deletar.
lanche.remove()     # Não indica a posição, indica o nome do produto. Ex: ("Pizza")
lanche.clear()      # Deleta toda a lista!

valores = list(range(1,11))     # Cria uma lista com valores de 1 a 10.
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                  # Ordena em ordem crescente
valores.sort(reverse=True)      # Ordena em ordem decrescente
len(valores)                    # Mostra a quantidade de elementos da lista

valores = list()                                            # = list() ou = []
for x in range(5):
    valores.append(int(input("Digite um valor: ")))         # Peço o valor dos itens da lista ao usuário
for posicao, valor in enumerate(valores):
    print(f"Na posição {posicao} tem o valor {valor}")

a = [1, 3, 6, 9]
b = a[:]            # Cria-se uma cópia da lista A.

