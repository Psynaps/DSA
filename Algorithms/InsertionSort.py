# Definition for a pair.
from dataclasses import dataclass


@dataclass
class Pair:
    # def __init__(self, key: int, value: str):
    #     self.key = key
    #     self.value = value

    key: int
    value: str


class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                # swap
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            res.append(pairs[:])

        return res
