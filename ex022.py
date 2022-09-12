#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúculas.
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome: ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #nome.count(' ') para eliminar espaços
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))