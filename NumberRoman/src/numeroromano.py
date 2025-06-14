class NumberRoman:

    @staticmethod
    def int_para_romano(numero: int):
        if not 1 <= numero <= 1000:
            return "\nNúmero fora do intervalo permitido (1 a 1000)."

        # resultado = ''

        # if numero >= 1000:
        #     resultado += 'M'
        #     numero -= 1000

        # if numero >= 900:
        #     resultado += 'CM'
        #     numero -= 900

        # if numero >= 500:
        #     resultado += 'D'
        #     numero -= 500

        # if numero >= 400:
        #     resultado += 'CD'
        #     numero -= 400

        # while numero >= 100:
        #     resultado += 'C'
        #     numero -= 100

        # if numero >= 90:
        #     resultado += 'XC'
        #     numero -= 90

        # if numero >= 50:
        #     resultado += 'L'
        #     numero -= 50

        # if numero >= 40:
        #     resultado += 'XL'
        #     numero -= 40

        # while numero >= 10:
        #     resultado += 'X'
        #     numero -= 10

        # if numero >= 9:
        #     resultado += 'IX'
        #     numero -= 9

        # if numero >= 5:
        #     resultado += 'V'
        #     numero -= 5

        # if numero >= 4:
        #     resultado += 'IV'
        #     numero -= 4

        # while numero >= 1:
        #     resultado += 'I'
        #     numero -= 1

        # return resultado


        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        

        resultado = ''
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado


if __name__ == "__main__":
    inteiro = int(input("Digite um número inteiro: "))
    romano = NumberRoman.int_para_romano(inteiro)
    print(f"O número {inteiro} em algarismos romanos é: {romano}.")