import random

nome = input('Digite seu nome: ')

if nome == 'Jeferson':
    print('Que nome bonito!')
    else:
    print('Seu nome é tão normal!')
    print('Bom dia, {}'.format(nome))

print('========== GAME ==========')

print('Vamos jogar um jogo de adivinhação!')
print('Estou pensando em um número entre 1 e 10. Tente adivinhar!')
numero_secreto = random.randint(1, 10)
print('pensando...')
jogador = int(input('Digite o seu palpite: '))
if jogador == numero_secreto:
    print('Parabéns, {}! Você acertou o número secreto!'.format(nome))
    else:
    print('Que pena, {}! Você errou. O número secreto era {}.'.format(nome, numero_secreto))

print('========== VELOCIDADE E MULTA ==========')

velocidade = float(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    print('Você foi multado! A velocidade máxima permitida é 80 km/h.')
    multa = (velocidade - 80) * 7
    print('O valor da multa é: R$ {:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade. Dirija com segurança!')

print('========== PAR OU ÍMPAR ==========')

print('Vamos jogar um jogo de par ou ímpar!')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))

print('========== VIAGEM E VALORES ==========')

print('Vamos calcular o valor da viagem!')
distancia = float(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('O valor da viagem é: R$ {:.2f}'.format(valor))

print('========== ANÁLISE DE ANO BISSEXTO ==========')

ano = int(input('Digite um ano para verificar se é bissexto: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))  

print('========== O MENOR E O MAIOR ENTRE TRÊS NÚMEROS ==========')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))

print('========== AUMENTO NO SALÁRIO ==========')

salario = float(input('Digite o salário atual: '))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

print('O aumento no salário será de: R$ {:.2f}'.format(aumento))

print(========== TRÊS RETAS PARA UM TRIÂGULO ==========)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
