from posixpath import split
from typing import List
import matplotlib.pyplot as plot
from time import time
import sys
import math


# Change Recursion maximum
sys.setrecursionlimit(10000)

def number_length( num: int ):
  return len(str(num))


def multiply_by_karatsuba(num_x: int, num_y: int):
  if (num_x < 10) or (num_y < 10) :
    return num_x * num_y
  else:
    max_length = max( number_length(num_x),  number_length(num_y)  )
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


def graph_bars(label: List[str], data: List[float], title: str, xlabel: str, ylabel: str):
  plot.bar(label,  data)
  plot.title(title)
  plot.xlabel(xlabel)
  plot.ylabel(ylabel)
  plot.show()


def algotithm_time( algorithm ):
  cpu_time_start = time()
  print( algorithm )
  cpu_time_end_karatsuba = (time() - cpu_time_start) * 1000
  return cpu_time_end_karatsuba




if __name__ == '__main__':
  karatsuba_time = algotithm_time( multiply_by_karatsuba(12, 100) )
  print(f'Milisegundos: {karatsuba_time}')

  normal_time = algotithm_time( 25 * 100 )
  print(f'Milisegundos: {normal_time}')
  
graph_bars(
  ['Karatsuba', 'Estandard'],
  [ karatsuba_time, normal_time ],
  'Comparación de tiempo',
  'Algoritmo',
  'Tiempo (Milisegundos)'
  )