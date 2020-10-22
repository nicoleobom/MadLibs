import random
# open madlibs file
f = open('madlibs.txt', 'r')

# read file and store each line in a list.
madlibtxt = f.read()

# Establish inputs for madlibs
# intro = input("Hi! What's your name?")

# adjective = input("Enter an adjective: ")

# adjective2 = input("Enter another adjective: ")

# room = input("Enter the name of a room: ")

plural_noun = input("Enter a plural noun: ")

plural_noun2 = input("Enter another plural noun: ")

noun = input("Gimme a noun!: ")

noun2 = input("Gimme another noun!: ")

noun3 = input("Ok, one more noun: ")

# adjective3 = input("Let's change it up. Give me an adjective: ")

noun4 = input("And yet another noun: ")

# number = input("Now enter a number: ")

plural_noun3 = input("Enter a plural noun: ")

noun5 = input("Enter another regular noun: ")

# color = input("What's your favorite color?: ")

# color2 = input("What's your least favorite color?: ")

# something_alive = input("Name something in the same room as you that is living: ")

# person1 = input("Name a person in the same room or household as you: ")

# person2 = input("Name another person in the same room or household as you: ")

# Replace nouns!

madlibtxt = madlibtxt.replace("noun", noun, 1).replace("noun2", noun2, 1).replace("noun3", noun3, 1).replace("noun4", noun4, 1).replace("noun5", noun5, 1)

# Replace plural nouns!

madlibtxt = madlibtxt.replace("plural", plural_noun, 1).replace("plural2", plural_noun2, 1).replace("plural3", plural_noun3, 1)

# Replace adjective!


# Print to console
print(madlibtxt)