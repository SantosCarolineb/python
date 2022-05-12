#FAÇA UM PROGRAMA QUE...

#1- mostre a mensagem "Alo mundo" na tela
print('Alo mundo')

#2- peça um número e então mostre a mensagem O número informado foi [número]
a = input('Digite um número: ')
print('O número informado foi: ', a)

#3- peça dois números e imprima a soma
print('Digite dois valores para somar')
b = int(input('Primeiro valor: '))
c = int(input('Segundo valor: '))
print('O resultado é: ', b+c)

#4- peça as 4 notas bimestrais e mostre a média
print('Digite suas notas e descubra sua média!')
d = int(input('Primeira nota: '))
e = int(input('Segunda nota: '))
f = int(input('Terceira nota: '))
g = int(input('Quarta nota: '))

somaNotas = d+e+f+g
mediaNotas = somaNotas/4

print('Sua média é de: ', mediaNotas)

#5- converta metros para centímetros
print('Conversão de metros para centímetros')
h = int(input('Digite um valor em metros: '))
hh = h*100
print(h, 'metro(s) equivalem a', hh, 'centímetros')

#6- peça o raio de um círculo, calcule e mostre sua área.
print('Área do círculo')
r = float(input('Informe o raio: '))
pi = 3.14

print('A área é: ', r*r*pi)

#7- calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
print('Área de um quadrado')
l = float(input('Informe a medida de um lado do quadrado: '))
aq = l*l
daq = aq*2

print('O quadrado tem área', aq, ', cujo dobro é', daq)


