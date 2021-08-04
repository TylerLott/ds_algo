import numpy as np
import time



# O(N) space but really slow because of the array shift when inserting
def merge(arr, left, mid, right): 
        # if right-mid <= 0 or mid-left <= 0:
        #     return
        # print('lmr', left, mid, right)
        while mid <= right and left < mid:
            if arr[left] > arr[mid]:
                temp = arr[mid]
                p = mid
                while p > left:
                    arr[p] = arr[p-1]
                    p -= 1
                arr[left] = temp
                mid += 1
            left += 1
        
def mergeSort(arr, l, r):
        if l>=r: return
        # print(arr)
        mid = l + (r-l) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid+1, r)


a =[6334, 4098, 7968, 4523, 277, 6956, 4560, 2062, 5705, 5743, 879, 5626, 9961, 491, 2995, 741, 4827]

a = np.arange(0, 10000)[::-1]

start = time.time()

mergeSort(a, 0, len(a)-1)


print(f'time: {time.time() - start}')



def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
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
a = np.arange(0, 10000)[::-1]

start = time.time()

mergeSort(a)


print(f'time: {time.time() - start}')