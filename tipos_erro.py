#!/usr/bin/python3

convidados = ['hugo', 'caio', 'luiz', 'daniel']

num = 0


try:
    convidado = int(input('Digite o numero do convidado: '))
    print(convidados[convidado -1])

except IndexError: 
    print('Este convidado não existe! A lista tem {} itens. Vc digitou {}'.format(len(convidados),convidado)

except ValueError:
    print('Digite somente números')

except Exception as f:
    print('Burro! {}'.format(e))
    




#print(len(convidados))

# if convidado in convidados:
#  print(convidado.index(convidados))

# lista convidados, quer um input o numero de um convidado, de 0 a X... - OK
# se ele digitar de um elemento da lista, devolvo o valor q ele digitou -OK
# se der um erro e ele colocar alguem q nao existe, eu trato o erro e printa pra ele, a lista tem X elementos e 
# vc tentou acessar um elemento que nao existe
