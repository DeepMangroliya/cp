# Get matrix size from user
n = int(input("Enter number of rows (n): "))
m = int(input("Enter number of columns (m): "))

matrix = []

print(f"\nEnter a {n}x{m} matrix (any numbers):")

# Take n rows of input
for i in range(n):
    row = list(map(float, input(f"Enter row {i+1} (separate numbers with space): ").split()))
    
    # Validate the row length
    if len(row) != m:
        print(f"Invalid input! Each row must have exactly {m} numbers.")
        exit()
    
    matrix.append(row)

for i in range(n-1):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

[row.reverse() for row in matrix]
        
print(matrix)