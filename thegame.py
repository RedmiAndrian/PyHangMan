import random

print("Welcome, user!")
print("I'm Python!")
print("Today, we are going to play Hangman")
print("You have only 5 lives, so you have to answer correctly.")
list = ["Pen" , "Pencil" , "Ruler" , "Eraser" , "Sharpener"]
rean = list[random.randint(0,4)]
lives = int(5)
cor = int(0)
print("The word has been generated, what's the first word you guessed? (Clue : It is a stationery)")
while lives > 0:
    ans = str(input())
    if ans not in rean:
        lives = lives - 1
        print("Wrong! Try again. you have " + str(lives) + " lives left.")
    else:
        print("Correct!")
        cor = cor + 1
        if cor == len(rean):
            print("You have beat the game! You're awesome!")
            break
