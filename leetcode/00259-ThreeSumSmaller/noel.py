from typing import *


class Solution:

    def _twoSumSmaller(self, nums:List[int], start_index:int, target: int) -> int:

        length_num = len(nums)

        index_b = start_index
        index_c = length_num - 1

        count = 0  

        print(f"target_b_and_c {target}")

        while index_b < index_c:
            b = nums[index_b]
            c = nums[index_c]

            while index_b < index_c and (index_b - 1) >= 0 and nums[index_b - 1] == b and (index_c + 1) <= (length_num - 1) and nums[index_c + 1] == c:
                b += 1
                c -= 1

            b_and_c = b + c
            print(f"b={b} c={c}")

            if b_and_c < target:

                print(f"b={b} c={c} OK")
                count += 1
                index_b += 1
            else:
                print("c <- ")
                index_c -= 1

        return count
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        print(nums)
        length_num = len(nums)
        boundary = length_num - 2
        index_a = 0

        count = 0

        while index_a < boundary:
            a = nums[index_a]

            
            target_b_and_c = target - a

            count += self._twoSumSmaller(nums, index_a + 1, target_b_and_c)

            index_a += 1
        return count


s = Solution()


s.threeSumSmaller([-2,0,1,3],2)