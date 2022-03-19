from typing import List
import matplotlib.pyplot as plt
from time import time
from read_file import parse_array

# Declare variables
file_path = 'test.txt'

# Insertion Sort Algorithm
def insertion_sort(list: List[int]):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j - 1]
            j -= 1

# Selection Sort Algorithm
def selection_sort(list: List[int]):
    # Linear search
    for i in range(len(list)):
        index = i
        # Search the minimum value in the subarray
        for j in range(i + 1, len(list)):
            if list[index] > list[j]:
                index = j
        list[i], list[index] = list[index], list[i]

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j + 1
            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k = k-1
        gap = gap // 2

# Time Flag
cpu_start_time = 0

# Run Selection and Shell sort
list = parse_array(file_path)
if list:
    # Insertion
    print("Ordenamiento por inserción")
    cpu_start_time = time()
    insertion_sort(list)
    cpu_insertion_sort = (time() - cpu_start_time) * 1000
    print(f'Milisegundos: {cpu_insertion_sort}')
    # Selection
    print("Ordenamiento por selección")
    cpu_start_time = time()
    selection_sort(list)
    cpu_selection_sort = (time() - cpu_start_time) * 1000
    print(f'Milisegundos: {cpu_selection_sort}')
    # Shell
    print("Ordenamiento por shell")
    cpu_start_time = time()
    shell_sort(list)
    cpu_shell_sort = (time() - cpu_start_time) * 1000
    print(f'Milisegundos: {cpu_shell_sort}')
    plt.bar(["Inserción","Selección", "Shell"], [cpu_insertion_sort,cpu_selection_sort,cpu_shell_sort])
    plt.title("Comparación de tiempo en algoritmos de ordenamiento")
    plt.xlabel("Tipo de ordenamiento")
    plt.ylabel("Tiempo (Milisegundos)")
    plt.show()
