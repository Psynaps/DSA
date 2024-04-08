# Implementation of a MinHeap complete with bubble_up, bubble_down, push, pop, top, and heapify methods


class MinHeap:

    def __init__(self):
        self.heap = [0]

    def _bubble_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            # swap
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def _bubble_down(self, index: int) -> None:
        child = 2 * index
        size = len(self.heap)
        while child < size:
            if child + 1 < size and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[child] >= self.heap[index]:
                break

            # otherwise swap parent and child
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child *= 2

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()  # swap with last element
        self._bubble_down(1)
        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)
