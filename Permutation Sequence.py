class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        a = [i for i in range(1,n+1)]
        res = ""
        
        perm = 1
        for i in range(1,n+1):
            perm *= i
           
        j = 0
        while j < n:
            perm //= n - j
            indx = (k-1) // perm
            val = a.pop(indx)
            #print(perm,indx,k)
            res += str(val)
            k -= indx * perm
            j += 1
            
        return res