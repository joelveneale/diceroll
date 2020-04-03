import random


print("Welcome to the virtual dice roller")

rollcounter = 0
while rollcounter < 10:

  input("Would you like to roll the dice? Y/N: ")
  if input == "Y":
     roll = random.randint(1,7)
     print("The dice roll was a " + str(roll))
     rollcounter = rollcounter + 1
  elif input == "N":
     print("Let me know when you are ready to roll.")
  else:
     print("Please enter Y or N to roll the dice")

  break

print("You have rolled the maximum number of times")

