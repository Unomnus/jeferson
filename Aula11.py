nome = str(input('Nome completo: ')).strip()
num = int(input('Digite um número entre 0 a 9999: '))
cidade = input('Digite o nome da sua cidade: ').strip()
frase = input('Digite uma frase: ')
name = input('Digite o seu nome: ').strip()

print('===== primeiro exercício =====')

print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(nome.find(' ')))

print('===== segundo exercício =====')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('unidade de: {}'.format(num[u]))
print('dezena de: {}'.format(num[d]))
print('centena de: {}'.format(num[c]))
print('milhar de: {}'.format(num[m]))

print('===== terceiro exercício =====')

print('A cidade começa com "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))

print('===== quarto exercício =====')

print('Quantas vezes a letra "A" aparece na frase? {}'.format(frase.upper().count('A')))
print('Em que posição a letra "A" aparece pela primeira vez? {}'.format(frase.upper().find('A') + 1))
print('Em que posição a letra "A" aparece pela última vez? {}'.format(frase.upper().rfind('A') + 1))

print('===== quinto exercício =====')

n = name.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n) - 1]))