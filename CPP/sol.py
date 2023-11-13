class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        count = 1
        result = 0
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                result += (count * (count + 1)) // 2
                count = 1
        
        result += (count * (count + 1)) // 2
        
        return result % MOD
