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

top = 0
bottom = n - 1
right = m - 1
left = 0

while left <= right or top <= bottom:
    for i in range(left,right+1):
        print(matrix[top][i], end=' ')
    print()
    top += 1

    for i in range(top,bottom+1):
        print(matrix[i][right], end=' ')
    print()
    right -= 1

    for i in range(right,left-1,-1):
        print(matrix[bottom][i], end=' ')
    print()
    bottom -= 1

    for i in range(bottom,top-1,-1):
        print(matrix[i][left], end=' ')
    print()
    left += 1


# for i in range(top,bottom+1):
#     print(matrix[top][right], end=' ')
#     if top != bottom:
#         top+=1
# bottom -= 1

# for i in range(left,right+1):
#     print(matrix[top][left], end=' ')
#     if left != right-1:
#         left+=1
# print(left)
# print()

    