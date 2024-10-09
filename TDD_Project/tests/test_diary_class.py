from lib.diary_class import *


def test_diary_class_instantiates():
    diary_class = Diary()
    assert diary_class.entries == []

def test_diary_class_count_words_starts_zero():
    diary_class = Diary()
    assert diary_class.count_words() == 0