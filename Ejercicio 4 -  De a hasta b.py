"""
Mi Cuarto programa
------------------

Ingrese 2 enteros a y b. Debe imprimir los numeros de a hasta b
"1 5"


Ejemplo:
-------

Entrada:
1 - 5
10 - 15 
30 - 40

Salida:
1 2 3 4 5
10 11 12 13 14 15
30 31 32 33, .....39 40

"""

a = int (input(""))
b = int (input(""))

for i in range(a,b+1):
  print(i)
