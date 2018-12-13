# Função Sort

lista = [1, 5, 4, 3, 2]
print('Lista bagunçada: {}\n'.format(lista) )

#Forma crescente
lista.sort()
print('Lista em ordem crescente: {}\n'.format(lista))

# Forma decrescente
lista = [1, 5, 4, 3, 2]
lista.sort(reverse= True)
print('Lista de forma decrescente: {}'.format(lista))

print('Listas mais complexas\n')

lista = [{'Nome': 'Maria', 'Idade': 32}, {'Nome': 'João', 'Idade': 23}, {'Nome': 'André', 'Idade': 45}, {'Nome': 'Paula', 'Idade': 27}]

def compara_idade(x):
    return (x['Idade'])

idade = lista.sort(key=compara_idade)
print('Lista com idade comparada \n{}'.format(idade))


