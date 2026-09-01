# === PROGRAMA DE CÁLCULO DE VIAGEM ESPACIAL ===

# Boas-vindas
print("==== BEM-VINDO À VIAGEM ESPACIAL ====")

# Coleta de dados do astronauta
nome = input("Nome: ")
distancia = float(input("Distância em quilômetros (km): "))
velocidade = float(input("Velocidade média (km/h): "))

# Cálculos
tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

# Exibição dos resultados formatados
print(f"\nAstronauta {nome:=^20}, bem-vindo a bordo!")
print(
    f"Sua viagem tem uma distância de {distancia:,.1f} km a uma velocidade de"
    f" {velocidade:,.1f} km/h."
)
print(
    f"Tempo estimado: {tempo_horas:.2f} horas (ou aproximadamente"
    f" {tempo_dias:.2f} dias). Boa sorte!"
)

print("========== FIM ==========")
