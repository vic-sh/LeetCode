class Solution:
    def twoSum(self, numbers, target):
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]
        numbers_dict = {}
        for i, number in enumerate(numbers):
            pair = target - number
            if pair in numbers_dict:
                return [i,numbers_dict[pair]]
            numbers_dict[number] = i   
        

a = Solution()
print(a.twoSum([2,7,11,15], 9))
print(a.twoSum([2,3,4], 6))
print(a.twoSum([-1,0], -1))
print(a.twoSum([0,0,3,4], 0))
