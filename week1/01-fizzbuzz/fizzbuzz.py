def fizzbuzz(n):
  check = []
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      check.append("FizzBuzz")
    elif i % 3 == 0:
      check.append("Fizz")
    elif i % 5 == 0:
      check.append("Buzz")
    else:
      check.append(str(i))
  return check