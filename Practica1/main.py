from typing import List
import matplotlib.pyplot as plt
from time import time
from datetime import datetime
from read_file import parse_array

# Declare variables
file_path = 'test.txt'
x = 9999

# Binary Search Algorithm
def binary_search(list: List[int], target: int):
    l = 0
    r = len(list) - 1
    while(l <= r):
        mid = l + (r - l) // 2
        if list[mid] == target:
            print(f'Elemento en el índice: {mid}')
            return
        elif list[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print("Elemento no encontrado")
    return

# Linear Search Algorithm
def linear_search(list: List[int], target: int):
    for i in range(len(list)):
        if list[i] == target:
            print(f'Elemento en el índice: {i}')
            return
    print("Elemento no encontrado")
    return


# Times Flags
cpu_start_time = 0
real_start_time = 0
cpu_binary_time = 0
real_binary_time = 0
cpu_linear_time = 0
real_linear_time = 0

# Run Binary and Linear Search
list = parse_array(file_path)
if list:
    # Binary Search
    print("Búsqueda Binaria")
    cpu_start_time = time()
    real_start_time = datetime.now()
    binary_search(list, x)
    cpu_binary_time = (time()-cpu_start_time)*1000
    real_binary_time = datetime.now()-real_start_time
    print(f'Milisegundos: {cpu_binary_time}')
    # Linear Search
    print("Búsqueda Linear")
    cpu_start_time = time()
    real_start_time = datetime.now()
    linear_search(list, x)
    cpu_linear_time = (time()-cpu_start_time)*1000
    real_linear_time = datetime.now()-real_start_time
    print(f'Milisegundos: {cpu_linear_time}')
    plt.bar(["Binaria", "Linear"],[cpu_binary_time,cpu_linear_time])
    plt.title("Comparación de tiempo en algoritmos de búsqueda")
    plt.xlabel("Tipo de búsqueda")
    plt.ylabel("Tiempo (Milisegundos)")
    plt.show()
