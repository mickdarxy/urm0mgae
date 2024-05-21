from unittesting import add_numbers, subtract_numbers, multiply_numbers

#write a test function using the pytest framework
def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_subtract_numbers():
    assert subtract_numbers(9, 5) == 4

def test_multiply_numbers():
    assert multiply_numbers(4, 4) == 16

