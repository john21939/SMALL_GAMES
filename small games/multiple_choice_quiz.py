# ---------------------


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0


def score(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS:")
    print("---------------------")
    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end="")
    print()


def play_again():
    pass

questions = {
    "Is Alonso a virgin?: ": "D",
    "What is Alonso's address?: ": "A",
    "Is Alonso in debt?: ": "A",
    "IS Alonso a munch?: ": "B",
    "What is the best way to eliminate him?: ": "A",
}

options = [["A. NO", "B. IDK", "C. SURE", "D. YES"],
          ["A. 942 North Moraga ST", "B. HOW TF AM I SUPPOSED TO KNOW!", "C. 942 Moraga Road, Temecula, CA", "D.942 Moraga Drive, Los Angeles, CA"],
          ["A. YES", "B. NO", "C. he rich", "D. IDK"],
          ["A. HELL NO", "B. HELL YEAH", "C. HE gay", "D. idk bruh" ],
          ["A. MESS HIM UP INFRONT OF HIS MOM", "B. POP HIS TIRES", "C. SEND SHIT TO HIS HOUSE", "D. KNOCK HIM OUT WITH A CHAIR"]]

new_game()