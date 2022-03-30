# -*- coding: utf-8 -*-
"""
Name: Spencer Haber
Navigator: Ethan Meyer
Assignment: Excersize 1
Date: 2_10_2022

"""
import sys
import argparse
import os
def determine_winner(p1, p2):
    '''Takes two strings that correspond to the two players hands and returns the winner
arguements:
    Args:
        p1 (string) : Player1s hand
        p2 (string) : Player2s hand
    Returns:
        player1 (string) or player2 (string) or tie (string)
        '''
        
    if (p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r"):
        return "player1"
    elif (p1 == "r" and p2 == "p") or (p1 == "s" and p2 == "r") or (p1 == "p" and p2 == "s"):
        return "player2"
    else:
        return "tie"
def main(player1_name, player2_name):
    '''Takes player1s name and player2s name and inputs handshape to each player
    Args:
        player1_name (string) : Player1s name
        player2_name (string) : Player2s name
    Returns:
        n/a

'''
    print("Enter player 1's hand shape ('r', 'p', 's'):")
    p1 = input()
    print ("Enter player 2's hand shape ('r', 'p', 's'):")
    p2 = input()
    winner = determine_winner(p1, p2)
    if winner == "player1":
        print(player1_name + " wins!")
    elif winner == "player2":
        print(player2_name + " wins!")
    else:
        print("Tie!")
        

    
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operationscommence.
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
    args = parser.parse_args(args_list) #We need to parse the list of command linearguments using this object.
    return args
if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?

    #It the script is being run as a module, the block of code under this will not beexecuted.
    #If the script is being run natively, the block of code below this will beexecuted.
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line argumentsto the parse_args function.
    #The returned object is an object with those command line arguments as attributesof an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ =="__main__":' statement.
    main(arguments.p1_name, arguments.p2_name)
