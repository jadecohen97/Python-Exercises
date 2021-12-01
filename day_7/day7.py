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

while not end_of_game:
    guess = input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            yourAnswer[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(lives)
    if lives == 0:
        end_of_game = True
        print("you lose")

    print(yourAnswer)
    if "_" not in yourAnswer:
        end_of_game = True
        print("you win!")
