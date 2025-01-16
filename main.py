import random as ran
import time

title = r"""
=================================================
  _                                            
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/

=================================================

Created by Gimerbone, Github: https://github.com/Gimerbone
Your game will start shortly..

                 
"""

stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
    r'''
  +---+
      |
      |
      |
      |
      |
=========
'''
]

with open("D:/Bootcamp/Udemy Python/100 Days Python/Day 7 - Hangman/word.txt", "r") as file:
    word_list = [line.strip() for line in file]
    
picked_word = ran.choice(word_list)
chances = 7
isPlayerWin = False
correctIndex = []
empty_box = len(picked_word)
tried_letter = ""

display_word = ""
for i in range(0, len(picked_word)):
        display_word = display_word + "_ "

print(title)
time.sleep(2)
        
while True:
        print(stages[max(0, chances)])
        print("\n")
        print(display_word)
        
        if chances > 0:
                guess = input("Guess a letter to fill the word. Your letter must be in lowercase.\nPicked Letter: ")
        else:
                break
        
        correctIndex.clear()
        for i in range(0, len(picked_word)):
                if guess == picked_word[i]:
                        correctIndex.append(i)
                        
        if correctIndex:                               
                for i in range(0, len(correctIndex)):
                        list_of_display_word = list(display_word)
                        list_of_display_word[2*correctIndex[i]] = guess
                        display_word = ''.join(list_of_display_word)
                        empty_box -= 1

                if empty_box <= 0:
                        isPlayerWin = True
                        break
        else:
                chances -= 1
                
        tried_letter = tried_letter + guess + " "
        
        print(f"Tried Letter: {tried_letter}")
        print(f"Chances left: {chances}")


print("\nAnd thats your final guess...")
time.sleep(2)
print("\n=================================================\n")
print("GAME OVER\n")
print(f"The word is {picked_word}\n")

if isPlayerWin:
        print("Congratulation! You Won!")
else:
        print("Oops... Looks like the man is hanging.")
        print("He's dead, but you aren't. You still have chances.")