"""
longest palendromic substring from leetcode 5.

find the longest palindromic substring. Best case is O(n) with a very abstract algo
best case for interviews should be O(n^2) with dynamic programming


When solving these follow these steps:

- determine what the brute force method would be
- determine time complexity of the brute force method

- find a way to improve upon the brute force method
- use that method

- find edge cases
- code the algo with the better case 
- account for edge cases
- go through cases by hand before running

- run and succeed
"""


def longPal(s: str) -> str:
    longest_palindrom = ""
    dp = [[0] * len(s) for _ in range(len(s))]
    # filling out the diagonal by 1
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]

    # filling the dp table
    for i in range(len(s) - 1, -1, -1):
        # j starts from the i location : to only work on the upper side of the diagonal
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:  # if the chars mathces
                # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True
                # if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    # we also need to keep track of the maximum palindrom sequence
                    if len(longest_palindrom) < len(s[i : j + 1]):
                        longest_palindrom = s[i : j + 1]
    return longest_palindrom


if __name__ == "__main__":
    a = "babad"
    b = "cbbd"
    c = "cbbdba"
    d = "ccc"
    e = "dd"
    f = "aaaa"
    print(longPal(a))
    print(longPal(b))
    print(longPal(c))
    print(longPal(d))
    print(longPal(e))
    print(longPal(f))
