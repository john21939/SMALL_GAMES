import random as r
guesses = 0
#gues gues gues s




high_number = input("Enter number:")
if high_number.isdigit():
    high_number = int(high_number)

else:
    print("Enter a number next time!")
    quit()




print(f"Enter number between 0-{high_number}")
random_number = r.randrange(high_number)
while True:
    guesses +=1
    guess = input(f"Guess Here: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter number!")
        continue
    if guess == random_number:
        print("You got it!")
        print(f"You guessed it in {guesses} guesses!")
        quit("bye")
    elif guess < random_number:
        print("Your guess was low!")
    else:
        print("Your guess was high!")








