def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    print("General Knowledge Quiz")
    print("Instructions: Every Question is given 4 options each, you have to enter the right option")
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "What does BBC stand for?: ": "A",
 "Who was British Prime Minister before Theresa May?: ": "B",
 "For one point, which house was Harry Potter almost put into by the sorting hat?": "C",
 "What are the colours of Google? For an extra point, can you name them in the order they appear online?": "A"
}

options = [["A. British Broadcasting Corporation", "B. Bol Bacchan Campions", "C. Britsh Broadcasting Company ", "D. British Broadcasting Cooking"],
          ["A. Winston Churchill", "B. David Cameron", "C. William Gladstone", "D. Clement Attlee"],
          ["A. Gryffindor", "B. Hufflepuff", "C. Slytherin", "D. Ravenclaw"],
          ["A. Blue, Red, Yellow and Green","B. Pink, Blue, Yellow, Red", "C. Gold, Red, Blue, Green", "D. Black, Blue, Yellow, Red"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
