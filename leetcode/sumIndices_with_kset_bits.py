"""
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding 
indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
"""


from typing import List


def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    total = 0
    for i, num in enumerate(nums):
        count = 0
        while i:
            count += i & 1
            i >>= 1
        if count == k:
            total += num
    return total
