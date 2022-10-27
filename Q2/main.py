import timeit

setupCode = """
import copy
import random
random.seed(43)
def insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array
              
def merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = 15
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size 

tim_list1 = random.sample(range(1,201), 100)
tim_list2 = random.sample(range(1,201), 125)
tim_list3 = random.sample(range(1,201), 150)
tim_list4 = random.sample(range(1,201), 200)"""
    
tim_code1 = """w = copy.deepcopy(tim_list1)
tim_sort(w)"""

tim_code2 = """x = copy.deepcopy(tim_list2)
tim_sort(x)"""

tim_code3 = """y = copy.deepcopy(tim_list3)
tim_sort(y)"""

tim_code4 = """z = copy.deepcopy(tim_list4)
tim_sort(z)"""

print("N = 100")
print(min(timeit.repeat(setup = setupCode,
                    stmt = tim_code1,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))

print("N = 125")
print(min(timeit.repeat(setup = setupCode,
                    stmt = tim_code2,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))

print("N = 150")
print(min(timeit.repeat(setup = setupCode,
                    stmt = tim_code3,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))

print("N = 200")
print(min(timeit.repeat(setup = setupCode,
                    stmt = tim_code4,
                    number = 10000,
                    repeat = 1,
                    globals=globals())))
