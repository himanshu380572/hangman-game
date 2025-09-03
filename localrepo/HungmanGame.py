import random

word_list = ["APPLE","MAN","CAMEL","BAMBOO","VINAY"]

choosen_word= random.choice(word_list)
placeholder = ""
lives = 6
word_lenght= len(choosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter =[]
while not game_over:
    guess = input("Guess the letter: ").upper()
    if guess in correct_letter:
        print("you already guessed this letter")

    display="" 
    for letter in choosen_word:
        if letter==guess:
            display+= letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+= letter
        else:
            display+= "_"
    print(display)


    if guess not in choosen_word:
        lives -=1
        print(f"total lives left: {lives}")
        if lives == 0:
            game_over=True
            print("you lose!")
    if "_" not in display:
        game_over= True
        print("You win!")
        