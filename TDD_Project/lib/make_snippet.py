def make_snippet(string):
    first_five_words = string.split()[:5]
    return (f"{' '.join(first_five_words)}...")