# 1. Definições de Funções e Procedimentos
# Foram criadas quatro funções: calcular_media, verificar_status, coletar_dados_alunos e gerar_relatorio.

# Função para calcular a média de duas notas
def calcular_media(nota1, nota2): #
    return (nota1 + nota2) / 2

# Função para verificar o status do aluno com base na média
def verificar_status(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Função para coletar dados dos alunos
def coletar_dados_alunos(qtd):
    lista_alunos = [] # Cria uma lista vazia para armazenar os dados dos alunos em uma matriz de dicionários
    for i in range(qtd): # Os dados de cada aluno são coletados em um loop que se repete a quantidade de vezes especificada pelo usuário
        print(f"\n--- Aluno {i + 1} ---")
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
# Calcula a média e o status do aluno
        media = calcular_media(nota1, nota2)
        status = verificar_status(media)
# Cria um dicionário para armazenar os dados do aluno e adiciona à lista
        aluno = {"nome": nome, "media": media, "status": status}
        lista_alunos.append(aluno) # comando append adiciona o dicionário do aluno à lista de alunos

    return lista_alunos

# Função para gerar o relatório de desempenho dos alunos
def gerar_relatorio(lista_alunos):
    print("\n" + "=" * 30)
    print("       RELATÓRIO DE DESEMPENHO")
    print("=" * 30)
# Exibe os dados de cada aluno e calcula a soma das médias
    soma_medias = 0
    for aluno in lista_alunos: # Exibe os dados de cada aluno e calcula a soma das médias
        print(f"Nome: {aluno['nome']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Status: {aluno['status']}")
        print("-" * 30)
        soma_medias += aluno['media']
# Calcula e exibe a média geral da turma
    if len(lista_alunos) > 0: # Calcula a média geral da turma apenas se houver alunos cadastrados
        media_turma = soma_medias / len(lista_alunos)
        print(f"Média geral da turma: {media_turma:.2f}")

# 2. Bloco Principal (Onde o programa realmente começa a rodar)
qtd_alunos = int(input("Digite a quantidade de alunos: "))

# Executa a coleta e guarda os dados estruturados
alunos_cadastrados = coletar_dados_alunos(qtd_alunos)

# Executa o relatório passando os dados coletados
gerar_relatorio(alunos_cadastrados)