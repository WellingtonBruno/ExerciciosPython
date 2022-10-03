#Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou impar

n1 = int(input('Digite um número: '))
resto = n1 % 2
if resto == 0:
    print('O número é PAR!')
else:
    print('O número é IMPAR')