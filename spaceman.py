import random

# List comprehension makes this program so much easier than nested for loops and such.

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    space = ""
    letters = space.join([x for x in secret_word if x in letters_guessed])
    if letters == secret_word:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    space = ""
    guess_so_far = [x if x in letters_guessed else "_" for x in secret_word]
    return space.join(guess_so_far)

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    return guess in secret_word


def letter_checker():
    while True:
        guess = input("Please enter a letter: ")
        formatted_guess = guess.lower().strip()
        if formatted_guess.isalpha():
            if len(guess) > 1:
                print("The entry was invalid.")
                print("---------------------------------------------------")
                continue
            else:
                return guess
                break
        else:
            print("The entry was invalid.")
            print("---------------------------------------------------")
            continue

def check_guess_in_word(guess, secret_word, guessed_letters, guesses_left):
    if guess in secret_word:
        if guess in guessed_letters:
            print("Letter already guessed: " +
                    get_guessed_word(secret_word, guessed_letters))
            is_word_guessed(secret_word, guessed_letters)
            print("---------------------------------------------------")
            return guesses_left
        else:
            guessed_letters.append(guess)
            print("Guess in word: " +
                    get_guessed_word(secret_word, guessed_letters))
            print("---------------------------------------------------")
            return guesses_left
    else:
        if guess in guessed_letters:
            print("Already guessed that letter: " +
                    get_guessed_word(secret_word, guessed_letters))
            print("---------------------------------------------------")
            return guesses_left
        else:
            guessed_letters.append(guess)
            guesses_left -= 1
            print("Letter is not in the word: " +
                    get_guessed_word(secret_word, guessed_letters))
            print("---------------------------------------------------")
            return guesses_left


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TESTING
    '''
    print(secret_word)
    guess = ["h","e","l","w"]
    print(is_word_guessed(secret_word, guess))
    print(get_guessed_word(secret_word, guess))
    print(is_guess_in_word("w", secret_word))
    '''
    play = True
    while play:
        #TODO: show the player information about the game according to the project spec
        print("Welcome to the Spaceman Game!")
        print("The secret word contains " + str(len(secret_word)) + " letters.")
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        #TODO: show the guessed word so far
        #TODO: check if the game has been won or lost

        word_guessed_status = False
        guess = ""
        guessed_letters = []
        guesses_left = 7

        while guesses_left > 0 and guesses_left <= 7 and word_guessed_status is False:
            if secret_word == get_guessed_word(secret_word, guessed_letters):
                word_guessed_status = True
                break
            print("You have " + str(guesses_left) + " guesses left.")
            print("---------------------------------------------------")

            guess = letter_checker()

            guesses_left = check_guess_in_word(guess, secret_word, guessed_letters, guesses_left)

        if is_word_guessed(secret_word, guessed_letters):
            print("You won!")
        elif guesses_left == 0:
            print("Game Over, you ran out of guesses. The word was " + secret_word + "!\n")
    
        again = input("Play again? Type y or n: ")
        if again == "y":
            secret_word = load_word()
        elif again == "n":
            play = False

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)