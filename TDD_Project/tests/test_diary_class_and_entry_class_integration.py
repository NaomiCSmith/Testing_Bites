from lib.diary_class import *
from lib.diary_class_entry import *

def test_diary_class_add_entries_and_list():
    diary_class = Diary()
    entry_1 = DiaryEntry("October", "This is basically the 8 o'clock of the calendar world")
    entry_2 = DiaryEntry("November", "Bit chilly sometimes, eh?")
    diary_class.add(entry_1)
    diary_class.add(entry_2)
    assert diary_class.all() == [entry_1, entry_2]

def test_diary_class_count_words():
    diary_class = Diary()
    entry_1 = DiaryEntry("October", "This is basically the 8 o'clock of the calendar world")
    entry_2 = DiaryEntry("November", "Bit chilly sometimes, eh?")
    diary_class.add(entry_1)
    diary_class.add(entry_2)
    assert diary_class.count_words() == 14

def test_diary_class_total_reading_time():
    diary_class = Diary()
    entry_1 = DiaryEntry("First", "One two three four five six seven eight nine ten")
    entry_2 = DiaryEntry("Second", "Eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty")
    diary_class.add(entry_1)
    diary_class.add(entry_2)
    assert diary_class.reading_time(5) == 4

def test_diary_class_best_entry_for_reading_time():
    diary_class = Diary()
    entry_1 = DiaryEntry("First", "One two three four five six seven eight nine ten")
    entry_2 = DiaryEntry("Second", "Eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree")
    diary_class.add(entry_1)
    diary_class.add(entry_2)
    assert diary_class.find_best_entry_for_reading_time(3, 4) == entry_1

def test_diary_class_best_entry_for_reading_time_returns_none_if_none_fit():
    diary_class = Diary()
    entry_1 = DiaryEntry("First", "One two three four five six seven eight nine ten")
    entry_2 = DiaryEntry("Second", "Eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree")
    diary_class.add(entry_1)
    diary_class.add(entry_2)
    assert diary_class.find_best_entry_for_reading_time(1, 1) == None





