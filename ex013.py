#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento

n = float(input('Digite seu salário R$ '))
f = (n*0.15)+n
print('Seu salário é R$ {}, com aumento de 15% ficou R$ {}'.format(n, f))