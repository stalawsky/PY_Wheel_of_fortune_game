import random
from enum import Enum
import pandas as pd 

FileName = 'List of sentences_no_polish.xlsx'

 def prepare_list_of_guesses(file_name ='C:/Users/stala/OneDrive/Pulpit/List of sentences_no_polish.xlsx') -> list:
     """ Enter a file location with the sentences to be used in game. Please adjust path of your file with sentences. 
     File should contain only one column. No polish signs. """
     df = pd.read_excel(file_name)
     ListOfWords = df.iloc[:, 0].to_list()
     return ListOfWords
    


def select_word_to_guess(EnterList) -> str:
    """ Enter a list of sentences to select a random sentence from. 
    Performs adjustments to chosen word to avoid potential errors.
    """
    WordToGuess = random.choice(EnterList)
    WordToGuess = WordToGuess.lower()
    WordToGuess = WordToGuess.replace('\xa0',' ')
    return WordToGuess

def prepare_empty_dictionary(Word) -> dict:
    """ Enter a word to create dictionary where for each sign is assigned empty value. 
    That dictionary is used later in game to assign guessed letters in sentence
    """
    HidedDict = {}
    for count, _ in enumerate(Word):
        HidedDict[count] = "_"
    return HidedDict

def prepare_dictionary_from_word(Word) ->dict:
    """ Enter a word to create dictionary where for each sign is assigned letter. 
    That dictionary is used later in game to assign guessed letters in sentence
    """
    DictToGuess = {}
    for count , letter in enumerate(Word):
        DictToGuess[count] = letter
    return DictToGuess


def adjust_values_in_dictonary(DictornaryToAdjust,SourceDictonary,Adjustments = [" "]) -> dict:
    """ Compare 2 dictionaries, if value of DictionaryToAdjust is equal to value of SourceDictionary then
    value of DictionaryToAdjust is adjusted to value of SourceDictionary. Function can perform multiple
    adjustments at once. Enter Adjustments as a List.
    """
    countOfAdjustments = len(Adjustments)
    Index = 0
    for Index in range(0,countOfAdjustments):
        for key,value in SourceDictonary.items():
            if value == Adjustments[Index]:
                DictornaryToAdjust[key] = value
        Index =+ 1
    return DictornaryToAdjust

def decide_difficulty_level(Word) -> list:
    """ Game will decide level of difficulty based on length of the word. 
    Difficulty level will determine numbers of Rounds where you guess a letter in a sentence
    and Reward to be won if guessed right. Enter Word to determine level of difficulty.
    """
    LenghtWord = len(Word)
    if LenghtWord in range(0,25):
        Rounds = 11
        Reward = 1000
        print(f"You drew the easiest level. You have {Rounds} rounds to guess letter ")
    elif LenghtWord in range(25,40):
        Rounds = 13
        Reward = 2000
        print(f"You drew the medium level. You have {Rounds} rounds to guess letter")
    elif LenghtWord >= 40:
        Rounds = 17
        Reward = 3000
        print(f"You drew the hardest level. You have {Rounds} rounds to guess letter")
    return Rounds, Reward

def wheel_of_fortune(Rounds,Reward,GuessMe,WordGuess,EmptyWord) -> int:
    """ Function performs game of guessing letters in the random sentence. 
    When round of guessing letters is over you will have chance to guess the sentence.
    If guess is correct reward will be received.
    Rounds is numbers of rounds to guess letter in sentence
    Reward is reward to win if guess is right.
    GuessMe is a word to be guessed.
    EmptyWord is returned by function prepare_empty_dictionary
    WordGuess is returned by function prepare_dictionary_from_word
    """
    i = 0 
    ListofGuessedLetters = []
    while i < Rounds:
        lettertoGuess = input("Guess letter: ")
        ListofGuessedLetters.append(lettertoGuess)
        Word = ""
        for key,value in WordGuess.items():
            if lettertoGuess == value:
                EmptyWord[key] = value
            Word = Word + EmptyWord[key]
        print(f"There is the list of guessed letters: {ListofGuessedLetters}")
        print(Word)
        i = i + 1
    Answer = input (f"This round is over your word to guess is {Word}. Please guess your word now ")
    if Answer == GuessMe:
        GameReward = 0 
        GameReward = GameReward + Reward
        print (f"Congratulations, you guessed it right. There is your reward: {GameReward}")
    else:
        print(f"I'm sorry. It is not a correct answer, the sentence was: {GuessMe}")
        GameReward = 0
    return GameReward




def play_game(list_of_guesses,NumberOfRounds = 3):
    """ Function performs necessary steps to run a game. Enter a list of sentences from which word to be guessed is chosen 
    and number of rounds of game. Functions used List of Sentences to chose random Word, perform preparation steps and run
    game of guessing letters in word and guessing word. Finally it returns final reward won during all rounds.
    """
    #w printahc daje mi duże spacje przez \ musze to poprawić
    print (f"Welcome in the game Wheel of Fortune. You will have {NumberOfRounds} rounds of guessing a sentence.\
            In each round you can guess letter hided in that sentence.\
            Number of guesses depends on the difficulty level and based on difficulty you can earn your reward.\
            Prepare yourself and enjoy!")    
    X = 0
    WonReward = 0
    while X < NumberOfRounds:
        WordToGuess = select_word_to_guess(list_of_guesses)
        EmptyDict = prepare_empty_dictionary(WordToGuess)
        WordDict = prepare_dictionary_from_word(WordToGuess)
        EmptyDict = adjust_values_in_dictonary(EmptyDict,WordDict,Adjustments= [" " , "," , "-"])
        LevelReward = decide_difficulty_level(WordToGuess)
        CashReward = wheel_of_fortune(Rounds = LevelReward[0] , Reward = LevelReward[1], 
                                      GuessMe =WordToGuess, WordGuess=WordDict , EmptyWord=EmptyDict)
        WonReward = WonReward + CashReward
        X = X + 1
    print(f"The game is over. You managed to win {WonReward}")


ListOfGuesses = prepare_list_of_guesses()
play_game(ListOfGuesses)
