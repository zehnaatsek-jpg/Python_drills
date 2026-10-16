def remove_duplicates(nums):
  number = []
  for num in nums:
    if num not in number:
      number.append(num)
  return number