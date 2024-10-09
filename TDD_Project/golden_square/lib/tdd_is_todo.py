# Design and test drive a function

# 1. Describe the problem

# As a user
# So that I can find my tasks among all my notes
# I want to check if a line from my notes includes the string `#TODO`.

# 2. Design the function signature

# parameters: notes - a list of strings of words (that may contain #TODO)
#return - any number of strings in the list with #TODO featuring, and disregards the others
#side effects - none predicted

# 4 Implement behaviour

def if_todo(notes):
    to_do_list = []
    for note in notes:
        if "#TODO" in note:
            to_do_list.append(note)
    return to_do_list
