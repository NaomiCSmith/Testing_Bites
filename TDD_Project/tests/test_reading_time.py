from lib.reading_time import *

def test_reading_time_the_hobbit():
    result = reading_time(95000)
    assert result == "Estimate Reading Time: 475 minutes"

def test_reading_time_lightning_thief():
    result = reading_time(87223)
    assert result == "Estimate Reading Time: 436 minutes"

def test_reading_time_paradise_lost():
    result = reading_time(79810)
    assert result == "Estimate Reading Time: 399 minutes"

def test_reading_time_yellow_wallpaper():
    result = reading_time(6000)
    assert result == "Estimate Reading Time: 30 minutes"