import random
import numpy as np
import pandas as pd

print("Welcome to the virtual dice roller")

rollcounter = 0
roll_history = []
max_roll_num = int(input("How many times would you like to roll? Please enter a number between 1 and 100: "))
minmax = list(range(0, 100))

if max_roll_num in minmax:
  print("Lets roll the dice " + str(max_roll_num) + " times")
else:
  print("Please input a number")

#max_roll_no = 10
while rollcounter < int(max_roll_num):

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

if rollcounter == max_roll_num:
  print("You have rolled the maximum number of times")
  print("Here is the roll history: " + str(roll_history))

roll_df = pd.DataFrame(roll_history, columns=["Number"])
roll_counts = roll_df.Number.value_counts()
most_common= roll_counts.max()

roll_mean = roll_df.Number.mean()


print("The most common roll was: " + str(most_common))
print("The mean of all rolls was: " + str(roll_mean))