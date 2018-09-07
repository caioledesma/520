#!/usr/bin/python3 

try:
    notas = int(input('Digite aqui o numero de notas: '))
except Exception as e:
    print('ERROU MIZERAVI!!!')
    exit()

soma = 0 
for x in range (notas):
    nota = int(input('Digite a {}ª nota:'.format(x+1)))
    soma += nota
    media = soma / notas


# saida
if media >= 7:
    print('Media {}, aprovado'.format(media))
elif media > 3:
    print('Media {}, recuperação'.format(media))
else:
    print('Media {}, reprovado'.format(media))
