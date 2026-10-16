def count_characters(text):
  count = {
    "letters": 0,
    "numbers": 0,
    "spaces": 0,
    "special": 0
  }
  for letter in text:
    if letter.isalpha():
      count["letters"] += 1
    elif letter.isdigit():
      count["numbers"] += 1
    elif letter == " ":
      count["spaces"] += 1
    else:
      count["special"] += 1
  return count