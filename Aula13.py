print("=========== FINANCIAMENTO DE CASA POR EMPRÉSTIMO BANCÁRIO ===========")

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))

if valor_casa > (salario * 0.30):
    print('Empréstimo negado! O valor da prestação excede 30% do salário.')
else:
    print('Empréstimo aprovado! O valor da prestação está dentro do limite permitido.')

print('=========== FIM DO PROGRAMA ===========')

print("=========== CONVERSÃO DE NÚMERO INTEIRO PARA BINÁRIO, OCTAL E HEXADECIMAL ===========")

numero = int(input('Digite um número inteiro: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
 if numero < 0:
    print('Número inválido! Por favor, digite um número inteiro positivo.')
else:
    print(f'Número digitado: {numero}')
    print(f'Binário: {binario}')
    print(f'Octal: {octal}')
    print(f'Hexadecimal: {hexadecimal}')

print("=========== FIM DO PROGRAMA ===========")

print("=========== COMPARAÇÃO DE NÚMEROS ===========")

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que {num2}.')
elif num1 < num2:
    print(f'O número {num2} é maior que {num1}.')
else:
    print('Os números são iguais.')

print("=========== FIM DO PROGRAMA ===========")

print("=========== DATA DE NASCIMENTO PARA ALISTAMENTO MILITAR ===========")

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f'Você tem {idade} anos. Ainda faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos. Está na hora de se alistar!')
else:
    print(f'Você tem {idade} anos. Já passou do tempo de alistamento há {idade - 18} anos.')

print("=========== FIM DO PROGRAMA ===========")

print("=========== MÉDIA DE NOTAS ===========")

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Média: {media:.2f}. Situação: REPROVADO.')
elif 5.0 <= media < 7.0:
    print(f'Média: {media:.2f}. Situação: RECUPERAÇÃO.')
else:
    print(f'Média: {media:.2f}. Situação: APROVADO.')

print("=========== FIM DO PROGRAMA ===========")

print("=========== CATEGORIA DE ATLETAS DE ACORDO COM A IDADE ===========")

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento
if idade < 9:
    categoria = 'MIRIM'
elif 9 <= idade < 14:
    categoria = 'INFANTIL'
elif 14 <= idade < 19:
    categoria = 'JUNIOR'
elif 19 <= idade < 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos. Categoria: {categoria}.')

print("=========== FIM DO PROGRAMA ===========")

PRINT("=========== CÁLCULO DO IMC (Índice de Massa Corporal) ===========")

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    classificacao = 'Peso ideal'
elif 25 <= imc < 30:
    classificacao = 'Sobrepeso'
else:
    classificacao = 'Obesidade'

print(f'Seu IMC é {imc:.2f}. Classificação: {classificacao}.')

print("=========== FIM DO PROGRAMA ===========")

