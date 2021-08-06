"""
leetcode problem 16.

find the 3 numbers in a list that sum clostest to the target

Brute force:
iterate through the list in 3 nested loops
O(n^3) - time
O(n) - space


Better #1:
sort array O(nlogn)
fix one point and use pointers to find the best solution O(n^2)

O(nlogn) + O(n^2) = O(n^2 + nlogn) = O(n^2)

"""


def sum3close(nums: list, t: int) -> int:
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i, e in enumerate(nums):
        if i >= len(nums)-2: break
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == t:
                return s
            if abs(s - t) < abs(res-t):
                res = s
            if s < t:
                j += 1
            else:
                k -= 1
    return res



if __name__ == "__main__":
    a = [-1, 2, 1, -4]

    print(sum3close(a, 1))
