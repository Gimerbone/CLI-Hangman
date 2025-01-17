import random as ran
import word_list as wl
import ascii_art as renderer
import time
    
tried_letter = ""
chances = 7
isPlayerWin = False
correctIndex = []

picked_word = ran.choice(wl.word_list)
empty_box = len(picked_word)
display_word = ""
for i in range(0, len(picked_word)):
        display_word = display_word + "_ "

print(renderer.title)
time.sleep(2)
        
while True:
        print(f"****************************{chances}/7 LIVES LEFT****************************")
        print(f"Tried Letter: {tried_letter}\n")
        print(renderer.stages[max(0, chances)] + "\n")
        print(display_word + "\n")
        
        if chances > 0:
                guess = input("Guess a letter to fill the word: ").lower()
                print("\n")
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

print("\nAnd thats your final guess...")
time.sleep(2)

print("\n==============================GAME OVER===============================\n")

if isPlayerWin:
        print("Congratulation! You Win!")
else:
        print("Oops... Looks like the man is hanging.")
        print("He's dead, but you aren't. You still have chances.")

print(f"\nThe word is {picked_word}")