#Program mengacak huruf dari sebuah kata
import random

def fisher_yates_shuffle(word):
    # Convert the word to a list of characters
    characters = list(word)
    
    # Perform Fisher-Yates shuffle
    for i in range(len(characters)-1, 0, -1):
        j = random.randint(0, i)
        characters[i], characters[j] = characters[j], characters[i]
    
    # Convert the shuffled characters back to a word
    shuffled_word = ''.join(characters)
    
    return shuffled_word

# Main program
word = input("Enter a word: ")
shuffled_word = fisher_yates_shuffle(word)
print("Shuffled word:", shuffled_word)