from typing import *


def solution(A: List[int]) -> int:
    output = index = 0
    is_zero_used = False

    while index <= len(A) - 1:  # o(n)

        # gather the index
        l_index = index
        is_last_iter = index == len(A) - 1
        r_index = 0 if is_last_iter else index + 1

        if is_zero_used and is_last_iter:
            break

        is_sum_even = (A[l_index] + A[r_index]) % 2 == 0

        if index == 0 and is_sum_even:
            is_zero_used = True

        if is_sum_even:
            output += 1
            index += 1
        index += 1

    return output


print(solution([4, 2, 4]))
print(solution([4, 2, 5, 8, 7, 3, 71]))
