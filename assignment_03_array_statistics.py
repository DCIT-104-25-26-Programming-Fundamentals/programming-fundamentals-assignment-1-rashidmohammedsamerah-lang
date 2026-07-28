# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def calculate_minimum(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


# Main program

n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Number of values must be positive.")
else:
    numbers = []

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print("\nResults:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", calculate_maximum(numbers))
    print("Minimum:", calculate_minimum(numbers))