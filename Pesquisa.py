print('========== Pesquisa de Opnião de Atendimento ==========')

opnion = 0
while opnion < 50:
    print('Digite sua opnião de atendimento: ')
    print('1 - Excelente')
    print('2 - Bom')
    print('3 - Ruim')

    opnion = int(input('Digite sua opnião: '))

    if opnion == 1:
        print('Você escolheu Excelente!')
    elif opnion == 2:
        print('Você escolheu Bom!')
    elif opnion == 3:
        print('Você escolheu Ruim!')
    else:
        print('Opnião inválida! Digite um número entre 1 e 3.')