class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        cand = None

        for i in nums:
            if count == 0:
                cand = i
                count = 1
            elif i == cand:
                count +=1
            else:
                count -=1
        if nums.count(cand) > len(nums) // 2:
            return cand