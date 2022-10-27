import timeit

setupCode = """
import copy
import random
random.seed(43)

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

insertion_list = random.sample(range(1,101), 100)
merge_list = random.sample(range(1,101), 100)
"""

insertioncode = """x = copy.deepcopy(insertion_list)
insertionSort(x)"""
mergecode = """y = copy.deepcopy(merge_list)
mergeSort(merge_list)"""

print("INSERTION")
print(min(timeit.repeat(setup = setupCode,
                    stmt = insertioncode,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))

print("MERGE")
print(min(timeit.repeat(setup = setupCode,
                    stmt = mergecode,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))



