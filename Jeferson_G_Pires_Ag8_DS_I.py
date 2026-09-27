# Inicialização dos contadores
qtd_excelente = 0
qtd_ruim = 0

print("=== Pesquisa de Satisfação - TudoWeb ===")

# Estrutura de repetição para 10 entrevistados
for i in range(1, 11):
    print(f"\nEntrevistado nº {i}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Validação da opinião do entrevistado
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opcao = int(input("Opção escolhida (1, 2 ou 3): "))
        
        # Estrutura de decisão para contabilizar os votos
        if opcao == 1:
            qtd_excelente += 1
            break
        elif opcao == 2:
            break
        elif opcao == 3:
            qtd_ruim += 1
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.\n")

# Exibição do relatório final
print("\n" + "="*35)
print("     RESULTADO DA PESQUISA")
print("="*35)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")