from lib.diary_entry import *

def test_class_initialise():
    diary_entry = DiaryEntry("Bugs", "Do they fall in love?")
    assert diary_entry.title == "Bugs"
    assert diary_entry.contents == "Do they fall in love?"

def test_diary_format():
    diary_entry = DiaryEntry("Title", "Contents")
    assert diary_entry.format() == "Title: Contents"

def test_diary_count_words():
    diary_entry = DiaryEntry("The importance of insanity", "Life is easier if you allow yourself to be a little mad.")
    assert diary_entry.count_words() == 12

def test_reading_time():
    diary_entry = DiaryEntry("Slight problem", "I've forgotten my birthday, do you think anyone will notice? I'm sure I'll remember on the day... is it today?")
    assert diary_entry.reading_time(10) == 2

def test_reading_chunk():
    diary_entry = DiaryEntry("Potatoes", "Boil 'em, mash 'em, stick 'em in a stew.")
    assert diary_entry.reading_chunk(2, 1) == "Boil 'em,"

def test_reading_chunk_progression():
    diary_entry = DiaryEntry("Monkeys are bananas", "Why else would they go bananas for them?!")
    diary_entry.reading_chunk(2, 1)
    next_chunk = diary_entry.reading_chunk(2, 1)
    assert next_chunk == "would they"