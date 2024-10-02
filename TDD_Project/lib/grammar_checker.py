
# User story:
# as a User
# so that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark

def grammar_checker(string):
    suitable_punct = ["?", ".", "!"]
    if string[-1] in (suitable_punct) and string[0].isupper():
        return "Good job! This text starts with a capital letter and ends with suitable punctuation."
    elif string[-1] in (suitable_punct) and string[0].islower():
        return "Not quite! This text does not start with a capital letter but does end with suitable punctuation."
    elif string[-1] not in (suitable_punct) and string[0].isupper():
        return "Not quite! This text starts with a capital letter but is missing suitable ending punctuation."
    else:
        return "Oh no! This sentence needs a capital letter to start and suitable ending punctuation."
    