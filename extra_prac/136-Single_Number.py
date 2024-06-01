# Leetcode 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]):
        num_count = [0]*(max(nums)+1)
        for num in nums:
            num_count[num]+=1
            print(nums)     #review on IDE

        dict1: dict = {}
        for number in nums:
            if number in dict1:
                dict1[number]+=1
            else:
                dict1[number] = 1
        return dict1         #preferred method

        # nums_count = Counter(nums)
        # for key, val in nums_count.items():
        #     if val == 1:
        #         return key        #works
