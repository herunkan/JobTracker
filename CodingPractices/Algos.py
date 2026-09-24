def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle -1
        elif nums[middle] < target:
            left = middle + 1
        
    return -1
        
nums = [1, 2, 5, 6, 7, 8, 9,13]
print(binary_search(nums=nums, target = 9))

# Pattern: Binary Search

# Signal:
# - sorted search space
# - need to find one target
# - can eliminate half the remaining possibilities each step

# Invariant:
# target, if present, must remain between left and right