from colorama import Fore, Style, init

# Inicializa o colorama para garantir a compatibilidade com o terminal
init()

# 1. Armazenando os níveis, situações e cores correspondentes em uma lista de dicionários
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def exibir_alerta(nivel_informado):
  """Função responsável por definir e exibir a cor da mensagem

  conforme o nível informado do reservatório.
  """
  # Busca o nível correspondente na lista
  dado_nivel = next(
      (item for item in niveis_reservatorio if item["nivel"] == nivel_informado),
      None,
  )

  if dado_nivel:
    cor = dado_nivel["cor"]
    situacao = dado_nivel["situacao"]

    # Exibe no terminal a situação atual com a cor correspondente
    print(f"{cor}[ALERTA] Nível {dado_nivel['nivel']} - Situação: {situacao}")

    # Restaura o estilo padrão do terminal após a exibição
    print(Style.RESET_ALL, end="")
  else:
    print(f"{Fore.RED}Nível inválido informado!{Style.RESET_ALL}")


def simular_sistema():
  print("========================================")
  print("   MONITORAMENTO DE RESERVATÓRIO DE ÁGUA  ")
  print("========================================\n")

  # Simulação com valores definidos no código (sem entrada do usuário)
  leituras_simuladas = [1, 2, 3, 4, 5, 2, 1]

  for idx, leitura in enumerate(leituras_simuladas, start=1):
    print(f"Leitura #{idx} do sensor:")
    exibir_alerta(leitura)
    print("-" * 40)


if __name__ == "__main__":
  simular_sistema()