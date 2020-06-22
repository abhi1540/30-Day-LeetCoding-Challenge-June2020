class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = [0]*32
        
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i):
                    count += 1
            res[31-i] = (count % 3)
  
        str1 = ''.join(str(e) for e in res)
        ans = int(str1,2)
        
        if ans >= 2**31:
            ans -= 2**32
            
        return ans