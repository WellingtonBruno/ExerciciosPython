#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes apareace a letra "A".
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite um frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.upper().find('A')+1)) # atribui +1 na string retirando a posição 0
print('A útima letra A aparece na posição {}'.format(frase.upper().rfind('A')+1))