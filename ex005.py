#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n1 = int(input('Digiter um número: '))
s = (n1+1)
a = (n1-1)
print('O sucessor do número {} é {} e o antecessor é {}' .format(n1, s, a))