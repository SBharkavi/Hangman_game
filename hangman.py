# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
#from ctypes import _NamedFuncPointer
#from itertools import count
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in str(letters_guessed):
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_Word = []
    for letter in secret_word:
      if (letter in letters_guessed):
        guessed_Word.append(letter +" ")
      else:
        guessed_Word.append("_"+" ") 
    return "".join(guessed_Word)

#guessedWord = get_guessed_word("ramayan", ['a','y','r'])
#print(guessedWord)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string 
    lower_case_letters = string.ascii_lowercase 
    for letter in letters_guessed:
        lower_case_letters = lower_case_letters.replace(letter,'') 
    return lower_case_letters
    


#print(get_available_letters(['a','e'])) 


def unique_letters(secret_word):
  unique = []
  for word in secret_word:
    if word not in unique:
      unique.append(word)
  return(len(unique))
  
    
    
    

def hangman(secret_word):
   '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up. 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   '''letters_guessed = []
   print('Welcome to the game Hangman!')
   print('I am thinking of a word that is',len(secret_word),'letters long.')
   print('The secret word you want to guess is :',get_guessed_word(secret_word,letters_guessed))
   print('\n','*****************','\n')
    
   guess = 6 
   warn = 3 
   print('You have 3 Warnings')
   while guess >= 1:
        if(guess < 2 or  warn<1 ):
          print('Press Hash # if you need some hint words ')
        print('You have',guess,'guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters you have, Please select any one of the letters given below: ','\n',get_available_letters(letters_guessed))
        userInput = (input('Please guess a letter: ')).lower()
        letters_guessed.extend(userInput)
        if(userInput in secret_word):
          if(userInput not in available_letters):
            print('The letter has already been guessed before')
            print('Oops! That is not a valid letter')
            warn = warn-1 
            if(warn == 0):
              print('Now you have 0 warning')
              guess = guess-1 
            if(warn >0):
              print('Now you have only',warn,'warn')
            if(warn<0):
              print('You have no warning remain 0!')
              print('Game is over')
              break 
          print('Good guess:',get_guessed_word(secret_word,letters_guessed))
          guess = guess
        elif(userInput not in available_letters):
          if(userInput == '*'):
            print('Possible word matches are:')
            my_word = get_guessed_word(secret_word,letters_guessed)
            available_matches = show_possible_matches(my_word,wordlist)
            print(available_matches)
            warning += 1

          
          if(userInput in letters_guessed and userInput != '#'):
            print('The letter has already been guessed before')
            print('Oops! That is not a valid letter')
          warning = warning-1 
          if(warning==0):
            print('Now you have 0 warning')
            guess = guess-1
          if(warning >= 0):
            print('Now you have only',warning,'warning')
          if(warning<0):
            print('You have no warning remain!')
            print('Game is over')
            needtoknowTheword = input('Need to know the word: say Yes or NO ')
            if(needtoknowTheword == 'Yes'):
                  print('The secret word is:,secret_word')
    
            break
        
        elif(userInput in 'aeiou'):
          print('You choosen vowel but that is not in secret word! So you loss 2 guess')
          guess = guess-2 
        else:
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
            guess = guess-1 
        if(is_word_guessed(secret_word,letters_guessed)):
            print("Yes! You are the winner! you find the secret word")
            print('The secret word is ',secret_word)
            unique_letters_in_secret_word = len(set(secret_word))
            total_score = guess * unique_letters_in_secret_word
            print('Your score is',total_score)
            break
        print('\n','*******************')
   if (guess < 1):
        print('Sorry! You have no guess and game is over')
        print('The secret word is:',secret_word) '''
    





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    acutal_word = my_word.replace(' ','')
    if(len(acutal_word) != len(other_word)):
        return False
    for index in range (0,len(acutal_word)):
        if(acutal_word[index] != other_word[index]):
            if(acutal_word[index] != '_'):
                return False 
    return True
    



def show_possible_matches(my_word,wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_match = ' '
    no_match = 'No matches found'
    for i in range (0,len(wordlist)):
        other_word = wordlist[i]
        if(match_with_gaps(my_word,other_word)):
            possible_match += other_word+' '
        if((i) ==  (len(wordlist)-1)):
            if(possible_match == ' '):
                return no_match
            return possible_match
    return no_match
    



def hangman_with_hints(secret_word,wordlist):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('The secret word you want to guess is :',get_guessed_word(secret_word,letters_guessed))
    print('\n','*****************','\n')
    
    guess = 6 
    warn = 3 
    print('You have 3 Warnings')
    while guess >= 1:
        if(guess < 2 or  warn<1 ):
          print('Press * if you need some hint words ')
        print('You have',guess,'guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters you have, Please select any one of the letters given below: ','\n',get_available_letters(letters_guessed))
        userInput = (input('Please guess a letter: ')).lower()
        letters_guessed.extend(userInput)
        if(userInput in secret_word):
          if(userInput not in available_letters):
            print('The letter has already been guessed before')
            print('Oops! That is not a valid letter')
            warn = warn-1 
            if(warn == 0):
              print('Now you have 0 warning')
              guess = guess-1 
            if(warn >0):
              print('Now you have only',warn,'warn')
            if(warn<0):
              print('You have no warning remain 0!')
              print('Game is over')
              break 
          print('Good guess:',get_guessed_word(secret_word,letters_guessed))
          guess = guess
        elif(userInput not in available_letters):
          if(userInput == '*'):
            print('Possible word matches are:')
            my_word = get_guessed_word(secret_word,letters_guessed)
            available_matches = show_possible_matches(my_word,wordlist)
            print(available_matches)
            warn += 1

          
          if(userInput in letters_guessed and userInput != '*'):
            print('The letter has already been guessed before')
            print('Oops! That is not a valid letter')
          warn = warn-1 
          if(warn==0):
            print('Now you have 0 warning')
            guess = guess-1
          if(warn >= 0):
            print('Now you have only',warn,'warning')
          if(warn<0):
            print('You have no warning remain!')
            print('Game is over')
            print('The secret word is:,secret_word')
    
            break
        
        elif(userInput in 'aeiou'):
          print('You choosen vowel but that is not in secret word! So you loss 2 guess')
          guess = guess-2 
        else:
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
            guess = guess-1 
        if(is_word_guessed(secret_word,letters_guessed)):
            print("Yes! You are the winner! you find the secret word")
            print('The secret word is ',secret_word)
            unique_letters_in_secret_word = len(set(secret_word))
            total_score = guess * unique_letters_in_secret_word
            print('Your score is',total_score)
            break
        print('\n','*******************')
    if (guess < 1):
        print('Sorry! You have no guess and game is over')
        print('The secret word is:',secret_word)
    
    hangman(secret_word,wordlist)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
        # pass

        # To test part 2, comment out the pass line above and
        # uncomment the following two lines.
        
        # secret_word = choose_word(wordlist)
        # hangman(secret_word)

    ###############
        
         # To test part 3 re-comment out the above lines and 
         # uncomment the following two lines.
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word,wordlist) 
    