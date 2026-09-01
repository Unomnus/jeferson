print('====BEM VINDO A VIAGEM ESPACIAL====')
nome = input('Nome: ')
distance = float(input('Distância em kilometros: '))
speed = float(input('Velocidade em km\h: '))
kmh = distance/speed
tempodias = kmh/24
print('Astronauta {:=^20}, bem vindo à bordo!'.format(nome))
print('Sua viagem tem uma distância de {}km com uma velocidade média de {}km/h.'.format(distance, speed))
print('Com um tempo estimado em {:.2f} horas ou {:.2f} dias. Boa sorte.'.format(kmh, tempodias))
print('==========FIM==========')