def fibonacci_generator(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
if __name__ == "__main__":
    n = 20 
    fibonacci_numbers = fibonacci_generator(n)
    print(fibonacci_numbers)

