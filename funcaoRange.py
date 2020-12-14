#função Range imprimi Array a partir de um valor

print (range(10))
print (range(5,10))
print (range(10,0))

i = int(input('Digite um numero: '))

if i in range(0,10):
    print('Esta contido')
else:
    print('Não esta contido')