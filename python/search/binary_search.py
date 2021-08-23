def binSearch(arr, l, h, val):
    """
    binary search implementation
        returns the index of the val
        return -1 if not in array

    """
    mid = l + (h - l) // 2  # we use floor division to make sure its an integer
    if l > h:
        return -1
    if val >= arr[l] and val < arr[mid]:
        return binSearch(arr, l, mid - 1, val)
    if val <= arr[h] and val > arr[mid]:
        return binSearch(arr, mid + 1, h, val)
    if val == arr[mid]:
        return mid
    return -1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    for i in range(1,10):
        if i <= 8:

            assert binSearch(a, 0, len(a)-1, i) == i-1
            print(f'{i} is in the array at index {i-1}')
        else:
            assert binSearch(a, 0, len(a)-1, i) == -1
            print(f'{i} is not in the array')
