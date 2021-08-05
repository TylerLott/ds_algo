# This is a quicksort which is aimed at sorting 3 groups
# this is O(n) time and O(1) space


def dutchSort(arr):
    a, b, c = 0, 0, len(arr) - 1

    while (
        b <= c
    ):  # important that this is <= so that it can swap while on the last element, even if the last element isn't being swapped
        if arr[b] == 0:  # if pointer b points to an element of catagory a, swap them
            arr[b], arr[a] = arr[a], arr[b]
            a += 1
            b += 1
        elif arr[b] == 1:  # if pointer b points to the correct item, increment b
            b += 1
        else:  # if pointer b points to an element of catagory c, swap them and increment c down
            arr[b], arr[c] = arr[c], arr[b]
            c -= 1


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    b = [2, 0, 1]
    c = [0, 1, 2, 0, 1, 2, 2, 1, 0]

    dutchSort(a)
    dutchSort(b)
    dutchSort(c)

    assert a == [0, 0, 1, 1, 2, 2]
    print("Test 1 Succeeded")
    assert b == [0, 1, 2]
    print("Test 2 Succeeded")
    assert c == [0, 0, 0, 1, 1, 1, 2, 2, 2]
    print("Test 3 Succeeded")
