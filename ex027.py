#Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida
#o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).split()
print('É um prazer em te conhecer!!')
print('Seu primeiro é {}'.format(nome[0].title()))
print('Seu último nome é {}'.format(nome[len(nome)-1].title()))

#split utilizamos para transformar uma string em palavras (listas)
# utilizando o comando nome[len(nome)-1])) - ele verifica a ultima posição da lista