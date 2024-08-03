import pytest
import time
import resources.my_functions as my_functions


def test_add():
    result = my_functions.add(4, 5)
    assert result == 9


def test_add_str():
    result = my_functions.add("I like ", "trains")
    assert result == "I like trains"


def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2


def test_zero_division():
    with pytest.raises(ValueError):
        my_functions.divide(3, 0)

@pytest.mark.slow
def test_very_divide_slow():
    time.sleep(2)
    result = my_functions.divide(6, 2)
    assert result == 3
