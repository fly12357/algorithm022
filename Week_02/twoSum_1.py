class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in cache:
                return [i, cache[delta]]
            cache[n] = i
