'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
    #make a dictionary with key/value nums[i]/last seen index
    hashmap = {}

    for i in range(0,len(nums)):
        #if you encounter an existing key, check the difference (otherwise make a new entry)
        if nums[i] in hashmap.keys():
            abs_dif = abs(i-hashmap[nums[i]])          
        #if the abs difference is within k, return True
            if abs_dif <= k:
                return True
        #else update the last seen index
            else:
                hashmap[nums[i]] = i
        else:
            hashmap[nums[i]] = i

    return False