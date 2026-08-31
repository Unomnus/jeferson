print('=====ENEL + AMIGA=====')
print('Cálculo do consumo mensal de energia elétrica')
nome = input('Aparelho elétrico-eletrônico: ')
potency = float(input('Digite a potência em watts (W): '))
horasDia = float(input('Digite o tempo de uso em horas (h): '))
monthlyConsumption = (potency * horasDia * 30) / 1000
valor = 0.75 * monthlyConsumption
print('O consumo mensal do aparelho {} é de {:.2f} kWh'.format(nome, monthlyConsumption))
print('O valor a ser pago é de R$ {:.2f}'.format(valor))