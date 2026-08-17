class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Step 1: Apply operations on adjacent elements
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        # Step 2: Shift all non-zero elements to the beginning
        insert_pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[insert_pos] = nums[insert_pos], nums[i]
                insert_pos += 1
                
        return nums
