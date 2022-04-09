from typing import List
import matplotlib.pyplot as plt
from time import time
import sys
import random

# Variables for pow algorithm
number = 0
target = 100

# Change Recursion maximum
sys.setrecursionlimit(10000)

# Insertion Sort Algorithm
def pow(number:int, target:int):
    if right >= left:
        middle = left + (right - left) // 2
        if list[middle] == target:
            print(f'El elemento se encuentra en el índice: {middle}')
            return
        elif list[middle] > target:
            return binary_search(list, left, middle - 1, target)
        else:
            return binary_search(list, middle + 1, right, target)
    else:
        print("El elemento no está en la lista")
        return
# Time Flag
cpu_start_time = 0

# Creation of list
list = [i for i in range(start,end+1,step)]
list_last_index = len(list)-1

# Binary Search
print("Algoritmo de potencia")
cpu_start_time = time()
binary_search(list, 0, list_last_index, target)
cpu_binary_search = (time() - cpu_start_time) * 1000
print(f'Milisegundos: {cpu_binary_search}')
# Binary Search
print("Búsqueda binaria aleatoria")
cpu_start_time = time()
random_binary_search(list, 0, list_last_index, target)
cpu_random_binary_search = (time() - cpu_start_time) * 1000
print(f'Milisegundos: {cpu_random_binary_search}')

# Chart
plt.bar(["Búsqueda Binaria", "Búsqueda Binaria Aleatoria"],
        [cpu_binary_search, cpu_random_binary_search])
plt.title("Comparación de tiempo en algoritmos de búsqueda")
plt.xlabel("Tipo de ordenamiento")
plt.ylabel("Tiempo (Milisegundos)")
plt.show()