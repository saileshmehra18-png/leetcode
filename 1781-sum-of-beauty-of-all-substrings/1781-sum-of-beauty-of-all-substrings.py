class Solution:
    def beautySum(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            d= {}   
            for j in range(i,len(s)):
                d[s[j]] = d.get(s[j],0)+1
                dif = max(d.values()) - min(d.values())
                sum += dif
        return sum