"""
Mi Segundo programa
------------------

Ingrese un entero y se imprime de 1 a ese n
"25"


Ejemplo:
-------

Entrada:
5
40
10

Salida:
1 2 3 4 5
1 2 3 4, .... 38 39 40
1 2 3, .... 8 9 10
"""

n = int(input(""))
for i in range(1,n+1):
  print(i)