'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. The relative order of the elements should be kept the same. Then return the number of 
unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were 
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
2. Return k.
'''

def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    k = len(nums)

    #check each element of the array against the last. Assume all elements are unique.
    while i < len(nums):            
        #if it's the same, pop the index as it's a double, decrement k
        if nums[i] == nums[i-1]:
            nums.pop(i)
            k-=1
        #otherwise move to the next position
        else:
            i += 1
    
    return k