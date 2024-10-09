from lib.diary_class_entry import *


def test_diary_entry_class_instantiates():
    diary_class_entry = DiaryEntry("Title", "Contents")
    assert diary_class_entry.title == "Title"
    assert diary_class_entry.contents == "Contents"

def test_diary_entry_count_words():
    diary_class_entry = DiaryEntry("Frogs", "I think they might be psychic!")
    assert diary_class_entry.count_words() == 6

def test_diary_entry_reading_time():
    diary_class_entry = DiaryEntry("How to be epic", "A short story by Homer")
    assert diary_class_entry.reading_time(5) == 1

def test_diary_entry_reading_chunk():
    diary_entry = DiaryEntry("Potatoes", "Boil 'em, mash 'em, stick 'em in a stew.")
    assert diary_entry.reading_chunk(2, 1) == "Boil 'em,"

def test_diary_entry_reading_chunk_progression():
    diary_entry = DiaryEntry("Monkeys are bananas", "Why else would they go bananas for them?!")
    diary_entry.reading_chunk(2, 1)
    next_chunk = diary_entry.reading_chunk(2, 1)
    assert next_chunk == "would they"