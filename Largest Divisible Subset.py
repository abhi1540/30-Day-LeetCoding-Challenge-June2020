class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
    
        if len(nums) == 0: return []
        nums.sort()
        print(nums)
        dp = [[i] for i in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                print(i,j)
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]          
        return max(dp, key=len) 