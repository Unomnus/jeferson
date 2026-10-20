print('========== CONTAGEM REGRESSIVA ==========')

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('========== FIM ==========')

print('========== NÚMEROS PARES ==========')

for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)

print('\n========== FIM ==========')

print('========== NÚMEROS ÍMPARES ==========')

for c in range(1, 501, 2):
    if c % 2 != 0:
        soma += c
    print(c, end=' ')
    sleep(0.5)
print('\nA soma de todos os números ímpares de 1 a 500 é:', soma)

print('\n========== FIM ==========')

print('========== TABUADA ==========')

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
    sleep(0.5)

print('========== FIM ==========')

print('========== SOMA DOS NÚMEROS PARES ==========')

soma = 0
for c in range(0, 7):
    if c % 2 == 0:
        soma += c
print('A soma dos números pares de 0 a 6 é:', soma)

print('========== FIM ==========')

print('========== PRIMEIRO TERMO E RAZÃO DE UMA PROGRASSÃO ARITMETICA ==========')

First_term = int(input('Digite o primeiro termo da PA: '))
Reason = int(input('Digite a razão da PA: '))

for c in range(First_term, First_term + (10 * Reason), Reason):
    print(c, end=' ')
    sleep(0.5)
    
print('\n========== FIM ==========')