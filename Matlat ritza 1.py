def create_increasing_matrix(size=50):
    matrix = []
    current_value = 1
    for i in range(size):
        row = []
        for j in range(size):
            row.append(current_value)
            current_value += 1
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix[:50]:
        print(' '.join([f"{cell:4}" for cell in row]))

# Iterative search: O(n)
def search_iterative(matrix, numbers):
    for number in numbers:
        found = False
        rows = len(matrix)
        cols = len(matrix[0]) # num of columns in first row

        # Start at the top right corner
        i, j = 0, cols - 1
        
        while i < rows and j >= 0:
            if matrix[i][j] == number:
                print(f"Number {number} found at position ({i}, {j}) using iterative search")
                found = True
                break
            elif matrix[i][j] > number:
                # Move left
                j -= 1
            else:
                # Move down
                i += 1
        
        if not found:
            print(f"Number {number} not found in the matrix using iterative search")

# Recursive Divide and Conquer search:
def divide_and_conquer_search(matrix, number, top=0, left=0, bottom=None, right=None):
    if bottom is None:
        bottom = len(matrix) - 1
    if right is None:
        right = len(matrix[0]) - 1

    # Check if the submatrix is empty
    if top > bottom or left > right:
        return False
    
    # Check if the number is out of matrix bounds
    if number < matrix[top][left] or number > matrix[bottom][right]:
        return False

    # Find middle element
    mid_row = (top + bottom) // 2
    mid_col = (left + right) // 2
    mid_element = matrix[mid_row][mid_col]

    # If middle element is the key
    if mid_element == number:
        print(f"Number {number} found at position ({mid_row}, {mid_col}) using recursive divide and conquer method")
        return True

    # If middle element is less than key, search in the right and bottom submatrices
    if mid_element < number:
        # Search bottom-right submatrix
        return (
            divide_and_conquer_search(matrix, number, mid_row + 1, left, bottom, right) or
            divide_and_conquer_search(matrix, number, top, mid_col + 1, mid_row, right)
        )

    # If middle element is greater than key, search in the left and top submatrices
    return (
        divide_and_conquer_search(matrix, number, top, left, bottom, mid_col - 1) or
        divide_and_conquer_search(matrix, number, top, mid_col, mid_row - 1, right)
    )

# Wrapper function to initiate the recursive search
def search_matrix(matrix, number):
    if divide_and_conquer_search(matrix, number):
        return True
    print(f"Number {number} not found in the matrix using recursive divide and conquer method")
    return False

# Create the 50x50 matrix
matrix = create_increasing_matrix()

# Print the matrix
print("Matrix:")
print_matrix(matrix)

# Ask the user for three numbers to search
try:
    numbers_to_search = []
    for i in range(3):
        number = int(input(f"Enter number {i+1} to search: "))
        numbers_to_search.append(number)

    # Iterative search
    print("\nIterative Search: ")
    search_iterative(matrix, numbers_to_search)

    # Recursive divide and conquer search
    print("\nRecursive Divide and Conquer Search: ")
    for number in numbers_to_search:
        search_matrix(matrix, number)

except ValueError:
    print("Please enter valid integers.")
