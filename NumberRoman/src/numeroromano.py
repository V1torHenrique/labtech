class NumberRoman:

    @staticmethod
    def int_para_romano(numero:int):
        if numero > 0 and numero <= 1000:
            valores = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
            ]
            
            resultado = '' 
            for valor, simbolo in valores:
                while numero >= valor:
                    resultado += simbolo
                    numero -= valor
            return resultado
        
        else:
            raise ValueError("Número fora do intervalo permitido (1 a 1000).")
    

if __name__ == "__main__":
    inteiro = int(input("Digite um número inteiro: "))
    romano = NumberRoman.int_para_romano(inteiro)
    print(f"O número {inteiro} em algarismos romanos é: {romano}")