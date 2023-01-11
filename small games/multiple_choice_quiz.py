# ---------------------


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------")
        print(key)


def check_answer():
    pass

def score():
    pass

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