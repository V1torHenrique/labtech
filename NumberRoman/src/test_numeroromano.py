import pytest

from src.numeroromano import NumberRoman

# def test_int_para_romano_0():
#     assert NumberRoman.int_para_romano(0) == "\nNúmero fora do intervalo permitido (1 a 1000)."

# def test_int_para_romano_1():
#     assert NumberRoman.int_para_romano(1) == "I"

# def test_int_para_romano_2():
#     assert NumberRoman.int_para_romano(2) == "II"

# def test_int_para_romano_3():
#     assert NumberRoman.int_para_romano(3) == "III"

# def test_int_para_romano_4():
#     assert NumberRoman.int_para_romano(4) == "IV"

# def test_int_para_romano_5():
#     assert NumberRoman.int_para_romano(5) == "V"

# def test_int_para_romano_9():
#     assert NumberRoman.int_para_romano(9) == "IX"

# def test_int_para_romano_0():
#     assert NumberRoman.int_para_romano(0) == "\nNúmero fora do intervalo permitido (1 a 1000)."

# def test_int_para_romano_1000():
#    assert NumberRoman.int_para_romano(1001) == "\nNúmero fora do intervalo permitido (1 a 1000)."


@pytest.mark.parametrize("input,expected",[
    (0, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (17, "XVII"),
    (20, "XX"),
    (30, "XXX"),
    (40, "XL"),
    (50, "L"),
    (60, "LX"),
    (70, "LXX"),
    (80, "LXXX"),
    (90, "XC"),
    (100, "C"),
    (200, "CC"),
    (300, "CCC"),
    (400, "CD"),
    (500, "D"),
    (600, "DC"),
    (700, "DCC"),
    (800, "DCCC"),
    (900, "CM"),
    (901, "CMI"),
    (1000, "M"),
    (1001, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (1500, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (2000, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (3000, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (4000, "\nNúmero fora do intervalo permitido (1 a 1000)."),
    (5000, "\nNúmero fora do intervalo permitido (1 a 1000)."),
])

def test_int_to_roman(input, expected):
    assert NumberRoman.int_para_romano(input) == expected