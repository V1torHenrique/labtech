class FizzBuzz:

    @staticmethod
    def fizzBuzz(numero):
        if not isinstance(numero, int):
            return "Isso não é um número inteiro."

        if numero % 3 == 0 and numero % 5 == 0:
            return "FizzBuzz"
        
        elif numero % 3 == 0:
            return "Fizz"
        
        elif numero % 5 == 0:
            return "Buzz"
        
        else:
            return str(numero)
        
if __name__ == "__main__":
    try:
        numero = int(input("Insira un número: "))
        print(FizzBuzz.fizzBuzz(numero))

    except ValueError:
        print("\nIsso não é um número inteiro.")



