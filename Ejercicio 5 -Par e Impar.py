"""
El Duelo de Pares e Impares
------------------

Haga un programa que reciba un entero e imprima PAR o IMPAR según corresponda.
"25"


Ejemplo:
-------

Entrada:
3
Entrada:
2
Entrada:
9

Salida:
Impar
Salida:
Par
Salida:
Impar
"""

n = int(input(""))
if n % 2 == 0:
  print("PAR")
else:
  print("IMPAR")