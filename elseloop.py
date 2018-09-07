#!/usr/bin/python3

nomes = ['daniel', 'caio', 'maria']

busca = input('Digite um nome: ')

for nome in nomes:
    if nome == busca.strip().lower():
        print('Achei')
        break
else:
    print('Não achei')

