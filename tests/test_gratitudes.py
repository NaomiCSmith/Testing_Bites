from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("not living underwater")
    result = gratitudes.format()
    assert result == "Be grateful for: not living underwater"

def test_gratitudes_multiple():
    gratitudes = Gratitudes()
    gratitudes.add("Greggs steak bakes")
    gratitudes.add("Pthalo green (it's fantastic)")
    gratitudes.add("No more smelly P.E classes")
    result = gratitudes.format()
    assert result == "Be grateful for: Greggs steak bakes, Pthalo green (it's fantastic), No more smelly P.E classes"