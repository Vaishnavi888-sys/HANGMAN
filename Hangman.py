import random
print("HANGMAN GAME\n")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
  ========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
  ========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
  ========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
  ========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
  ========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
  ========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
  ========''' ]

lives = 5
word_list = ["rose","tulip","lilly","lotus","jasmine"]
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)
place_holder = ""
for letter in chosen_word:
    place_holder += "_"
print(f"Here is your word : {place_holder}")
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess the letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(" uh-oh ,Guess again")
        if lives == 0:
            game_over = True
            print("oopsie,You lost!")

    if "_" not in display:
        game_over = True
        print("You won!")

    print(HANGMANPICS[lives])
