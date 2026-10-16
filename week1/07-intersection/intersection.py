def intersection(a, b):
  result = []
  for x in a:
    if x in b and x not in result:
      result.append(x)
  return result