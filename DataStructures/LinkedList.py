# Two implementations of LinkedList are provided below. The first implementation is without a dummy node and the second implementation is with a dummy node.
# The second implementation is more efficient and easier to implement.


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


# class LinkedList_NoDummy:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def get(self, index: int) -> int:
#         rover = self.head
#         while index > 0 and rover:
#             rover = rover.next
#             index -= 1
#         if rover is None:
#             return -1
#         return rover.val

#     def insertHead(self, val: int) -> None:
#         node = ListNode(val, self.head)
#         # node.next = self.head
#         if self.tail is None:
#             self.tail = node
#         self.head = node
#         # print(self.getValues(), 'head:', self.head.val, 'tail:', self.tail.val)

#     def insertTail(self, val: int) -> None:
#         node = ListNode(val)
#         if self.tail is None:
#             # print('tail was none')
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         # print(self.getValues(), 'head:', self.head.val, 'tail:', self.tail.val)

#     def remove(self, index: int) -> bool:

#         if self.head is None:
#             return False

#         if index == 0:
#             if self.head == self.tail:
#                 self.tail = None
#             self.head = self.head.next
#             return True

#         current = self.head
#         while index > 1 and current.next:
#             print("move next")
#             current = current.next
#             index -= 1

#         if current.next is None and index >= 1:
#             return False

#         if current.next is None or current.next == self.tail:
#             # print('this case1,', self.head.val, self.tail.val, current.val, current.next.val, 'tail:', self.tail.val)
#             self.tail = current
#             current.next = None
#             return True

#         if current and current.next:
#             # print('this case 2,', self.head, self.tail)
#             current.next = current.next.next
#             return True

#         return False

#     def getValues(self) -> List[int]:
#         res = []
#         rover = self.head
#         while rover:
#             res.append(rover.val)
#             rover = rover.next
#         return res


# Improved implementation using dummy node

# Duplcate of above list node
# class ListNode:
#     def __init__(self, val, next_node=None):
#         self.val = val
#         self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = self.head

    def get(self, index: int) -> int:
        rover = self.head.next
        while rover and index > 0:
            rover = rover.next
            index -= 1

        if index > 0 or rover is None:
            return -1

        return rover.val

        # curr = self.head.next
        # i = 0
        # while curr:
        #     if i == index:
        #         return curr.val
        #     i += 1
        #     curr = curr.next
        # return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        if node.next is None:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        rover = self.head
        while index > 0 and rover:
            rover = rover.next
            index -= 1

        if rover and rover.next:
            if rover.next == self.tail:
                self.tail = rover
            rover.next = rover.next.next
            return True
        return False

    def getValues(self) -> list[int]:
        res = []
        rover = self.head.next
        while rover:
            res.append(rover.val)
            rover = rover.next
        return res


# Test cases
LL = LinkedList()
LL.insertHead(1)
LL.insertHead(2)
print(LL.getValues())  # [2, 1]
LL.insertHead(3)
print(LL.get(1))  # 2
print(LL.getValues())  # [3, 2, 1]
