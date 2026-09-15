print('========== Consumo de água ==========')

property = input('Escola o tipo da propriedade: ')
consumo = float(input('Informe o consumo de água em m³: '))
def calcular_valor(consumo):
    match property:
        case 1:
            print("Comercial")
        case 2:
            print("Casa")
        case 3:
            print("Apartamento")
        case _:
            print("Tipo de propriedade inválido")

calcular_valor(consumo)