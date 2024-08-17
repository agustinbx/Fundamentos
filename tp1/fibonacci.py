# FIBONACCI
"""
0 = 0
1 = 1
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
"""
aux = input("Escribe tu nombre:")
print(f"hola {aux}, te mostraremos la sucesion de Fibonacci")

x = 0
y = 1
for i in range(0,19):
    print(x)
    aux = x + y
    x = y
    y = aux
