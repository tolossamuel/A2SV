class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        for i in range(k-1):
            nums.remove(max(nums))
        return str(max(nums))
