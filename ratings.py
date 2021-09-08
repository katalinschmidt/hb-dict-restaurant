"""Restaurant rating lister."""


"""
INSTRUCTIONS:

LINK: https://fellowship.hackbrightacademy.com/materials/serft8/exercises/dicts-restaurant-ratings/

FUNCTIONALITY A: Reading Ratings in from a File

INPUT: text file, scores.txt, containing a series of local restaurant ratings.
The format of each line is: 'RestaurantName:Rating'

OUTPUT:
    Reads the ratings in from the file
    Stores them in a dictionary
    And finally, spits out the ratings in alphabetical order by restaurant

Sample output:
    $ python3 restaurant-ratings.py
    Big Bean Shack is rated at 3.
    Chip Shop is rated at 3.
    Diagon Alley cafe is rated at 2.
    Eternelle's Elixir of Refreshment is rated at 5.
    Florean Fortescue's Ice Cream Parlour is rated at 4.
    Jellied Eel Shop is rated at 3.
    Luchino Caffe is rated at 1.
    Ministry Munchies is rated at 1.
    The Bear & Staff is rated at 2.
    The Club is rated at 2.
    The Porcupine is rated at 5.
    The Tavern is rated at 3.
"""

import sys

# R: file (scores.txt)
# M: nothing;
#    reads rest & rating, & stores in dict
# E: outputs sorted ratings

# filename = sys.argv[1]

def read_ratings(filename):
    """Opens file, reads it, and returns a dictionary of restaurant ratings."""
    # Create empty dict
    ratings_dict = {}

    # Open file
    input_file = open(filename)

    # Split line at :
    for line in input_file:
        key, value = line.rstrip().split(":")
        # Add each element to dict
        ratings_dict[key] = int(value)
        # dict format: RestaurantName:Rating
    
    input_file.close()

    return ratings_dict


def sort_dict(mydict):
    return sorted(mydict.items())


def print_ratings(mydict):
    """Print restaurant ratings from the ratings dictionary and return nothing."""
    for key, value in mydict.items():
        print(f"{key} is rated at {value}.")


def fxn_a(filename):
    """Opens file and outputs rest & rating"""
    # Read ratings
    ratings_dict = read_ratings(filename)
    
    # Sort dict
    ratings_dict = dict(sort_dict(ratings_dict))

    # Output rest & ratings
    print_ratings(ratings_dict)

    return ratings_dict


def main():
    mydict = fxn_a("scores.txt")
    fxn_b(mydict)


"""
FUNCTIONALITY B: Allowing the User to Add Ratings

Modify your script so that after it reads the scores file from disk, it prompts the user for a new restaurant and rating.

The program should:

Prompt the user for a restaurant name
Prompt the user for a restaurant score
Store the new restaurant/rating in the dictionary
Print all of the ratings in alphabetical order (including the new one, of course)
"""

def fxn_b(mydict):
    print("Starting fxn_b now")
    ask_for_new_rating(mydict)
    mydict = dict(sort_dict(mydict))
    print_ratings(mydict)


def ask_for_new_rating(mydict):
    """Ask for user inputs for a new restuarant name and rating, which is stored in the given dictionary."""
    restaurant_name = input('Restaurant name: ')
    restaurant_score = ask_for_valid_score()
    mydict[restaurant_name] = int(restaurant_score)
    return mydict


def ask_for_valid_score():
    """Return restaurant score (int between 1 and 5 inclusive) based on user input."""
    while True:
        try:
            restaurant_score = int(input('Restaurant score: '))
        except ValueError:
            print("This is an invalid score. Please input an integer between 1 and 5 inclusive.")
        else:
            break
    if 1 <= restaurant_score <= 5:
        return restaurant_score
    else:
        print("This is an invalid score. Please input an integer between 1 and 5 inclusive.")
        ask_for_valid_score()



if __name__ == "__main__":
    main()
