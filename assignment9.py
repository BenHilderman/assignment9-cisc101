"""
This program turns the lines found from a url into a list of strings. The program uses this list to create a 3x3 bingo game!
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Nov 20, 2022
"""

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import random

def readWords(urlLink):
    """
    This function reads the data from the link provided and returns a list of strings (line by line)
    Parameters: urlLink - string
    Return Value: list
    """
    try:
        itemsList = []
        response = urllib.request.urlopen(urlLink)
        data = response.readline().decode('utf-8')
        # removing last character of first line
        data = str(data)[:-1]
    except:
        # if url gets an error
        print("The URL is invalid")
        return []
    
    while len(data) != 0:
        # adding each line to list
        itemsList += [data]
        data = response.readline().decode('utf-8')
        # removing last character of each line
        data = str(data)[:-1]
    return itemsList

def bingoCardGenerator(listOfLists):
    """
    This function uses the list of strings (listOfLists) to randomly generate a 3x3 bingo card
    Parameters: listOfLists - list
    Return Value: string
    """
    # randomly shuffle values
    random.shuffle(listOfLists)
    
    # storing first 9 values for the bingo card. storing these values as lists of a list
    bingoCardListOfLists = [
        [listOfLists[0], listOfLists[1], listOfLists[2]],
        [listOfLists[3], listOfLists[4], listOfLists[5]],
        [listOfLists[6], listOfLists[7], listOfLists[8]]]
    # display bingo card as 3x3
    print(listOfLists[0] + ' || ' + listOfLists[1] + ' || ' + listOfLists[2] + '\n' + listOfLists[3] + ' || ' + listOfLists[4] + ' || ' + listOfLists[5] + '\n' + listOfLists[6] + ' || ' + listOfLists[7] + ' || ' + listOfLists[8] + '\n')
    return bingoCardListOfLists

def newItem(listOfLists, bingoCard):
    """
    This function chooses a random line from the list of strings and checks if the value appears on the bingo card
    Parameters: listOfLists - list, bingoCard - string
    Return Value: list
    """
    randomItem = (random.choice(listOfLists))
    # telling user the random item they got
    if randomItem == "SEEN":
        print("Item has already been seen on card...")
    else: print("Random item chosen: " + randomItem)

    # loop 9 times for 9 bingo spots
    for i in range(9):
        if randomItem == listOfLists[i]:
            # replaces sentence with SEEN when there is a match
            listOfLists[i] = "SEEN"
    # create the bingo card
    bingoCard = listOfLists[0] + ' || ' + listOfLists[1] + ' || ' + listOfLists[2] + '\n' + listOfLists[3] + ' || ' + listOfLists[4] + ' || ' + listOfLists[5] + '\n' + listOfLists[6] + ' || ' + listOfLists[7] + ' || ' + listOfLists[8]
    print(bingoCard + '\n')
    return listOfLists

def checkWin(listOfLists):
    if (listOfLists[0] == "SEEN" and listOfLists[1] == "SEEN" and listOfLists[2] == "SEEN") or (listOfLists[3] == "SEEN" and listOfLists[4] == "SEEN" and listOfLists[5] == "SEEN") or (listOfLists[6] == "SEEN" and listOfLists[7] == "SEEN" and listOfLists[8] == "SEEN") or (listOfLists[0] == "SEEN" and listOfLists[2] == "SEEN" and listOfLists[6] == "SEEN" and listOfLists[8] == "SEEN"):
        return "win"
    else: return "no"
            

def main():
    # initialze list
    listOfLists = readWords('https://research.cs.queensu.ca/home/cords2/zoombingo.txt')
    # generate random bingo card
    bingoCard = bingoCardGenerator(listOfLists)

    play = 'Y'
    # if user inputs N the loop ends
    while play != 'N':
        win = checkWin(listOfLists)
        # if user wins
        if win == "win":
            print('YOU WIN!')
        else:
            # ask user if they want to continue playing
            play = input("Is it time to choose a new item? (Y or N): ")
            # if user inputs a value that isnt N or Y
            while play != 'N' and play != 'Y':
                play = input("Is it time to choose a new item? Input Y for yes or N for no: ")
            if play == 'Y':
                listOfLists = newItem(listOfLists, bingoCard)
main()