class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0:
            return 0

        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i+1
