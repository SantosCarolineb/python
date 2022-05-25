# 1- Escreva um programa que some todos os itens de uma lista.

listaNum = []

while True:
    num = float(input("Digite um número para somar a lista: "))
    listaNum.append(num)
    
    
    def somaTotal(listaNum):
        soma = 0
        for num in listaNum:
          soma = soma + num
        return soma
    
    soma = somaTotal(listaNum)
        
    print(soma)
    
    continua = input("Deseja continuar somando? Digite S ou N: ")
    if continua.upper() == "N":
        break

print(f"Soma final: {soma}")


# 2- Escreva um programa que multiplique todos os itens de uma lista.

listaNum = []

while True:
    num = float(input("Digite um número para somar a lista: "))
    listaNum.append(num)
    
    
    def multFinal(listaNum):
        resultado = 1
        for num in listaNum:
          resultado = resultado * num
        return resultado
    
    resultado = multFinal(listaNum)
        
    print(resultado)
    
    continua = input("Deseja continuar somando? Digite S ou N: ")
    if continua.upper() == "N":
        break

print(f"Soma final: {resultado}")


# 3- Escreva um programa que retorne o maior e o menor número de uma lista.

listaNum, maiorn, menorn = [], 0, 0
qtd = int(input("Quantos valores quer adicionar na lista? "))

for num in range(qtd):
    listaNum.append(float(input("Adicione um valor a lista: ")))
    if num == 0:
        maiorn = menorn = listaNum[num]
    elif listaNum[num] > maiorn:
        maiorn = listaNum[num]
    elif listaNum[num] < menorn:
        menorn = listaNum[num]
        
print(f'''Maior valor: {maiorn}
Menor valor: {menorn}''')


# 4- Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com'
# Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )

palavra = input("Contaremos os caracteres! Digite uma palavra: ")

def qtdCaracter(palavra):
    D = {}
    
    for caracter in palavra:
        if caracter in D:
            D[caracter] += 1
        else:
            D[caracter] = 1
    return D
    
print(qtdCaracter(palavra))


# 5- Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais. (Exemplo de lista: ['abc','xyz','aba', '1221']
# Resultado esperado: 2 )

print("Digite 5 palavras para colocar na lista:")

palavras = []

palavras2 = []

for i in range(5):
    palavras.append(input("Digite aqui... "))
    
for p in palavras:
    if len(p) > 2 and p[0] == p[-1]:
        palavras2.append(p)
        
print(len(palavras2))


# 6- Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da tupla (Exemplo de lista: [(2, 5), (1, 2), (4, 4),(2,3), (2, 1)]
# Resultado esperado: [(2, 1),(1,2), (2, 3), (4, 4), (2, 5)] )

listaTup = []

print("Digite 5 tuplas.")

for t in range(5):
    listaTup.append(tuple(input("Digite aqui... ")))
    
print(f"Lista de tuplas digitada: {listaTup}")
    
listaTup.sort(key=lambda x: x[1], reverse=False)

print("-"*20)

print(f"Lista de tuplas digitada ordenada: {listaTup}")


# 7- Escreva um programa que adicione uma chave (key) a um dicionário. (Exemplo dicionário(Dict): {0:10, 1:20} 
# Resultado esperado: {0: 10, 1: 20, 2: 30} )

d = {1:2, 3:4}
d.update({5:6})
# d[5] = int(input("5: ")) para o usuário digitar

print(d)


# 8- Escreva um programa que concatene os dicionários abaixo e crie um novo.
# Exemplo dicionário(Dict):
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}'''
# Resultado esperado: {1: 10, 2: 20, 3: 30, 4:40, 5:50, 6: 60}

dicio1 = {"oi": "tchau", "quente": "frio"}
dicio2 = {"top": "bom", "gostei": "curti"}

dicio = {}
dicio.update(dicio1)
dicio.update(dicio2)

print(dicio)


# 9- Escreva um programa que leia chaves e valores, crie um dicionário, e depois, verifique se uma chave informada existe em um dicionário.

dcv = {}

print("Em extenso.")
dcv[1] = input("1: ")
dcv[2] = input("2: ")
dcv[3] = input("3: ")

k = int(input("Digite a chave que quer verificar: "))

print(dcv)

if k in dcv:
    print("Esta chave existe")
else:
    print("Esta chave não existe")


# 10- Escreva um programa que itere em um dicionário utilizando loops.

dicio = {
    "claro": "escuro",
    "ruido": "silencio"
}

for key, value in dicio.items():
    print(f"{key} = {value}")


# 11- Escreva um programa que remova itens duplicados de uma lista.

listaUsuario = []

q = int(input("Quantos itens adiocionará na lista? "))

for item in range(q):
    listaUsuario.append(input("Adicionar item: "))
    
tirarDuplicados = []
for item in listaUsuario:
    if item not in tirarDuplicados:
        tirarDuplicados.append(item)
        
print(f'''Lista digitada: {listaUsuario}
Lista sem os duplicados: {tirarDuplicados}''')


# 12- Escreva um programa que verifique se uma lista está vazia ou não.

while True:

    listaVerificar1 = []
    listaVerificar2 = [3, 4, 7]

    lista = input("Qual lista você quer verificar? 1 ou 2: ")
    if lista == "1":
        if not listaVerificar1:
            print("Lista vazia!")
        else:
            print("Lista não vazia!")
        break
    elif lista == "2":
        if not listaVerificar2:
            print("Lista vazia!")
        else:
            print("Lista não vazia!")
        break
    else:
        print("Por favor, digite 1 ou 2!")
        
print(f'''Lista 1: {listaVerificar1}
Lista 2: {listaVerificar2}''')


# 13- Escreva um programa que clone ou copie uma lista.

lista1 = []
print("Adicione 5 itens na lista.")
for item in range(5):
    lista1.append(input("Adicionar item: "))

lista2 = lista1.copy()

print("Clonamos a lista, adicione dois itens a lista 2.")
for i in range(2):
    lista2.append(input("Adicionar item: "))

print(f'''Lista 1: {lista1}
Lista 2: {lista2}''')
