class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrace(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrace(nums, [])
        return res
