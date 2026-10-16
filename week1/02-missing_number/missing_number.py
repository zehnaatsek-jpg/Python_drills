def find_missing(nums):
    for i in range(len(nums)-1):
      if nums[i+1] - nums[i] != 1:
        return nums[i] + 1

numbers = [10, 11, 12, 14, 15, 16]
print(find_missing(numbers))