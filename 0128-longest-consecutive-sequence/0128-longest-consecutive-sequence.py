class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for i in seen:
            if i-1 not in seen:
                pivot = i
                count = 1
                while pivot+1 in seen:
                    count +=1
                    pivot +=1
                longest = max(count,longest)
        return longest

        