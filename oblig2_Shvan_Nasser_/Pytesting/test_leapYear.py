import main


def test_divide400():
    assert main.isLeapYear(2000) == True

def test_divide4Not100():
    assert main.isLeapYear(1640) == True


def test_divide100AndNot400():
    assert main.isLeapYear(1700) == False

def test_notDividedBy4():
    assert main.isLeapYear(2050) == True







