class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        len_nums = len(nums)
        reachable = len_nums - 1
        for i in range(len_nums-1, -1, -1):
            if nums[i] + i >= reachable:
                reachable = i
        return reachable == 0
