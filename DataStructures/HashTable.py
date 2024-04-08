# Implement a HashTable using separate chaining to handle collisions. Automatically resize the table when
# the load factor exceeds 0.5. The table should double in size when this happens. The table should be an array of linked lists.
# Each linked list contains nodes with a key and a value. The key should be an integer and the value can be any data type.


class Node:
    def __init__(self, key: int, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self.hash_function(key)
        # node = Node(key, val)
        curr = self.table[idx]

        if curr is None:
            self.table[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while curr is not None:
                if curr.key == key:
                    curr.val = value
                    return
                prev = curr
                curr = curr.next
            prev.next = Node(key, value)
            self.size += 1

        # Resize if needed
        if self.size >= self.capacity / 2:
            self.resize()

    def get(self, key: int) -> int:

        curr = self.table[self.hash_function(key)]
        while curr is not None:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        if self.size == 0:
            return False
        idx = self.hash_function(key)
        curr = self.table[idx]
        prev = None
        while curr is not None:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                idx = node.key % new_capacity
                if new_table[idx] is None:
                    new_table[idx] = Node(node.key, node.val)
                else:
                    curr = new_table[idx]
                    while curr.next:
                        curr = curr.next
                    curr.next = Node(node.key, node.val)
                node = node.next

        self.capacity = new_capacity
        self.table = new_table
