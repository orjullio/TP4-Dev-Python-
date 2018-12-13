lista = [1, 5, 4, 3, 2]

lista.sort()
print('Lista ordenada: {}\n'.format(lista))

lista.sort(reverse=True)
print('Lista no modo reverso: {}\n'.format(lista))

tupla = [{'Nome': 'João', 'Idade': 23}, {'Nome': 'Paula', 'Idade': 27}, {'Nome': 'Maria', 'Idade': 32},
         {'Nome': 'André', 'Idade': 45}]

def comp_idade(x):
    return(x['Idade'])

tupla.sort(key=comp_idade)
print('Tupla: {}'.format(tupla))



