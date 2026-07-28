def read_matrix(rows, cols, name):
    matrix = []

    print(f"\nEnter values for {name}:")

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(matrix[i][j])

        transpose.append(row)

    return transpose


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    result = []

    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


# Main Program

print("PART A - Transpose Matrix")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols, "Matrix")

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


print("\nPART B - Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = read_matrix(rows, cols, "Matrix A")
matrix2 = read_matrix(rows, cols, "Matrix B")

print("\nMatrix Addition Result:")
display_matrix(add_matrices(matrix1, matrix2))


print("\nPART C - Matrix Multiplication")

rows_a = int(input("Enter rows of Matrix A: "))
cols_a = int(input("Enter columns of Matrix A: "))

matrix_a = read_matrix(rows_a, cols_a, "Matrix A")

rows_b = int(input("Enter rows of Matrix B: "))
cols_b = int(input("Enter columns of Matrix B: "))

if cols_a != rows_b:
    print("Matrix multiplication is not possible.")
else:
    matrix_b = read_matrix(rows_b, cols_b, "Matrix B")

    print("\nMatrix Multiplication Result:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))