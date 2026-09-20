print('========== Consumo de água ==========')

# Programa de classificação de consumo de água

# 1. Solicita o tipo de imóvel
tipo_imovel = input('Digite o tipo de imóvel (comercial, casa ou apartamento): ').strip().lower()

# strip().lower(): Trata a entrada do texto para que digitações com letras maiúsculas ou espaços extras não afetem a validação (ex: "Apartamento " ou "CASA").

# 2. Solicita o consumo mensal em m³

    consumo = float(input("Informe o consumo mensal de água em m³ (ex: 15.5): "))

# 3. Classificação de acordo com as regras de negócio
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif tipo_imovel in ["apartamento", "casa"] and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    # Qualquer outro caso acima do limite residencial
    # (casa > 25 ou apartamento > 25)
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")