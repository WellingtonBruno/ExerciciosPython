#Um professor quer sortear um dos seus quatros alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido
import random
n1 = str(input('Digite um Nome: '))
n2 = str(input('Digite um Nome: '))
n3 = str(input('Digite um Nome: '))
n4 = str(input('Digite um Nome: '))
n5 = str(input('Digite um Nome: '))
lista = [n1, n2, n3, n4, n5] # [] cria uma lista
escolhido = random.choice(lista) #usar para sortear uma string []
print('O nome escolhido foi: {}'.format(escolhido))
