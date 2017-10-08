""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

import sys

def checkBST(root):
    return bst(root, -sys.maxint, sys.maxint)

def bst(node, left, right):
    if node == None:
        return True
    elif node.data <= left or node.data >= right:
        return False
    return bst(node.left, left, node.data) and bst(node.right, node.data, right)

    