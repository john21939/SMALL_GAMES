print("Hello, Welcome to The Battle Cats Quiz! ")

answer = input("Are you ready to play(yes/no): ")
score = 0
total_q = 5

if answer.lower() == "yes":
    answer = input("1. What does wall cat evolve into?: ")
    if answer.lower() == "eraser cat":
        score +=1
        print("correct")
    else:
        print("incorrect")

    answer = input("2. What does macho cat evolve into?: ")
    if answer.lower() == "mohawk cat":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("3. What does cow cat evolve into?: ")
    if answer.lower() == "giraffe cat":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("4. Is crazed wall cat stronger than wall cat?: ")
    if answer.lower() == "yes":
        score += 1
        print("correct")
    else:
        print("incorrect")

    answer = input("5. What does lizard cat evolve into?: ")
    if answer.lower() == "dragon cat":
        score += 1
        print("correct")
    else:
        print("incorrect")

print(f"You got {score}/5 questions correct!")
mark = (score/total_q) *100
print(f"You got {mark}%")


