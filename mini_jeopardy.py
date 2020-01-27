#Overall description
#Author: Christine Chen

import requests #module for making API requests
from datetime import datetime #module for creating the date parameters for the API requests
import random
import sys

#global variables
NUM_CLUES = 5
ACCEPTABLE_INPUT = ['1','2','3','4','5','Q']

USR_ERROR = 'usr_error'
QUIT = 'quit'
CLUE_SELECTION = 'clue_selection'
STATE = CLUE_SELECTION #starts at CLUE_SELECTION

#helper methods

#description
#input:
#returns:
def get_clues(parameters):

    api = 'http://www.jservice.io/api/clues'
    response = requests.get(api, params=parameters)

    if(response.status_code!=200):
        #there is an error, return an empty list
        return []
    else:
        clues = response.json()

        cleaned_clues = []
        for clue in clues:
            #we don't want an invalid clue and we want our clue to have a value
            if (clue['invalid_count']==None and clue['value']!=None):
                cleaned_clues.append(clue)

        return cleaned_clues

#description
#input:
#returns:
def pick_and_sort(cleaned_clues):
    values = []
    clue_objs = []

    while (len(values)!=NUM_CLUES):
        clue = random.choice(cleaned_clues)

        if(clue['value'] in values):
            #don't want multiple clues that have the same value
            cleaned_clues.remove(clue)
            continue
        else:
            values.append(clue['value'])
            clue_objs.append(clue)
            cleaned_clues.remove(clue)

    #sort the clues in ascending value
    #https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    clue_objs.sort(key=lambda x: x['value'])

    return clue_objs

#description
#input:
#returns:
def check_input(usr_input, sorted_clues):
    global STATE
    if (usr_input in ACCEPTABLE_INPUT):
        if (usr_input=='Q'):
            STATE = QUIT
            return 'Thanks for playing!'
        else:
            STATE = CLUE_SELECTION
            #list index starts at 0
            clue_idx = int(usr_input)-1
            return 'Here is the question: '+sorted_clues[clue_idx]['question']
    else:
        STATE = USR_ERROR
        return 'Input error. Try again.'

#main
def main():
    #greet the user and provide instructions
    greeting = 'Welcome to Mini Jeopardy - Science!\n'
    instructions = ('Here are instructions on how to play:\n'
                    '1. Type the row number corresponding to the point value you want (e.g. 1-5).\n'
                    '2. shift-Q and Enter to exit.\n')
    print(greeting)
    print(instructions)

    #get "science" clues that aired in 1996
    min_date = datetime.strptime('01/01/1996,00:00:00,UTC', '%m/%d/%Y,%H:%M:%S,%Z')
    max_date = datetime.strptime('12/31/1996,23:59:59,UTC', '%m/%d/%Y,%H:%M:%S,%Z')

    parameters = {
     'category':25,
     'min_date':min_date,
     'max_date':max_date
    }

    clues = get_clues(parameters)
    if(clues==[]):
        print("Sorry! We're having trouble getting clues.")
        sys.exit()

    #pick five clues and sort them in ascending value
    sorted_clues = pick_and_sort(clues)
    
    #print
    ctr = 1

    #want a game board that looks like:
    #1: val
    #2: val
    #...
    for clue in sorted_clues:
        print(str(ctr)+': '+str(clue['value']))
        ctr = ctr + 1
    print('\n')

    #time for user interaction
    go = True
    while (go):

        #get user input
        usr_input = input("Select a clue ([1-5] and hit Enter): ")
        #to do: wouldn't want to pass sorted_clues as mini jeopardy scales
        check_msg = check_input(usr_input, sorted_clues)
        #print(usr_input, check_msg)

        print(check_msg)
        #print(STATE)

        if (STATE==QUIT):
            go = False
            sys.exit()


if __name__ == "__main__":
    main()
