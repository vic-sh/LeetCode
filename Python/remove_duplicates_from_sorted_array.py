class Solution:
    def removeDuplicates(self, nums):
        count = 0
        _ = 3 * pow(10, 5)
        for i in range(1,len(nums)):
            print(i)
            if nums[i] == nums[i-1]:
                nums[i-1] = _
                count += 1
                #print(count)
                print(nums)
        nums.sort()
        k = len(nums) - count
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
a = Solution()
a.removeDuplicates(nums)
print(nums)