import timeit

bst_setup = """
import copy
import random
random.seed(42)
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data


l = random.sample(range(1,1000000001), 10000000)"""

bst_code = """x = copy.deepcopy(l)
root = Node(x[0])
for i in range(1, len(x)):
    root.insert(x[i])"""

dict_code = """x = copy.deepcopy(l)
d = {}
for i in range(len(x)):
    d[i] = x[i]"""


print("BST")
print(min(timeit.repeat(setup = bst_setup,
                    stmt = bst_code,
                    number = 1,
                    repeat = 1,
                    globals=globals())))
print("DICTIONARY")
print(min(timeit.repeat(setup = bst_setup,
                    stmt = dict_code,
                    number = 1,
                    repeat = 1,
                    globals=globals())))

