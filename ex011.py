#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessaria para pinta-la, sabendo que cada litro de tinta pintta uma área de 2m²

n1 = float(input('Digite a altura: '))
n2 = float(input('Digite a largura: '))
m = (n1*n2)/2
print("Você vai precisar de {} litros de tinta para pintar ".format(m))
