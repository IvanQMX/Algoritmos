from typing import List
import matplotlib.pyplot as plot
from time import time
import math
import os
import sys
sys.path.append( os.getcwd() + "/mixins")
import functions


# Variables for pow algorithm
number = 2
target = 10

# multiply
number_x: int = 12
number_y: int =  100


# Change Recursion maximum
sys.setrecursionlimit(10000)


def multiply_by_karatsuba(num_x: int, num_y: int):
  if (num_x < 10) or (num_y < 10) :
    return num_x * num_y
  else:
    max_length = max( functions.number_length(num_x),  functions.number_length(num_y)  )
    max_length_avr = max_length / 2
    max_length_avr = math.floor( max_length_avr )

    print( num_x, num_y, max_length_avr )
    a = num_x / 10**(max_length_avr)
    b = num_x % 10**(max_length_avr)
    c = num_y / 10**(max_length_avr)
    d = num_y % 10**(max_length_avr)
    ac = multiply_by_karatsuba(a,c)
    bd = multiply_by_karatsuba(b,d)
    ad_plus_bc = multiply_by_karatsuba(a+b,c+d) - ac - bd
    prod = ac * 10**(2*max_length_avr) + (ad_plus_bc * 10**max_length_avr) + bd
    return prod


def pow(number:int, target:int):
  if target == 0:
    return 1
  else:
    return number*pow(number,target-1)




if __name__ == '__main__':
  karatsuba_time = functions.algotithm_time( multiply_by_karatsuba(number_x, number_y), "Algoritmo de karatsuba" )
  print(f'Milisegundos: {karatsuba_time} \n ')

  normal_time = functions.algotithm_time( number_x * number_y, "Algoritmo de multiply" )
  print(f'Milisegundos: {normal_time} \n')
  
  divide_conquer_pow_time = functions.algotithm_time( pow(number, target), "Algoritmo de potencia" )
  print(f'Milisegundos: {divide_conquer_pow_time} \n')

  functions.graph_bars(
    ['Karatsuba', 'Estandard'],
    [ karatsuba_time, normal_time ],
    'Comparación de tiempo',
    'Algoritmo',
    'Tiempo (Milisegundos)'
    )

  functions.graph_bars(
    [ "Potencia" ],
    [ divide_conquer_pow_time ],
    "Comparación de tiempo en algoritmos de búsqueda",
    "Tipo de ordenamiento",
    "Tiempo (Milisegundos)"
  )