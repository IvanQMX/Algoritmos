import matplotlib.pyplot as plt
from time import time
import sys

# Variables for pow algorithm
number = 2
target = 1000

# Change Recursion maximum
sys.setrecursionlimit(10000)

# Insertion Sort Algorithm
def pow(number:int, target:int):
    if target == 0:
        return 1
    else:
        return number*pow(number,target-1)
# Time Flag
cpu_start_time = 0

# Pow Algorithm
print("Algoritmo de potencia")
cpu_start_time = time()
print(pow(number, target))
cpu_pow = (time() - cpu_start_time) * 1000
print(f'Milisegundos: {cpu_pow}')

# Chart
plt.bar(["Potencia"],[cpu_pow])
plt.title("Comparación de tiempo en algoritmos de búsqueda")
plt.xlabel("Tipo de ordenamiento")
plt.ylabel("Tiempo (Milisegundos)")
plt.show()