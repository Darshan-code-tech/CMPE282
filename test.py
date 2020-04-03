class Solution(object):
    def twoSum(self,nums,target):
        self.nums = nums
        self.target = target
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                required[nums[i]] = i
if __name__ == "__main__":
    nums = [2,8,12,15]
    target = 10
    s1 = Solution()
    x = s1.twoSum(nums,target)
        print(x)               

