pessoas = [["Pedro", 25], ["Maria", 19], ["João", 32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

galera = []
dados = []

for c in range(3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()  

for c in galera:
    print(c)