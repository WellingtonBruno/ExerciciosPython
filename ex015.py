#Escreva umprograma que pergunte a quantidade de KM percorridos por um carro alugado, e a quantidade de dias pelos quais ela foi alugado
#Calcule o preço a apagar , sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

d = float(input('Por quantos dias o carro foi alugado: '))
k = float(input('Quantos Km você andou com o carro: '))
custo = (60 * d) + (k * 0.15)
print('O valor a ser pago será de R$: {}'.format(custo))