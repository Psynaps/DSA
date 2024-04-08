# Double ended queue implementation using doubly linked list


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        val = last_node.val
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        val = first_node.val
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head
        return val
