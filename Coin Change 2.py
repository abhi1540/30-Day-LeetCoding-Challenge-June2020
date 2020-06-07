class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if i <= j:
                    dp[j] = dp[j] + dp[j - i] #main formula
                    
                
        return dp[-1]