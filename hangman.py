# H A N G M A N
import random

while True:
    words = ['python', 'java', 'kotlin', 'javascript']
    print("H A N G M A N")
    menu = input('Type "play" to play the game, "exit" to quit:').lower()
    if menu == 'play':
        random.seed()
        word = random.choice(words)
        mask = list("-" * len(word))
        unmask = ''.join(mask)
        guessed = set()
        lives = 0

        while lives < 8:
            print()
            print("".join(mask))
            unmask = ''.join(mask)
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print('You should input a single letter')
            elif letter in guessed:
                print('You\'ve already guessed this letter')
            elif letter.isupper() or letter.isalpha() is False:
                print('Please enter a lowercase English letter')
            elif letter in word:
                guessed.add(letter)
                idx = [i for i, ch in enumerate(word) if ch == letter]
                if len(idx) > 0:
                    for j in idx:
                        mask[j] = letter
            elif letter not in word:
                guessed.add(letter)
                print("That letter doesn't appear in the word")
                lives += 1
            if unmask == word:
                print('You guessed the word!')
                print('You survived!')
            else:
                print('You lost!')
    elif menu == 'exit':
        break
