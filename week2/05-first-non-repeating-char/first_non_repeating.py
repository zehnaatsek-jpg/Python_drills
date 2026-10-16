def first_non_repeating(s, case_sensitive=True):
  if len(s) == 0:
    return None
  if case_sensitive:
    once = {}
    for item in s:
      if item not in once:
        once[item] = 1
      else:
        once[item] += 1

    count = 1
    for item, value in once.items():
      if value == count:
        return item
      else:
        continue
    return None
  else:
    once = {}
    carbon = s.lower()
    for item in carbon:
      if item not in once:
        once[item] = 1
      else:
        once[item] += 1

    count = 1
    strings = ""
    for item, value in once.items():
      if value == count:
        strings += item
        break
      else:
        continue
    for i in s:
      if i.lower() == strings:
        return i 
    return None
  