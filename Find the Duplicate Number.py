class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in range(len(nums)):
            if nums[abs(nums[i])] >= 0:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
            else:
                res = abs(nums[i])  
        return res