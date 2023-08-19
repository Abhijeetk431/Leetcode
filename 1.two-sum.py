#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Order n - Not optimized
        # num_index_pairs = [
        #     [i, nums[i]] for i in range(len(nums))
        # ]
        # sorted_pairs = sorted(
        #     num_index_pairs,
        #     key= lambda x: x[1])
        # i=0
        # j=len(sorted_pairs)-1
        # while True:
        #     if sorted_pairs[i][1]+sorted_pairs[j][1] == target:
        #         return [sorted_pairs[i][0], sorted_pairs[j][0]]
        #     if sorted_pairs[i][1]+sorted_pairs[j][1] > target:
        #         j=j-1
        #     if sorted_pairs[i][1]+sorted_pairs[j][1] < target:
        #         i=i+1
        
        # Order n2
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # Order n - Optimized
        checked = {}
        for i in range(len(nums)):
            needed_num = target-nums[i]
            if needed_num in checked:
                return [i, checked[needed_num]]
            else:
                checked[nums[i]] = i
# @lc code=end

