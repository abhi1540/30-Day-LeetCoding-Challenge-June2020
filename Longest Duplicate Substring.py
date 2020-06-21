class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        A = [ord(c) - ord('a') for c in S]
        # The ord() function in Python accepts a string of length 1 as an argument 
        # and returns the unicode code point representation of the passed argument. 
        # For example ord('B') returns 66 which is a unicode code point value of character ‘B’. 
        mod = 2**63 - 1
        low = 0
        high = len(S)

        while low < high:
            mid = (low + high + 1) // 2
            print(low,high,mid)
            pos = self.test(S,mid,A,mod)
            if pos:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res:res + low]
    
    def test(self, S, L, A, mod):
        p = pow(26, L, mod)
        cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
        seen = {cur}
        for i in range(L, len(S)):
            cur = (cur * 26 + A[i] - A[i - L] * p) % mod
            if cur in seen: return i - L + 1
            seen.add(cur)
        res, lo, hi = 0, 0, len(S)