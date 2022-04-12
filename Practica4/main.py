from typing import List
import math
import copy
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

# A class to represent a Point in 2D plane
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
P = [Point(2, 3), Point(12, 30),
  	Point(40, 50), Point(5, 1),
  	Point(12, 10), Point(3, 4)]
n = len(P)


# Change Recursion maximum
sys.setrecursionlimit(10000)


def bruteForce(P, n):
	min_val = float('inf')
	for i in range(n):
		for j in range(i + 1, n):
			if functions.dist(P[i], P[j]) < min_val:
				min_val = functions.dist(P[i], P[j])

	return min_val


def stripClosest(strip, size, d):
	min_val = d
	for i in range(size):
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val:
			min_val = functions.dist(strip[i], strip[j])
			j += 1

	return min_val


def closestUtil(P, Q, n):
	if n <= 3:
		return bruteForce(P, n)

	mid = n // 2
	midPoint = P[mid]

	Pl = P[:mid]
	Pr = P[mid:]

	dl = closestUtil(Pl, Q, mid)
	dr = closestUtil(Pr, Q, n - mid)

	d = min(dl, dr)

	stripP = []
	stripQ = []
	lr = Pl + Pr
	for i in range(n):
		if abs(lr[i].x - midPoint.x) < d:
			stripP.append(lr[i])
		if abs(Q[i].x - midPoint.x) < d:
			stripQ.append(Q[i])

	stripP.sort(key = lambda point: point.y) #<-- REQUIRED
	min_a = min(d, stripClosest(stripP, len(stripP), d))
	min_b = min(d, stripClosest(stripQ, len(stripQ), d))
	
	return min(min_a,min_b)


def closest(P, n):
	P.sort(key = lambda point: point.x)
	Q = copy.deepcopy(P)
	Q.sort(key = lambda point: point.y)

	return closestUtil(P, Q, n)


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
  elif target%2==0:
	  return pow(number, target/2)*pow(number, target/2)
  else:
    return number*pow(number, target//2)*pow(number, target//2)




if __name__ == '__main__':
  karatsuba_time = functions.algotithm_time( multiply_by_karatsuba(number_x, number_y), "Karatsuba" )
  print(f'Milisegundos: {karatsuba_time} \n ')

  normal_time = functions.algotithm_time( closest(P, n), "Menor functions.distancia" )
  print(f'Milisegundos: {normal_time} \n')
  
  pow_time = functions.algotithm_time( pow(number, target), "Potencia" )
  print(f'Milisegundos: {pow_time} \n')
 


  functions.graph_bars(
    ['Karatsuba', 'Menor functions.distancia', "Potencia"],
    [ karatsuba_time, normal_time, pow_time ],
    'Comparación de tiempo',
    'Algoritmo',
    'Tiempo (Milisegundos)'
    )