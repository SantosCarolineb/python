#1-Faça um Programa que peça dois números e imprima o maior deles.
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
if a > b:
    print(f'O maior número é {a}')
elif a < b:
    print(f'O maior número é {b}')
elif a==b:
    print('Eles são iguais')

#2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
c = int(input('Digite um número: '))
if c < 0:
    print('O número informado é negativo!')
else:
    print('O número informado é positivo!')

#3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino M - Masculino, Sexo Inválido.
sexo = input('Informe seu sexo (digite F ou M): ')
if sexo == 'M' or sexo == 'm':
    print('Sexo masculino')
elif sexo == 'F' or sexo == 'f':
    print('Sexo feminino')
else:
    print('Sexo inválido')

#4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
if letra == 'A' or letra == 'a' or letra == 'E' or letra == 'e' or letra == 'I' or letra == 'i' or letra == 'O' or letra == 'o' or letra == 'U' or letra == 'u':
    print('É uma vogal!')
else:
    print('É uma consoante!')

#5-Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar: A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete; A mensagem “Reprovado”, se a média for menor do que sete. A mensagem “Aprovado com Distinção”, se a média for igual a dez.”
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota = nota1+nota2
media = nota/2
if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distinção')

#6-Faça um Programa que leia três números e mostre o maior e o menor deles.
lista1, maiorv, menorv = [], 0, 0

print('Digite três números')
for n in range(0, 3):
    lista1.append(int(input('Digite aqui: ')))
    if n == 0:
        maiorv = menorv = lista1[n]
    else:
        if lista1[n] > maiorv:
            maiorv = lista1[n]
        if lista1[n] < menorv:
            menorv = lista1[n]

print(f'''
    Valores: {lista1}
    Maior valor: {maiorv}
    Menor valor: {menorv}
''')

#7-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
lista2, menorpreco = [], 0

print('Informe o preço dos três produtos')
for p in range(0, 3):
    lista2.append(float(input(f'Preço do produto {p+1}: ')))

    if p == 0:
        menorpreco = lista2[p]
    elif lista2[p] < menorpreco:
        menorpreco = lista2[p]

for produto, preco in enumerate(lista2):
    if preco == menorpreco:
        print(f'Você deve comprar o produto {produto+1} que custa {preco}')

#8-Faça um Programa que leia três números e mostre-os em ordem decrescente
lista3 = []

print('Veja ordem decrescente de três números')
for num in range(0, 3):
    lista3.append(int(input('Digite aqui: ')))
    
print(sorted(lista3, reverse=True))

#9-Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso
turno = input('''Informe em que turno você estuda:
M- Matutino
V- Vespertino
N- Noturno

Digite aqui: ''')

if turno == 'M' or turno == 'm':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite!')
else:
    print('Valor inválido!')

#10-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
 
#Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Informe seu salário: '))

if salario > 0 and salario <= 280:
    aumento = salario * 0.2
    percentual = '20%'
    
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    percentual = '15%'
    
elif salario > 700 and salario < 1500:
    aumento = salario * 0.1
    percentual = '10%'
    
elif salario >= 1500:
    aumento = salario * 0.05
    percentual = '5%'


reajuste = salario + aumento

print(f'''Seu salário foi reajustado! Confira abaixo:
    Valor do salário antes do ajuste: {salario}
    Percentual aplicado: {percentual}
    Valor do aumento: {aumento}
    Valor do salário reajustado: {reajuste}''')

#11-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20%

# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

valor_hora = float(input('Informe quanto ganha por hora: '))
horas = int(input('Informe quantidade de horas trabalhadas: '))
sa_bruto = valor_hora * horas

#Calcular desconto IR **%
if sa_bruto <= 900:
    perc_desconto = '(isento)'
    ir = 0
elif sa_bruto > 900 and sa_bruto <= 1500:
    perc_desconto = '(5%)'
    ir = sa_bruto * 0.05
elif sa_bruto > 1500 and sa_bruto <= 2500:
    perc_desconto = '(10%)'
    ir = sa_bruto * 0.1
elif sa_bruto > 2500:
    perc_desconto = '(20%)'
    ir = sa_bruto * 0.2

#Calcular desconto Sindicato 3%
sindicato = sa_bruto * 0.03

#Calcular FGTS 11%
fgts = sa_bruto * 0.11

#Calcular total de desconto
tot_desconto = ir + sindicato

#Calcular o salario liquido
sa_liquido = sa_bruto - tot_desconto

print(f'''
Salário bruto: R${sa_bruto}
Desconto IR {perc_desconto}: R${ir}
Desconto sindicato: R${sindicato}
FGTS: R${fgts}

Total de descontos: R${tot_desconto}
Salário líquido: R${sa_liquido}
''')

# 12-Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

pos = int(input('Digite um número de 1 a 7: ')) - 1

dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

print(dias[pos])

#13-Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
# Média de Aproveitamento Conceito 
# Entre 9.0 e 10.0 A 
# Entre 7.5 e 9.0 B 
# Entre 6.0 e 7.5 C 
# Entre 4.0 e 6.0 D 
# Entre 4.0 e zero E 
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print('Informe suas notas')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

#calcular media das notas
soma_nts = n1 + n2
media_nts = soma_nts/2

#atribuir conceitos ABCDE (if)
if media_nts > 9 and media_nts <= 10:
    conceito = 'A'
elif media_nts > 7.5 and media_nts <= 9:
    conceito = 'B'
elif media_nts > 6 and media_nts <= 7.5:
    conceito = 'C'
elif media_nts > 4 and media_nts <= 6:
    conceito = 'D'
elif media_nts <= 4:
    conceito = 'E'

#aprovado ou nao
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    condicao = 'Aprovado!'
elif conceito == 'D' or conceito == 'E':
    condicao = 'Reprovado!'

# as notas, a média, o conceito e a mensagem “APROVADO”  ou  “REPROVADO” 

print(f'''
Suas notas são: {n1} e {n2}
Sua média é de: {media_nts}
Conceito atribuído: {conceito}
Condição: {condicao}
''')

# 14-Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

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



# 15-Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c 



 

# 16-Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 





# 17-Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

 



# 18-Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo


