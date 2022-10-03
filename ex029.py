#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7 por cada Km acima do limite

n1 = int(input('Digite a velocidade do carro: '))
if n1>80:
    print('Seu carro foi Multado, sua velocidade é {} Km/h'.format(n1))
    print('A multa tem um adicional de R$7,00 por cada Km acima do limite')
else:
    print('Dentro do limite de velocidade')
