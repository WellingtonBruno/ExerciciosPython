#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
#Calcule e mostre o comprimento da hipotenusa
import math
ca = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(ca, ad)
print('A hipotenusa vai medir {:.2f}'.format(hi))


#ca = float(input('Digite o comprimento do cateto oposto: '))
#ad = float(input('Digite o comprimento do cateto adjacente: '))
#hi = (ca ** 2 + ad ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))