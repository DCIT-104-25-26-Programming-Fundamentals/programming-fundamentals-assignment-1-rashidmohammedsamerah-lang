def generate_fibonacci(n):
    sequence = []

    a = 0
    b = 1

    for i in range(n):
        sequence.append(a)

        next_number = a + b
        a = b
        b = next_number

    return sequence


def check_fibonacci(number):
    a = 0
    b = 1

    while a <= number:
        if a == number:
            return True

        next_number = a + b
        a = b
        b = next_number

    return False


# Main Program

# Part A
terms = int(input("How many terms? "))

if terms <= 0:
    print("Error: Number of terms must be positive.")
else:
    fibonacci = generate_fibonacci(terms)

    print("Fibonacci sequence:", end=" ")

    for number in fibonacci:
        print(number, end=" ")


# Part B
print()

number = int(input("\nEnter a number to check: "))

if check_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is NOT a Fibonacci number.")