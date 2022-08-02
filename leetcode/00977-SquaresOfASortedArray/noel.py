from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        squares = [0 for _ in range(length)]

        l = 0
        r = length - 1

        c = r
        while c >= 0:
            ls = nums[l] * nums[l]
            rs = nums[r] * nums[r]
            if ls > rs:
                squares[c] = ls
                l += 1
            else:
                squares[c] = rs
                r -= 1
            c -= 1
        return squares
