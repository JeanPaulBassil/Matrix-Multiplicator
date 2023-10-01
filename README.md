# Matrix Multiplicator

## Overview
This Python script uses the Sympy library to perform matrix multiplication. It allows users to input two matrices and then outputs the result of their multiplication. It also includes a function to format the matrix for better visualization.

## Requirements
- Python 3.x
- Sympy library

## Installation
1. Clone the repository
    ```
    git clone https://github.com/JeanPaulBassil/Matrix-Multiplicator.git
    ```
2. Navigate to the directory
    ```
    cd MatrixMultiplication
    ```
3. Install the required package
    ```
    pip install sympy
    ```

## How to Use

### 1. Input Dimensions
- The user inputs the number of rows and columns for Matrix 1 and Matrix 2.

### 2. Input Elements
- The user inputs the elements for each matrix.

### 3. Multiplication and Output
- The script multiplies the matrices and outputs the result in a formatted manner.

## Code Explanation

### Importing Libraries
- `sympy` is used for symbolic mathematics.
- `re` is used for regular expressions.

### Functions

#### format_matrix(matrix)
- Formats the matrix into a readable string representation with superscripts for exponents.

#### preprocess_input(input_str)
- Takes a user input as a string and preprocesses it by inserting multiplication symbols where needed.

#### matrix_multiply(matrix1, matrix2)
- Multiplies two matrices and returns the result.

#### main()
- Takes care of user input and function calls.

