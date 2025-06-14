class StringCalculator:

    @staticmethod
    def add(numeros: str):
        # se string vazio, retorna 0.
        if not numeros:
            return 0

        # substitui delimitadores por vírgula e divide a string em números.
        delimitadores = [',', '\n', '/', '###', '///', ' ', ';', ':']
        for delimitador in delimitadores:
            numeros = numeros.replace(delimitador, ',')
        
        # remove espaços em branco e divide a string em números.
        number_strings = numeros.split(',')

        # converte strings para inteiros, soma os positivos e verifica negativos.
        total = 0
        negativos = []
        for num_str in number_strings:
            if num_str.strip():
                num = int(num_str)

                if num < 0:
                    negativos.append(num)

                elif num < 1000:
                    total += num

        if negativos:
            return f"Números negativos não permitidos: {', '.join(map(str, negativos))}"

        return total

# Exemplo de uso:
if __name__ == "__main__":
    calc = StringCalculator()
    print(calc.add("1,2,3"))  # Saída: 6
    print(calc.add("1\n2,3,5,7, 8"))  # Saída: 26
    print(calc.add("1,-2,3,-4"))  # Saída: Números negativos não permitidos: -2, -4
    print(calc.add("1001,2,3"))  # Saída: 5
    print(calc.add("1000,2000,3000"))  # Saída: 0