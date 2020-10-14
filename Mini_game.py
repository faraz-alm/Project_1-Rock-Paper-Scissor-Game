import random

# Rock Paper Scissor game
def gameWin(comp, you):
    # If both chose same, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose Rock
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose Paper
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose Scissor
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Computer's Turn: Rock(r) Paper(p) or Scissor(s)?")
randomNo = random.randint(1, 3) 
if randomNo == 1:
    comp = 'r'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")