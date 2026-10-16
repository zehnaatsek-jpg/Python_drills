import random


def play_game(target=None, max_attempts=None):
  define_max = True
  if max_attempts == None:
    max_attempts = 0
    define_max = False

  if target is None:
    target = random.randint(1, 100)
  else:
    target = int(target)

  while True:
    if define_max and max_attempts == 0:
      print(f"You missed it, the number was {target}")
      break

    try:
      guess = int(input("Enter your number: "))
    except:
      print("invalid input. enter a whole number between 1 and 100")
      continue

    if guess > 100 or guess < 1:
      print("invalid input. enter a whole number between 1 and 100")
      continue

    if define_max and guess == target:
      max_attempts -= 1
      print(f"correct! you had {max_attempts} guesses left")
      break
    elif not define_max and guess == target:
      max_attempts += 1
      print(f"correct! you got it in {max_attempts} guesses ")
      break
    elif guess > target:
      if define_max:
        print("too high")
        max_attempts -= 1
        continue
      else:
        print("too high!")
        max_attempts += 1
        continue
    elif guess < target:
      if define_max:
        print("too low")
        max_attempts -= 1
        continue
      else:
        print("too low")
        max_attempts += 1
        continue
    
      


  rerun = input("Do you want to play again('yes' / 'no)? ")
  if rerun.lower() == "yes":
    play_game()
  elif rerun.lower() == "no":
    print("Goodbye")
    return
  else:
    print("Invalid input")
    return



# Do not modify below this line
if __name__ == "__main__":
  play_game(max_attempts=5)
