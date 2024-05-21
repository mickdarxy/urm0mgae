import random
def roll_dice():
   die1 = random.randint(1, 6)
   die2 = random.randint(1, 6)
   return (die1, die2)
print(roll_dice())