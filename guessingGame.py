import random
print ("Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")

while chances < 5 :
    if guess == number:
        print ("Congratulations, you won!")
        break
    if not chances < 5:
        print ("You lose! The number is", number)
