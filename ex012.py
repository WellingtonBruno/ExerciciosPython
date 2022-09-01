#Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n1 = float(input('Digite o preço do produto: '))
d = n1*0.05
r = n1-d
print("O valor do Produto é: R${}, com um desconto de 5% sai por: R${}".format(n1,r))