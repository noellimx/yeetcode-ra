from typing import *

def solution(A: int) -> int:
    # to find max # pairs, we need to each element have to start once and iterate all elements in order
    length_A = len(A)
    max_number_of_even_pairs = 0

    for offset in range(len(A)): # for each starting element
        number_of_even_pairs = 0
        i = offset # pointer which move one element, or two if pair is found
        start_index = offset # keep track for the case when first pair is even
        c = 0 # count number of passes i.e how much i have moved

        last_index = (offset - 1 + length_A) % length_A  # mod to keep in range
        
        is_first_pair_even = False
        
        while c <= length_A:

            left_index = i
            print(f"{offset} {i}:{left_index}")
            right_index = (i + 1) % length_A # mod to keep in range

            if left_index == last_index: # This is the last iteration

                if not is_first_pair_even:
                    is_sum_even = (A[left_index] + A[right_index]) % 2 == 0
                    number_of_even_pairs += 1 if is_sum_even else 0
                break

            is_sum_even = (A[left_index] + A[right_index]) % 2 == 0

            if is_sum_even and left_index == start_index:
                is_first_pair_even = True


            if is_sum_even:
                number_of_even_pairs += 1
                i += 1
                c += 1

            i =  (i + 1) % length_A # mod to keep in range
            c += 1

        max_number_of_even_pairs = max(max_number_of_even_pairs,number_of_even_pairs)

    return max_number_of_even_pairs


print(solution([12,14, 21, 16, 35, 22]))
