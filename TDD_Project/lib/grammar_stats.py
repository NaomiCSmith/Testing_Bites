class GrammarStats:
    def __init__(self):
        self.texts_tested = 0
        self.passed_check = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        suitable_punct = ["?", ".", "!"]
        if text[-1] in (suitable_punct) and text[0].isupper():
            self.texts_tested += 1
            self.passed_check += 1
            return True
        else:
            self.texts_tested += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return ((self.passed_check / self.texts_tested) * 100)
