#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
n1 = (int(input('Tente adivinhar o número que o computador está pensando entre 0 á 5: ')))
d = random.randint(0, 5)
print('O número do computador é {}'.format(d))

if d == n1:
    print('Você Venceu!!')
else:
    print('Você Perdeu!!!')

#print('O número do computador é {}'.format(random.randint(0, 5)))
