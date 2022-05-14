# 1- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe quanto ganha por hora: "))
qtd_hora = int(input("Informe quantas horas trabalhou no mês: "))
print(f"Salário do mês: {valor_hora * qtd_hora}")


# 2- Faça um Programa que peça dois números e imprima a soma.

print("Soma de dois números")

n1 = float(input("Digite um némuro: "))
n2 = float(input("Digite um némuro: "))

print(f"A soma é {n1 + n2}")


# 3- Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Insira suas quatra notas e receba a média")

notas = []
for nota in range(0, 4):
    notas.append(float(input("Insira aqui: ")))
    
def soma_total(notas):
    resultado = 0
    for nota in notas:
        resultado = resultado + nota
    return resultado
    
resultado = soma_total(notas)
media = resultado/4

print(f"Sua média é de: {media}")


# 4- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# o produto do dobro do primeiro com metade do segundo .

# a soma do triplo do primeiro com o terceiro.

# o terceiro elevado ao cubo.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Agora um número real: "))

import math

dobro1 = num1 * 2
metade2 = num2/2
triplo1 = num1 * 3

print(f'''
O produto do dobro do primeiro com metade do segundo: {dobro1*metade2}
A soma do triplo do primeiro com o terceiro: {triplo1+num3}
O terceiro elevado ao cubo: {num3**3}
''')


# 5- Faça um Programa que peça dois números e imprima o maior deles.

numeros, maiorn = [], 0

print("Digite dois números")

for n in range(0, 2):
    numeros.append(float(input("Digite aqui: ")))
    if n == 0:
        maiorn = numeros[n]
    elif numeros[n] > maiorn:
        maiorn = numeros[n]

print(f"Você digitou os valores: {numeros}, o maior deles é {maiorn}")


# 6- Faça um Programa que leia três números e mostre o maior deles.

numeros, maiorn = [], 0

print("Digite dois números")

for n in range(0, 3):
    numeros.append(float(input("Digite aqui: ")))
    if n == 0:
        maiorn = numeros[n]
    elif numeros[n] > maiorn:
        maiorn = numeros[n]

print(f"Você digitou os valores: {numeros}, o maior deles é {maiorn}")


# 7- Faça um Programa que leia três números e mostre o maior e o menor deles.

numeros, maiorn, menorn = [], 0, 0

print("Digite dois números")

for n in range(0, 3):
    numeros.append(float(input("Digite aqui: ")))
    if n == 0:
        maiorn = menorn = numeros[n]
    elif numeros[n] > maiorn:
        maiorn = numeros[n]
    elif numeros[n] < menorn:
        menorn = numeros[n]

print(f"Você digitou os valores: {numeros}, o maior deles é {maiorn} e menor é {menorn}")


# 8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

lista, menorpreco = [], 0

print("Informe o preço dos três produtos")
for p in range(0, 3):
    lista.append(float(input(f"Preço do produto {p+1}: ")))

    if p == 0:
        menorpreco = lista[p]
    elif lista[p] < menorpreco:
        menorpreco = lista[p]

for produto, preco in enumerate(lista):
    if preco == menorpreco:
        print(f"Você deve comprar o produto {produto+1} que custa {preco}")


# 9- Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

print('Veja ordem decrescente de três números')
for num in range(0, 3):
    lista.append(int(input('Digite aqui: ')))
    
print(sorted(lista, reverse=True))


# 10- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

print("Descubra qual é o triângulo informando a medida dos lados")

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

l1l2 = lado1+lado2

if l1l2 > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 != lado2:
        if lado3 == lado1 or lado3 == lado2:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    elif lado1 != lado3:
        if lado2 == lado1 or lado2 == lado3:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    elif lado2 != lado3:
        if lado1 == lado2 or lado1 == lado3:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")

else:
    print("Não é um triângulo!")
