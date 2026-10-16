def rotate_list(nums, k):
  if len(nums) == 0:
    return []
  if k > len(nums):
    val = k % len(nums)
    k = val * -1
  else:
    k = k * -1

  test = nums[k:] + nums[:k]
  return test