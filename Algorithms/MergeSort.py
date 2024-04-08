# Merge sort with minimal additional arrays, merge in place

from dataclasses import dataclass


# Definition for a pair as a dataclass
@dataclass
class Pair:

    key: int
    value: str


class Solution:
    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        # if len(pairs) <= 1:
        #     return pairs

        # M = len(pairs) // 2
        # left = self.mergeSort(pairs[0:M])
        # right = self.mergeSort(pairs[M:])
        # return self.merge(left, right)

        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: list[Pair], start: int, end: int) -> list[Pair]:
        if start >= end:
            return pairs

        M = (start + end) // 2

        self.mergeSortHelper(pairs, start, M)

        self.mergeSortHelper(pairs, M + 1, end)

        self.merge(pairs, start, M, end)

        return pairs

    def merge(self, arr: list[Pair], start: int, mid: int, end: int) -> None:
        L = arr[start : mid + 1]
        R = arr[mid + 1 : end + 1]

        i = 0
        j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    # def merge(self, list1, list2):
    #     i = 0
    #     j = 0
    #     res = []
    #     while i < len(list1) and j < len(list2):
    #         if list1[i].key <= list2[j].key:
    #             res.append(list1[i])
    #             i += 1
    #         else:
    #             res.append(list2[j])
    #             j += 1

    #     # add on remaining list
    #     if i < len(list1):
    #         res += list1[i:]
    #     elif j < len(list2):
    #         res += list2[j:]
    #     return res


# pairs=[(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
pairs = [
    Pair(5, "apple"),
    Pair(2, "banana"),
    Pair(9, "cherry"),
    Pair(1, "date"),
    Pair(9, "elderberry"),
]
s = Solution()
print(s.mergeSort(pairs))

correct = [
    Pair(1, "date"),
    Pair(2, "banana"),
    Pair(5, "apple"),
    Pair(9, "cherry"),
    Pair(9, "elderberry"),
]

for i in range(len(pairs)):
    assert pairs[i].key == correct[i].key
    assert pairs[i].value == correct[i].value
print("All tests passed!")

# test list equality
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # True

l3 = [Pair(1, "a"), Pair(2, "b")]
l4 = [Pair(1, "a"), Pair(2, "b")]
print(l3 == l4)  # False
