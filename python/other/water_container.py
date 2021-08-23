"""
This is the water container questions from leetcode 11.
Given a list of heights for lines, find between which two lines the most water
could be held

Essentially this question is about maximizing a square between points 
in an unsorted list
"""


def maxWater(heights: list) -> int:
    # we can do this in O(n) time, we need to start with pointers at the
    # begining and end. This is esentially like sorting one of the dimensions
    # for the square (length) now we just nees to find where the min of two heights
    # is the greatest

    # set our variables for iteration
    i, j = 0, len(heights) - 1
    maxW = 0
    
    while i != j:
        minHeight = min(heights[i], heights[j])
        length = j - i
        
        # condition for keeping track of max square
        maxW = minHeight*length if minHeight*length > maxW else maxW

        # iterating conditions
        if heights[i] < heights[j]: # move the lower height pointer
            i += 1
        else:
            j -= 1
    return maxW


if __name__ == "__main__":
    a = [1,8,6,2,5,4,8,3,7]
    b = [1,1]
    c = [4,3,2,1,4]

    assert maxWater(a) == 49
    print("Passed Testcase 1")
    assert maxWater(b) == 1
    print("Passed Testcase 2")
    assert maxWater(c) == 16
    print("Passed Testcase 3")
