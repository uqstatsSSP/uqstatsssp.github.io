'''write quick sort in python'''
import random   
import time
import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def quicksort(arr, low, high):
    # Base condition for recursion
    if low < high:
        # Find pivot element such that 
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursive call for elements on the left of pivot
        quicksort(arr, low, pi - 1)

        # Recursive call for elements on the right of pivot
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr,0,n-1)
    print(arr)

