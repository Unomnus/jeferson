print("==== EXERCÍCIOS CATETOS ====")

catopos = float(input('Cateto oposto: '))
catadja = float(input('Cateto adjacente: '))
hipotenusa = (catopos ** 2 + catadja ** 2) ** (1/2)
print(f'Hipotenusa: {hipotenusa:.2f}')

print("========== FIM ==========")
