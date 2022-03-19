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

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(start, end, array): 
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1    
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1 
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
        
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end

def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

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
    # Merge
    print("Ordenamiento por mezcla")
    cpu_start_time = time()
    merge_sort(list)
    cpu_merge_sort = (time() - cpu_start_time) * 1000
    print(f'Milisegundos: {cpu_merge_sort}')
    # Quick
    print("Ordenamiento por rápido")
    cpu_start_time = time()
    quick_sort(0, len(list) - 1, list)
    cpu_quick_sort = (time() - cpu_start_time) * 1000
    print(f'Milisegundos: {cpu_quick_sort}')
    plt.bar(["Inserción","Selección", "Shell", "Mezcla", "Rápido"], [cpu_insertion_sort,cpu_selection_sort,cpu_shell_sort,cpu_merge_sort,cpu_quick_sort])
    plt.title("Comparación de tiempo en algoritmos de ordenamiento")
    plt.xlabel("Tipo de ordenamiento")
    plt.ylabel("Tiempo (Milisegundos)")
    plt.show()
