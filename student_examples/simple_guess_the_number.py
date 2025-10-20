import random

# Generate a random integer between 1 and 10.
number = random.randint(1,10)

# Let user input guess.
print("Type a number here:")
guess = int(input())

# Loop while answer is not right.
while(guess != number):
    if(guess < number):
        print("Too Small!")
    if(guess > number):
        print("Too High!")

    print("Type a number here:")
    guess = int(input())

  # Print correct number.  
print("Correct! The number was " + str(number))
