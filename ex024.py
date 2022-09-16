#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

nome = str(input('Digite o nome da sua cidade: ')).strip()
print(nome[:5].upper() =='SANTO')


