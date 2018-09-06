#!/usr/bin/python3 

notas = int(input('Digite aqui o nume de notas: '))

soma = 0
for x in range (notas):
    nota = int(input('Digite n {}'.format(x+1)))
    soma += nota
media = soma / notas

