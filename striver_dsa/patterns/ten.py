n = int(input())

# for i in range(1, n+1):
#     print(''.join('*' for j in range(0,i)))

# for i in range(1, n+1):
#     print(''.join('*' for j in range(1,n-i+1)))
# print()

for i in range(1, 2*n):
    stars=i
    if i>n:
        stars=2*n-i
    for j in range(0,stars):
        print('*', end='')
    print()