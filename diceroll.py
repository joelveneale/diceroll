import random


print("Welcome to the virtual dice roller")

rollcounter = 0
while rollcounter < 10:

  input("Would you like to roll the dice? Y/N")
  if input == 'Y' or 'y':
     roll = random.randint(1,7)
     print("The dice roll was a " + str(roll))
     rollcounter = rollcounter - 1
  else:
     print("Let me know when you are ready to roll.")

print("You have rolled the maximum number of times")

