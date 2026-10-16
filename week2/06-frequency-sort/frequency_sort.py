def frequency_sort(items):
  hold = {}
  for num in items:
    if num not in hold:
      hold[num] = 1
    else:
      hold[num] += 1

  sorted_keys = sorted(hold.items(), key = lambda x: x[0])
  sort_dict = {}

  for key, value in sorted_keys:
    sort_dict[key] = value
  hold = sorted(sort_dict.items(), key = lambda x:x[1], reverse=True)

  res = []
  for num, count in hold:
    holder = [num] * count
    res.extend(holder)
  return res