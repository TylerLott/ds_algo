"""
Leetcode 12. integer to roman


This felt like the grossest thing to code ever, it seemed to be the 
best python solution though from what others had done, so thats good i guess

"""


def intToRom(num):
    hm = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    s = ""
    for i in hm.keys():
        n = num // i
        if n != 0:
            for j in range(n):
                s += hm[i]
            num -= n * i

    return s
