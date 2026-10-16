def longest_word(sentence):
  if len(sentence) == 0:
    return ""

  result = []
  text = ""
  for letter in range(len(sentence)):
    if sentence[letter].isalpha():
     text += sentence[letter]
    elif sentence[letter] == " ":
      if text:
        result.append(text)
        text = ""
      continue
    elif sentence[letter] == "-" and sentence[letter-1].isalpha() and sentence[letter+1].isalpha():
      text += sentence[letter]
    elif sentence[letter] == "":
      result.append(text)
      text = ""
    else:
      continue

  if text:
    result.append(text)

  high = ""
  count = 0

  for word in result:
    if len(word) > count:
      high = word
      count = len(word)
  
  return high

  

# bonus
def longest_words(sentence):
  if len(sentence) == 0:
    return []

  result = []
  text = ""
  for letter in sentence:
    if letter.isalpha():
     text += letter
    elif letter == " ":
      if text:
        result.append(text)
        text = ""
      continue
    else:
      continue

  if text:
    result.append(text)

  high = ""
  count = 0

  for word in result:
    if len(word) > count:
      high = word
      count = len(word)

  lst = []
  for word in result:
    if len(word) == count:
      lst.append(word)
  
  return lst