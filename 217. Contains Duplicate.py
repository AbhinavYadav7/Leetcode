# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Brute Force
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in nums:
#             count = 0

#             for j in nums:
#                 if i == j:
#                     count +=1
#             if count > 1:
#                 return True
#         else :
#             return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	repeat ={}

    	for i,n in enumerate(nums):
    		if n in repeat:
    			return True
    		else:
    			repeat[n] = i
    	return False
