def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer,guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("Results")
    print("-----------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+ str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "What is 12 + 24?: ": "A",
    "What year was Python Created?: ": "B",
    "Who is the Main Character in Never Have I Ever?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. 36", "B. 24", "C. 123", "D. No Answer"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2002"],
           ["A. Ben", "B. Paxton", "C. Devi", "D. Eleanor"],
           ["A. True", "B. False", "C. No Idea", "D. Never"]]

new_game()

while play_again():
    new_game()

print("Toodles!")