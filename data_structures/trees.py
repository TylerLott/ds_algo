class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[v {self.val}  l {self.left}  r {self.right}]"


def create_bst(nums: list) -> TreeNode:
    # take in list of numbers and return the root node
    root = TreeNode(val=nums[0])
    for i in nums[1:]:
        insert_bst(root, i)

    return root


def insert_bst(root: TreeNode, num: int):
    # insert given root node
    if num > root.val:
        if root.right == None:
            root.right = TreeNode(val=num)
        else:
            insert_bst(root.right, num)
    if num < root.val:
        if root.left == None:
            root.left = TreeNode(val=num)
        else:
            insert_bst(root.left, num)


def traverse(root: TreeNode, depth, dict) -> None:
    if root.left and root.right:
        traverse(root.left, depth + 1, dict)
        traverse(root.right, depth + 1, dict)
    elif root.left:
        traverse(root.left, depth + 1, dict)
    elif root.right:
        traverse(root.right, depth + 1, dict)

    dict[root] = depth


def run_bst():
    nums = [5, 2, 1, 7]
    root = create_bst(nums)
    print(root)
    res = {}
    insert_rebalance(root)
    traverse(root, 0, res)
    done = False
    layer = 0
    while not done:
        still_goin = False
        for i in res.keys():
            if res[i] == layer:
                print(i.val, end=" ")
                still_goin = True
        print("")
        layer += 1
        if not still_goin:
            break


def insert_rebalance(root: TreeNode) -> None:
    # shifts every node where either right or left are None
    """
        5
      2   7
    1

        |
        v

        5
      1   7
        2

    """
    pass


if __name__ == "__main__":
    run_bst()
