import random
dias = float(input('Dias: '))
km_round = float(input('Kilometros Rodados: '))
num = random.randint(1, 10)
valor = (60*dias)+(km_round*0.15)
print(f'Total: R${valor:.2f}')
print(num)