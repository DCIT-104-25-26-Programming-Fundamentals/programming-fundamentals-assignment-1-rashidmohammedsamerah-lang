def single_table(number):
    print(f"\nMultiplication Table for {number}:")

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def tables_from_one_to_n(n):
    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

        print("---------------------------")


# Main Program

number = int(input("Enter a number for multiplication table: "))

if number <= 0:
    print("Error: Number must be positive.")
else:
    # Part A
    single_table(number)

    # Part B
    n = int(input("\nEnter N for tables from 1 to N: "))

    if n <= 0:
        print("Error: N must be positive.")
    else:
        tables_from_one_to_n(n)