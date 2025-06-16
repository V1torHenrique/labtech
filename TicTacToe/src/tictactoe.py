class TicTacToe:

    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def movimentar(self, linha, coluna):
        if not (0 <= linha < 3 and 0 <= coluna < 3):
            return False  # Fora dos limites

        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        return False


    def jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def verifica_vencedor(self):
        # Checa linhas e colunas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return self.tabuleiro[i][0]
            
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return self.tabuleiro[0][i]
            
        # Checa diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return self.tabuleiro[0][2]
        return None

    def empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return self.verifica_vencedor() is None

    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            print(f"É a vez do jogador {self.jogador_atual}.")

            try:
                linha = int(input("Insira a linha (0, 1, 2): "))
                coluna = int(input("Insira a coluna (0, 1, 2): "))

            except ValueError:
                print("Entrada inválida. Por favor, escolha entre 0, 1 ou 2.")
                continue

            if linha not in range(3) or coluna not in range(3):
                print("Movimento inválido. Tente novamente.")
                continue

            if not self.movimentar(linha, coluna):
                print("Posição já preenchida. Tente novamente.")
                continue

            vencedor = self.verifica_vencedor()
            if vencedor:
                self.imprimir_tabuleiro()
                print(f"Jogador {vencedor} VENCEU!")
                break

            if self.empate():
                self.imprimir_tabuleiro()
                print("Deu empate!")
                break

            self.jogador()

if __name__ == "__main__":
    game = TicTacToe()
    game.jogar()



