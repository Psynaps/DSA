# Implementation of a Binary Search Tree (BST) with key-value pairs
# See remove and removeHelper for tricky part of the implementation


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = Node(key, val)
        if self.root is None:
            self.root = node
            return
        rover = self.root
        while True:
            if key == rover.key:
                rover.val = val
                return
            if key > rover.key:
                if rover.right:
                    rover = rover.right
                else:
                    rover.right = node
                    return
            else:
                if rover.left:
                    rover = rover.left
                else:
                    rover.left = node
                    return

    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        rover = self.root
        while rover:
            if rover.key == key:
                return rover.val
            if key > rover.key:
                rover = rover.right
            else:
                rover = rover.left
        return -1

    def getMin(self) -> int:
        if self.root is None:
            return -1
        return self.findMin(self.root).val

    def findMin(self, node: Node) -> Node:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if self.root is None:
            return -1
        rover = self.root
        while rover.right:
            rover = rover.right
        return rover.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: Node, key: int) -> Node:
        if curr is None:
            return None
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)

        else:  # Removing node curr
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)

        return curr

    def getInorderKeys(self) -> list[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res

    def inorderTraversal(self, root, res):
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)
