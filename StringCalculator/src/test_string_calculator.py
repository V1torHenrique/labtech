import pytest
from .string_calculator import StringCalculator

# def test_add_string_vazia():
#     assert StringCalculator.add("") == 0

# def test_add_numero_solo():
#     assert StringCalculator.add("5") == 5

# def test_add_dois_numeros():
#     assert StringCalculator.add("1,2") == 3

# def test_add_multiplos_numeros():
#     assert StringCalculator.add("1,2,3,4,5") == 15

# def test_add_ignora_numeros_maiores_que_1000():
#     assert StringCalculator.add("2,1001") == 2
#     assert StringCalculator.add("2,1000") == 2
#     assert StringCalculator.add("1001,2000,3000") == 0  

# def test_add_numeros_com_nova_linha():
#     assert StringCalculator.add("1\n2,3") == 6

# def test_add_numeros_com_espacos():
#     assert StringCalculator.add(" 1, 2, 3 ") == 6

# def test_add_numeros_negativos():
#     assert StringCalculator.add("1,-2,3,-4") == "Números negativos não permitidos: -2, -4"

@pytest.mark.parametrize("input_str, expected", [
    ("", 0),
    ("5", 5),
    ("1,2", 3),
    ("1,2,3,4,5", 15),
    ("1\n2,3", 6),
    (" ###1, 2, 3 ", 6),
    ("1,-2,3,-4", "Números negativos não permitidos: -2, -4")
])

def test_add_parametrizado(input_str, expected):
    assert StringCalculator.add(input_str) == expected


