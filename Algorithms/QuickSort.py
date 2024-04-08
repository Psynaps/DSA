# In place quicksort implementation

from dataclasses import dataclass


# Definition for a pair.
@dataclass
class Pair:
    # def __init__(self, key: int, value: str):
    #     self.key = key
    #     self.value = value

    key: int
    value: str


class Solution:
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr, s, e) -> None:
        # if e - s + 1 <= 1:
        #     return
        if s >= e:
            return

        pivot = arr[e]
        L = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[L], arr[i] = arr[i], arr[L]
                L += 1
        # arr[e] = arr[L]
        # arr[L] = pivot
        arr[e], arr[L] = arr[L], arr[e]

        self.quickSortHelper(arr, s, L - 1)
        self.quickSortHelper(arr, L + 1, e)
