numero1 = int(input('Digite um numero'))
numero2 = int(input('Digite outro numero'))

if numero1 == 1:
    print('Numero1 é igual a 1')

elif numero1 == 2 or numero2 == 3:
    print('Numero1 é diferente de 1 ou Numero2 é diferente de 2')

elif numero1 >= 1000 or numero2 <= -1000:
    print('Numero1 é maior que 1000 ou Numero2 é menos que -1000')

else:
    print('Todas as alternativas incorretas')