import pytest
from .tictactoe import TicTacToe

def test_inicializacao():
    jogo = TicTacToe()
    assert jogo.tabuleiro == [[' ' for _ in range(3)] for _ in range(3)]
    assert jogo.jogador_atual == 'X'

def test_movimentar():
    jogo = TicTacToe()
    assert jogo.movimentar(0, 0) is True
    assert jogo.tabuleiro[0][0] == 'X'
    assert jogo.movimentar(0, 0) is False  # Já ocupado

def test_jogador():
    jogo = TicTacToe()
    assert jogo.jogador_atual == 'X'
    jogo.jogador()  # Troca para 'O'
    assert jogo.jogador_atual == 'O'
    jogo.jogador()  # Troca de volta para 'X'
    assert jogo.jogador_atual == 'X'

def test_verifica_vencedor():
    jogo = TicTacToe()
    # linha
    jogo.tabuleiro = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert jogo.verifica_vencedor() == 'X'
    
    # coluna
    jogo.tabuleiro = [['O', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
    assert jogo.verifica_vencedor() == 'O'
    
    # diagonal
    jogo.tabuleiro = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
    assert jogo.verifica_vencedor() == 'X'
    
    # sem vencedor
    jogo.tabuleiro = [[' ', ' ', ''], [' ', 'O', 'X'], ['O', ' ', 'X']]
    assert jogo.verifica_vencedor() is None

def test_empate():
    jogo = TicTacToe()
    jogo.tabuleiro = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
    assert jogo.empate() is True  # Tabuleiro cheio, sem vencedor

    jogo.tabuleiro = [['X', 'O', 'X'], [' ', 'X', 'O'], ['O', 'X', 'O']]
    assert jogo.empate() is False  # Ainda há espaço no tabuleiro

@pytest.mark.parametrize("linha, coluna, esperado", [
    (0, 0, True),  # Válido
    (1, 1, True),  # Válido
    (3, 3, False),  # Inválido
    (-1, -1, False),  # Inválido
    (0, 1, True),  # Válido
])

def test_movimentar_parametrizado(linha, coluna, esperado):
    jogo = TicTacToe()
    resultado = jogo.movimentar(linha, coluna)
    assert resultado == esperado
    if esperado:
        assert jogo.tabuleiro[linha][coluna] == jogo.jogador_atual
    elif 0 <= linha < 3 and 0 <= coluna < 3:
        assert jogo.tabuleiro[linha][coluna] == ' '


 
