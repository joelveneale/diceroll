import random
import numpy as np
import pandas as pd

print("Welcome to the virtual dice roller")

rollcounter = 0
roll_history = []
max_roll_no = 10
while rollcounter < max_roll_no:

  input("Would you like to roll the dice? y/n: ")
  if "y":
     roll = random.randint(1,6)
     print("You rolled a " + str(roll))
     rollcounter = rollcounter + 1
     roll_history.append(roll)
  elif "n":
     print("Let me know when you are ready to roll.")
  else:
     print('Please enter \'y\' or \'n\' to roll the dice: ')

if rollcounter == max_roll_no:
  print("You have rolled the maximum number of times")
  print("Here is the roll history: " + str(roll_history))

roll_df = pd.DataFrame(roll_history, columns=["Number"])
roll_counts = roll_df.Number.value_counts()
most_common= roll_counts.max()

roll_mean = roll_df.Number.mean()


print("The most common roll was: " + str(most_common))
print("The mean of all rolls was: " + str(roll_mean))