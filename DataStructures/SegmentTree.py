# Segment Tree implementation using Node class and helper methods


class Node:
    def __init__(self, total, start, end):
        self.sum = total
        self.left = None
        self.right = None
        self.start = start
        self.end = end


class SegmentTree:

    def __init__(self, nums: list[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, start, end):
        if start == end:
            return Node(nums[start], start, end)

        M = (start + end) // 2
        root = Node(0, start, end)
        root.left = self.build(nums, start, M)
        root.right = self.build(nums, M + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index: int, val: int) -> None:
        if root.start == root.end:  # found node to update
            root.sum = val
            return

        M = (root.start + root.end) // 2
        if index > M:  # updating node in right child branch
            self.update_helper(root.right, index, val)
        else:  # updating node in left child branch
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, start, end):
        if start <= root.start and end >= root.end:
            return root.sum

        if end < root.start or start > root.end:
            return 0

        return self.query_helper(root.left, start, end) + self.query_helper(
            root.right, start, end
        )


# test cases
nums = [1, 3, 5]
st = SegmentTree(nums)
print(st.query(0, 2))  # 9
