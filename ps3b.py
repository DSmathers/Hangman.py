from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

    possible_words = []

    for length in range(1, HAND_SIZE+1):
        perms = get_perms (hand, length)
        possible_words.extend(perms)

    max_points = 0
    max_word = None

    for word in possible_words:
        if word in word_list:
            if get_word_score(word, HAND_SIZE) > max_points:
                max_points = get_word_score(word, HAND_SIZE)
                max_word = word
    return max_word
            
            
       
    


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    points = 0
    hand_size = calculate_handlen(hand)
    while calculate_handlen(hand) > 1:
        print "The Computer's Hand Is:"
        display_hand(hand)
        print ''
        print 'Thinking....'
        print ''
        word = comp_choose_word(hand.copy(), word_list)
        if word == None:
            break
        else:
            print 'The Computer Plays:',word, 'for', get_word_score(word, HAND_SIZE), 'points'
            points = points + get_word_score(word, HAND_SIZE)
            hand = update_hand(hand, word)
    print 'The Computer Ends its Turn with', points, 'points!'
    
    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    hand = deal_hand(HAND_SIZE)
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    
    while True:
        print ''
        print 'Select "n" to deal a new hand, "r" to replay last hand, or "e" to exit game'
        user_input = raw_input('What is your selection? ')
        if user_input == 'n':
            print ''
            hand = deal_hand(HAND_SIZE)
            print 'Select "u" to play turn or "c" for computer to play turn'
            player = raw_input('What is your selection? ')
            if player == 'u':
                play_hand(hand.copy(), word_list)
                print
            elif player == 'c':
                comp_play_hand(hand.copy(), word_list)
                print
            else:
                print 'Invalid Entry'
        elif user_input == 'r':
            print 'Select "u" to play turn or "c" for computer to play turn'
            player = raw_input('What is your selection? ')
            if player == 'u':
                play_hand(hand.copy(), word_list)
                print
            if player == 'c':
                comp_play_hand(hand.copy(), word_list)
                print
            else:
                print 'Invalid Entry'
        elif user_input == 'e':
            print 'Thank You For Playing'
            break
        else:
            print "invalid Command"
        
                           
                        
            
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
