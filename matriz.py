
matriz = [
    [1, 3, 6],
    [3, 5, 7],
    [6, 9, 11]
]  

cont = 0
a = 0
b = 0
for x in matriz:
    print(x[cont])
    b += x[-(cont+1)]
    cont = cont +1

print(a + b)

