""" 
this question involves creating a partitioning algorithm to find the 
median of two sorted arrays
"""


def findMed(arr1, arr2) -> float:
    # Find the smaller array
    A, B = arr1, arr2
    if len(B) < len(A):
        A, B = B, A

    # get the total and the midway point
    total = len(A) + len(B)
    half = total // 2  # int divide because this is an index

    # get the origin partition
    # we know A is the shortest so we use this
    # this allows us to only binary search one of the lists
    l, r = 0, len(A) - 1

    while True:
        # define the partition bounds
        i = (l + r) // 2  # l and r are only associated with the smaller array

        """
        we find the partition bounds of the larger array using the partition bounds
        from the smaller array. We do this be subtracting the half way point by the 
        bound of the smaller array. then to account for the array being indexed at 0
        and the bound not including the higher value we subtract 2

        ex. 
        A = [1,2,3,4]
             ^   ^ ^
             l   i r

        B = [1,2,3,4,5,6,7,8]
                 ^
                 j

        len(B) = 8
        len(A) = 4
        total = 12
        half = 6
        j = 6 - i - 2
        j = 6 - 2 - 2
        j = 2
        """
        j = half - i - 2

        """
        Next we set the values to compare and deal with edge cases
        """
        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i + 1] if i + 1 < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j + 1] if j + 1 < len(B) else float("inf")

        """
        Next we do checks to see if the parition was done correctly, and either return
        or adjust the partition accordingly
        """

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        # in this case we adjust the right index of the smaller array because the
        # right side of the partition on the larger array is larger than A
        elif Aleft > Bright:
            r = i - 1

        # Bleft > Aright
        # in this case we add to the left side of the smaller array because the
        # left side of the partition of the larger array if larger, meaning that
        # the median value lies closer to the right value of the smaller array
        else:
            l = i + 1
