#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127 , O númeor 6.127 tem a parte inteira 6.

import math
n1 = float(input('Digite um número: '))
print('O valor inteiro é:{}'.format(math.trunc(n1)))

