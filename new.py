#Guess number game
import random

top_range=input("Enter a number")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range <= 0:
        print("Enter a larger number greater than 0")
        quit()
else:
    print("Enter a number")
    quit()


random_number_generator = random.randrange(top_range)
guess_count = 0


print(f"Guess the number between 0 and {top_range}")
while True:
    guess_count += 1
    answer = input("Enter Guess: ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("Enter a number next time")
        continue
    if answer == random_number_generator:
        print(" You guessed it")
        break
    elif answer > random_number_generator:
        print("You are above the number")
    else:
        print("You are below the number")


print("you guessed it in", guess_count, " guesses!")


