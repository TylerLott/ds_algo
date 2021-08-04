import numpy as np

def quicksort(arr):
    helper(arr, 0, len(arr)-1)

def helper(arr, l, r):
    if l>=r: return
    piv = arr[(l+r) // 2]
    ind = partition(arr, l, r, piv)
    helper(arr, l, ind-1)
    helper(arr, ind, r)


def partition(arr, l, r, piv):
    while l <= r:
        while arr[l] < piv:
            l += 1
        while arr[r] > piv:
            r -= 1
        if l <= r:
            swap(arr, l, r)
            l += 1
            r -= 1
    return l

def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

a = np.arange(10000)[::-1]

quicksort(a)
print(a)