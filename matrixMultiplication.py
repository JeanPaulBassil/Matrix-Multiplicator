from sympy import symbols, Matrix, init_printing
import re

def format_matrix(matrix):
    superscript_map = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶',
        '7': '⁷', '8': '⁸', '9': '⁹'
    }

    for i, row in enumerate(matrix.tolist()):
        formatted_row = []
        for element in row:
            element_str = str(element)
            for num, sup in superscript_map.items():
                element_str = element_str.replace(f'**{num}', sup)
            element_str = element_str.replace('*', '')
            formatted_row.append(element_str)

        print(f"[{', '.join(formatted_row)}]")

def preprocess_input(input_str):
    return re.sub(r'(\d)([a-zA-Z])', r'\1*\2', input_str)

def matrix_multiply(matrix1, matrix2):
    result = matrix1 * matrix2
    return result

def main():
    init_printing()
    alphabet_symbols = symbols(' '.join(list('abcdefghijklmnopqrstuvwxyz')))

    rows1 = int(input("Enter the number of rows for matrix 1: "))
    cols1 = int(input("Enter the number of columns for matrix 1: "))
    rows2 = int(input("Enter the number of rows for matrix 2: "))
    cols2 = int(input("Enter the number of columns for matrix 2: "))

    if cols1 != rows2:
        print("Matrix multiplication is not possible. Number of columns in matrix 1 must be equal to the number of rows in matrix 2.")
        return

    print("Enter elements for matrix 1:")
    matrix1 = Matrix([[preprocess_input(input(f"Enter element ({i+1},{j+1}): ")) for j in range(cols1)] for i in range(rows1)])

    print("Enter elements for matrix 2:")
    matrix2 = Matrix([[preprocess_input(input(f"Enter element ({i+1},{j+1}): ")) for j in range(cols2)] for i in range(rows2)])

    result = matrix_multiply(matrix1, matrix2)

    print("Matrix multiplication result:")
    format_matrix(result)

if __name__ == "__main__":
    while(True):
        main()
        print()
        print()
        print()
