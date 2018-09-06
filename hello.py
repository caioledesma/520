#!/usr/bin/python3
#nome = 'Caio'
#sobrenome = 'Ledesma'
#print(nome,sobrenome, sep=':', end='\n\n\n')

#nome = input ('Digite seu nome: ')

#print('Seja bem vindo', nome)

#Aqui é onde vem as entradas de informação
nota1 = int(input('Digite aqui a nota 1: '))
nota2 = int(input('Digite aqui a nota 2: '))

# aqui é o processamento da média 
media = (nota1 + nota2) / 2

# aqui é onde vão as condições e o bloco de saída
if media >= 7:
    print('Media {}, Aprovado'.format(media))
elif media > 3:
    print('Media {}, Recuperacao'.format(media))
else: 
    print('Media {}, Reprovado'.format(media))





