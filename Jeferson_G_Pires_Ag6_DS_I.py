print('========= DESCONTO EM COMPRAS =========')

valor = int(input('Digite o valor pago R$'))
if valor < 200:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print(f'Valor final com desconto de 5% foi R${valor_final:.2f}')
elif valor >= 200 and valor < 300:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f'Valor final com desconto de 10% foi R${valor_final:.2f}')
elif valor >= 300:
    desconto = valor * 0.15
    valor_final = valor - desconto
    print(f'Valor final com desconto de 15% foi R${valor_final:.2f}')

print('========= FIM =========')