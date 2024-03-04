# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 10, 2023

# Description:
# This program prompts the user to input a file name for a file
# containing a list of words. It then uses the list of words to create
# and display a dictionary consisting of each letter as a key and each
# word from the file beginning with that letter as the values.

# Logic:
# import pickle module
# initialize global variable with string of alphabet for use throughout
# main:
#   initialize word list and dictionary
#   open word file
#   open dictionary file
#   for loop to process lines to word list:
#       skip blank lines, make lowercase, rstrip and strip '.'
#       append
#   sort word list
#   for loop through alphabet to create dictionary:
#       create set
#       key = letter; values = set
#   dump dictionary into dictionary file
#   reopen dictionary file for reading
#   for loop through alphabet to display results:
#       if key contains set: print key and set
#       else: print key and 'No words found'

# open word file:
#   prompt user for file name
#   try: open file
#   except: display error, try again
#   return file name

# create output file:
#   prompt user for file name
#   try to open file for reading to see if it is found
#   if found, inform user and ask if it shoud be replaced
#       if y: open file for writing and end function
#       else: start over at prompt
#   if not found, open file for writing and end function

# create set:
#   initialize empty set
#   for loop to iterate through words in list
#   check first letter of word
#   if first letter == target from alphabet:
#       add to set

#   call main

# import the pickle module to allow for serializing
import pickle

# initialize global variable for alphabet string
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# create main function to begin program execution
def main():
    # initialize list to read file words into
    word_list = []
    # create dictionary for alphabet and words
    word_dic = {}
    # call function to open input file
    word_file = get_word_file()
    # call function to get name for output file and create output file
    dic_file, entered_name = create_dic_file()

    # for loop to read input file words
    for line in word_file:
    # if not blank line, strip newline characters, make all lowercase,
    # strip '.' and append to word list
        if not line.isspace():
            word_list.append(line.lower().rstrip().strip('.'))

    # close input file
    word_file.close()
    # sort word list alphabetically
    word_list.sort()

    # for loop to create set value for each alphabet letter key
    for letter in LETTERS:
        # call create_set function to create set of words for letter
        entry_set = create_set(letter, word_list)
        # assign resulting set to key
        word_dic[letter] = entry_set

    # use dump method to write word dictionary to file
    pickle.dump(word_dic, dic_file)
    # close dictionary file
    dic_file.close()

    # reopen dictionary file for binary reading
    out_file = open(entered_name, 'rb')

    # read dictionary file into variable out_dic
    out_dic = pickle.load(out_file)
    # close dictionary file
    out_file.close()

    # for loop to print saved dictionary
    for letter in LETTERS:
        # if value set is not empty, print the resulting entry
        if out_dic[letter] != set():
            print(f'\n{letter} - {out_dic[letter]}\n')
        # if set is empty, print appropriate message
        else:
            print(f'\n{letter} - No words found')
    
    

# function to prompt user for input file name, test whether file exists
# and open file for reading
def get_word_file():
    # get input file name from user and assign to variable for testing
    test = input(f'Please enter the name of the file to read: ')

    # initialize control variable and begin while loop
    not_done = True
    while not_done:
        # try opening file for reading
        # if successful, update control variable to end loop / function
        try:
            file_name = open(test, 'r')
            not_done = False
        # if unsuccessful, prompt user for a new name and iterate again
        except:
            test = input(f'File not found. Please try another name: ')
    # return name of file to be used for word list
    return file_name

# function to prompt user for output file name and open file for writing
# checks whether filename already exists, and confirms with user whether
# they would like to replace the existing file if applicable
def create_dic_file():
    # get output file name from user and assign to variable for testing
    test = input(f'Please enter a name for your dictionary file: ')

    # initialize control variable and begin while loop
    not_done = True
    while not_done:
        # try opening file for reading, to see if it already exists
        try:
            file_name = open(test, 'r')
            # if successful, close file and ask user if it should be replaced
            file_name.close()
            replace = input(f'This file already exists. Replace? (y/n): ')
            # if user entered 'y' or 'Y', open file for binary writing and end loop
            if replace.lower() == 'y':
                file_name = open(test, 'wb')
                not_done = False
            # if user did not enter 'y' or 'Y', prompt for another filename
            else:
                test = input(f'Please try another name: ')
        # if no existing file found, open for binary writing and end loop
        except:
            file_name = open(test, 'wb')
            not_done = False
    # return output file and output file name
    return file_name, test

# function to create set of words that begin with target letter
def create_set(char, words):
    # initialize empty set to hold words
    word_set = set()
    # for loop to iterate through words in word list
    for item in words:
        # if first letter of word matches target letter, add to set
        if item[0] == char:
            word_set.add(item)
    # return set of words that begin with target letter
    return word_set

# call main to execute program
if __name__ == '__main__':
    main()
