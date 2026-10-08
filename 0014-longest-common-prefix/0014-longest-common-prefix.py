class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or strs[0]=="":
            return ""
        ans = ""
        for i in range(len(strs[0])):
            check = strs[0][i]
            for word in strs[1:]:
                if i<len(word):
                    if check != word[i]:
                        return ans
                else:
                    return ans
            ans += strs[0][i]
        return ans

        
