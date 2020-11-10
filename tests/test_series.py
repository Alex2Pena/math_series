from math_series.series_module import fibonacci, lucas, sum_series

# import TESTS
def test_import():
    assert fibonacci
    assert lucas
    assert sum_series

# fibonacci TESTS
def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_negative():
    actual = fibonacci(-3)
    expected = None
    assert actual == expected

# lucas TESTS
def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_negative():
    actual = lucas(-3)
    expected = None
    assert actual == expected

# sum_series TESTS
def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_1_a_b():
    actual = sum_series(1,22,42)
    expected = 42
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(2,18,23)
    expected = 41
    assert actual == expected

def test_sum_series_3():
    actual = sum_series(3,6,3)
    expected = 12
    assert actual == expected

def test_sum_series_4():
    actual = sum_series(4,1,2)
    expected = 8
    assert actual == expected

def test_sum_series_negative():
    actual = sum_series(-13)
    expected = None
    assert actual == expected
