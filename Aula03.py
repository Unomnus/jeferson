altura = int(input('Altura: '))
largura = int(input('Largura: '))
valor = float(input('Preço R$'))
wage = float(input('Salário R$'))
metroq = altura * largura
tinta = metroq / 2
print('A parede tem {} metros quadrados e precisa de {} litros de tinta.'.format(metroq, tinta))
print('O valor da tinta com desconto de cinco por cento é de R${:.2f}'.format(valor - (valor * 0.05)))
print('O novo aumento de quinze reais fica R${:.2f}'.format((wage * 0.15) + wage))