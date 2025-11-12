matrix = []

print("Enter a 4x4 binary matrix (only 0s and 1s):")

# Loop to take 4 rows of input
for i in range(4):
    # Take input, split by spaces, and convert each element to integer
    row = list(map(int, input(f"Enter row {i+1} (separate numbers with space): ").split()))
    
    # Validate the row
    if len(row) != 4 or any(num not in (0, 1) for num in row):
        print("Invalid input! Each row must have exactly 4 binary numbers (0 or 1).")
        exit()
    
    matrix.append(row)
    
col0 = 1
n=4
m=4
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            #mark the ith-row
            matrix[i][0] = 0
            #mark the jth-col
            if j !=0:
                matrix[0][j] = 0
            else:
                col0 = 0
    
for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j]!=0:
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

if matrix[0][0] == 0:
    for j in range(0, m):
        matrix[0][j] = 0

if col0 == 0:
    for i in range(0,n):
        matrix[i][0] = 0
        
print(matrix)