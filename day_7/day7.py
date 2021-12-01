# hanmgman
import random
word_list = ["tiger", "giraffe", "elephant"]
chosen_word = random.choice(word_list)
print("the chosen word is:", chosen_word)

yourAnswer = []
for _ in range(len(chosen_word)):
    yourAnswer += "_"
print(yourAnswer)

end_of_game = False

lives = len(chosen_word)
total_lives = len(chosen_word)


while not end_of_game:
    guess = input("guess a letter: ").lower()
    if guess in yourAnswer:
        print("you already guessed this letter:", guess)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            yourAnswer[position] = letter
            print("correct!")
    if guess not in chosen_word:
        print("your guess:", guess)
        lives -= 1
        print("Incorrect, please try again!")
        print("Your total lives left:", lives, "/", total_lives)
    if lives == 0:
        end_of_game = True
        print("you lose")

    print(yourAnswer)
    if "_" not in yourAnswer:
        end_of_game = True
        print("you win!")
