# Coding Challenge 3, hangman.py
# Name: Louie Darke
# Student No: 1905864

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

wordlist_file = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(wordlist):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    open_words = open('words.txt','r')
    for word in open_words:
        words = word.split()        #Opens the words file and splits up each word, and chooses a random word
    return random.choice(words)


# end of helper code
# -----------------------------------

guesses = 0
def load_words():
    print('The list of words is being loaded..')
    try:
        open_words = open('words.txt','r')
    except IOError:
        print('The file could not be found.')   #Opens the words file and reads it, but if it cannot find the file and there is an IOError, you will get a user-friendly message
    all_words = 0
    for line in open_words:
        words = line.split()
        all_words += len(words)     #Splits each word up, and counts up each word into all_words so that the correct number can be printed
    print((all_words), 'words loaded')
    open_words.close()      #Closes the words file since it is done with it, to avoid any corruption
        

wordlist = load_words()     #The wordlist is found by using the load_words function
letters_guessed = []        #the letters_guessed variable starts off as an empty list

def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here

    for ch in letters_guessed:      #For each character in the letters_guessed list, print True or False depending on if that character is in the word to guess
        if ch in word:
            print(True)
        else:
            print(False)


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here

    print('Here is the word: ')
    for ch in word:
        if ch in letters_guessed:       #For each character in the word to guess, if the character has been guessed, print it. Otherwise, print an underscore
            print (ch,end="")
        else:
            print ("_ ",end="")
    print('\n')

def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
    available = ''
    from string import ascii_lowercase
    for ch in ascii_lowercase:          #For each character in ascii lowercase, if the character is in letters_guessed, the available letters are ascii_lowercase but without ones in letters_guessed
        if ch in letters_guessed:
            available = (ascii_lowercase(letters_guessed))
            print('Available letters:', available)

def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("-------------")
    # TODO: Fill in your code here
    from string import ascii_lowercase
    guesses = 8
    while guesses > 0:
        print('You have', guesses, 'guesses left.')
        get_guessed_word(word, letters_guessed)     #Calls the get_guessed_word function
        guess = input('Please guess a letter: ')
        guess = guess.lower()       #If the guess was a capital letter, it would be changed to lower case
        print('-------------')

        
        if guess in word:                       #If the guess is a letter in the word
            if guess not in letters_guessed:        #if the guess is not already in letters_guessed
                if (len(guess)) == 1:       #if the input guess is 1 letter
                    print('Good guess! ')
                    guesses = guesses           #guesses remaining stay the same
                    letters_guessed.append(guess)       #Add that guess to letters_guessed
                else:
                    print('Sorry, you can only guess one character at a time!')     #Else, the guess was more than 1 character
            elif guess in letters_guessed:
                print('You have already guessed that correct letter!')
                guesses = guesses
        elif guess in letters_guessed:
            print('You have already guessed that letter!')      #The letter was already found in letters_guessed
            guesses = guesses
        
        elif guess not in letters_guessed:          #Else, if the guess is not already in letters_guessed
            if guess not in ascii_lowercase:        #If the guess is also not in ascii_lowercase, (letters from a-z)
                print('Sorry, you can only guess single letters from a-z!')
                guesses = guesses - 1           #Remove 1 remaining guess
            elif guess not in word:                 #Else, if the guess is not a letter in the word
                if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':            #If the guess is any of the vowels
                    print('Unlucky! That vowel is not in the word!')
                    guesses = guesses - 2       #Remove 2 remaining guesses
                    letters_guessed.append(guess)
                else:
                    print('Unlucky! That letter is not in the word!')       #Else, if it's a consonant that is not in the word
                    guesses = guesses - 1
                    letters_guessed.append(guess)
            
        if all(ch in letters_guessed for ch in word):                           #If all the characters in the word are now in letters_guessed
            print('Congratulations, you won! You guessed the word:', word)
            print('Your total score for this game is:', guesses * (len(word)))      #Print win message and their score, which is their remaining guesses multiplied by the length of the word
            break           #End the loop, and therefore the program
                
    if guesses <= 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was:', word)             #If guesses reaches 0, end the game and reveal the word


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    # Uncomment the line below once you have finished testing.
    word = choose_random_word(wordlist)

    # Uncomment the line below once you have implemented the hangman function.
    hangman(word)
