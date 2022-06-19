# 1- Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro.

def find_maiorn(ls):
    maiorn = 0
    for n in ls:
        if n == 0:
            maiorn = n
        elif n > maiorn:
            maiorn = n
    return maiorn


numeros = []
print("Digite cinco números")
for n in range(0, 5):
    numeros.append(int(input("Número: ")))

maiorn = find_maiorn(numeros)

print(f"Valores digitados: {numeros}, o maior deles é {maiorn}")

# 2- Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro.

def soma_total(ls):
    resultado = 0
    for n in ls:
        resultado = resultado + n
    return resultado
    
numeros = []
q = int(input("Quantos valores deseja somar? "))
for n in range(q):
    numeros.append(int(input("Valor: ")))
    
soma = soma_total(numeros)

print(f"A soma de todos os números digitados é: {soma}")

# 3- Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.

def multiplica(ls):
    resultado = 1
    for n in ls:
        resultado = resultado * n
    return resultado
    
numeros = []
q = int(input("Quantos valores deseja multiplicar? "))
for n in range(q):
    numeros.append(int(input("Valor: ")))
    
mult_result = multiplica(numeros)

print(f"O resultado final da multiplicação é: {mult_result}")

# 4- Escreva um programa que execute uma função que retorne o inverso de uma string passada por parâmetro.

def inverte(texto):
    return texto[::-1]

tx = input("Digite algo para ver invertido: ")

print(inverte(tx))

# 5- Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro.

def calcFatorial(n):
    r = 1
    while n >= 1:
        r = n*r
        n = n-1
    return r
        
    

n = int(input("Digite um número para calcular seu fatorial: "))

if n >= 1:
    resultado = calcFatorial(n)
    print(f"O fatorial é: {resultado}")
else:
    print("Erro! O número deve ser maior ou igual a 1!")

# 6- Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final, chame outra função para imprimir o resultado.

def contarQtd(texto):
    maiuc = 0
    minusc = 0
    for letra in texto:
        if letra.isupper():
            maiuc += 1
        elif letra.islower():
            minusc += 1
    return maiuc, minusc
        

def mostrarQtd():
    print(f"A quantidade de letras maiúsculas é {maiuc} e a quantidade de letras minúsculas é {minusc}.")


texto = input("Digite uma palavra ou frase e verifique quantas letras maiúsculas e minúsculas: ")

maiuc, minusc = contarQtd(texto)
mostrarQtd()

# 7- Escreva um programa Python que execute uma string que contenha um código Python

# forma simples:
codigo = '''print("Hey! Olá!")'''
exec(codigo)

# usuário digita o cod:
codigo = input("Digite uma linha de código python para treinar! ")
exec(codigo)

# usando função
def executarCod(tx):
    exec(tx)

codigo = '''print("Hey! Olá!")'''

executarCod(codigo)

# 8- Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não.

def numPrimo(n):
    p = "é"
    np = "não é"
    if n in [2, 3]:
        return p
    if n % 2 == 0:
        return np
    r = 3
    while r * r <= n:
        if n % r == 0:
            return np
        r += 2
    return p
    

num = int(input("Digite um número e descubra se ele é primo: "))

if num >= 1:
    print(f"O número {num} {numPrimo(num)} primo")    
else:
    print("Erro! O número deve ser maior ou igual a 1!")

# 9- Escreva um programa que execute uma função que valide se o número informado é um número perfeito ou não.

# 10- Escreva uma função que imprima as primeiras n linhas do triângulo de pascal.
