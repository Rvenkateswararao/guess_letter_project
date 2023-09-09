# we creating hangman game by using random module and control statements and loops ....
# random is used to to generate random numbers or any letters or words to given ....
import random
frutes_list = ["apple","banana","mango","grape","lemon","orange","kiwi","pineapple","watermilon","strawberry","avocada","apricot","papaya","grapefruit",
             "blueberry","jackfruit","guava"]
choose_random_word = random.choice(frutes_list)
print(choose_random_word)
lives = 6
display = []
for letter in choose_random_word:
    display += '_'
print("you want guess the",len(choose_random_word),"letters of word...?")
print("you have only lives ! guess correct letter ")
game_over = False
while not game_over:
    guess_letter = input("enter letter: ").lower()
    for position in range(len(choose_random_word)):
        letter = choose_random_word[position]
        if letter == guess_letter:
            display[position] =  guess_letter
    if guess_letter not in choose_random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose !")
    if '_' not in display:
        game_over = True
        print("yow win ")
print("THANK YOU ")
# succesfuly completd 
        
        

 



















































