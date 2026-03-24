class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        # Mark numbers as seen by negating the value at the corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # The indices with positive numbers are missing
        missing = []
        for i in range(n):
            if nums[i] > 0:
                missing.append(i + 1)
        
        return missing

# Example usage:
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
print(sol.findDisappearedNumbers([1,1]))              # Output: [2]