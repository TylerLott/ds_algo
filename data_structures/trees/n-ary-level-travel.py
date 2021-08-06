"""
Leetcode daily question

Nary-tree travel and print all of the levels

ex.

root = [1, null, 3, 2,4, null, 5, 6]
out = [[1], [3,2,4], [5,6]]



"""


class Node:
    def __init___(self, val=None, children=None):
        self.val = val
        self.children = children


"""
Immediate thought is recursion, although I like iteration better
Iteration could be done with some sort of backtracking

I think Ill go for recursion though and pass a solutions array with the function
This will append nums to the index of the array based on their height

ex.

           1
      2    3    4
          5 6

[
    [1]
    [2,3,4]
    [5,6]
]
"""


def levelOrder(self, root):
    s = []
    helper(root, s, 0)
    return s


def helper(node, s, depth):
    if not node:
        return

    if depth < len(s):
        s[depth].append(node.val)
    else:
        s.append([node.val])

    for i in node.children:
        helper(i, s, depth + 1)
