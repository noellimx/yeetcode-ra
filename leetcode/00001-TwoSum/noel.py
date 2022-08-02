from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        # a + b = target
        #  0  1  2  3  4  5  .......
        # [x, x, x, b, x, a, x, x]

        for i in range(len(nums)):
            try:
                # only return when i know the index of complement of a and index of a itself
                return [h_map[target - nums[i]], i]
            except:  # catch
                # { complement of a : 3 , a : ?}
                # key is the complement of b
                # value is the index of the b
                h_map[nums[i]] = i
