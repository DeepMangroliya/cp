n = int(input())

for i in range(1,n+1):
    for j in range(1,2*n):
        if (j <= n-i) or (j >= n+i):
            print(' ', end='')
        else:
            print('*', end='')
    print()
    
for i in range(0, n+1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0,2*n-(2*i+1)):
        print('*',end='')
    for j in range(0, i):
        print(' ',end='')
    print() 