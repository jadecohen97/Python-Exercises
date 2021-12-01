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

while not end_of_game:
    guess = input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            yourAnswer[position] = letter

    print(yourAnswer)
    if "_" not in yourAnswer:
        end_of_game = True
        print("you win!")
