#Step 1
import random
import words
import art

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

random_number = random.randint(0, len(word_list) - 1)
chosen_word = words.word_list[random_number]
word_list = []
for letter in chosen_word:
  word_list.append(letter)
print(word_list)
display = []
lives = 7

print(f"the selected word is {chosen_word}")

for letter in range(0, len(chosen_word)):
      display.append('_')

while word_list != display:
    guess = input("Guess a letter\n").lower()
    

    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter

    if guess not in chosen_word:
      lives = lives -1
      print(f"Wrong guess, you got {lives} remaining")
      print(art.stages[lives])
      if lives == 0:
        print("game over")
        break;
        
    print(display)

if word_list == display:
  print("you have won")
    
