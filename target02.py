def is_fibonacci(num):
    # Função para verificar se o número pertence à sequência de Fibonacci
    if num < 0:
        return False

    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


def main():
    # Função para pessoa escolher o número
    number = int(input('Digite um número para descobrir se ele pertence à sequência de Fibonacci: '))

    if is_fibonacci(number):
        print(f"O número {number} está na sequência de Fibonacci")
    else:
        print(f"O número {number} não está na sequência de Fibonacci")


if __name__ == "__main__":
    main()
