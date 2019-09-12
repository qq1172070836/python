'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if (nums.count(nums[i]) == 1) and (nums[i]!=(target-nums[i])):
                    return [i, nums.index(target-nums[i])]
                elif (nums.count(nums[i]) > 1) :
                    return [i, nums.index((target-nums[i]), i+1)]
                else:
                    return []

obj = Solution()
result = obj.twoSum([3,2,4], 6)
print(result)