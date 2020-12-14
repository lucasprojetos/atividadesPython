pessoas = []

pessoas.append ('Pessoa 1')
pessoas.append ('Pessoa 2')
pessoas.append ('Pessoa 3')
pessoas.append ('Pessoa 4')

print('Tenho ', len(pessoas), 'Pessoas')

pessoas.sort()

print('São eles: ')

print(pessoas)

print('A primeira pessoa é o ', pessoas[0])

pessoas.remove('Pessoa 1'); #a função remove retira itens da lista

print ("Agora tenho somente ", len(pessoas)," Pessoas")

print ("Sao eles:")

for pessoa in pessoas:
    
print (pessoas)
