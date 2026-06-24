class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        def helper(i,res,sign,started):
            if i == len(s):
                return max(INT_MIN, min(INT_MAX, sign * res))

            c = s[i]
            if not started and c == " ":
                return helper(i+1,res,1,False)
            if not started and c in ("+","-"):
                return helper(i+1,res,1 if c == "+" else -1, True)
            if c.isdigit():
                return helper(i+1,res*10+int(c),sign,True)
            return max(INT_MIN, min(INT_MAX, sign * res))
        return helper(0,0,1,False)