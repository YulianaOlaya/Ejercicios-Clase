"""
Mi tercer programa
------------------

Ingrese un entero y se imprime de 0 a ese n
"25"


Ejemplo:
-------

Entrada:
6
15
30

Salida:
0 1 2 3 4 5 6
0 1 2 3 4, ....13 14 15
0 1 2 3 4 5 6, ..... 28 29 30
"""

n = int(input(""))
if n >=0: 
  for i in range(n+1):
    print(i)

else:
  for i in range(n,1):
   print(i)