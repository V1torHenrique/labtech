import pytest
from .fizzbuzz import FizzBuzz

# # 
# def test_fizzbuzz_1():
#     assert FizzBuzz.fizzBuzz(1) == "2"


# def test_fizzbuzz_1():
#     assert FizzBuzz.fizzBuzz(1) == "1"

# def test_fizzbuzz_3():
#     assert FizzBuzz.fizzBuzz(3) == "Fizz"

# def test_fizzbuzz_5():
#     assert FizzBuzz.fizzBuzz(5) == "Buzz"

# def test_fizzbuzz_15():
#     assert FizzBuzz.fizzBuzz(15) == "FizzBuzz"

# def test_fizzbuzz_a():
#     assert FizzBuzz.fizzBuzz('a') == "Isso não é um número inteiro."

# def test_fizzbuzz_b():
#     assert FizzBuzz.fizzBuzz('b') == "Isso não é um número inteiro."

@pytest.mark.parametrize("input,expected",[
    ('a', "Isso não é um número inteiro."),
    ('b', "Isso não é um número inteiro."),
    (1, "1"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (0, "FizzBuzz")])

def test_fizzbuzz_parametrized(input, expected):
    assert FizzBuzz.fizzBuzz(input) == expected