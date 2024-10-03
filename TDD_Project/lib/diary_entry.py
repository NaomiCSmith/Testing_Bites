class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.chunk_position = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return (f"{self.title}: {self.contents}")

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(list(self.contents.split()))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        length_of_contents = self.count_words()
        return length_of_contents / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        # Calculate total words and split contents into list
        wpm_times_minutes = wpm * minutes
        contents_list = list(self.contents.split())

        # Find current position and calculate next readable chunk
        current = self.chunk_position
        future = current + wpm_times_minutes
        
        # Check the reader hasn't reached the end of the contents
        if self.chunk_position >= len(contents_list):
            self.chunk_position = 0

        # Rejoin words with appropriate whitespace, update position, return next unread chunk of words
        next_chunk = " ".join(contents_list[current:future])
        self.chunk_position = future
        return next_chunk
