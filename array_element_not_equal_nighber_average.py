class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        while(True):
            random.shuffle(nums)
            for i in range(1,len(nums)-1,+1):
                if(nums[i]*2==nums[i-1]+nums[i+1]):
                    break
            else:
                return nums
