# Estimate reading time if average 200 words equals one minute of reading.
# Round down floats.

# User story:
# as a User
# so that I can amange my time
# I want to see an estimate fo reading tinme for a test, assuming that I can read 200 words a minute

def reading_time(words):
    return (f"Estimate Reading Time: {round(words / 200)} minutes")